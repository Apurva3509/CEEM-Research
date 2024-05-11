import torch
import numpy as np
from waymo_open_dataset import dataset_pb2 as open_dataset
from sklearn.cluster import DBSCAN
from sklearn.preprocessing import StandardScaler
from sklearn.metrics.pairwise import euclidean_distances

# func process LiDAR data
def process_lidar(lidar_data):
    lidar_points = np.array([[p.x, p.y, p.z] for p in lidar_data])
    
    # scale the data
    scaler = StandardScaler()
    lidar_points_scaled = scaler.fit_transform(lidar_points)
    
    # DBSCAN clustering
    dbscan = DBSCAN(eps=0.5, min_samples=10)
    dbscan.fit(lidar_points_scaled)
    
    labels = dbscan.labels_
    
    
    unique_labels = np.unique(labels)
    cluster_centers = []
    for label in unique_labels:     # finding centroids of each cluster
        if label != -1:  # removal of noise points
            cluster_points = lidar_points[labels == label]
            cluster_center = np.mean(cluster_points, axis=0)
            cluster_centers.append(cluster_center)
    
    return cluster_centers

#  object detection model
class ObjectDetector:
    def __init__(self):
        self.classes = ['left', 'straight', 'right']

    def detect(self, image):
        detections = []
        height, width = image.shape[:2]

        # Detect objects in the left third of the image
        left_box = (0, 0, width // 3, height)
        if np.mean(image[:, :width // 3]) > 128:
            detections.append({'class': 'left', 'box': left_box})

        # Detect objects in the middle third of the image
        middle_box = (width // 3, 0, width // 3, height)
        if np.mean(image[:, width // 3:2 * width // 3]) > 128:
            detections.append({'class': 'straight', 'box': middle_box})

        # Detect objects in the right third of the image
        right_box = (2 * width // 3, 0, width // 3, height)
        if np.mean(image[:, 2 * width // 3:]) > 128:
            detections.append({'class': 'right', 'box': right_box})

        return detections

# Dummy object detection function
def detect_objects(image):
    detector = ObjectDetector()
    detections = detector.detect(image)

    objects_detected = {
        'left': False,
        'straight': False,
        'right': False
    }

    for detection in detections:
        objects_detected[detection['class']] = True

    return objects_detected

# Function to generate control signals based on object positions
def generate_signals(objects_detected, lidar_info):
    left_signal = 0
    straight_signal = 0
    right_signal = 0

    # Generate signals accordingly
    if objects_detected['left']:
        left_signal = -1
    if objects_detected['right'] and objects_detected['straight']:
        straight_signal = 1
    if objects_detected['right'] and not objects_detected['straight']:
        right_signal = 1

    return left_signal, straight_signal, right_signal

def process_waymo_dataset(dataset_path):
    dataset = open_dataset.Dataset(dataset_path)

    for frame in dataset:
        # using LiDAR data
        lidar_data = frame.lasers
        lidar_info = process_lidar(lidar_data)

        # using camera images for object detection
        for camera_image in frame.images:
            image = np.frombuffer(camera_image.image, dtype=np.uint8)
            image = image.reshape((camera_image.height, camera_image.width, -1))

            # Detect objects in the image
            objects_detected = detect_objects(image)

            # generate signals based on detected objects and LiDAR data
            left_signal, straight_signal, right_signal = generate_signals(objects_detected, lidar_info)

            print("Left Signal:", left_signal)
            print("Straight Signal:", straight_signal)
            print("Right Signal:", right_signal)

# main function
if __name__ == "__main__":
    dataset_path = '/Users/apurva/Desktop/Apurva/Columbia/SEM2/Distillation/waymo-open-dataset/src/waymo_open_dataset'
    process_waymo_dataset(dataset_path)

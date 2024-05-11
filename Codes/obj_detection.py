import os
import torch
from torch.utils.data import Dataset, DataLoader
import torchvision.transforms as transforms
import numpy as np
from PIL import Image
from sklearn.model_selection import train_test_split

# transforms
transform = transforms.Compose([
    transforms.Resize((224, 224)),  # resizing image to fit model input size
    transforms.ToTensor(),
])

class WaymoDataset(Dataset):
    def __init__(self, data_dir, transform=None):
        self.data_dir = data_dir
        self.transform = transform
        self.image_paths = []
        self.labels = []
        self.load_data()

    def load_data(self):
        label_map = {'car': 0, 'pedestrian': 1, 'cyclist': 2}  # maping Waymo labels to integers
        for folder in os.listdir(self.data_dir):
            label = label_map[folder]
            folder_path = os.path.join(self.data_dir, folder)
            for file in os.listdir(folder_path):
                if file.endswith('.jpg'):
                    self.image_paths.append(os.path.join(folder_path, file))
                    self.labels.append(label)

    def __len__(self):
        return len(self.image_paths)

    def __getitem__(self, idx):
        img_path = self.image_paths[idx]
        label = self.labels[idx]
        img = Image.open(img_path).convert('RGB')

        if self.transform:
            img = self.transform(img)

        return img, label

# NN model for distillation
class DistillationModel(torch.nn.Module):
    def __init__(self, num_classes):
        super(DistillationModel, self).__init__()
        self.model = YourPretrainedModel()  # Use a pre-trained model as the backbone
        self.fc = torch.nn.Linear(YourPretrainedModelOutputSize, num_classes)  # Output layer

    def forward(self, x):
        features = self.model(x)
        output = self.fc(features)
        return output

# HP
batch_size = 32
lr = 0.001
num_epochs = 10

# datasets and dataloaders
data_dir = '/Users/apurva/Desktop/Apurva/Columbia/SEM2/Distillation/waymo-open-dataset/src/waymo_open_dataset'
waymo_dataset = WaymoDataset(data_dir, transform=transform)
train_dataset, val_dataset = train_test_split(waymo_dataset, test_size=0.2, random_state=42)

train_loader = DataLoader(train_dataset, batch_size=batch_size, shuffle=True)
val_loader = DataLoader(val_dataset, batch_size=batch_size, shuffle=False)

# model
num_classes = 3  # no of classes (car, pedestrian, cyclist)
model = DistillationModel(num_classes)

# loss function and optimizer
criterion = torch.nn.CrossEntropyLoss()
optimizer = torch.optim.Adam(model.parameters(), lr=lr)

# trainig loop
for epoch in range(num_epochs):
    model.train()
    for images, labels in train_loader:
        optimizer.zero_grad()
        outputs = model(images)
        loss = criterion(outputs, labels)
        loss.backward()
        optimizer.step()

    # valdn loop
    model.eval()
    val_loss = 0.0
    correct = 0
    total = 0
    with torch.no_grad():
        for images, labels in val_loader:
            outputs = model(images)
            loss = criterion(outputs, labels)
            val_loss += loss.item()
            _, predicted = torch.max(outputs, 1)
            total += labels.size(0)
            correct += (predicted == labels).sum().item()

    val_loss /= len(val_loader)
    accuracy = 100 * correct / total
    print(f'Epoch [{epoch+1}/{num_epochs}], Loss: {val_loss:.4f}, Accuracy: {accuracy:.2f}%')

# save the trained model
torch.save(model.state_dict(), 'distillation_model.pth')

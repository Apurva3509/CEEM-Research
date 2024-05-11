# Deep Learning CE

This repository contains code files for CIEN9101: Civil Engineering Research project.

## Overview

This repository contains code for processing the Waymo dataset to detect objects in camera images and generate control signals based on the detected objects and LiDAR information. The generated signals can be used to assist in autonomous vehicle navigation and decision-making.

## Features

- **Data Processing**: Preprocesses LiDAR data to identify clusters of points representing objects.
- **Object Detection**: Utilizes a trained object detection model to detect objects in camera images.
- **Signal Generation**: Generates control signals based on the detected objects and LiDAR information, indicating potential obstacles or safe paths for the autonomous vehicle.

## Requirements

- Python 3.x
- Libraries:
  - `torch`
  - `numpy`
  - `waymo_open_dataset`
  - `scikit-learn`

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/Apurva3509/CEEM-Research.git
    ```

2. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Waymo dataset
- Website: https://waymo.com/open
- GitHub: https://github.com/waymo-research/waymo-open-dataset


## Usage

1. Download the Waymo dataset and specify the dataset path in the `process_waymo_dataset` function.
2. Run the main script.
3. The program will process LiDAR data and camera images from the Waymo dataset, detect objects, and generate control signals.


## Project Timeline

### January

- **Week 1-2**: Introduction to ongoing projects in DITECT lab. Finalize project scope and objectives with Zhaobin.

### February

- **Weeks 1-4**: Dive deep into understanding data distillation and condensation techniques. Conduct extensive literature review to grasp the underlying mathematical concepts. Begin coding implementation.

### March

- **Week 1**: Explore the Waymo dataset for autonomous navigation, gaining insights into its structure and contents.
- **Week 3**: Dive deeper into the Waymo dataset, focusing on visualization and further literature review. 

### April

- **All Weeks**: Implement control signal generation algorithms using Waymo dataset frames. Address any challenges, including resolving GCP dataloader issues for handling large data volumes.

### May

- **Week 1**: Focus on final exams and report preparation. Ensure code modularity and documentation.
- **Week 2**: Finalize the project report, summarizing findings, methodologies, and outcomes.

This structured timeline delineates each month's activities, ensuring a comprehensive understanding of tasks and milestones throughout the project duration.


## Future Work

While the current implementation focuses on generating control signals based on static frames from the Waymo dataset, future work could explore the possibility of incorporating multiple frames to better capture the complexities of the vehicle's surroundings. This enhancement could provide more comprehensive information about dynamic changes in the environment, such as moving objects, changing road conditions, and varying traffic patterns.

### Utilizing Temporal Information

By leveraging multiple consecutive frames, the system could analyze the temporal evolution of the scene, allowing for better prediction and understanding of the vehicle's immediate surroundings. This approach could enhance the robustness and accuracy of the control signal generation process, especially in dynamic and rapidly changing scenarios.

### Integration of Motion Estimation Techniques

Incorporating motion estimation techniques could further improve the system's ability to track moving objects and anticipate their future trajectories. Techniques such as optical flow analysis and Kalman filtering could be utilized to estimate the motion of objects across frames, enabling more precise control signal generation.

### Deep Learning-based Approaches

Deep learning models, such as recurrent neural networks (RNNs) and convolutional neural networks (CNNs), could be employed to process sequential frames and extract relevant spatiotemporal features. These models have shown promising results in various computer vision tasks, including object detection and motion prediction, and could be adapted to enhance control signal generation in autonomous vehicles.

### Real-time Implementation and Testing

Once developed, the enhanced system should undergo rigorous testing and validation in real-world scenarios. This would involve deploying the system in simulated and on-road environments to evaluate its performance under diverse conditions and validate its effectiveness in improving autonomous vehicle navigation and decision-making.

Incorporating multiple frames into the control signal generation process represents an exciting avenue for future research, offering the potential to enhance the safety, efficiency, and autonomy of self-driving vehicles in complex real-world environments.




## Contributing

Contributions are welcome! If you'd like to contribute to this project, please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/improvement`).
3. Make your changes.
4. Commit your changes (`git commit -am 'Add new feature'`).
5. Push to the branch (`git push origin feature/improvement`).
6. Create a new Pull Request.


## Acknowledgements

- This project was inspired by the Waymo Open Dataset.
- Thanks to Zhaobin Mo and Professor Sharon Di for the opportunity to work on the project.

## Contact

For any inquiries or feedback, please contact [Apurva patel] at [apurva.patel@columbia.edu].

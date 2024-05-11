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


## Timeline of work

- **Jan 1st week and 2nd week**: Introduction to projects ongoing in DITECT lab and finalizing project with Zhaobin.

- **Feb all 4 weeks**: Understanding data distillation and data condensation, coding for it with extensive literature survey, and understanding the complex mathematics involved.

- **March 1st week**: Understanding Waymo dataset for autonomous navigation.

- **March 2nd week**: Spring break.

- **March 3rd week**: Understanding Waymo dataset, visualizing it, and literature survey for it.

- **April all 4 weeks**: Control signal generation from frames in the Waymo dataset and solving GCP dataloader issue for high volume data.

- **May 1st week**: Finals week and report making with making the code modular.

- **May 2nd week**: Final report.



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

# Edge AI Aerial Object Detection
An edge-deployed aerial object detection system developed for intelligent UAV surveillance. This project implements a real-time perception module using YOLOv8, optimized to run on a Raspberry Pi 5 for detecting people from aerial imagery. The detector forms the first stage of a distributed UAV surveillance architecture, identifying potential events and triggering downstream processing only when relevant objects are detected.

---

## Overview

Traditional UAV surveillance systems continuously transmit video streams to a ground station for analysis. This approach consumes significant bandwidth, increases latency, and wastes computational resources when no relevant events are present.

This project addresses these challenges by performing object detection directly on the UAV. A lightweight YOLOv8 model processes live camera frames on a Raspberry Pi 5, detects people in real time, and triggers event recording whenever a target is identified. Only relevant clips and detection metadata are transmitted to the ground station for further analysis, resulting in a more efficient and scalable surveillance system.

---

## Features

* Real-time aerial person detection
* Edge AI deployment on Raspberry Pi 5
* YOLOv8-based object detection
* Optimized NCNN inference
* Event-triggered video recording
* Confidence-based detection filtering
* Integration with a distributed UAV surveillance system
* Low-latency edge inference

---

## System Architecture

The object detection module follows the pipeline below:

```
USB Camera
      │
      ▼
Frame Capture
      │
      ▼
Image Preprocessing
      │
      ▼
YOLOv8 Inference
      │
      ▼
Object Detection
      │
      ▼
Confidence Thresholding
      │
      ▼
Bounding Box Generation
      │
      ▼
Trigger Video Recording
      │
      ▼
Generate Detection Metadata
      │
      ▼
Transmit Event to Ground Station
```

This repository implements the perception layer of the overall surveillance architecture.

---

## Hardware

| Component      | Purpose                      |
| -------------- | ---------------------------- |
| Raspberry Pi 5 | Edge computing platform      |
| USB Camera     | Real-time image acquisition  |
| MicroSD Card   | Operating system and storage |
| LTE USB Modem  | Network communication        |
| Power Supply   | Raspberry Pi power           |

---

## Software Stack

| Technology  | Purpose                      |
| ----------- | ---------------------------- |
| Python      | Primary programming language |
| YOLOv8      | Object detection model       |
| OpenCV      | Image capture and processing |
| Ultralytics | Model training and export    |
| NCNN        | Optimized edge inference     |

---

## Dataset

### Dataset Source

The detector was trained using an aerial object detection dataset consisting of aerial images of people collected from publicly available datasets.

### Target Class
* Person

### Annotation Format
YOLO bounding box format.

### Dataset Split
* Training Set
* Validation Set
* Test Set

### Data Augmentation
Data augmentation techniques were applied during training to improve model robustness for aerial imagery.

---

## Model Development
The detector was developed using the following workflow:

1. Dataset preparation and annotation
2. YOLOv8 model training
3. Model validation
4. Selection of the best-performing weights
5. Export to NCNN format
6. Deployment on Raspberry Pi 5
7. Integration with the UAV surveillance pipeline

---

## Deployment

The trained YOLOv8 model was converted to NCNN format to improve inference performance on the Raspberry Pi 5. The deployed detector continuously processes incoming camera frames and performs real-time inference while maintaining a lightweight computational footprint suitable for edge devices.

When a valid detection is made, the system records a short video clip and generates metadata that is transmitted to the ground station for additional analysis.

---

## Detection Pipeline

```
Capture Frame
      │
      ▼
Resize & Preprocess
      │
      ▼
YOLOv8 Inference
      │
      ▼
Filter by Confidence
      │
      ▼
Draw Bounding Boxes
      │
      ▼
Trigger Event Recording
      │
      ▼
Generate Detection Metadata
```

---

## Performance

| Metric       | Result |
| ------------ | ------ |
| Precision    | 0.8308 |
| Recall       | 0.7277 |
| mAP@0.5      | 0.7934 |
| mAP@0.5:0.95 | 0.5226 |

The detector achieved reliable performance for real-time aerial person detection while remaining lightweight enough for deployment on edge hardware.

---

## Sample Results

Include screenshots demonstrating:

* Successful person detection
* Bounding box visualization
* Detection under different flight altitudes
* Detection under different lighting conditions

---

## Challenges

Some of the engineering challenges encountered during development included:

* Optimizing inference for resource-constrained edge hardware.
* Balancing detection accuracy with real-time performance.
* Maintaining reliable detections from aerial viewpoints.
* Reducing unnecessary event recordings while minimizing missed detections.

---

## Lessons Learned

This project demonstrated that deploying computer vision models on embedded hardware requires more than achieving high validation accuracy. Practical deployment demands optimization of inference speed, efficient resource utilization, and seamless integration with communication and event-processing pipelines.

---

## Future Improvements

Potential future enhancements include:
* Object tracking
* Model quantization
* Edge TPU acceleration
* Dynamic confidence thresholding
* Multi-camera support
* Integration with object re-identification

---

## Related Projects

This repository is part of a larger distributed UAV surveillance system.

* UAV Edge AI Surveillance System
* Remote Video and Data Streaming System
* Ground Station Action Recognition
* UAV Autonomous Navigation

---

## License

This project is released under the MIT License.

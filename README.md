# Opencv-Finger-Detector
A simple real-time hand tracking and finger labeling application using Python, OpenCV, and cvzone's MediaPipe wrapper. Ideal for HCI, AR/VR, and robotics.

# Real-Time Hand Tracking & Finger Labeling Engine
A high-performance computer vision application built in **Python** that detects, tracks, and individually labels human fingers in real-time via a live webcam feed. 

By leveraging **Google’s MediaPipe** hand topology framework (abstracted via the **cvzone** library), the system maps **21 distinct structural landmarks** on the human hand to establish precise spatial coordinate awareness.

## 🚀 Key Features

* **Real-Time Spatial Detection:** Processes live video feeds using **OpenCV** with minimal latency.
* **Landmark Mapping:** Extracts 3D coordinates for all 21 key skeletal joints of the hand.
* **Targeted Finger Labeling:** Isolates the coordinate points for individual fingertips (Thumb, Index, Middle, Ring, Pinky), highlighting them with visual anchors and custom text overlays.
* **Broad Core Applications:** Serves as a foundation for Human-Computer Interaction (HCI), sign language translation, AR/VR menu navigation, and robotics control.

## 🛠️ Tech Stack

* **Language:** Python 3.x
* **Core Vision Framework:** OpenCV (`cv2`)
* **Tracking Wrapper:** `cvzone` (HandTrackingModule powered by Google MediaPipe)

## 📋 Prerequisites

Before running the project, ensure you have a working webcam and the following dependencies installed:

```bash
pip install opencv-python cvzone mediapipe
```

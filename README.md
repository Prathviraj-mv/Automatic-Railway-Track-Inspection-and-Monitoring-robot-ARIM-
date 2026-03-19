

# 🚆 ARIM – Automatic Railway Inspection & Monitoring Robot

Autonomous rail-mounted inspection robot that detects track defects using edge AI and marks damaged locations in real time.

---

## 📌 Overview

ARIM is a robotic system designed for continuous railway track monitoring. It uses a **Raspberry Pi 5 running MobileNetV2** to perform real-time defect detection directly on-device (edge AI), eliminating cloud dependency.

The system not only detects faults but also:
- Sends GPS coordinates to the operator
- Marks the faulty region physically using a paint mechanism

---

## ⚙️ Key Features

- 🧠 **Edge AI Detection**
  - Real-time defect detection using MobileNetV2
  - Runs directly on Raspberry Pi 5

- 🚄 **Rail-Compatible Locomotion**
  - Custom-designed rover that runs on railway tracks
  - Stable and aligned wheel system

- 📍 **Location Tracking**
  - GPS module provides coordinates of detected faults

- 📡 **Remote Communication**
  - GSM module sends alerts and data to operator

- 🎯 **Physical Fault Marking**
  - Paint mechanism marks damaged track sections

- 🌙 **Day/Night Operation**
  - LDR-based automatic lighting system

- 🔋 **Hybrid Power System**
  - Battery-powered with solar charging support

---

## 🛠️ Hardware Components

- Raspberry Pi 5  
- Camera module  
- GPS module  
- GSM module  
- LDR sensor + LED lighting  
- Motor driver (BTS7960)
- Servo Driver (PCA6986)
- Geared DC motors  
- Custom rail wheels  
- Paint marking mechanism  
- Solar panel + battery pack  

---

## 💻 Software Stack

- Python  
- PyTorch / TorchVision  
- OpenCV  
- Raspberry Pi OS (Linux)  

---

## 🧪 AI Model

- Model: **MobileNetV2**
- Type: Convolutional Neural Network (CNN)
- Purpose: Detect track defects from captured images

### Pipeline:
1. Capture image from camera
2. Preprocess (resize, normalize)
3. Run inference using CNN
4. Classify:
   - Crack
   - Misalignment
   - Surface wear
   - Normal

---



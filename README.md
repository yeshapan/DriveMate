## DriveMate: Driver Drowsiness Detection with Voice Alerts
*A basic demo for driver drowsiness detection with voice alerts – prototype for future in-car AI.*

---

## Overview

**DriveMate** is a proof-of-concept driver monitoring system built to detect signs of drowsiness using facial cues and trigger **voice-based alerts** in real time. 
This early demo helps us visualize detection workflows, and serves as a stepping stone toward a more robust automotive safety solution.
> Note that this current project is just a prototype. The expected upgrades (work-in-progress) are listed below

---

## Features

-  Basic drowsiness detection using eye aspect ratio (EAR)
-  Instant voice alerts when drowsiness is detected
-  Real-time camera feed processing using OpenCV
-  Visual debugging overlay for eye tracking and EAR value
-  Demo-level implementation to validate core ideas


## Upcoming Improvements

We plan to expand this project in future iterations with the following upgrades:

-  **Upgrade to YOLOv10** for enhanced facial landmark precision
-  **Low-light condition support**: Training with low-light driving datasets + CV-based light detection
-  **Edge integration** with in-car **infotainment systems** like NVIDIA Jetson (Nano/Orin)
-  **Wearable integration** for haptic (vibration) alerts on smart bands or smartwatches
-  Logging and analytics for long-duration fatigue pattern detection


## Repository Structure

```bash
DriveMate
├── data/              #contains data used for training, including images and annotations.
│   └── labels/        #stores label files (e.g., YOLO format) corresponding to the images.
├── labelImg/          
├── src/               #source code directory for the main application logic.
├── yolov5/            #contains the YOLOv5 repository or relevant files for object detection.
├── .gitignore         #specifies intentionally untracked files to ignore.
├── poetry.lock        #records exact versions of project dependencies managed by Poetry.
├── pyproject.toml     #defines project metadata and dependencies for Poetry.
```
---
## Approach - A note from our team
Hey fellow tech enthusiasts and sleepless hackathon judges!  
As 20-something CS students who've pulled one too many all-nighters, we know one undeniable truth:

> The secret sauce to any brainy AI project? **Seriously good data.**

This repo? It’s where the groundwork happens. Before the real AI magic kicks in, we’re teaching our model to *see* drowsiness — one perfectly labeled image at a time.


### Hooking Up with YOLO: Our AI’s First "Eye-Opener"

While our ultimate mission is **specialized driver drowsiness detection** using YOLOv10 (because nobody wants a sleepy co-pilot!), we started by integrating a robust, pre-trained `YOLOv5s`.

### So... What’s YOLOv5s?
- It’s like the starter pack of the legendary **You Only Look Once** family, by Ultralytics.
- Known for being **blazingly fast** and **shockingly accurate** at real-time object detection.
- We’re basically giving our AI a solid pair of *pre-trained eyes* to begin its vision journey.
- We'll later **fine-tune** this model for the subtle art of detecting:  
  > “Are they dozing… or just deep in thought about life?” 

### Our “Photo Shoot” Pipeline (No Glam Squad Needed)
To teach our AI the difference between a wide-eyed driver and one about to nap on the wheel, we built a simple, efficient image collection script.

### Here's How It Works:
-  **Plugs into your webcam** – no fancy hardware needed!
-  You choose your label: `"awake"` or `"drowsy"`  
-  Captures a *fixed number of images* per label (default is **20**, but easily configurable)
-  Stores them cleanly in a structured dataset:  
  `data/images/awake/` and `data/images/drowsy/`

####  Real-Time Staring Contest & Smart Labeling
Let’s just say… we spent more time awkwardly watching ourselves on webcam than we’d like to admit. 

But here's the cool part:

-  **Live frame previews** while capturing (like a real-time mirror!)
-  **Each image is saved with a unique filename** using `uuid` (bye-bye, duplicates)
-  Super-organized folder structure with clear labeling
-  Result: a **clean, model-ready dataset** (because a messy dataset = confused AI =  sleepy mistakes)


####  Why This Matters: Laying the Foundation
This isn’t just a script. It’s **step 1** of teaching our AI to understand real-world driver behavior.

By creating this robust image dataset, we’re laying the foundation for:

- Accurate driver state detection
- Future YOLOv10 upgrades
- Potential integration with **infotainment systems** (like NVIDIA Jetson in-car kits!)

We’re empowering **DriveMate** to be your always-alert, never-complaining digital co-pilot — no more “Are you even awake?!” shouts from the passenger seat.

## Tech Stack & Tools

- Python + OpenCV
- YOLOv5s (Ultralytics)
- UUID for clean image naming
- Simple CLI interface for data collection
- Directory structure auto-generated and maintained

## Coming Soon

- [ ] Upgrade to YOLOv10 for better performance in **low-light driving conditions**
- [ ] Collect data from **real-world drivers** (not just us sleep-deprived students 😅)
- [ ] Integrate with **Jetson Nano / Xavier** for real-time in-car deployment
- [ ] Add computer vision-based **low-light enhancement** preprocessing

---


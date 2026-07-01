from ultralytics import YOLO
import numpy as np
import time
import cv2 as cv
import math
import logging
import threading

logger = logging.getLogger(__name__)  # Get a logger for this module

model = YOLO('') #change this 

CLASS_NAMES = ['fire_smoke', 'person', 'vehicle']

VIDEO_FPS = 10
VIDEO_DURATION = 10  # seconds

shared.last_event_time = 0
EVENT_COOLDOWN_SEC = 20   # choose 15–30 seconds

DETECTION_INTERVAL = 0.5
last_detection_time = 0

'''
Format for detections 
detections = [
    {
        "class": "person",
        "bbox": [120, 90, 340, 400]   # [x1, y1, x2, y2]
    },
    {
        "class": "fire",
        "bbox": [500, 200, 640, 480]
    }
]
'''

def init_cam(resolution=(640, 480), device_index=0):
    """
    Initializes a USB camera and returns a function that captures frames,
    similar to the Picamera2 version.
    """
    cap = cv.VideoCapture(device_index)

    if not cap.isOpened():
        raise RuntimeError("[ERROR] Could not open USB camera")

    # Set resolution
    cap.set(cv.CAP_PROP_FRAME_WIDTH, resolution[0])
    cap.set(cv.CAP_PROP_FRAME_HEIGHT, resolution[1])

    # Try MJPEG for better performance (falls back automatically if unsupported)
    cap.set(cv.CAP_PROP_FOURCC, cv.VideoWriter_fourcc(*"MJPG"))  # type: ignore
    logging.info("[VISION] USB Camera initialized.")

    def get_frame():
        ret, frame = cap.read()
        if not ret:
            logging.warning("[WARNING] Frame capture failed. Retrying...")
            return None
        return frame
    return get_frame, cap


def detect_and_track(frame):
    logging.info("[VISION] Object Detection Started.")
    results = model(frame, conf=0.5, imgsz=320)

    detections = [] #list for overall detections

    for r in results:
        for box in r.boxes:
            x1, y1, x2, y2 = map(int, box.xyxy[0])
            conf = math.ceil((box.conf[0] * 100)) / 100
            cls = int(box.cls[0])
            current_class = class_names[cls]
            if current_class == "fire_smoke":
                if conf < 0.8:
                    continue
            #append values to objects dictionary
            obj = {
                "class": current_class,
                "bbox": [x1, y1, x2, y2]
            }
            #append values to detections list
            detections.append(obj)
    time.sleep(0.5)
    return detections

#to start video
get_frame, cam = init_cam()

while True:
  detect_and_track(get_frame)

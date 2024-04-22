# Andrew Kozempel
# CMPSC 497
# Lab 5

import cv2
from IPython.display import display, Image
import ipywidgets as widgets

# This is the camera location that needs to be input into the VideoCapture arugments in order to
# properly locate the camera and access it.
camera_pipeline = "nvarguscamerasrc sensor-id=0 ! video/x-raw(memory:NVMM), width=640, height=480, format=(string)NV12, framerate=(fraction)30/1 ! nvvidconv ! video/x-raw, width=(int)640, height=(int)480, format=(string)BGRx ! videoconvert ! appsink"

# CAP_GSTREAM is the type of feed the camera uses in order to display the image. Both
# arguments are required.
camera = cv2.VideoCapture(camera_pipeline, cv2.CAP_GSTREAMER)

# This loop is here since the first few frames taken by the camera are dark. This allows it to take a
# few moments to adjust the picture quality.
for i in range(100):
    __, frame = camera.read()

# Converts the image to jpeg fromat.
__, frame = cv2.imencode('.jpeg', frame)

# This converts the frame image to bytes so it can be displayed.
frame = Image(data=frame.tobytes())

# Displays the picture.
display(frame)

# Turns off the camera.
camera.release()
# Andrew Kozempel
# CMPSC 497
# Lab 6

import cv2
from IPython.display import display, Image
import ipywidgets as widgets
import threading

# This is the camera location that needs to be input into the VideoCapture arugments 
# in order to properly locate the camera and access it.
camera_pipeline = "nvarguscamerasrc sensor-id=0 ! video/x-raw(memory:NVMM), width=640, height=480, format=(string)NV12, framerate=(fraction)30/1 ! nvvidconv ! video/x-raw, width=(int)640, height=(int)480, format=(string)BGRx ! videoconvert ! appsink"

# CAP_GSTREAM is the type of feed the camera uses in order to display the image. 
# Both arguments are required.
camera = cv2.VideoCapture(camera_pipeline, cv2.CAP_GSTREAMER)

# This is a simple button that follows most GUI library standards. This button is 
# important because it allows the program to have a way to stop the video so 
# the camera is still not running after the program has stopped.
stopButton = widgets.ToggleButton(
value=False,
description='Stop',
disabled=False,
button_style='danger',
tooltip='Description',
icon='square'
)

# The main part of the program where the camera rapidly takes images in a loop and displays them.
def view(button):

    display_handle = display(None, display_id=True) # Displays the image box.

    while True:

        # Reads the information from the camera and returns a value to frame.
        _, frame = camera.read()

        # Converts the information to jpeg to it can be displayed properly.
        _, frame = cv2.imencode('.jpeg', frame)

        # Updates the image box to display the updated frame. A conversion to bytes here is needed.
        display_handle.update(Image(data=frame.tobytes()))
        
        # Checks to see if the button was pressed which will stop the camera from functioning.
        if stopButton.value == True:
            camera.release()
            display_handle.update(None)

# Displays the stopButton.
display(stopButton)

# Connects the stopButton to view.
thread = threading.Thread(target=view, args=(stopButton,))
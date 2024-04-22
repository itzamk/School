# Andrew Kozempel
# CMPSC 497
# Lab 6b

import cv2
import numpy as np
from IPython.display import display, Image
import ipywidgets as widgets
import threading

# This is the camera location that needs to be input into the VideoCapture arugments in order to
# properly locate the camera and access it.
camera_pipeline = "nvarguscamerasrc sensor-id=0 ! video/x-raw(memory:NVMM), width=640, height=480, format=(string)NV12, framerate=(fraction)30/1 ! nvvidconv ! video/x-raw, width=(int)640, height=(int)480, format=(string)BGRx ! videoconvert ! appsink"

# Initialize the video capture object
cap = cv2.VideoCapture(camera_pipeline, cv2.CAP_GSTREAMER)

# The main part of the program where the camera rapidly takes images in a loop and displays them.
def view(button):
    
    display_handle = display(None, display_id=True) # Displays the image box.
    
    while True:
        
        # Read the current frame from the camera
        ret, frame = cap.read()
        
        # Convert the frame from BGR to RGB color space
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        
        # Define the lower and upper bounds for the red color in RGB
        lower_red = np.array([112, 0, 0])
        upper_red = np.array([255, 80, 80])
        
        # Create a mask for the red color
        mask = cv2.inRange(rgb, lower_red, upper_red)
        
        # Apply morphological operations to remove noise
        kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
        mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
        mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
        
        # Find contours of the red objects in the mask
        contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        
        # Draw bounding boxes around the red objects
        for contour in contours:
            x, y, w, h = cv2.boundingRect(contour)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        
        # Converts the information to jpeg to it can be displayed properly.
        _, frame = cv2.imencode('.jpeg', frame)
        
        # Updates the image box to display the updated frame. A conversion to bytes here is needed.
        display_handle.update(Image(data=frame.tobytes()))
        
        # Checks to see if the button was pressed which will stop the camera from functioning.
        if stopButton.value == True:
            cap.release()
            display_handle.update(None)

# This is a simple button that follows most GUI library standards. This button 
# is important because it allows the program to have a way to stop the video 
# so the camera is still not running after the program has stopped.
stopButton = widgets.ToggleButton(
    value=False,
    description='Stop',
    disabled=False,
    button_style='danger',
    tooltip='Description',
    icon='square'
)

# Displays the stopButton.
display(stopButton)

# Connects the stopButton to view.
thread = threading.Thread(target=view, args=(stopButton,))
thread.start()
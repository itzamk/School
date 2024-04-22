# A program that uses the camera to detect a red object and draw a bounding box around it.
from jetbot import Robot
from IPython.display import display, Image
import cv2
import numpy as np
import ipywidgets as widgets
import threading
import time


def start_spinning():
    robot.set_motors(0.15, -0.15)
    time.sleep(0.5)


def stop_spinning():
    robot.stop()


def move_left():
    robot.left(0.10)
    time.sleep(0.5)


def move_right():
    robot.right(0.10)
    time.sleep(0.5)


def move_straight():
    robot.forward(0.1)
    time.sleep(0.5)


def calculate_center(left, top, width, height):
    return left + width // 2, top + height // 2


# This is the camera location that needs to be input into the VideoCapture arguments in order to properly locate the
# camera and access it.
camera_pipeline = ("nvarguscamerasrc sensor-id=0 ! video/x-raw(memory:NVMM), width=640, height=480, "
                   "format=(string)NV12, framerate=(fraction)30/1 ! nvvidconv ! video/x-raw, width=(int)640, "
                   "height=(int)480, format=(string)BGRx ! videoconvert ! appsink")
is_spinning = True  # Flag to control spinning.
display_camera = True  # Flag to control camera display.

# Initialize the video capture object.
camera = cv2.VideoCapture(camera_pipeline, cv2.CAP_GSTREAMER)
robot = Robot()
#start_spinning()

while True:

    # Read the current frame from the camera.
    ret, frame = camera.read()

    # Convert the frame from BGR to RGB color space.
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Define the lower and upper bounds for the red color in RGB.
    lower_red = np.array([150, 0, 0])
    upper_red = np.array([255, 80, 80])

    # Create a mask for the red color.
    mask = cv2.inRange(rgb, lower_red, upper_red)

    # Apply morphological operations to remove noise.
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
    mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)

    # Find contours of the red objects in the mask.
    contours, _ = cv2.findContours(
        mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    # If there is at least one detected contour, continue.
    if len(contours) > 0:

        # Stop spinning if it's currently spinning.
        stop_spinning()

        # Record the area from each contour.
        areas = [cv2.contourArea(contour) for contour in contours]

        # Save the index of the largest area.
        largest_area_index = np.argmax(areas)

        # Draw a blue bounding box around the largest red object.
        x, y, w, h = cv2.boundingRect(contours[largest_area_index])

        # Find the center of the largest bounding box.
        center = calculate_center(x, y, w, h)

        # Calculate regions based on the frame's width.
        frame_width = frame.shape[1]
        column_width = frame_width // 3
        left_column = column_width
        center_column = 2 * column_width

        # If center of largest red object is located in left region, move left.
        if center[0] < left_column:
            move_left()
            print('left')

        # If center largest red object is located in right region, move right.
        elif center[0] > center_column:
            move_right()
            print('right')

        # If center largest red object is located in center region, move straight.
        while left_column <= center[0] < center_column:
            move_straight()
            print('straight')

    else:
        # Start spinning if no contours are detected.
        start_spinning()


# This is a simple button that follows most GUI library standards. This button is important because it allows the
# program to have a way to stop the video so the camera is still not running after the program has stopped.
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
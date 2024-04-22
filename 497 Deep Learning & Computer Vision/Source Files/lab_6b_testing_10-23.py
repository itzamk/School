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
    robot.forward(0.10)
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
start_spinning()


# The main part of the program where the camera rapidly takes images in a loop and displays them.
def view(button):
    global is_spinning, display_camera
    display_handle = display(None, display_id=True)  # Displays the image box.
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
        # Draw green bounding boxes around the red objects.
        for contour in contours:
            x, y, w, h = cv2.boundingRect(contour)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            # If there is at least one detected contour, continue.
        if len(contours) > 0:
            # Stop spinning if it's currently spinning.
            if is_spinning:
                stop_spinning()
                is_spinning = False
            # Record the area from each contour.
            areas = [cv2.contourArea(contour) for contour in contours]
            # Save the index of the largest area.
            largest_area_index = np.argmax(areas)
            # Draw a blue bounding box around the largest red object.
            x, y, w, h = cv2.boundingRect(contours[largest_area_index])
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
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
            # If center largest red object is located in center region, move straight.
            elif left_column <= center[0] < center_column:
                move_straight()
            # If center largest red object is located in right region, move right.
            else:
                move_right()
            if display_camera:
                # Converts the information to jpeg to it can be displayed properly.
                _, frame = cv2.imencode('.jpeg', frame)
                # Updates the image box to display the updated frame. A conversion to bytes here is needed.
                display_handle.update(Image(data=frame.tobytes()))
                # Disable camera display when contours are detected.
                display_camera = False
        else:
            # Start spinning if no contours are detected.
            start_spinning()
            is_spinning = True
            # Enable camera display when no contours are detected.
            display_camera = True
            # Display the camera feed only when display_camera is True.
        if display_camera:
            # Converts the information to jpeg to it can be displayed properly.
            _, frame = cv2.imencode('.jpeg', frame)
            # Updates the image box to display the updated frame. A conversion to bytes here is needed.
            display_handle.update(Image(data=frame.tobytes()))
        # Checks to see if the button was pressed which will stop the camera from functioning.
        if stopButton.value:
            camera.release()
            display_handle.update(None)


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
# Andrew Kozempel
# CMPSC 497
# Lab 8

import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt


def canny(image):
    # convert to grayscale
    gray = cv.cvtColor(image, cv.COLOR_RGB2GRAY)
    # apply gaussian blur
    blur = cv.GaussianBlur(gray, (5,5), 0)
    # canny edge detection
    canny = cv.Canny(blur, 50, 150)

    # return binary/edge image
    return canny

def display_lines(image, lines):
    # make a copy of image
    line_image = np.copy(image)

    # if there are lines
    if lines is not None:
        for line in lines:

            # start and end coords of line
            x1, y1, x2, y2 = line.reshape(4)
            # draw line on image
            cv.line(line_image, (x1, y1), (x2, y2), (0, 0, 255), 10)
            # calculate and print line angle
            angle = np.arctan2(y2 - y1, x2 - x1) * 180.0 / np.pi
            print(f"Angle of line: {angle}")

    # return original image with drawn lines
    return line_image

def region_of_interest(image):
    # get dimensions of image
    height, width = image.shape[0], image.shape[1]
    # triangle region of interest
    polygons = np.array([[(4*width//10, height), (width, height), (width//2, 250)]])
    # create mask with image dimensions
    mask = np.zeros_like(image)
    # fill ROI with white
    cv.fillPoly(mask, polygons, 255)
    # bitwiseAND image and mask
    masked_image = cv.bitwise_and(image, mask)

    return masked_image

# read first image and process
image = cv.imread('road4.jpg')
lane_image = np.copy(image)
canny1 = canny(lane_image)
cropped_image = region_of_interest(canny1)

# use houghline to detect lines and display
lines = cv.HoughLinesP(cropped_image, 2, np.pi/180, 100, np.array([]), minLineLength=180, maxLineGap=4)
print("\nImage 1 line angles:")
line_image = display_lines(lane_image, lines)
cv.imshow("results", line_image)

# read first image and process
image2 = cv.imread('road7.jpeg')
lane_image2 = np.copy(image2)
canny2 = canny(lane_image2)
cropped_image2 = region_of_interest(canny2)

# use houghline to detect lines and display
lines2 = cv.HoughLinesP(cropped_image2, 2, np.pi/180, 100, np.array([]), minLineLength=180, maxLineGap=4)
print("\nImage 2 line angles:")
line_image2 = display_lines(lane_image2, lines2)
cv.imshow("results 2", line_image2)
    
    
cv.waitKey(0)
cv.destroyAllWindows()
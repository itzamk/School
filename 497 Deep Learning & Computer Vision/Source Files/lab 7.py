# Andrew Kozempel
# CMPSC 497
# Lab 7

import cv2 as cv
import numpy as np

# set up camera
cap = cv.VideoCapture(0)

while(1):
    # Take each frame
    _, frame = cap.read()

    # Convert BGR to HSV
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

    # define range of blue color in HSV
    lower_blue = np.array([110,50,50])
    upper_blue = np.array([130,255,255])
    
    # Threshold the HSV image to get only blue colors
    blue_mask = cv.inRange(hsv, lower_blue, upper_blue)
    blue_kernel = cv.getStructuringElement(cv.MORPH_ELLIPSE, (4, 4))
    blue_mask = cv.morphologyEx(blue_mask, cv.MORPH_OPEN, blue_kernel)
    blue_mask = cv.morphologyEx(blue_mask, cv.MORPH_CLOSE, blue_kernel)

    # get blue contours
    blue_contours, _ = cv.findContours(blue_mask, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
    
    # if blue items are found
    if blue_contours:

        # find max contour based on key (contour area)
        blue_largest_contour = max(blue_contours, key=cv.contourArea)
        
        # reset mask to 0s to redraw largest contour
        blue_mask[:] = 0

        # draw contour (image, contour(s), index, color:white, fill contour)
        cv.drawContours(blue_mask, [blue_largest_contour], -1, (255), thickness=cv.FILLED)

        # calculate centroid position
        blue_M = cv.moments(blue_largest_contour)
        blue_x = int(blue_M["m10"] / blue_M["m00"])
        blue_y = int(blue_M["m01"] / blue_M["m00"])

    # define range of red color in HSV
    lower_red = np.array([0,50,50])
    upper_red = np.array([11,255,255])

    # Threshold the HSV image to get only red colors
    red_mask = cv.inRange(hsv, lower_red, upper_red)
    red_kernel = cv.getStructuringElement(cv.MORPH_ELLIPSE, (4, 4))
    red_mask = cv.morphologyEx(red_mask, cv.MORPH_OPEN, red_kernel)
    red_mask = cv.morphologyEx(red_mask, cv.MORPH_CLOSE, red_kernel)

    # get red contours
    red_contours, _ = cv.findContours(red_mask, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
    
    # if red items are found
    if red_contours:

        # find max contour based on key (contour area)
        red_largest_contour = max(red_contours, key=cv.contourArea)
        
        # reset mask to 0s to redraw largest contour
        red_mask[:] = 0

        # draw contour (image, contour(s), index, color:white, fill contour)
        cv.drawContours(red_mask, [red_largest_contour], -1, (255), thickness=cv.FILLED)

        # calculate centroid position
        red_M = cv.moments(red_largest_contour)
        red_x = int(red_M["m10"] / red_M["m00"])
        red_y = int(red_M["m01"] / red_M["m00"])
    
    # Bitwise-AND mask and original image
    res_blue = cv.bitwise_and(frame, frame, mask=blue_mask)
    res_red = cv.bitwise_and(frame, frame, mask=red_mask)
    res_combined = cv.addWeighted(res_blue, 1, res_red, 1, 0)

    if blue_contours:
        # draw blue centroid
        cv.circle(res_combined, (blue_x, blue_y), 5, (255, 255, 255), -1)

    if red_contours:
        # draw red centroid
        cv.circle(res_combined, (red_x, red_y), 5, (255, 255, 255), -1)

    # merge mask
    merged_mask = cv.bitwise_or(blue_mask, red_mask)

    # show images/cam feed
    cv.imshow('frame', frame)
    cv.imshow('mask', merged_mask)
    cv.imshow('res', res_combined)

    k = cv.waitKey(5) & 0xFF

    if k == 27: # escape key is 27; space is 32, etc
        break

cv.destroyAllWindows()
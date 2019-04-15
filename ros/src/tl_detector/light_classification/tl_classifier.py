import cv2
from cv_bridge import CvBridge
import os
import rospy
import numpy as np
from styx_msgs.msg import TrafficLight

class TLClassifier(object):
    def __init__(self):
        #TODO load classifier
        pass

    def get_classification(self, image):
        result = TrafficLight.UNKNOWN
        output = image.copy()
        hsv_transform = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

        lower_hue_1 = np.array([0,100,100])
        lower_hue_2 = np.array([10,255,255])
        lower_hue = cv2.inRange(hsv_transform, lower_hue_1 , lower_hue_2)

        upper_hue_1 = np.array([160,100,100])
        upper_hue_2 = np.array([179,255,255])
        upper_hue = cv2.inRange(hsv_transform, upper_hue_1 , upper_hue_2)

        converted_img = cv2.addWeighted(lower_hue, 1, upper_hue, 1, 0)

        blur_img = cv2.GaussianBlur(converted_img, (15, 15), 0)

        circles = cv2.HoughCircles(blur_img, cv2.HOUGH_GRADIENT, 0.5, 40, param1 = 70, param2 = 30, minRadius = 5, maxRadius = 150)
  
        colorized_blur_img = cv2.cvtColor(blur_img, cv2.COLOR_GRAY2BGR)

        if circles is not None:
            result = TrafficLight.RED

        return result, colorized_blur_img








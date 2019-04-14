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
        red = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

        lower_red = np.array([0,50,50])
        upper_red = np.array([10,255,255])
        red1 = cv2.inRange(red, lower_red , upper_red)

        lower_red = np.array([170,50,50])
        upper_red = np.array([180,255,255])
        red2 = cv2.inRange(red, lower_red , upper_red)

        converted_img = cv2.addWeighted(red1, 1.0, red2, 1.0, 0.0)

        blur_img = cv2.GaussianBlur(converted_img,(15,15),0)
        # blur_img = cv2.GaussianBlur(red,(15,15),0)

        circles = cv2.HoughCircles(blur_img,cv2.HOUGH_GRADIENT,0.5,41, param1=70,param2=30,minRadius=5,maxRadius=150)
        # circles = cv2.HoughCircles(blur_img,cv2.HOUGH_GRADIENT,1,60, param1=100,param2=50,minRadius=8,maxRadius=80)
        # circles = cv2.HoughCircles(blur_img, cv2.HOUGH_GRADIENT, 1, 80, param1=100, param2=50)

        colorized_blur_img = cv2.cvtColor(blur_img, cv2.COLOR_GRAY2BGR)
        
        if circles is not None:
            result = TrafficLight.RED

        return result, colorized_blur_img








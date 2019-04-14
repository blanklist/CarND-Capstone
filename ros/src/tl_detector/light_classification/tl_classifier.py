import cv2
import os
import numpy as np
from styx_msgs.msg import TrafficLight

class TLClassifier(object):
    def __init__(self):
        #TODO load classifier
        pass

    def get_classification(self, image):

        output = image.copy()

        cv2.imwrite('img_results/image.jpg', output)
        rospy.loginfo("just saved image")

        result = TrafficLight.UNKNOWN

        return result, output









        # EXPERIMENT
        # result = TrafficLight.UNKNOWN
        # output = image.copy()
        # red = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)


        # # lower_red = np.array([0,50,50])
        # # upper_red = np.array([10,255,255])
        # # red1 = cv2.inRange(red, lower_red , upper_red)


        # # lower_red = np.array([170,50,50])
        # # upper_red = np.array([180,255,255])
        # # red2 = cv2.inRange(red, lower_red , upper_red)

        # # converted_img = cv2.addWeighted(red1, 1.0, red2, 1.0, 0.0)

        # # blur_img = cv2.GaussianBlur(converted_img,(15,15),0)

        # blur_img = cv2.GaussianBlur(red, (15, 15), 0)

        # #edges = cv2.Canny(imgray,thresh,thresh*3)

        # circles = cv2.HoughCircles(blur_img,cv2.HOUGH_GRADIENT,0.5,41, param1=70,param2=30,minRadius=5,maxRadius=150)

        # found = False 
        # if circles is not None:
        #     result = TrafficLight.RED
        # #    for i in circles[0,:3]:
        # #        cv2.circle(output,(i[0],i[1]),maxRadius,(255, 100, 100),2)
      
        
        # #need to include more image, so ignore other colors
        # #green may be trees.  Just look for red lights
        # #if red_area > 40:
        # return result, output
#!/usr/bin/env python

import rospy
import cv2
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import sys
import random
def randpointgen():
	#random generator
	x = random.randint(0,194)
	y = random.randint(0,231)
	return x,y
def main(args):
    rospy.init_node('rrt_node', anonymous=True)
    print("i m in")
    try:
	cv_image = cv2.imread("/home/neha/Downloads/turtlebot/src/maps/playground1.pgm",cv2.IMREAD_UNCHANGED)
	
        sift = cv2.xfeatures2d.SIFT_create()
        #kp = sift.detect(cv_image, None)
        #cv_image = cv2.drawKeypoints(cv_image, kp, None)
	cv2.imshow("neha", cv_image)
	print(cv_image.shape)
	print(cv_image[140])
	#o/p of shape is 194,231
	#make binary file 
	
	#define start and end pose
	start = randpointgen()
	goal = randpointgen()
	
	print(start)
	print(goal)
	cv2.waitKey()
	print("m out")
    except KeyboardInterrupt:
        print("Shutting Down")
    cv2.destroyAllWindows()
if __name__ == '__main__':
    main(sys.argv)

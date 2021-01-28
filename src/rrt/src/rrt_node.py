#!/usr/bin/env python

import rospy
import cv2
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import sys
import random
import numpy as np
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
	#print(cv_image.shape)
	#print(cv_image[140])
	#o/p of shape is 194,231
	#make binary file 
	
	#define start and end pose
	start = randpointgen()
	nodes = np.array([start])
	graph = np.zeros((1,1))
	goal = randpointgen()
	print(nodes)
	print(graph)
	for i in range(100):
		rand_pt = randpointgen()
		#minimum distace among all nodes
		min_node = nodes[0]
		print(min_node)
		mini = np.linalg.norm(min_node - rand_pt)
		for i in range(len(nodes[:,0])):
			print("m here")
			print(nodes[i])
			if np.linalg.norm(nodes[i]-rand_pt)<mini:
				min_node = nodes[i]
				mini = np.linalg.norm(nodes[i] - rand_pt)	
		print(mini)
		print(min_node)
		#align in direction and fix the distance to get the node
		new_node = nodes[0]
		print(new_node)
		print(cv_image[new_node[0],new_node[1]])
		if cv_image[new_node[0],new_node[1]]>=254:
			nodes = np.array(nodes,[new_node])

		print(graph)
		print(nodes)
	cv2.waitKey()
	print("m out")
    except KeyboardInterrupt:
        print("Shutting Down")
    cv2.destroyAllWindows()
if __name__ == '__main__':
    main(sys.argv)

#!/usr/bin/env python
#pblm1 node being created inside obstacle region
#pblm2 area more than map i.e. surounding area being explored w.r.t. edge not vertices 
#pblm3 every node is related to node 1&2
#!!!!!!!!!!!!x and y have been shuffeled
#add condition for edge not being in obstacle
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
	#if cv_image[x,y]<200:
	#	randpointgen()
	return x,y

cv_image = cv2.imread("/home/neha/Downloads/turtlebot/src/maps/playground1.pgm",cv2.IMREAD_UNCHANGED)

def main(args):
    rospy.init_node('rrt_node', anonymous=True)
    print("i m in")
    try:

	cv2.imshow("neha", cv_image)
	#print(cv_image.shape)
	#print(cv_image[140])
	#o/p of shape is x=231 y=194
	#make binary file 
	#define start and end pose
	start = randpointgen()
	nodes = np.array([start])
	graph = np.zeros((1,1))
	goal = randpointgen()
	cv2.circle(cv_image, (start[0],start[1]), 3,(0),-1)
	cv2.circle(cv_image, (goal[0],goal[1]), 3,(0),-1)
	print(nodes)
	print(graph)
	while len(nodes[:,0])<100:
		rand_pt = randpointgen()
		min_node = nodes[0]
		#print(min_node)
		mini = np.linalg.norm(min_node - rand_pt)
		for i in range(len(nodes[:,0])):
			#print(nodes[i])
			if np.linalg.norm(nodes[i]-rand_pt)<mini:
				min_node = nodes[i]
				mini = np.linalg.norm(nodes[i] - rand_pt)	
		new_node = min_node+rand_pt
		new_node = new_node/2
		if(np.linalg.norm(new_node - goal)<10):
			print("goal reached")
			break
		#print(cv_image[new_node[0],new_node[1]])
		if cv_image[new_node[0],new_node[1]]>=210:
			n = len(nodes[:,0])
			graph = np.concatenate( (graph,[np.zeros(n)-1]) ,axis=0)
			graph = np.concatenate( (graph,(np.zeros((n+1,1))-1)) ,axis=1)
			graph[len(nodes[:,0]),np.where(nodes == min_node)] = mini/2
			graph[np.where(nodes == min_node),len(nodes[:,0])] = mini/2
			graph[len(nodes[:,0]),len(nodes[:,0])] = 0
			nodes = np.concatenate((nodes,[new_node]))
			print("i got in")
			print(nodes)
			print(cv_image[new_node[0],new_node[1]])
			#print(graph)
			cv2.circle(cv_image, (new_node[0],new_node[1]), 1,(0),-1)
			cv2.line(cv_image,(min_node[0],min_node[1]),(new_node[0],new_node[1]),(150),1)
			cv2.imshow("neha", cv_image)
			print(len(nodes[:,0]))
			print("m here")
			print(goal)
	cv2.waitKey()
	print("m out")
    except KeyboardInterrupt:
        print("Shutting Down")
    cv2.destroyAllWindows()

def print_path(nodes,graph,start):
	pt = nodes[-1]
	i = -1
	while (1):
		arr = np.where(graph[i] > 0)
		i = arr[0]
		print(i)
		new_pt = nodes[i]
		cv2.line(cv_image,(pt[0],pt[1]),(new_pt[0],new_pt[1]),(150),1)
		pt = new_pt
if __name__ == '__main__':
    main(sys.argv)

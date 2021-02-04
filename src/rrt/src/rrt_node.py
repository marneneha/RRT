#!/usr/bin/env python
#o/p of shape is x=231 y=194
#add condition for edge not being in obstacle
import rospy
import cv2
import sys
import random
import numpy as np
def randpointgen():
	x = random.randint(0,231)
	y = random.randint(0,194)
	return x,y

cv_image = cv2.imread("/home/neha/Downloads/turtlebot/src/maps/playground1.pgm",cv2.IMREAD_GRAYSCALE)

def main(args):
    rospy.init_node('rrt_node', anonymous=True)
    print("i m in")
    try:
	start = randpointgen()
	while cv_image[start[1],start[0]]<=220:
		start = randpointgen()
	goal = randpointgen()
	while cv_image[goal[1],goal[0]]<=220:
		goal = randpointgen()
	nodes = np.array([start])
	graph = np.zeros((1,1))
	cv2.circle(cv_image, (start[0],start[1]), 3,0,-1)
	cv2.circle(cv_image, (goal[0],goal[1]), 5,0,-1)
	print(start)
	print(cv_image[start[1],start[0]])
	print(goal)
	print(cv_image[goal[1],goal[0]])
	print(graph)
	while len(nodes[:,0])<300:
		rand_pt = randpointgen()
		min_node = nodes[0]
		#print(min_node)
		mini = np.linalg.norm(min_node - rand_pt)
		for i in range(len(nodes[:,0])):
			if np.linalg.norm(nodes[i]-rand_pt)<mini:
				min_node = nodes[i]
				mini = np.linalg.norm(nodes[i] - rand_pt)	
		new_node = min_node+rand_pt
		new_node = new_node/2
		print(((np.where(nodes == min_node))[0])[0])
		print("new_node is")
		print(new_node)
		print("min_node is")
		print(min_node)
		if(np.linalg.norm(new_node - goal)<10):
			n = len(nodes[:,0])
			graph = np.concatenate( (graph,[np.zeros(n)-1]) ,axis=0)
			graph = np.concatenate( (graph,(np.zeros((n+1,1))-1)) ,axis=1)
			graph[len(nodes[:,0]),((np.where(nodes == min_node))[0])[0]] = mini/2
			graph[((np.where(nodes == min_node))[0])[0],len(nodes[:,0])] = mini/2
			graph[len(nodes[:,0]),len(nodes[:,0])] = 0
			nodes = np.concatenate((nodes,[new_node]))
			print("goal reached")
			print_path(nodes,graph,start,new_node,)
			break
		if cv_image[new_node[1],new_node[0]]>=210:
			n = len(nodes[:,0])
			graph = np.concatenate( (graph,[np.zeros(n)-1]) ,axis=0)
			graph = np.concatenate( (graph,(np.zeros((n+1,1))-1)) ,axis=1)
			graph[len(nodes[:,0]),((np.where(nodes == min_node))[0])[0]] = mini/2
			graph[((np.where(nodes == min_node))[0])[0],len(nodes[:,0])] = mini/2
			graph[len(nodes[:,0]),len(nodes[:,0])] = 0
			nodes = np.concatenate((nodes,[new_node]))
			print("i got in")
			#print(nodes)
			#print(cv_image[new_node[1],new_node[0]])
			print(graph)
			cv2.circle(cv_image, (new_node[0],new_node[1]), 1,(0),-1)
			cv2.line(cv_image,(min_node[0],min_node[1]),(new_node[0],new_node[1]),(150),1)
			cv2.imshow("neha", cv_image)
			print(len(nodes[:,0]))
			print("m here")
			print(goal)
		
	print(graph[-1])			
	print("m out")
	cv2.waitKey()
    except KeyboardInterrupt:
        print("Shutting Down")
    cv2.destroyAllWindows()

def print_path(nodes,graph,start,new_node):
	print(new_node)
	print(nodes)
	print(len(nodes[:,0]))
	print(np.where(nodes == new_node))
	pt = nodes[np.where(nodes == new_node)]
	pt_idx = np.where(nodes == new_node)
	print(pt)
	print(pt_idx)
	while ((pt[0]!=start[0])and(pt[1]!=start[1])):
		print(graph[pt_idx])
		arr = np.where(graph[pt_idx] > 0)
		print(arr)
		print((arr[0])[0])
		new_pt_idx = (arr[0])[0]
		new_pt = nodes[new_pt_idx]
		cv2.line(cv_image,(pt[0],pt[1]),(new_pt[0],new_pt[1]),(0),2)
		pt = new_pt
		pt_idx = new_pt_idx
		print(new_pt)
		cv2.imshow("neha", cv_image)
	print(nodes)
if __name__ == '__main__':
    main(sys.argv)

//this is first commit
#include<ros/ros.h>
//import map 
#include <opencv2/core.hpp>
#include <opencv2/imgcodecs.hpp>
#include <opencv2/highgui.hpp>
#include <iostream>
using namespace cv;
int main(int argc, char **argv)
{
    ros::init(argc, argv, "rrt_node");
    ros::NodeHandle n;
    std::string image_path = "/home/neha/workspace/src/turtlebot3/turtlebot3_navigation/maps";
    Mat img = imread(image_path, IMREAD_GRAYSCALE);
    if(img.empty())
    {
        std::cout << "Could not read the image: " << image_path << std::endl;
        return 1;
    }
    imshow("Display window", img);
    int k = waitKey(0); // Wait for a keystroke in the window
    if(k == 's')
    {
        imwrite("map.pgm", img);
    }
    return 0;
}

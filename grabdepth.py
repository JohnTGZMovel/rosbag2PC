#/usr/bin/env python

import rospy
import numpy as np
import cv2
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError
cvb=CvBridge()
i=0
depth_mem=None
first_flag=True

def imnormalize(xmax,image):
    """
    Normalize a list of sample image data in the range of 0 to 1
    : image:image data.
    : return: Numpy array of normalize data
    """
    xmin = 0
    a = 0
    b = 255
    
    return ((np.array(image,dtype=np.float32) - xmin) * (b - a)) / (xmax - xmin)

def checkdepth(msg):
    global i
    global depth_mem
    global first_flag
    try:
        cv_image = cvb.imgmsg_to_cv2(msg,msg.encoding)
    except CvBridgeError as e:
        print(e)
    
    image_normal= np.array(cv_image,dtype=np.uint16)
    numpy_image= np.array(cv_image,dtype=np.uint16)
    if first_flag == True:
        depth_mem = np.copy(numpy_image)

        base = 1000000
        temp = base + i
        cv2.imwrite("./"+str(temp)[1:]+".png", image_normal)
        first_flag=False
    if (depth_mem==numpy_image).all() :
        return
    else:
        base = 1000000
        temp = base + i
        depth_mem = np.copy(numpy_image)
        cv2.imwrite("./"+str(temp)[1:]+".png", image_normal)
    i+=1
    
if __name__ == '__main__':
    
    rospy.init_node("grabdepth")
    
    rate=rospy.Rate(2) #2hz
    rospy.loginfo("Running depth Grabber")
    while not rospy.is_shutdown():
        rospy.Subscriber('/d400/depth/image_raw',Image,checkdepth)
    
        rate.sleep()
    
    

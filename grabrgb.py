#/usr/bin/env python

import rospy
import numpy as np
import cv2
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError
cvb=CvBridge()
i=0
rgb_mem=None
first_flag=True

def grabrgb(msg):
    global i
    global rgb_mem
    global first_flag
    try:
        cv_image = cvb.imgmsg_to_cv2(msg,"rgb8")
        print(msg.encoding)
    except CvBridgeError as e:
        print(e)
    
    image_normal= np.array(cv_image)
    if first_flag == True :
        rgb_mem = np.copy(image_normal)
        base = 1000000
        temp = base + i
        cv2.imwrite("./"+str(temp)[1:]+".jpg", image_normal)
        first_flag=False
    elif np.array_equal(rgb_mem,image_normal) :
        return
    else :
        base = 1000000
        temp = base + i
        rgb_mem = np.copy(image_normal)
        cv2.imwrite("./"+str(temp)[1:]+".jpg", image_normal)
    i+=1
    
if __name__ == '__main__':
    
    rospy.init_node("grabrgb")
    
    rate=rospy.Rate(2) #2hz
    rospy.loginfo("Running RGB Grabber")
    
    while not rospy.is_shutdown():
        
        rospy.Subscriber("/d400/color/image_raw",Image,grabrgb)
        rate.sleep()
        
    
    
    

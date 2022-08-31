#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist
from sensor_msgs.msg import NavSatFix
import time
import csv
import pandas as pd
import rosbag

import re



if __name__=="__main__":
    try: 
        rospy.init_node('gps_listener', anonymous=True)
        #csv_file = rospy.get_param('~csv_value')
        f = open("/home/jiwon/catkin_ws/src/gps_test/src/0801_PMU_first_HERO10 Black-GPS5.csv", 'r')
        rdr = csv.reader(f)
        gps_pub = rospy.Publisher('gps_data', NavSatFix, queue_size=1)
        rate = rospy.Rate(1)
        for line in rdr:
            lat = float(line[2])
            lon = float(line[3])
            lonlat = NavSatFix()
            lonlat.header.stamp = rospy.Time.now()
            lonlat.header.frame_id = "gps"
            lonlat.latitude = lat
            lonlat.longitude = lon
            if(line ==0 or line ==1): 
                for i in range(25):
                    gps_pub.publish(lonlat)
            else:
                for i in range(13):
                    gps_pub.publish(lonlat)
            
                # print(lat,lon)
                
                # print(lonlat.latitude,lonlat.longitude)
                
            rate.sleep()
        f.close()
    except rospy.ROSInterruptException:
        pass




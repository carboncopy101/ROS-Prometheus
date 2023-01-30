#!/usr/bin/env python

import rospy
import sys
import os

sys.path.remove(os.path.dirname(__file__))
from std_msgs.msg import String

s = String()

from prometheus_client import start_http_server, Gauge

rssi_chatter = Gauge('rssi_gauge', 'rssi log')

def ros_setup():
    rospy.init_node('RSSI_node', anonymous = False)
    rospy.Subscriber('chatter', String, callback)


def callback(data):
    s = data
    print(s.data)
    rssi_chatter.set(s.data)

if __name__ == '__main__':
    start_http_server(8014)
    while True:
        ros_setup()

    

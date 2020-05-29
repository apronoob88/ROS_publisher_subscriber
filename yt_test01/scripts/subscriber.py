#!/usr/bin/env python

import rospy
from std_msgs.msg import String

def callback(data):
    rospy.loginfo("Subscriber with id %s received: %s", rospy.get_caller_id(), data.data)


def subscriber():

    rospy.init_node('mySubscriber', anonymous= True)
    rospy.Subscriber('publish_and_subscribe', String, callback)

    # prevent python from exiting until the node is stopped
    rospy.spin()

if __name__ == '__main__':
    subscriber()
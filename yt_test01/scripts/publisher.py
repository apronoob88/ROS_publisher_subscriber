#!/usr/bin/env python

import rospy
from std_msgs.msg import String

def publisher():
    pub = rospy.Publisher('publish_and_subscribe', String, queue_size = 50)
    rospy.init_node('myPublisher', anonymous=True)
    rate = rospy.Rate(1) # 1 publish per sec
    count = 1
    while not rospy.is_shutdown():
        publish_str = "Hello from publisher %s"  %count
        rospy.loginfo(publish_str)
        pub.publish(publish_str)
        count += 1
        rate.sleep()

    

if __name__ == '__main__':
    try:
        publisher()
    except rospy.ROSInterruptException:
        pass
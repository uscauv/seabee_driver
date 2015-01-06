#!/usr/bin/env python

import roslib
roslib.load_manifest('seabee_driver')
import rospy

from seabee_driver.msg import Power

def callback(data):
	rospy.loginfo("Got powerboard message")

# Main loop function
def listener():
# Get the ~private namespace parameters from command line or launch file.
	topic = rospy.get_param('~topic', '/seabee/power_board')
	# Create a subscriber with appropriate topic, custom message and name of callback function.
	rospy.Subscriber(topic, Power, callback)
# Wait for messages on topic, go to callback function when new messages arrive.
	rospy.spin()

if __name__ == '__main__':
	rospy.init_node('powerboard')
	listener()

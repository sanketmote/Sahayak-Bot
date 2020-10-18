#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
import time

def pose_callback(pos):
    rospy.loginfo("Revolving in a circle. Theta: %.5f",pos.theta)

def main():

	rospy.init_node('turtle_revolve', anonymous=True)

	ros_sub = rospy.Subscriber("/turtle1/pose", Pose, pose_callback)

	velocity_publisher = rospy.Publisher('/turtle1/cmd_vel', Twist,queue_size=10)

	var_loop_rate = rospy.Rate(10)

	cond = True

	start_time = time.time()

	while cond == True:

		vel_msg = Twist()

		vel_msg.linear.x = 3
		vel_msg.linear.y = 0
		vel_msg.linear.z = 0
		vel_msg.angular.x = 0
		vel_msg.angular.y = 0
		vel_msg.angular.z = 3

		velocity_publisher.publish(vel_msg)
		var_loop_rate.sleep()

		# there's a delay of 0.3 sec between start of python time
		# and start of the movement of bot. Thus we need to subtract 
		# 0.3 from the actual "break time" provided in the if condition below
		## 0.7 sec travel ( 1 sec break time - 0.3) => theta of 2.112 rad   
		## (actual break time - 0.3) => theta of 2*pi rad 
		## solving this corelation , we get break time = 2.38249513

		if (time.time() - start_time >= (2.38249513)):
			vel_msg.linear.x = 0 
			vel_msg.linear.y = 0
			vel_msg.linear.z = 0
			vel_msg.angular.x = 0
			vel_msg.angular.y = 0
			vel_msg.angular.z = 1.5

			velocity_publisher.publish(vel_msg)
			cond = False

	ros_sub.unregister()
	rospy.loginfo("Goal reached")
	rospy.spin()


if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass

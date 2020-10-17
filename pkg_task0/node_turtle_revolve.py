#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
import time

def pose_callback(pos):
    rospy.loginfo("Revolving in a circle. Theta: %.5f",pos.theta)

def main():

	rospy.init_node('turtle_revolve', anonymous=True)

	rospy.Subscriber("/turtle1/pose", Pose, pose_callback)

	velocity_publisher = rospy.Publisher('/turtle1/cmd_vel', Twist,queue_size=10)

	var_loop_rate = rospy.Rate(10)

	cond = True

	start_time = time.time()
	rospy.loginfo("Time start: "+str(start_time))
	while cond == True:
		    
		vel_msg = Twist()

		# vel_msg.linear.x = 12.5663 
		# vel_msg.linear.y = 2.0
		# vel_msg.linear.z = 0
		# vel_msg.angular.x = 0
		# vel_msg.angular.y = 0
		# vel_msg.angular.z = 6.283185

		
		vel_msg.linear.x = 3
		vel_msg.linear.y = 0
		vel_msg.linear.z = 0
		vel_msg.angular.x = 0
		vel_msg.angular.y = 0
		vel_msg.angular.z = 3

		
		velocity_publisher.publish(vel_msg)
		#rospy.loginfo("Time wasted: "+str(time.time()))
		var_loop_rate.sleep()

		if (time.time() - start_time >= (2.337494534)):
			vel_msg.linear.x = 0
			vel_msg.linear.y = 0
			vel_msg.linear.z = 0
			vel_msg.angular.x = 0
			vel_msg.angular.y = 0
			vel_msg.angular.z = 1.5

			velocity_publisher.publish(vel_msg)
			
			#rospy.loginfo("Breaking the loop")
			cond = False

	#rospy.spin()


if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass



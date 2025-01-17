#!/usr/bin/env python 

import rospy
from psm_coop import coop

if __name__ == '__main__':
	name = rospy.get_param('/name')
	num = rospy.get_param('/number')
	gazebo_on = rospy.get_param('/gazebo_on')
	track_force = rospy.get_param('/track_force')
	
	a = coop.mainframe(name, num,gazebo_on,track_force)
	r = rospy.Rate(1500)
	rospy.sleep(1)

	print('READY TO START')
	while not rospy.is_shutdown():
		for i in range(num):
			if (i>0):
				a.make_object_v(i)
		a.run()  
		r.sleep()
	#rospy.spin()
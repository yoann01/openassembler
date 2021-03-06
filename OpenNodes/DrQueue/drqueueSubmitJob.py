###OpenAssembler Node python file###

'''
define
{
	name drqueueSubmitJob
	tags drqueue
	input string Command "" ""
	input string Name "" ""
	input int Priority "100" ""
	input int startFrame "1" ""
	input int endFrame "10" ""
	input int blockSize "1" ""
	output any jobID "" ""

}
'''

import sys,os
try:
	import drqueue.base.libdrqueue as drqueue
except:
	print "There was some problem with loading the drqueue module..."


class drqueueSubmitJob():
	def drqueueSubmitJob_main(self, **connections):

		try:
			Command=str(connections["Command"])
		except:
			Command=""
		try:
			Name=str(connections["Name"])
		except:
			Name=""
		try:
			Priority=int(connections["Priority"])
		except:
			Priority=100
		try:
			startFrame=int(connections["startFrame"])
		except:
			startFrame=1
		try:
			endFrame=int(connections["endFrame"])
		except:
			endFrame=10
		try:
			blockSize=int(connections["blockSize"])
		except:
			blockSize=1
		try:
			job = drqueue.job()
			job.name = Name
			job.frame_start = startFrame
			job.frame_end = endFrame
			job.cmd = Command
			job.block_size=blockSize
			job.priority = Priority
			job.send_to_queue()
			id=job.id
			#drqueue.request_job_limits_nmaxcpuscomputer_set(id,1,1)
			return id
		except:
			return None
			pass


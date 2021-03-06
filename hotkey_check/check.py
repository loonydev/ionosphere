import os
import argparse
import hotkeys
import csv
import cv2
'''
EXAMPLE USAGE
python check.py -d example/ -f 0000 -i 3 -s 0.4

CONTROL
rigth - approved (1)
left - unapproved (0)
up/down - doubtful (-1)
space - stop

'''
def argument_parser():
	ap = argparse.ArgumentParser()
	ap.add_argument("-d", "--dest", type=str, help="path to directory with data")
	ap.add_argument("-f", "--first", type=str, default='0000', help="first TGF's ID")
	ap.add_argument("-i", "--sid", type=int, default=3, help="first index of ID in image's name")
	ap.add_argument("-s", "--scale", type=float, default=1, help="scale of image")
	return vars(ap.parse_args())

class CheckClass(object):
	def __init__(self,args):
		self.args = args
		self.result = {}
		self.next = True
		self.work = True

	def approved(self,event):
		self.result[self.id] = 1
		self.next = True

	def unapproved(self,event):
		self.result[self.id] = 0
		self.next = True

	def doubtful(self,event):
		self.result[self.id] = -1
		self.next = True

	def finish(self,event):
		print('SPACE')
		# self.next = False
		self.work = False
		# hotkeysdetector.cancel()
		# cv2.destroyAllWindows()

	def check(self):
		hotkeysdetector = hotkeys.HotKeysDetector()
		hotkeysdetector.addhotkeys("RIGHT",self.approved)
		hotkeysdetector.addhotkeys("LEFT",self.unapproved)
		hotkeysdetector.addhotkeys("UP",self.doubtful)
		hotkeysdetector.addhotkeys("DOWN",self.doubtful)
		hotkeysdetector.addhotkeys("SPACE",self.finish)
		hotkeysdetector.start()

		filelist = os.listdir(args['dest'])
		filelist.sort()

		for file_ in filelist:
			while not self.next:
				pass
			if self.work:
				if file_.endswith(".png") and file_[self.args['sid']+4]=='.':
					self.id = file_[self.args['sid']:self.args['sid']+4]
					if int(self.id) >= int(self.args['first']):
						print(self.id)
						self.next = False
						self.img = cv2.imread(args['dest']+file_)
						self.img = cv2.resize(self.img,(int(self.img.shape[1]*self.args['scale']),
										 				int(self.img.shape[0]*self.args['scale'])))
						cv2.imshow('TGF',self.img)
						cv2.waitKey(0)
			else:
				self.next = False
				break

		while not self.next:
			pass

		hotkeysdetector.cancel()
		cv2.destroyAllWindows()

		if os.path.exists('hand_check_result.csv'):
			with open('hand_check_result.csv', 'a') as f:
				w = csv.writer(f)
				w.writerows(self.result.items())
		else:
			with open('hand_check_result.csv', 'w') as f:
				w = csv.writer(f)
				w.writerows(self.result.items())

if __name__ == '__main__':
	args = argument_parser()
	CheckClass(args).check()

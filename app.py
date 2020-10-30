import os

print('Welcome! This is the Crowd Detection and Counter Developed for Myntra HackerRamp, 2020 by Team Illuminati.')
print('Following are th utilities provided : ')
print('1 -> Select a video of your choice.')
print('2 -> Stream via webcam.')

x = int(input('Enter 1 or 2 to choose:  '))

if (x == 1):
	s = input('Enter path to video (For example use - videos/live_cctv.mp4):  ')
	os.system('python people_counter.py --prototxt mobilenet_ssd/MobileNetSSD_deploy.prototxt --model mobilenet_ssd/MobileNetSSD_deploy.caffemodel --input ' + s + ' --output output/output_01.avi')
elif (x == 2):
	os.system('python people_counter.py --prototxt mobilenet_ssd/MobileNetSSD_deploy.prototxt --model mobilenet_ssd/MobileNetSSD_deploy.caffemodel --output output/webcam_output.avi')
else:
	print('INVALID SELECTION')

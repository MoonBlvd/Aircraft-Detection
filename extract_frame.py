import cv2

# This loads a picture then displays it
# pic_name = 'cessna.jpg'
# pic = cv2.imread(pic_name)
# cv2.imshow(pic_name, pic)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
# exit()

# < 81
# ^ 82
# > 83
# v 84

video_header = 'NASA_Video_Files/'


# vid = cv2.VideoCapture('NASA_Video1.mp4')
# vid = cv2.VideoCapture('NASA_Video_Files/migcc_sr22_92415_1305_right.MP4')
# vid = cv2.VideoCapture('NASA_Video_Files/migcc_y6_92415_1040_center.MP4')
# vid = cv2.VideoCapture('NASA_Video_Files/migcc_null_92315__1338_center.MP4')
# vid = cv2.VideoCapture('NASA_Video_Files/migcc_bixler_92515_950_right.MP4')
#print vid.get(cv2.cv.CV_CAP_PROP_FOURCC)
# video_name = 'migcc_bixler_92515_950_right'
video_name = 'migcc_bixler_92415_1116_left'


video_suffix = '.MP4'

vid = cv2.VideoCapture( video_header + video_name + video_suffix)

#vid.set(cv2.cv.CV_CAP_PROP_POS_MSEC, 296000)
vid.set(cv2.cv.CV_CAP_PROP_POS_MSEC, 139000)
# vid.set(cv2.cv.CV_CAP_PROP_POS_FRAMES, 8901)
# vid.set(cv2.cv.CV_CAP_PROP_POS_AVI_RATIO, 0.303)
print vid.get(cv2.cv.CV_CAP_PROP_POS_FRAMES)
print vid.get(cv2.cv.CV_CAP_PROP_POS_MSEC)
print vid.get(cv2.cv.CV_CAP_PROP_POS_AVI_RATIO)

retval, image = vid.read()
# patch = image[800:900, 800:900]

if retval:
	cv2.imshow('frame', image)
else:
	print 'not opened'

height = vid.get(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT)
height = int(height)
print height
width = vid.get(cv2.cv.CV_CAP_PROP_FRAME_WIDTH)
print width
width = int(width)

'''
# getting video information
fourcc = vid.get(cv2.cv.CV_CAP_PROP_FOURCC)
fourcc = int(fourcc)
print "4-character code: %f" % fourcc

fps = vid.get(cv2.cv.CV_CAP_PROP_FPS)
fps = int(fps)
print fps
height = vid.get(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT)
height = int(height)
print height
width = vid.get(cv2.cv.CV_CAP_PROP_FRAME_WIDTH)
print width
width = int(width)

new_vid = cv2.VideoWriter('new.mp4', 828601953, 30, (1080, 1920))
if not new_vid.isOpened():
	print 'new_vid not opened'
	exit()
'''

success = 1

while success:
	cv2.destroyAllWindows()
	retval, image = vid.read()
#	image = image[100:200, 1450:1550]
	#image = image[100:600, 0:1800]
	# x1 = 1500
	# x2 = 3000
	x1 = 2500
	x2 = 4000
	y1 = 0
	y2 = 800
	cv2.rectangle(image, (x1,y1), (x2,y2), (0,255, 0), 1)
	# cv2.rectangle(image, (1500,0), (3000,800), (0,255, 0), 1)
#  	image = image[y1+1:y2, x1+1:x2]

	if retval:
		# subtract one because it points to the next available frame
		current_frame = vid.get(cv2.cv.CV_CAP_PROP_POS_FRAMES) - 1

		window_name = "frame %f" % current_frame

		# calculate time of frame
		window_time = vid.get(cv2.cv.CV_CAP_PROP_POS_MSEC)

		window_time /= 1000;
		window_min = window_time // 60;
		window_sec = window_time % 60;	
		window_time_string = " time: %d:%f" % (window_min, window_sec)

		print window_name + window_time_string 
			
		# This lets the window be resized 
		cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)
		cv2.setWindowProperty(window_name, cv2.WND_PROP_FULLSCREEN, cv2.cv.CV_WINDOW_FULLSCREEN)
		cv2.imshow(window_name, image)

	else:
		print "no image loaded"

	val = cv2.waitKey(0)
	val = (val & 255)

	if val == 81:
		print "left"
		vid.set(cv2.cv.CV_CAP_PROP_POS_FRAMES, current_frame-1)
	elif val == 82:
		print "up"
	elif val == 83:
		print "right"
	elif val == 84:
		print "down"
	elif val == 102:
		print "extracting frame %f" % current_frame
	elif val == 115:
		print 's'
	
		cv2.destroyAllWindows()	
	  	output_filename = raw_input('Enter filename for frame\n')
		cv2.imwrite(output_filename, image)
		
	elif val == 113:
	# q
		success = 0

cv2.destroyAllWindows()
	

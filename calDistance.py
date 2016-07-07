import sys
import numpy as np

## calculate the target distance based on 2 cameras
# it's assuming that the 2 cameras are the same and are installed parallel
def calDistance(imgL, imgR, targetL, targetR):
    phi = 60 # assume the viewing angle of the 2 cameras are the same
    B = 1000 # the distance
	
	imageSize = imgL.shape
	x = imageSize[1]/2
	xL = targetL[1]-x
	xR = x-targetR[1]

	D = B*x/(2*tan(phi/2)*(xL-xR))

	return D

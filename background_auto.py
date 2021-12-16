import os
import sys
import ctypes
import random

class Wallpaper:
	def __init__(self):

		# Gets absolute path to current dir and adds to self.path
		self.path = os.path.abspath('')
		# os.walk is 3 tuple but only need files
		# joins absolute path and backgrounds to get path to background
		for root, directories, files in os.walk(os.path.join(self.path, 'backgrounds')):
			# creates backgrounds array to store each image and converts them to lowercase
			self.backgrounds = [file.lower() for file in files if file.endswith(('.png', '.jpg', '.jpeg'))]
		# Controls background and sets it to random one from that array
		#ctypes.windll.user32.SystemParametersInfoW(20, 0, os.path.join(self.path, 'backgrounds', random.choice(self.backgrounds)) , 0)
		
		ctypes.windll.user32.SystemParametersInfoW(20, 0, os.path.join(self.path, 'backgrounds', 'winter_snowfall.jpg'), 0)

		'''
		HKEY_CURRENT_USER\Control Panel\Desktop\WallpaperStyle
		Wallpaper styles: 1 is scale, 2 is stretch. Scale slim wallpapers, Stretch wide ones.
		1. Find way to set HKEY to 1 or 2 programmatically before wallpaper is set
		2. Get screen Height and Width in pixels (only once higher up in code)

		Use scaling library for this!
			https://www.geeksforgeeks.org/image-processing-in-python-scaling-rotating-shifting-and-edge-detection/
			get image size with library. Get difference between height of picture and height of screen (screen height - pic height). 
				If number is negative, apply scale else continue
				Add difference to height and width of image
				If new image width is <70% of screen width, apply scale (1)
				Else apply stretch (2)
		3. Multi monitor? Test spanning picture to width of 2 monitors
			If that works. Then need to stitch wallpapers together and span (like debian hydrapaper)
		4. Add timer to change on interval
		5. GUI?
		'''

runit = Wallpaper()
# print(os.path.join(runit.path, 'backgrounds'))
# print(runit.backgrounds)
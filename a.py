import time
import pyautogui
import sys
import keyboard

time.sleep(3)
print('Import Successful')

try:
	while True:
#		pyautogui.scroll(100)
#		time.sleep(1)
		pyautogui.click()
		time.sleep(2)
		if keyboard.is_pressed('q'):
			print('Yes')
			sys.exit()
		if keyboard.is_pressed('o'):
			print('Pause')
			time.sleep(10)
		
except KeyboardInterrupt:
	sys.exit()
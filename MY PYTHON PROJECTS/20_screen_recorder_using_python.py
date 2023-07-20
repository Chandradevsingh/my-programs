import cv2
import pyautogui
from win32api import GetSystemMetrics
import numpy as np
import time

width = GetSystemMetrics(0)
height = GetSystemMetrics(1)
dimentions = (width, height)
format = cv2.VideoWriter_fourcc(*'XVID')
output = cv2.VideoWriter( 'tets.mp4', format, 30.0, dimentions)
start_time = time.time()
duration = 10
end_time = start_time + duration
while True:
    image = pyautogui.screenshot()
    frame_1 = np.array(image)
    frame = cv2.cvtColor(frame_1, cv2.COLOR_BGR2RGB)
    output.write(frame)
    c_time = time.time()
    if c_time > end_time:
        break
output.release()
print('--END--')
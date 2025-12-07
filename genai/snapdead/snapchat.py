import cv2
import os

# Get the directory of the current script
script_dir = os.path.dirname(os.path.abspath(__file__))
image_path = os.path.join(script_dir, 'jkr.png')

bg = cv2.imread(image_path)

cv2.imshow('ARChat', bg)
cv2.waitKey(0)


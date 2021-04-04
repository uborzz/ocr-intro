from pytesseract import Output
import pytesseract
import argparse
import imutils
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="path to input image")
ap.add_argument("-o", "--output", required=True, help="path to output image")
ap.add_argument("-a", "--angle", required=True, help="rotation angle", type=int)
args = vars(ap.parse_args())

original = cv2.imread(args["image"])

# rotate the image and save to disk
rotated = imutils.rotate_bound(original, angle=args["angle"])
cv2.imwrite(args["output"], rotated)
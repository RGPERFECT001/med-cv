import pytesseract
import cv2
pytesseract.pytesseract.tesseract_cmd = r"C:\Users\rhyth\OneDrive\Documents\Tesseract.exe"
cam_port=0
cam = cv2.VideoCapture(cam_port)
result, image = cam.read()

out_below = pytesseract.image_to_string(image)
print(out_below)

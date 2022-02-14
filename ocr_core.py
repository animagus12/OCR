import cv2
import pytesseract

# This is the core of the program it extracts text from an image using tesseract


def core(img):
    config = "--psm 3"
    text = pytesseract.image_to_string(img, config=config)
    return text


# Resizing the image to help the program to scan for everything

def resize_img(img):
    return cv2.resize(img, None, fx=0.9, fy=0.9)

# Converting the image to Grayscale to remove colors


def convert_grayscale(img):
    return cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Thresholding is a type of image segmentation, where we change the pixels of an image to make the image easier to analyze.


def adaptive_thresholding(img):
    return cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 91, 11)

# Removong noise from the image
# def remove_noise(img):
#     return cv2.medianBlur(img, 5)


# Reading the image using OpenCV
# Using the full path of the image location
img = cv2.imread(
    'C:/Users/subhr/OneDrive/Documents/Programs/Python/OCR/img.png')

img = resize_img(img)
img = convert_grayscale(img)
img = adaptive_thresholding(img)
# img = remove_noise(img)

# Shoing the final image to check if it's legible
# cv2.imshow("img", img)
# cv2.waitKey(0)

print(core(img))

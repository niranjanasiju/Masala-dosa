import cv2
import numpy as np
import pytesseract

def preprocess_image(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    thresh = cv2.threshold(blurred, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
    return thresh

def extract_braille_text(img):
    custom_config = r'--oem 3 --psm 6'
    braille_text = pytesseract.image_to_string(img, config=custom_config, lang='brl')
    return braille_text

def main(image_path):
    image = cv2.imread(image_path)
    preprocessed_image = preprocess_image(image)
    braille_text = extract_braille_text(preprocessed_image)
    print("Extracted Braille Text:")
    print(braille_text)

if __name__ == "__main__":
    image_path = '/Users/niranjanasiju/Desktop/practice python/braille image.jpeg'  # Change this to your image path
    main(image_path)

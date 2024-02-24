import cv2
import pytesseract

# Load image
image = cv2.imread('braille_image.jpg')

# Preprocessing
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Perform OCR
text = pytesseract.image_to_string(gray)

# Print recognized text
print("Recognized Text:")
print(text)

import cv2
import numpy as np

# Load the image
image_path = "/Users/niranjanasiju/Desktop/braille_A.jpg"
image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

# Preprocess the image
image = cv2.GaussianBlur(image, (5, 5), 0)
_, image = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY_INV)

# Find contours to extract individual braille dots
contours, _ = cv2.findContours(image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Initialize an empty list to store braille dots
braille_dots = []

# Iterate through the contours and extract braille dots
for contour in contours:
    x, y, w, h = cv2.boundingRect(contour)
    aspect_ratio = h / w

    # Filter based on aspect ratio to remove non-braille dots
    if 0.8 < aspect_ratio < 1.2:
        braille_dots.append(image[y:y + h, x:x + w])
braille_to_text = {
    "000000": " ",
    "100000": "a",
    "110000": "b",
    "110001": "c",
    "010001": "d",
    "011001": "e",
    "011000": "f",
    "001001": "g",
    "001000": "h",
    "001100": "i",
    "101100": "j",
    "111000": "k",
    "111001": "l",
    "111101": "m",
    "111100": "n",
    "011100": "o",
    "011101": "p",
    "011111": "q",
    "001111": "r",
    "001110": "s",
    "010111": "t",
    "101110": "u",
    "110111": "v",
    "110110": "w",
    "111110": "x",
    "111111": "y",
    "111011": "z",
    "011011": "1",
    "001011": "2",
    "000111": "3",
    "000110": "4",
    "000101": "5",
    "000100": "6",
    "100100": "7",
    "100101": "8",
    "100111": "9",
    "100110": "0"
}

def braille_to_text_conversion(braille_dots):
    braille_string = "".join(braille_dots)
    text = braille_to_text.get(braille_string, "⠿")
    return text


# Convert braille dots to text
text = ""
for dot in braille_dots:
    dot = cv2.resize(dot, (6, 3))
    dot_binary = cv2.cvtColor(dot, cv2.COLOR_BGR2GRAY)
    dot_string = "".join(["{:06b}".format(x)[::-1] for x in dot_binary.flatten()])
    text += braille_to_text_conversion([dot_string])

print(text)
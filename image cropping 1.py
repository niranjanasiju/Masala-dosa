from PIL import Image

def crop_image(input_image_path,output_image_path, crop_box):
    """
    Crop the input image using the specified crop box coordinates and save the cropped image.
    
    :param input_image_path: Path to the input image file.
    :param output_image_path: Path to save the cropped image file.
    :param crop_box: Tuple (left, upper, right, lower) specifying the crop box coordinates.
    """
    # Open the input image
    img = Image.open(input_image_path)
    
    # Crop the image using the specified box coordinates
    cropped_img = img.crop(crop_box)
    
    # Save the cropped image
    cropped_img.save(output_image_path)

# Example usage:
input_image_path = "/Users/niranjanasiju/Desktop/practice python/hello.jpg"
output_image_path = "/Users/niranjanasiju/Desktop/practice python/temp image.jpg"

# Define the crop box coordinates: (left, upper, right, lower)
crop_box = (410,0,570, 300)  # Crop a 200x200 region starting from (100, 100)

# Crop the image and save the cropped image
crop_image(input_image_path, output_image_path, crop_box)
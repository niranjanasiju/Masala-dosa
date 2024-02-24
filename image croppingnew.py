from PIL import Image

def crop_image(image_path):
    """Crop an image into five smaller images."""
    # Open the image
    img = Image.open(image_path)
    
    # Get the dimensions of the image
    width, height = img.size
    
    # Calculate the width and height of each cropped image
    crop_width = width // 5
    crop_height = height
    
    # Crop the image into five smaller images
    cropped_images = []
    for i in range(5):
        left = i * crop_width
        upper = 0
        right = left + crop_width
        lower = crop_height
        box = (left, upper, right, lower)
        cropped_img = img.crop(box)
        cropped_images.append(cropped_img)
    
    return cropped_images

def save_images(images, output_dir):
    """Save cropped images to the output directory."""
    for i, img in enumerate(images):
        rgb_img = img.convert("RGB")  # Convert the image to RGB format
        rgb_img.save(f"{output_dir}/letter_{i+1}.jpg")

def main():
    image_path = "smile.jpg"  # Path to the input image
    output_dir = "cropped"  # Output directory to save the cropped images
    
    # Crop the image
    cropped_images = crop_image(image_path)
    
    # Save the cropped images
    save_images(cropped_images, output_dir)
    
    print("Images cropped and saved successfully.")

if __name__ == "_main_":
    main()
from PIL import Image
import imagehash

# Load the images
image1 = Image.open("/Users/niranjanasiju/Desktop/practice python/A.jpg")
image2 = Image.open("/Users/niranjanasiju/Desktop/practice python/A.jpg")

# Compute the perceptual hash (phash) for each image
hash1 = imagehash.phash(image1)
hash2 = imagehash.phash(image2)

# Compare the similarity between the two hashes
similarity = 1 - (hash1 - hash2) / len(hash1.hash) ** 2

# Print the similarity
print("Similarity between the images: {:.2f}%".format(similarity * 100))
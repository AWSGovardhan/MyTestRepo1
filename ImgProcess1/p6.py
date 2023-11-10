from PIL import Image


size = (40, 40)
img = Image.open(r"Photos/messi5.jpg")

print("Original size of the image")
print(img.size)

# resizing the image
r_img = img.resize(size, resample = Image.BILINEAR)

# resized_test.png => Destination_path
r_img.save("resized_test.jpg")

# Opening the new image
img = Image.open(r"resized_test.jpg")

print("\nNew size of the image")
print(img.size)

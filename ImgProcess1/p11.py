# Importing Image class from PIL module
from PIL import Image

# Opens a image in RGB mode
im = Image.open(r"Photos/messi5.jpg")

# Blurring the image
im1 = im.filter(ImageFilter.BLUR)

# Shows the image in image viewer
im1.show()

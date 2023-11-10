# This will import Image and ImageChops modules
from PIL import Image, ImageEnhance

# Opening Image
im = Image.open(r"Photos/messi5.jpg")

# Creating object of Sharpness class
im3 = ImageEnhance.Sharpness(im)

# showing resultant image
im3.enhance(5.0).show()

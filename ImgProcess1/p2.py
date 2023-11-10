# Importing Image module from 
# PIL package
from PIL import Image
import PIL
 
# creating a image object (main image)
im1 = Image.open(r"Photos/messi5.jpg")
 
# rotating a image 90 deg counter clockwise
im1 = im1.rotate(45, PIL.Image.NEAREST, expand = 1)
 
# to show specified image
im1.show()

# This will import Image and ImageEnhance modules
from PIL import Image, ImageEnhance
 
# Opening Image
im = Image.open(r"Photos/messi5.jpg")
 
# Creating object of Color class
im3 = ImageEnhance.Color(im)
 
# showing resultant image
im3.enhance(100.0).show()
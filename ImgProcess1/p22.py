# This will import Image and ImageEnhance modules
from PIL import Image, ImageEnhance
 
# Opening Image
im = Image.open(r"Photos/messi5.jpg")
 
# Creating object of Brightness class
im3 = ImageEnhance.Brightness(im)
 
# showing resultant image
im3.enhance(1.5).show()
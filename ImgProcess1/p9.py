
# importing Image class from PIL package
from PIL import Image
 
# creating a object
image = Image.open(r"Photos/messi5.jpg")
MAX_SIZE = (100, 100)
 
# Creating the thumbnail
image.thumbnail(MAX_SIZE)
 
image.show()
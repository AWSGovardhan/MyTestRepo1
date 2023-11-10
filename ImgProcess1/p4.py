# importing PIL Module
from PIL import Image

# open the original image
original_img = Image.open("Photos/messi5.jpg")

# Flip the original image vertically
vertical_img = original_img.transpose(method=Image.FLIP_TOP_BOTTOM)
vertical_img.save("vertical.png")

vertical_img.show()

# close all our files object
original_img.close()
vertical_img.close()

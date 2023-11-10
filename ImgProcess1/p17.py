# importing image object from PIL
import math
from PIL import Image, ImageDraw

w, h = 220, 190
shape = [(40, 40), (w - 75, h - 75)]

# creating new Image object
img = Image.new("RGB", (w, h))

# create line image
img1 = ImageDraw.Draw(img)
img1.line(shape, fill="green", width=0)
img.show()

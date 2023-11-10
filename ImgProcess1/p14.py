# Importing Image and ImageFont, ImageDraw 
# module from PIL package
from PIL import Image, ImageFont, ImageDraw

# creating a image object
image = Image.open(r'Photos/messi5.jpg')

draw = ImageDraw.Draw(image)

# specified font size
font = ImageFont.truetype(r'DroidSans.ttf', 15)

text = u"""\
Custom
Text \n On Image"""

# drawing text size
draw.text((6, 8), text, fill ="cyan", font = font, align ="right")
# colors - red, blue, green, yellow, BLUE,.....
image.show()

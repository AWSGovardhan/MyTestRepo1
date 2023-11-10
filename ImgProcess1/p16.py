
# import all the libraries
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
 
# image opening
image = Image.open("Photos/messi5.jpg")
 
# creating a copy of original image
watermark_image = image.copy()
 
# Image is converted into editable form using
# Draw function and assigned to draw
draw = ImageDraw.Draw(watermark_image)
 
# ("font type",font size)
font = ImageFont.truetype("DroidSans.ttf", 50)
 
# Decide the text location, color and font 
# (255,255,255)-White color text
draw.text((0, 0), "Some Text that will be displayed on the Image!", (255, 255, 255), font=font)
 
watermark_image.show()
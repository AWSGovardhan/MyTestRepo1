from PIL import Image, ImageDraw, ImageFont



social_media_dimensions = {
    'Facebook': {'width': 1200, 'height': 628},
    'Twitter': {'width': 1500, 'height': 500},
    'Instagram': {'width': 1080, 'height': 1080},
    # Add dimensions for other platforms
}


# poster_content = {
#     'text': 'Your poster text here',
#     'image_path': 'path/to/your/image.jpg',
#     # Add other elements as needed
# }

poster_content = {
    'text': 'My Message on the poster',
    'image_path': '/image1.jpg',
    # Add other elements as needed
}

target_platform = input("Enter target social media platform: ")
target_dimensions = social_media_dimensions.get(target_platform, None)

if not target_dimensions:
    print("Invalid platform.")
    exit()



def resize_poster(poster_content, target_width, target_height):
    # Create a blank canvas with the target dimensions
    poster = Image.new('RGB', (target_width, target_height), color='white')

    # Add text to the poster
    draw = ImageDraw.Draw(poster)
    font = ImageFont.load_default()
    draw.text((10, 10), poster_content['text'], font=font, fill='black')

    # Add image to the poster
    image = Image.open(poster_content['image_path'])
    image = image.resize((target_width, target_height), Image.ANTIALIAS)
    poster.paste(image, (0, 0))

    poster.save(f'poster_{target_platform}.jpg')

# Resize the poster for the chosen platform
resize_poster(poster_content, target_dimensions['width'], target_dimensions['height'])

print(f"Final poster for {target_platform} is ready.")

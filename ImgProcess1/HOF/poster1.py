from PIL import Image

social_media_dimensions = {
    'Facebook': {'width': 1200, 'height': 628},
    'Twitter': {'width': 1500, 'height': 500},
    'Instagram': {'width': 1080, 'height': 1080},
    # Add dimensions for other platforms
}
target_platform = input("Enter target social media platform: ")
target_dimensions = social_media_dimensions.get(target_platform, None)

if not target_dimensions:
    print("Invalid platform.")
    exit()



def resize_poster(poster_path, target_width, target_height):
    original_image = Image.open(poster_path)
    resized_image = original_image.resize((target_width, target_height))
    resized_image.save('resized_poster.jpg')

# Assuming poster_path is the path to the original poster image
resize_poster(poster_path, target_dimensions['width'], target_dimensions['height'])


def add_watermark(original_image_path, watermark_image_path, output_image_path, position):
    original_image = Image.open(original_image_path)
    watermark = Image.open(watermark_image_path)
    original_image.paste(watermark, position, watermark)
    original_image.save(output_image_path)

# Example: Add a watermark to the resized poster
watermark_path = '~/watermark.png'
output_path = '~/final_poster.jpg'
add_watermark('resized_poster.jpg', watermark_path, output_path, position=(10, 10))

print(f"Final poster for {target_platform} is ready: {output_path}")

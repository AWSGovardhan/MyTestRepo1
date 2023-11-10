import pymongo
from PIL import Image
from io import BytesIO

# Connect to the MongoDB server
client = pymongo.MongoClient("mongodb://localhost:27017")

# Access the database and collection
# db = client["your_database_name"]
# collection = db["your_collection_name"]

db = client["local"]
collection = db["imges"]

# Open the image file using Pillow
image = Image.open("images/pic-1.png")

# Convert the image to bytes
image_bytes = BytesIO()
image.save(image_bytes, format="PNG")
image_data = image_bytes.getvalue()

# Create a document with the image data
data = {
    "image_name": "example_image.jpg",
    "image_data": image_data
}

# Insert the image document into the collection
collection.insert_one(data)

# Close the MongoDB connection when done
client.close()

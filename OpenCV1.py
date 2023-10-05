import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load an image from a file
image_path = 'path_to_image.jpg'
image = cv2.imread(image_path)

# Check if the image was successfully loaded
if image is None:
    print("Error: Could not open or read the image.")
else:
    # Display the original image
    cv2.imshow('Original Image', image)
    cv2.waitKey(0)  # Wait for a key press to close the window
    cv2.destroyAllWindows()

    # Convert the image to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Display the grayscale image
    cv2.imshow('Grayscale Image', gray_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # Apply Gaussian blur to the grayscale image
    blurred_image = cv2.GaussianBlur(gray_image, (5, 5), 0)

    # Display the blurred image
    cv2.imshow('Blurred Image', blurred_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # Detect edges in the blurred image using the Canny edge detector
    edges = cv2.Canny(blurred_image, 100, 200)

    # Display the edge-detected image
    cv2.imshow('Edge-detected Image', edges)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # Save the processed image to a file
    processed_image_path = 'processed_image.jpg'
    cv2.imwrite(processed_image_path, edges)
    print(f"Processed image saved as '{processed_image_path}'.")

    # Display the processed image using Matplotlib
    plt.imshow(edges, cmap='gray')
    plt.title('Edge-detected Image (Matplotlib)')
    plt.axis('off')  # Hide axes
    plt.show()

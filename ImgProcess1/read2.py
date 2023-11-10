import cv2

# Load an image
image = cv2.imread("Photos/Cup1.jpg")

# Check if the image was loaded successfully
if image is not None:
    # Display the image
    cv2.imshow("Custom Title for Image", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Failed to load the image.")

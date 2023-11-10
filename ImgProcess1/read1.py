import cv2 as cv

imgArray = cv.imread('Photos/Cup1.jpg')

# cv.imshow('Cup-n-Saucer Image',imgArray)

# cv.waitKey(0)

print(type(imgArray))
print(imgArray.ndim)
print(imgArray.size)
print(imgArray.shape)
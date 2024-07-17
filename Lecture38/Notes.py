# Displaying and Manipulating Images with OpenCV

import cv2

# Read an image
image = cv2.imread('path_to_image.jpg')

# Display the image
cv2.imshow('Image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()

#This code reads an image from a file, displays it using OpenCV's imshow function, and waits indefinitely (cv2.waitKey(0)) for a key press to close the window (cv2.destroyAllWindows()).

# Convert the image to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

#cv2.cvtColor converts the color image (image) from BGR to grayscale (cv2.COLOR_BGR2GRAY).

# Resize the image to 100x100
resized_image = cv2.resize(image, (100, 100))

#cv2.resize resizes the image (image) to a specified size (100, 100).

# Draw a rectangle
cv2.rectangle(image, (50, 50), (150, 150), (255, 0, 0), 2)

# Draw a circle
cv2.circle(image, (100, 100), 50, (0, 255, 0), 2)

# Display the image with shapes
cv2.imshow('Shapes', image)
cv2.waitKey(0)
cv2.destroyAllWindows()

#cv2.rectangle and cv2.circle draw a rectangle and a circle on image, respectively. They are displayed together with imshow, waiting for a key press to close.

# Apply Gaussian blur
blurred_image = cv2.GaussianBlur(image, (5, 5), 0)

# Apply Canny edge detection
edges = cv2.Canny(gray_image, 100, 200)

# Display the edges
cv2.imshow('Edges', edges)
cv2.waitKey(0)
cv2.destroyAllWindows()

"""cv2.GaussianBlur applies Gaussian blur with a kernel size (5, 5).
cv2.Canny performs Canny edge detection on gray_image with thresholds 100 and 200."""

# Extracting HOG Features with scikit-image
import cv2
from skimage.feature import hog
import matplotlib.pyplot as plt

# Read the image
image = cv2.imread('path_to_image.jpg', cv2.IMREAD_GRAYSCALE)

# Resize the image
image = cv2.resize(image, (128, 64))

# Extract HOG features
features, hog_image = hog(image, pixels_per_cell=(8, 8), cells_per_block=(2, 2), visualize=True)

# Display the HOG image
plt.imshow(hog_image, cmap='gray')
plt.title('HOG Features')
plt.show()

"""cv2.imread reads the image in grayscale (cv2.IMREAD_GRAYSCALE).
cv2.resize resizes the image to (128, 64) pixels.
hog computes the HOG features with specified parameters (pixels_per_cell, cells_per_block).
plt.imshow and plt.show display the computed HOG features as an image using Matplotlib."""

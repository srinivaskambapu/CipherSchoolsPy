# Loading and Exploring the Dataset

from tensorflow.keras.datasets import fashion_mnist
import numpy as np

# Load the dataset
(x_train, y_train), (x_test, y_test) = fashion_mnist.load_data()

# Display dataset shapes
print("Training data shape:", x_train.shape)
print("Training labels shape:", y_train.shape)
print("Testing data shape:", x_test.shape)
print("Testing labels shape:", y_test.shape)

# Visualizing the Dataset

import matplotlib.pyplot as plt

# Function to plot initial images with labels
def plot_initial_images(images, labels, class_names):
    fig, axes = plt.subplots(1, 10, figsize=(20, 3))
    for i in range(10):
        ax = axes[i]
        ax.imshow(images[i], cmap='gray')
        ax.set_title(class_names[labels[i]])
        ax.axis('off')
    plt.show()

# Class names for Fashion MNIST
class_names = ['T-shirt/top', 'Trouser/pants', 'Pullover', 'Dress', 'Coat',
               'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']

# Plot initial images with labels
plot_initial_images(x_train, y_train, class_names)

# Data Preprocessing

# Normalize the data to scale pixels between 0 and 1
x_train = x_train / 255.0
x_test = x_test / 255.0

# Reshape images for HOG feature extraction
x_train = x_train.reshape(x_train.shape[0], 28, 28, 1)
x_test = x_test.reshape(x_test.shape[0], 28, 28, 1)

print("Reshaped Training data shape:", x_train.shape)
print("Reshaped Testing data shape:", x_test.shape)

#Extracting HOG Features

import cv2
from skimage.feature import hog

def extract_hog_features(images):
    hog_features = []
    for image in images:
        # Extract HOG features
        features = hog(image, pixels_per_cell=(4, 4), cells_per_block=(2, 2), visualize=False, multichannel=False)
        hog_features.append(features)
    return np.array(hog_features)

# Extract HOG features from training and testing data
x_train_hog = extract_hog_features(x_train)
x_test_hog = extract_hog_features(x_test)

# Display shapes of HOG features
print("Training HOG features shape:", x_train_hog.shape)
print("Testing HOG features shape:", x_test_hog.shape)

#Training SVM Classifier with HOG Features

from sklearn.svm import SVC

# Create SVM classifier with linear kernel
classifier = SVC(kernel='linear', random_state=0)

# Train the classifier on HOG features
classifier.fit(x_train_hog, y_train)

# Evaluate training accuracy
train_accuracy = classifier.score(x_train_hog, y_train)
print("Training Accuracy:", train_accuracy)

# Evaluate testing accuracy
test_accuracy = classifier.score(x_test_hog, y_test)
print("Testing Accuracy:", test_accuracy)

# Visualizing Predictions

# Get predictions on the test set
y_pred = classifier.predict(x_test_hog)

# Function to plot images with true and predicted labels
def plot_output_images(images, true_labels, predicted_labels, class_names):
    fig, axes = plt.subplots(1, 10, figsize=(20, 3))
    for i in range(10):
        ax = axes[i]
        ax.imshow(images[i].reshape(28, 28), cmap='gray')
        ax.set_title(f"True: {class_names[true_labels[i]]}\nPred: {class_names[predicted_labels[i]]}", fontsize=10)
        ax.axis('off')
    plt.tight_layout()
    plt.show()

# Plot some test images along with their true and predicted labels
plot_output_images(x_test, y_test, y_pred, class_names)
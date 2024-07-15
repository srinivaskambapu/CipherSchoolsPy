"""Data Manipulation and Analysis with NumPy
    Installation and Import
        To get started with NumPy, you need to install it using pip and import it into your Python script."""

#run these first
#pip install numpy
import numpy as np
"""Creating Arrays
Creating a 1D Array from a List"""

arr1 = np.array([10, 20, 30, 40, 50])
print(arr1)
# Output: [10 20 30 40 50]
#Creating a 2D Array from a List of Lists

arr2 = np.array([[10, 20, 30], [40, 50, 60]])
print(arr2)
# Output:
# [[10 20 30]
#  [40 50 60]]

"""Creating Arrays with Functions
Array of Zeros"""

zeros = np.zeros((4, 5))
print(zeros)
# Output:
# [[0. 0. 0. 0. 0.]
#  [0. 0. 0. 0. 0.]
#  [0. 0. 0. 0. 0.]
#  [0. 0. 0. 0. 0.]]

#Array of Ones

ones = np.ones((3, 4))
print(ones)
# Output:
# [[1. 1. 1. 1.]
#  [1. 1. 1. 1.]
#  [1. 1. 1. 1.]]

#Array with a Range of Values

range_arr = np.arange(5, 15, 2)
print(range_arr)
# Output: [ 5  7  9 11 13]

#Array with Random Values

random_arr = np.random.rand(4, 4)
print(random_arr)
# Output:
# [[0.68513231 0.07814781 0.36626845 0.95607844]
#  [0.60533412 0.85994041 0.96322264 0.34316617]
#  [0.18962002 0.75315849 0.69763621 0.17132924]
#  [0.24416829 0.51731535 0.59652975 0.48443296]]

#Basic Array Operations - Element Wise Operations

arr = np.array([10, 20, 30, 40, 50])

# Element-wise operations
print(arr + 3)
# Output: [13 23 33 43 53]

print(arr * 2)
# Output: [20 40 60 80 100]

print(arr - 5)
# Output: [ 5 15 25 35 45]

print(arr / 2)
# Output: [ 5. 10. 15. 20. 25.]

#Mathematical Functions

arr = np.array([2, 4, 6, 8, 10])

print(np.sqrt(arr))
# Output: [1.41421356 2.         2.44948974 2.82842712 3.16227766]

print(np.exp(arr))
# Output: [7.38905610e+00 5.45981500e+01 4.03428793e+02 2.98095799e+03 2.20264658e+04]

print(np.log(arr))
# Output: [0.69314718 1.38629436 1.79175947 2.07944154 2.30258509]

print(np.sin(arr))
# Output: [ 0.90929743 -0.7568025  -0.2794155   0.98935825 -0.54402111]

#Indexing and Slicing
#Slicing
arr = np.array([10, 20, 30, 40, 50])

print(arr[1:4])
# Output: [20 30 40]

print(arr[:3])
# Output: [10 20 30]

print(arr[2:])
# Output: [30 40 50]
#Advanced Indexing
#Boolean Indexing
arr = np.array([10, 20, 30, 40, 50])

print(arr[arr > 25])
# Output: [30 40 50]

#Fancy Indexing
arr = np.array([10, 20, 30, 40, 50])
indices = [0, 2, 4]

print(arr[indices])
# Output: [10 30 50]
#Reshaping and Transposing
#Reshaping Arrays
arr = np.array([[10, 20, 30], [40, 50, 60]])
print(arr)
# Output:
# [[10 20 30]
#  [40 50 60]]

reshaped = arr.reshape((3, 2))
print(reshaped)
# Output:
# [[10 20]
#  [30 40]
#  [50 60]]
#Transposing Arrays
arr = np.array([[10, 20, 30], [40, 50, 60]])
transposed = arr.T
print(transposed)
# Output:
# [[10 40]
#  [20 50]
#  [30 60]]
#Aggregation Functions
#Sum and Mean
arr = np.array([[10, 20, 30], [40, 50, 60]])

print(np.sum(arr))
# Output: 210

print(np.sum(arr, axis=0))  # Sum along columns
# Output: [50 70 90]

print(np.sum(arr, axis=1))  # Sum along rows
# Output: [ 60 150]

print(np.mean(arr))  # Mean of all elements
# Output: 35.0

print(np.argmin(arr))  # Index of minimum value
# Output: 0

print(np.argmax(arr))  # Index of maximum value
# Output: 5
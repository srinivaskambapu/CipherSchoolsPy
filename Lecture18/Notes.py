"""Introduction to Matplotlib and Seaborn
Installing Matplotlib"""

#pip install matplotlib
#Basic Line Plot with Matplotlib

import matplotlib.pyplot as plt

# Data
x = [1, 2, 3, 4, 5]
y = [3, 6, 9, 12, 15]

# Create a line plot
plt.plot(x, y, linestyle=':', color='b', linewidth=2, marker='o', markerfacecolor='b', markersize=8)
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Basic Line Plot')
plt.show()
#Multiple Line Plots with Matplotlib

import numpy as np
import matplotlib.pyplot as plt

# Data
y1 = np.array([1, 4, 2, 8])
y2 = np.array([3, 6, 1, 9])

plt.plot(y1)
plt.plot(y2)
plt.show()
#Scatter Plot with Matplotlib

import matplotlib.pyplot as plt

# Data
x = [1, 2, 3, 4, 5]
y = [5, 7, 3, 8, 10]

# Create a scatter plot
plt.scatter(x, y, color='g')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Scatter Plot')
plt.show()
#Simple Bar Plot with Matplotlib

# Data
products = ['Laptop', 'Tablet', 'Smartphone', 'Monitor']
sales = [10, 15, 7, 13]

# Creating a bar plot
plt.bar(products, sales, color='purple', width=0.5)
plt.xlabel('Products')
plt.ylabel('Sales')
plt.title('Bar Plot')
plt.show()
#Horizontal Bar Plot with Matplotlib
# Data
products = ['Laptop', 'Tablet', 'Smartphone', 'Monitor']
sales = [10, 15, 7, 13]

# Creating a horizontal bar plot
plt.barh(products, sales, color='orange', height=0.5)
plt.xlabel('Sales')
plt.ylabel('Products')
plt.title('Horizontal Bar Plot')
plt.show()
#Histogram with Matplotlib

# Data
data = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5]

# Creating a histogram
plt.hist(data, bins=5, color='cyan')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.title('Histogram')
plt.show()

#Subplots with Matplotlib
# Data
x = [1, 2, 3, 4, 5]
y1 = [2, 4, 6, 8, 10]
y2 = [1, 3, 5, 7, 9]

# Creating subplots
fig, axs = plt.subplots(2)
axs[0].plot(x, y1, color='red')
axs[0].set_title('First Plot')
axs[1].plot(x, y2, color='blue')
axs[1].set_title('Second Plot')

# Displaying the plot
plt.tight_layout()
plt.show()
#Adding Annotations with Matplotlib
# Data
x = [1, 2, 3, 4, 5]
y = [5, 7, 10, 15, 20]

# Creating a plot with annotations
plt.plot(x, y)
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Plot with Annotations')
plt.annotate('Peak', xy=(5, 20), xytext=(4, 18), arrowprops=dict(facecolor='black', shrink=0.05))
plt.show()

#Simple Line Plot with Seaborn
import seaborn as sns
import matplotlib.pyplot as plt

# Data
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

# Creating a line plot
sns.lineplot(x=x, y=y)
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Simple Line Plot with Seaborn')
plt.show()

#Simple Bar Plot with Seaborn
import seaborn as sns
import matplotlib.pyplot as plt

# Data
categories = ['A', 'B', 'C', 'D']
values = [10, 15, 5, 8]

# Creating a bar plot
sns.barplot(x=categories, y=values)
plt.xlabel('Categories')
plt.ylabel('Values')
plt.title('Bar Plot with Seaborn')
plt.show()

#Pair Plot with Seaborn
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris

# Loading iris dataset
iris_data = sns.load_dataset("iris")

# Creating a pair plot
sns.pairplot(iris_data, hue='species')
plt.title('Pair Plot with Seaborn')
plt.show()

#Heatmap with Seaborn
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

# Data
data = np.random.rand(10, 12)

# Creating a heatmap
sns.heatmap(data, cmap='viridis')
plt.title('Heatmap with Seaborn')
plt.show()
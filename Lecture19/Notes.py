"""Creating Interactive Visualizations with Plotly
Installing Plotly"""
#pip install plotly
#Loading the Dataset

import pandas as pd

# Load the dataset
df = pd.read_csv('/content/Sales.csv')
print(df.head())

#Creating a Line Plot

import plotly.express as px

# Create a line plot
fig = px.line(df, x='Date', y='Sales', title='Sales Trend Over Time', markers=True)
fig.show()

#Creating a Bar Chart

import plotly.express as px

# Create a bar chart
fig = px.bar(df, x='Region', y='Sales', title='Sales by Region', color='Region')
fig.show()

#Creating a Scatter Plot

import plotly.express as px

# Create a scatter plot
fig = px.scatter(df, x='Sales', y='Profit', title='Sales vs Profit', color='Region', size='Quantity', hover_data=['Product'])
fig.show()

#Creating a Histogram

import plotly.express as px

# Create a histogram
fig = px.histogram(df, x='Sales', title='Distribution of Sales', nbins=10)
fig.show()

#Creating a Pie Chart

import plotly.express as px

# Create a pie chart
fig = px.pie(df, values='Sales', names='Product', title='Sales Distribution by Product')
fig.show()

#Creating an Interactive Line Chart

import plotly.express as px

# Create an interactive line chart
fig = px.line(df, x='Date', y='Sales', title='Interactive Sales Trend Over Time', markers=True, color='Region', hover_data=['Product', 'Quantity', 'Profit'])
fig.show()

#Creating a Geographical Map
import plotly.express as px
import pandas as pd

# Sample data
data = {
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix'],
    'State': ['NY', 'CA', 'IL', 'TX', 'AZ'],
    'Population': [8419000, 3980400, 2716000, 2328000, 1690000]
}

# Creating the DataFrame
df = pd.DataFrame(data)

# Create a geographical map
fig = px.choropleth(df, locations='State', locationmode='USA-states', color='Population', scope='usa', title='Population by State')
fig.show()
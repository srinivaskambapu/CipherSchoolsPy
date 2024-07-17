#Import necessary libraries for data processing, machine learning, and building the Dash application.

import pandas as pd
import nltk
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline
from sklearn.model_selection import train_test_split
import dash
from dash import dcc, html
from dash.dependencies import Input, Output

#Load the dataset and preprocess the text data.


# Load dataset
data = pd.read_excel('training dataset.xlsx')

# Data preprocessing
nltk.download('punkt')
data['Concept'] = data['Concept'].apply(lambda x: ' '.join(nltk.word_tokenize(x.lower())))

#Split the data into training and testing sets.


# Split data
x_train, x_test, y_train, y_test = train_test_split(data['Concept'], data['Description'], test_size=0.2, random_state=42)

#Create a model pipeline with TF-IDF vectorization and Naive Bayes classifier, then train the model.


# Create model pipeline
model = make_pipeline(TfidfVectorizer(), MultinomialNB())
model.fit(x_train, y_train)

#Define a function to get the response from the trained model.

def get_response(question):
    question = ' '.join(nltk.word_tokenize(question.lower()))
    answer = model.predict([question])[0]
    return answer

#Initialize the Dash app and define the layout.

# Initialize Dash app
app = dash.Dash(__name__)

# Define layout
app.layout = html.Div([
    html.H1("ChatBot", style={'textAlign': 'center'}),
    dcc.Textarea(id='user-input', value='Ask something...', style={'width': '100%', 'height': 100}),
    html.Button('Submit', id='submit-button', n_clicks=0),
    html.Div(id='chatbot-output', style={'padding': '10px'})
])

#Define a callback function to update the chatbot response based on user input.

@app.callback(
    Output('chatbot-output', 'children'),
    [Input('submit-button', 'n_clicks')],
    [dash.dependencies.State('user-input', 'value')]
)
def update_output(n_clicks, user_input):
    if n_clicks > 0:
        response = get_response(user_input)
        return html.Div([
            html.P(f"You: {user_input}", style={'margin': '10px'}),
            html.P(f"ChatBot: {response}", style={'margin': '10px', 'backgroundColor': 'beige', 'padding': '10px'})
        ])
    return "Ask me something!"

#Run the Dash app in debug mode.

if __name__ == '__main__':
    app.run_server(debug=True)
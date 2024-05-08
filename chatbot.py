import re
import json
import random
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
import pickle as pk
lemmatizer = WordNetLemmatizer()

# Load intents from JSON file
with open('datasets/intents.json') as file:
    intents = json.load(file)

def clean_up_sentence(sentence):
    # Tokenize sentence
    tokens = word_tokenize(sentence)
    # Lemmatize words
    lemmatized_tokens = [lemmatizer.lemmatize(word.lower()) for word in tokens]
    return lemmatized_tokens

def get_response(user_query, intents):
    # Clean up user query
    cleaned_query = clean_up_sentence(user_query)
    
    # Iterate through intents
    for intent in intents['intents']:
        # Iterate through patterns in each intent
        for pattern in intent['patterns']:
            # Clean up pattern
            cleaned_pattern = clean_up_sentence(pattern)
            # Check if all words in pattern are in user query
            if all(word in cleaned_query for word in cleaned_pattern):
                # Return a random response from the matched intent
                return random.choice(intent['responses'])
    
    # If no intent is matched, return a default response
    return "Sorry, I didn't understand that."

# Example usage:
user_query = "Do you have any resources?"
response = get_response(user_query, intents)
print(response)

from flask import Flask, request, jsonify, render_template_string
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
import string
import numpy as np

app = Flask(__name__)

# Ensure you have the stopwords dataset downloaded
import nltk
nltk.download('punkt')
nltk.download('stopwords')

df = pd.read_pickle('data/processed_quotes.pkl')
def preprocess_text(text):
    # Convert text to lowercase
    text = text.lower()
    # Remove punctuation
    text = text.translate(str.maketrans('', '', string.punctuation))
    # Tokenize
    tokens = word_tokenize(text)
    # Remove stopwords
    stop_words = set(stopwords.words('english'))
    tokens = [word for word in tokens if word not in stop_words]
    # Stemming
    stemmer = PorterStemmer()
    tokens = [stemmer.stem(word) for word in tokens]
    # Join the tokens back into a string
    return ' '.join(tokens)
# Vectorizing the quotes
vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(df['processed_quote'])

# Function to find similar quotes
def find_similar_quotes(query, top_n=20):
    # Preprocess the query
    query_processed = preprocess_text(query)
    # Vectorize the query
    query_vec = vectorizer.transform([query_processed])
    # Calculate cosine similarity
    cosine_similarities = cosine_similarity(query_vec, tfidf_matrix).flatten()
    # Get the top_n similar quotes indices
    similar_indices = np.argsort(-cosine_similarities)[:top_n]
    # Return the top_n similar quotes
    return df.iloc[similar_indices]

@app.route('/')
def home():
    return render_template_string(open('index.html').read())

@app.route('/search', methods=['POST'])
def search():
    query = request.form['query']
    results = find_similar_quotes(query)
    return jsonify(results=[{'quote': row['quote'], 'author': row['author'], 'category': row['category']} for index, row in results.iterrows()])

if __name__ == '__main__':
    app.run(debug=True)

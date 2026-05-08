import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pickle

# Load dataset
books = pd.read_csv('Books.csv')

# Keep required columns
books = books[['Book-Title', 'Book-Author', 'Image-URL-M']]

# Use smaller dataset
books = books.head(1000)

# Rename columns
books.columns = ['title', 'authors', 'image_url']

# Remove null values
books.dropna(inplace=True)

# Remove duplicates
books.drop_duplicates(subset='title', inplace=True)
books = books.iloc[:5000]

# Create tags
books['tags'] = books['title'] + ' ' + books['authors']

# Vectorization
cv = CountVectorizer(max_features=5000, stop_words='english')

vector = cv.fit_transform(books['tags'])
similarity = cosine_similarity(vector)

# Save files
pickle.dump(books, open('books.pkl', 'wb'))
pickle.dump(similarity, open('similarity.pkl', 'wb'))

print("Model created successfully")
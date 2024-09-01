import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# let's suppose this is our small dataset
data = {
    'resource_id': [1, 2, 3, 4, 5],
    'title': ['Physics: An introduction', 'The magic of Chemistry', 'Biology: The life science', 'Math for fun', 'Space: The final frontier'],
    'keywords': ['physics', 'chemistry', 'biology', 'mathematics', 'astronomy']
}

df = pd.DataFrame(data)

# The student shows interest in Physics
student_interests = ['physics']

# Using CountVectorizer to convert text into matrix of token counts
vectorizer = CountVectorizer().fit_transform(df['keywords'])
vectors = vectorizer.toarray()

# Now, let's get the cosine similarity matrix from these vectors
csim = cosine_similarity(vectors)

# Get the index of the resource that the student is interested in
resource_index = df[df['keywords'].isin(student_interests)].index[0]

# Get a list of similar resources in descending order of similarity score
similar_resources = list(enumerate(csim[resource_index]))
similar_resources = sorted(similar_resources, key=lambda x:x[1], reverse=True)

# print titles of top 2 most similar resources
for i in similar_resources[1:3]:
    print(df.title[i[0]])
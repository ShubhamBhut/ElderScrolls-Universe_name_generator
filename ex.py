from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.cluster import KMeans
import numpy as np

# Sample data (replace this with your dataset)
names = ["Alduin", "Paarthurnax", "Dovahkiin", "Serana", "Nazeem", "Farkas", "Maiq the Liar"]

# Step 2: Tokenization
tokenized_names = [name.split() for name in names]

# Step 3: Vectorization
vectorizer = TfidfVectorizer()
name_vectors = vectorizer.fit_transform([" ".join(tokens) for tokens in tokenized_names])

# Step 4: Similarity Measures
similarity_matrix = cosine_similarity(name_vectors)

# Step 5: Clustering
num_clusters = 2  # Adjust based on your dataset
kmeans = KMeans(n_clusters=num_clusters, random_state=42)
clusters = kmeans.fit_predict(similarity_matrix)

# Step 6: Outlier Detection
centroid_vectors = np.array([np.mean(name_vectors[clusters == i].toarray(), axis=0) for i in range(num_clusters)])
distances_to_centroids = [np.linalg.norm(name_vector - centroid) for name_vector, centroid in zip(name_vectors.toarray(), centroid_vectors)]

# Identify outliers
outliers = [names[i] for i, distance in enumerate(distances_to_centroids) if distance > np.mean(distances_to_centroids) + np.std(distances_to_centroids)]

print("Clusters:", clusters)
print("Outliers:", outliers)

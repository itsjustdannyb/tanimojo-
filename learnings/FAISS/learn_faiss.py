import faiss
import numpy as np
import time

start = time.time()
# random vectors
dimension = 64
num_vectors = 1000000

vectors = np.random.random((num_vectors, dimension)).astype("float32")


index = faiss.IndexFlatL2(dimension)

# add vectors to index
index.add(vectors)

print("index created with", index.ntotal, "vectors.")

# perform a similarity search
query_vector = np.random.random((1, dimension)).astype("float32")

# search for top k nearest neighbors

k = 5
distances, indices = index.search(query_vector, k)

print("Distances", distances)
print("indices of nearest neighbor", indices)

print("time:", time.time() - start)
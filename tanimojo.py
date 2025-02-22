import numpy as np
import pickle
import os
from deepface import DeepFace
from utils import get_image_embedding, search, get_embeddings

imgs_path = r"C:\Users\Daniel\Desktop\tanimojo-\learnings\vhdl"


# # load vhdl image embeddings
with open("image_embeddings.pkl", "rb") as f:
    embeddings = pickle.load(f)

query = r"C:\Users\Daniel\Desktop\tanimojo-\1739977716275.jpg"

# print(len(embeddings))

dist, idx = search(embeddings, query)

# list of images
images = [img for img in embeddings]

# return name of image 
top_n_matches = {}
for i, pos in enumerate(idx[0]):
    top_n_matches[images[pos]] = dist[0][i]

# save top matches
with open("top_matches_moxie.pkl", "wb") as f:
    pickle.dump(top_n_matches, f)
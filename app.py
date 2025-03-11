import io
import pickle
import uvicorn
import numpy as np
from PIL import Image
from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware

from utils import get_image_embedding, search


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

# on load
@app.get('/')
async def home():
    return {'message': "try '/lookalike' "}


@app.post("/lookalike")
async def lookalike(file:UploadFile=File(...)):
    # # load vhdl image embeddings
    with open("image_embeddings.pkl", "rb") as f:
        embeddings = pickle.load(f)

    img_file = await file.read()
    img = Image.open(io.BytesIO(img_file))
    embedding = get_image_embedding(np.array(img))
    distances, indices = search(embeddings, embedding, search_space=3)

    # get best image match name
    # list of images
    images = [img for img in embeddings]

    # return name of image 
    top_n_matches = {}
    for i, pos in enumerate(indices[0]):
        top_n_matches[images[pos]] = distances[0][i]

    return {f"top {len(top_n_matches)} matche": top_n_matches}



# run app
if __name__ == "__main__":
    uvicorn.run(app)

# http://127.0.0.1:8000

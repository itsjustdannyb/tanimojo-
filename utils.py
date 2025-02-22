from deepface import DeepFace
import os
import numpy as np
import pickle
import faiss


def main():
    dimensions = 4096
    path = r"C:\Users\Daniel\Desktop\tanimojo-\learnings\vhdl"
    index = get_embeddings(path)


def get_embeddings(path, save_embeddings=False):
    """
    Get the image embeddings for all the images in a file
    Args: 
        path: str,
        save_embeddings:  bool

    Returns:
        image names, image embeddings
    """

    # store embeddings
    image_embeddings_names = {}
    images_removed = 0
    # no_images = len(os.listdir(path))
    image_names = os.listdir(path)

    # index = faiss.IndexFlatL2(dimensions)

    print("creating image embeddings...")
    # find embedding for all the faces
    for i, image in enumerate(image_names):
        try:
            embeddings = DeepFace.represent(img_path=os.path.join(path, image))[0]["embedding"]
            image_embeddings_names[image] = embeddings
            print(f"[{i+1}/{len(image_names)}] images")
        except (ValueError):
            # remove bad images
            os.system(f'copy {os.path.join(path, image)} {r"C:\Users\Daniel\Desktop\tanimojo-\error_imgs"}')
            os.remove(os.path.join(path, image))
            images_removed += 1
            continue
    # print("...saved image embeddings\n")
    print(f"removed {images_removed} images")


    # save embeddings as a pickle file
    if save_embeddings == True:
        with open("image_embeddings.pkl", "wb") as f:
            pickle.dump(image_embeddings_names, f)

    return image_embeddings_names



def get_image_embedding(image_path):
    """
    get embedding of a single image

    Args:  
        image_path (str)
    Returns: 
        embeddings (List(int))
    """

    
    print("creating image embedding...")

    try:
        embedding = DeepFace.represent(img_path=image_path)[0]["embedding"]
    except (ValueError):
        print("bad image! ")

    print("embedding created")
        
    return embedding


def search(img_embeddings_names, query, dimensions=4096, search_space=5):
    """
    look for images similar to a query image
    
    Args:
        embeddings: Dict(str: List(int)),
        query: image path to search for (str),
        dimensions: embedding dimensions (int),
        search_space: no of searches to return (int)

    Returns:
        distances: embedding distances,
        indices: index of imaage searches in list of images
    """

    print("searching...")
    index = faiss.IndexFlatL2(dimensions)

    embeddings = []
    for img in img_embeddings_names:
        embeddings.append(img_embeddings_names[img])
        
    embeddings_np = np.array(embeddings).astype("float32")

    index.add(embeddings_np)

    # get image embeddings
    image_embedding = np.array(get_image_embedding(query)).astype("float32").reshape(1,-1)

    # search 
    distances, indices = index.search(image_embedding, search_space)

    print("------------ done ------------------")

    return distances, indices


if __name__ == "__main__":
    main()
import pickle
from PIL import Image
import os
import time

with open("top_matches_moxie.pkl", "rb") as f:
    results = pickle.load(f)


def view_images(results):
    imgs = [img for img in results]
    distances = [results[img] for img in imgs]

    for img in imgs:
        img_pth = os.path.join(r"C:\Users\Daniel\Desktop\tanimojo-\learnings\vhdl", img)
        img_show = Image.open(img_pth)
        img_show.show()
    return imgs, distances

imgs, dist = view_images(results)
print(imgs)
print(dist)



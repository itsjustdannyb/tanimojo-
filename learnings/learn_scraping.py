# #  learning to scrape images

# from bs4 import BeautifulSoup
# import requests

# with open("htmls/howtodad.html", "r") as f:
#     doc = BeautifulSoup(f, "html.parser")


# images = doc.find_all("img", attrs={"alt":"wolves laughing meme"})
# print(images[0]["src"])
# for i, img_tag in enumerate(images):
#     img_url = img_tag['src']
#     response = requests.get(img_url)
#     print(img_url, response.status_code)
#     with open(str(i) + ".jpg", "wb") as f:
#         for chunk in response.iter_content(chunk_size=128):
#             f.write(chunk)


from bs4 import BeautifulSoup
import requests

url = ""

# response = requests(url)

with open("htmls/howtodad.html", "r") as f:
    doc = BeautifulSoup(f, "html.parser")

print(doc.prettify())



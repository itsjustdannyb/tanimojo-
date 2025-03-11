from urllib.parse import urljoin
from bs4 import BeautifulSoup
import requests
import time
import os

url = "http://reg.run.edu.ng/class_register.php"


headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "en-US,en;q=0.6",
    "Cache-Control": "max-age=0",
    "Connection": "keep-alive",
    "Content-Type": "application/x-www-form-urlencoded",
    "Host": "reg.run.edu.ng",
    "Origin": "http://reg.run.edu.ng",
    "Referer": "http://reg.run.edu.ng/class_register",
    "Sec-GPC": "1",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36",
}


url_response = requests.get(url)
if (url_response.status_code) != 200:
    print("couldn't connect")

soup = BeautifulSoup(url_response.content, "html.parser")

# get list of all courses and thier htlml values
courses_codes = {}
course_tags = soup.find_all("option")[1:]
# print(course_tags)
for course in course_tags:
    course_code = course.get("value")
    courses_codes[course.text] = course_code
# print(courses_codes)


# Step 1: Set up the session
session = requests.Session()

form_data = {
    "hid_view_registered_per_course": "xjhhdhhs",
    "lstCoursesInPrograms" : courses_codes[' CPE 301 , DIGITAL SYSTEM DESIGN WITH VHDL , 2 unit(s)']
}

response = session.post(url, headers=headers, data=form_data)
soup = BeautifulSoup(response.text, "html.parser")

img_tags = soup.find_all("img")
images = []
for i, img in enumerate(img_tags):
    image_path = img.get("src")
    img_link = urljoin("http://reg.run.edu.ng/", image_path)
    images.append(img_link)


# save images
# if os.path.exists(os.path.join(os.getcwd(), "vhdl")):
#     os.mkdir("vhdl")
#     os.chdir(os.path.join(os.getcwd(), vhdl_img_folder))
#     print(os.getcwd())

# download images
def download_images(img_links, dir):
    os.chdir(dir)
    no_links = len(img_links)
    for i, link in enumerate (img_links):
        response = requests.get(link)
        print(f"[{i + 1}/{no_links}] images downloaded - {response.status_code}")
        with open(str(i) + ".jpg", "wb") as f:
            for chunk in response.iter_content(chunk_size=128):
                f.write(chunk)
    time.sleep(1) # make i no dos run portal, lol XD


cwd = os.path.join(os.getcwd(), "vhdl")
download_images(images[2:], cwd)
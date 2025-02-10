from bs4 import BeautifulSoup
import requests

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
print(url_response.status_code)

soup = BeautifulSoup(url_response.content, "html.parser")

# get list of all courses
all_courses = []
course_tags= soup.find_all("option")[1:]
for course in course_tags:
    all_courses.append(course.string)


# Step 1: Set up the session
session = requests.Session()

form_data = {
    "hid_view_registered_per_course": "xjhhdhhs",
    "lstCoursesInPrograms" : "UTFaRklEUXdPU295TURJeU1Ea3dNUT09LDM"
}

response = session.post(url, headers=headers, data=form_data)
soup = BeautifulSoup(response.text, "html.parser")

img_tags = soup.find_all("img")
print(img_tags[5])

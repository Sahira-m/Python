from PIL import image
import requests
import bs4

# Step 1: Use the requests library to grab the page
# Note, this may fail if you have a firewall blocking Python/Jupyter
# Note sometimes you need to run this twice if it fails the first time
res = requests.get("https://www.example.com")
print("type is", type(res))
print("result is", res.text)
# lxml package not installed successfully, So i don't get element data(div,p,..)
soup = bs4.BeautifulSoup(res.text, "lxml")
print("soup is", soup)
print("print title", soup.select("title"))
print("print title", soup.select("h1"))
print("print title", soup.select("p"))
# to get image from website
res = requests.get("https://en.wikipedia.org/wiki/Deep_Blue_(chess_computer)")
soup = bs4.BeautifulSoup(res.text, "lxml")
image_info = soup.select(".thumbimage")
print("image info", image_info)

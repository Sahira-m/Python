import requests
import bs4

# Step 1: Use the requests library to grab the page
# Note, this may fail if you have a firewall blocking Python/Jupyter
# Note sometimes you need to run this twice if it fails the first time
res = requests.get("https://www.example.com")
print(type(res))
print(res.text)
soup = bs4.BeautifulSoup(res.text, "lxml")
print("soup is", soup)
print("print title", soup.select("title"))
print("print title", soup.select("h1"))
print("print title", soup.select("p"))

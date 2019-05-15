from urllib.request import urlopen
from bs4 import BeautifulSoup
import pyexcel
from collections import OrderedDict

url = "https://www.bbcgoodfood.com/"

conn = urlopen(url)


raw_data = conn.read()

html_content = raw_data.decode('utf8')

with open("food_db.html", "wb") as f:
    f.write(raw_data)
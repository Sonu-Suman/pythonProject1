import requests
from bs4 import BeautifulSoup
import io

url = "https://www.nytimes.com/international/"
r = requests.get(url)

soup = BeautifulSoup(r.content, "html.parser")
links = soup.find_all("a")

g_data = soup.find_all('div')

for item in g_data:
    with io.open("nytimes.txt", "w", encoding="utf-8") as f:
        f.write(''.join(str(item.text)))
        f.close()
        print(item.text)
        break

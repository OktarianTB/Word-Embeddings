import requests
from bs4 import BeautifulSoup

url = "https://en.wikipedia.org/wiki/France"
data = requests.get(url)
soup = BeautifulSoup(data.text, 'html.parser')
text = soup.find_all(text=True)

output = ''
blacklist = ['[document]', 'noscript', 'header', 'html', 'meta', 'head', 'input', 'script']

for t in text:
    if t.parent.name not in blacklist and t != "\n":
        output += '{} '.format(t)

print(output)
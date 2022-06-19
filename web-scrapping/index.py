import requests
import bs4

results = requests.get("http://www.example.com/")

# print(results.text)

soup = bs4.BeautifulSoup(results.text, "lxml")

print(soup)

print(soup.select('title'), "\n")
print(soup.select('title')[0], "\n")
print(soup.select('title')[0].getText(), "\n")

print(soup.select('p'), "\n")
print(soup.select('p')[0], "\n")
print(soup.select('p')[0].getText(), "\n")


res = requests.get("https://en.wikipedia.org/wiki/Grace_Hopper")

soup = bs4.BeautifulSoup(res.text, 'lxml')

for item in soup.select('.toctext'):
    print(item.text)

i = 0

for img in soup.select('.thumbimage'):
    print(img['src'])
    imgd = requests.get("https:"+img['src'])
    f = open('image_'+str(i)+'.jpg', 'wb')
    f.write(imgd.content)
    i = i+1
    f.close()

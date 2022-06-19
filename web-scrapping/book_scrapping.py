from pickle import TRUE
import requests
import bs4

baseUrl = "http://books.toscrape.com/catalogue/page-{}.html"


# print(baseUrl.format(1))
# res = requests.get(baseUrl.format(1))


# soup = bs4.BeautifulSoup(res.text, 'lxml')

# print(soup.select(".product_pod")[0].select("h3<a"))

two_star_book = []

for n in range(1, 51):
    res = requests.get(baseUrl.format(n))
    soup = bs4.BeautifulSoup(res.text, 'lxml')
    books = soup.select(".product_pod")
    print("page ---> ", n)

    for book in books:
        if len(book.select('.star-rating.Two')) != 0:
            book_title = book.select('a')[1]['title']
            two_star_book.append(book_title)


print(two_star_book)

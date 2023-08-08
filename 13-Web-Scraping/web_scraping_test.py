import requests
import bs4


base_url = "http://quotes.toscrape.com/page/{}"
search_author = input("Please select an author: ")

pages = True
page = 1
found = False

while pages:
    page += 1
    scrape_url = base_url.format(page)
    res = requests.get(scrape_url)

    if "No quotes found!" in res.text:
        break

    soup = bs4.BeautifulSoup(res.text, "lxml")
    for quote in soup.select(".quote"):
        if quote.select(".author")[0].text == search_author:
            found = True
            print(f"The quote is on page {page}")
            text = quote.select(".text")[0].text
            print("The quote is:")
            print(text)

if found == False:
    print("That author has not been found")

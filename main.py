import requests
from bs4 import BeautifulSoup as bs
import pandas as pd

base_url = "http://quotes.toscrape.com/page/{}/"

quote_list = []
author_list = []
tags = []

for page in range(1,6):
    response = requests.get(base_url.format(page))
    soup = bs(response.content, 'html.parser')

    all_quotes = soup.find_all('div', class_='quote')

    for quote in all_quotes:
        author = quote.find('small', class_='author').get_text()
        author_list.append(author)

        text = quote.find('span', class_='text').get_text()
        quote_list.append(text)

        all_tags = quote.find_all('a', class_='tag')
        tag_list = []
        for tag in all_tags:
            tag_list.append(tag.get_text())
        tags.append(', '.join(tag_list))

data = pd.DataFrame({
    'Quote': quote_list,
    'Author': author_list,
    'Tags': tags
})

data.to_csv('quote_list.csv', index=False)
# import requests
# from bs4 import BeautifulSoup
# import pandas as pd
#
# base_url = "http://quotes.toscrape.com/page/{}/"
#
# quotes = []
# authors = []
# tags = []
#
# for page in range(1, 6):
#     response = requests.get(base_url.format(page))
#     soup = BeautifulSoup(response.content, 'html.parser')
#
#     all_quotes = soup.find_all('div', class_='quote')
#
#     for quote in all_quotes:
#         author = quote.find('small', class_='author').get_text()
#         authors.append(author)
#
#         text = quote.find('span', class_='text').get_text()
#         quotes.append(text)
#
#         all_tags = quote.find_all('a', class_='tag')
#         tag_list = []
#         for tag in all_tags:
#             tag_list.append(tag.get_text())
#         tags.append(", ".join(tag_list))
#
#
# data = pd.DataFrame({
#     'Quote': quotes,
#     'Author': authors,
#     'Tags': tags
# })
#
#
# data.to_csv('quote_list.csv', index=False)
#

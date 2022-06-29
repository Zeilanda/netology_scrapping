
import requests
from bs4 import BeautifulSoup
from fake_headers import Headers

header = Headers(
    browser="chrome",  # Generate only Chrome UA
    os="win",  # Generate ony Windows platform
    headers=True  # generate misc headers
)


headers = header.generate()
KEYWORDS = ['дизайн', 'фото', 'web', 'python', 'electronic', 'wordle']

ret = requests.get('https://habr.com/ru/all/', headers=headers)

soup = BeautifulSoup(ret.text, 'html.parser')
articles = soup.find_all('article')
for article in articles:
    post_time = article.find('time')['title']
    post_title_links = article.find_all('h2', class_='tm-article-snippet__title tm-article-snippet__title_h2')

    for post_title_link in post_title_links:
        post_title = post_title_link.find_all('span')
        post_link = post_title_link.find('a')['href']
        post_title = [post_title.text.strip() for post_title in post_title][0]

        preview = article.find_all(class_='article-formatted-body article-formatted-body article-formatted-body_version-2')
        preview = [preview.text.strip() for preview in preview]
        for text in preview:
            text_words = text.split()
            for text_word in text_words:
                if text_word.lower() in KEYWORDS:
                    print(f'{post_time}-{post_title}-https://habr.com{post_link}')



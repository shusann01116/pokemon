import bs4
import requests

url = "https://zukan.pokemon.co.jp/detail/001"
value = requests.get(url)

soup = bs4.BeautifulSoup(value.content, features="html.parser")

metas = soup.head.find_all('meta')

# <meta content="https://zukan.pokemon.co.jp/zukan-api/up/images/index/5e1db695135dd89787cfe0927d08211c.jpg" property="og:image"/>

image_url = [meta.get('content') for meta in soup.head.find_all(
    'meta') if meta.get('property') == 'og:image'][0]

print(image_url)

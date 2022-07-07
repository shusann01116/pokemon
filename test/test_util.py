# pylint: disable=C0114, C0116, W0212
import bs4
import requests
from pokemon_collector import core, util


def test__parse_zukan_pokemon_co_jp():
    response = requests.get("https://zukan.pokemon.co.jp/detail/001")
    soup = bs4.BeautifulSoup(response.content, "html.parser")

    title = "フシギダネ｜ポケモンずかん"
    result_title = util.Collector._parse_zukan_pokemon_co_jp(soup, "og:title")

    assert title == result_title

    image_url = "https://zukan.pokemon.co.jp/zukan-api/up/images/index/5e1db695135dd89787cfe0927d08211c.jpg"
    result_url = util.Collector._parse_zukan_pokemon_co_jp(soup, "og:image")

    assert image_url == result_url


def test_fetch_pokemon_info():
    fushigidane = core.Pokemon(
        1,
        "フシギダネ｜ポケモンずかん",
        "https://zukan.pokemon.co.jp/zukan-api/up/images/index/5e1db695135dd89787cfe0927d08211c.jpg",
    )

    result = util.Collector.fetch_pokemon_info(1)

    assert fushigidane == result

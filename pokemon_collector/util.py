# pylint: disable=C0114
import bs4
import requests
from pokemon_collector import core


class Collector:
    def __init__(self) -> None:
        pass

    @staticmethod
    def fetch_pokemon_info(
        pokemon_id: int, base_url: str = "https://zukan.pokemon.co.jp/detail/"
    ) -> core.Pokemon:
        url = "".join([base_url, f"{pokemon_id:03}"])
        response = requests.get(url)
        soup = bs4.BeautifulSoup(response.content, features="html.parser")
        name = Collector._parse_zukan_pokemon_co_jp(soup, "og:title")
        image_url = Collector._parse_zukan_pokemon_co_jp(soup, "og:image")
        return core.Pokemon(pokemon_id, name, image_url)

    @staticmethod
    def _parse_zukan_pokemon_co_jp(soup: bs4.BeautifulSoup, meta_property: str) -> str:
        return str(
            [
                meta.get("content")
                for meta in soup.head.find_all("meta")
                if meta.get("property") == meta_property
            ][0]
        )

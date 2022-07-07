# pokemon

## Usage

```python
from pokemon_collector import core, util

pokemon_number = 1

result = util.Collector.fetch_pokemon_info(pokemon_number)
print(f"Name: {result.name}")
print(f"ImgURL: {result.image_url}")
```

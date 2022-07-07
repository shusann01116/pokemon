class Pokemon:
    def __init__(self, id_num: int, name: str, image_url: str) -> None:
        self.id_num: int = id_num
        self.name: str = name
        self.image_url: str = image_url

    def __eq__(self, __o: object) -> bool:
        return (
            isinstance(__o, Pokemon)
            and __o.id_num == self.id_num
            and __o.name == self.name
            and __o.image_url == self.image_url
        )

    def __ne__(self, __o: object) -> bool:
        return not self == __o

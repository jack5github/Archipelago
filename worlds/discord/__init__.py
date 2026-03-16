from BaseClasses import Tutorial
from worlds.AutoWorld import WebWorld, World
from . import locations


class DiscordWebWorld(WebWorld):
    theme: str = "ocean"
    setup_en: Tutorial = Tutorial(
        tutorial_name="TODO: Add title",
        description="TODO: Add description",
        language="English",
        file_name="setup_en.md",
        link="setup/en",
        authors=["Jack5"],
    )
    tutorials: list[Tutorial] = [setup_en]


class Discordworld(World):
    game: str = "Discord"
    web: DiscordWebWorld = DiscordWebWorld()
    origin_region_name: str = "Server"
    # TODO: Add items
    item_name_to_id: dict[str, int] = {}
    location_name_to_id: dict[str, int] = locations.location_names_to_ids

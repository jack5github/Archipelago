from BaseClasses import Location
from typing import Literal, TypeAlias
from . import options as ops


class DiscordLocation(Location):
    game = "Discord"


LocationType: TypeAlias = Literal[
    "button",
    "emoji-chain",
    "emoji-message",
    "file",
    "game-time",
    "gif",
    "join",
    "message",
    "phrase",
    "poll",
    "reaction",
    "reactions",
    "reply-chain",
    "spotify-time",
    "sticker",
    "voice-activity-time",
    "voice-time",
]


class DiscordLocationData:
    name: str
    loc_type: LocationType
    amount: int
    group: int | None

    def __init__(
        self, name: str, loc_type: LocationType, amount: int, group: int | None = None
    ) -> None:
        self.name = name.replace("%#", str(amount))
        if group is not None:
            if not loc_type.startswith("voice"):
                self.name += f" in Text Channel Group {group}"
            else:
                self.name += f" in Voice Channel Group {group}"
        self.loc_type = loc_type
        self.amount = amount
        self.group = group


locations: list[DiscordLocationData] = []
for i in range(ops.MAX_NEW_MEMBERS):
    locations.append(DiscordLocationData("%# New Members", "join", i + 1))
for i in range(ops.MAX_TRIGGER_WORDS):
    locations.append(DiscordLocationData("Trigger Word %#", "phrase", i + 1))
for i in range(ops.MAX_BUTTONS):
    locations.append(DiscordLocationData("Button %# Clicked", "button", i + 1))
for i in range(ops.MAX_GAME_HOURS):
    locations.append(DiscordLocationData("%# Hours of Games", "game-time", i + 1))
for i in range(ops.MAX_SPOTIFY_HOURS):
    locations.append(DiscordLocationData("%# Hours of Spotify", "spotify-time", i + 1))
for i in range(ops.MAX_MESSAGES):
    locations.append(DiscordLocationData("%# Messages Sent", "message", i + 1))
# TODO: Instead of generating all possible locations for all groups, reduce the number of generated locations depending on the group number, e.g. group 1 and 2 will generate half as many locations, group 3 will generate 1/3, group 4 1/4, etc.
for i in range(ops.MAX_MESSAGES):
    for j in range(ops.MAX_TEXT_GROUPS):
        locations.append(
            DiscordLocationData("%# Messages Sent", "message", i + 1, j + 1)
        )
for i in range(ops.MAX_REPLIES):
    locations.append(DiscordLocationData("%# Replies Sent", "message", i + 1))
for i in range(ops.MAX_REPLIES):
    for j in range(ops.MAX_TEXT_GROUPS):
        locations.append(
            DiscordLocationData("%# Replies Sent", "message", i + 1, j + 1)
        )
for i in range(ops.MAX_REPLY_CHAIN_LENGTH):
    locations.append(DiscordLocationData("%# Reply Chain Length", "reply-chain", i + 1))
for i in range(ops.MAX_REPLY_CHAIN_LENGTH):
    for j in range(ops.MAX_TEXT_GROUPS):
        locations.append(
            DiscordLocationData("%# Reply Chain Length", "reply-chain", i + 1, j + 1)
        )
for i in range(ops.MAX_SINGLE_MESSAGE_REACTIONS):
    locations.append(
        DiscordLocationData("%# Reactions on a Single Message", "reactions", i + 1)
    )
for i in range(ops.MAX_SINGLE_MESSAGE_REACTIONS):
    for j in range(ops.MAX_TEXT_GROUPS):
        locations.append(
            DiscordLocationData(
                "%# Reactions on a Single Message", "reactions", i + 1, j + 1
            )
        )
for i in range(ops.MAX_SINGLE_REACTIONS):
    locations.append(DiscordLocationData("%# of a Single Reaction", "reaction", i + 1))
for i in range(ops.MAX_SINGLE_REACTIONS):
    for j in range(ops.MAX_TEXT_GROUPS):
        locations.append(
            DiscordLocationData("%# of a Single Reaction", "reaction", i + 1, j + 1)
        )
for i in range(ops.MAX_EMOJI_ONLY_MESSAGES):
    locations.append(
        DiscordLocationData("%# Emoji-Only Messages Sent", "emoji-message", i + 1)
    )
for i in range(ops.MAX_EMOJI_ONLY_MESSAGES):
    for j in range(ops.MAX_TEXT_GROUPS):
        locations.append(
            DiscordLocationData(
                "%# Emoji-Only Messages Sent", "emoji-message", i + 1, j + 1
            )
        )
for i in range(ops.MAX_EMOJI_CHAIN_LENGTH):
    locations.append(DiscordLocationData("%# Emoji Chain Length", "emoji-chain", i + 1))
for i in range(ops.MAX_EMOJI_CHAIN_LENGTH):
    for j in range(ops.MAX_TEXT_GROUPS):
        locations.append(
            DiscordLocationData("%# Emoji Chain Length", "emoji-chain", i + 1, j + 1)
        )
for i in range(ops.MAX_GIFS):
    locations.append(DiscordLocationData("%# GIFs Sent", "gif", i + 1))
for i in range(ops.MAX_GIFS):
    for j in range(ops.MAX_TEXT_GROUPS):
        locations.append(DiscordLocationData("%# GIFs Sent", "gif", i + 1, j + 1))
for i in range(ops.MAX_STICKERS):
    locations.append(DiscordLocationData("%# Stickers Sent", "sticker", i + 1))
for i in range(ops.MAX_STICKERS):
    for j in range(ops.MAX_TEXT_GROUPS):
        locations.append(
            DiscordLocationData("%# Stickers Sent", "sticker", i + 1, j + 1)
        )
for i in range(ops.MAX_FILES):
    locations.append(DiscordLocationData("%# Files Sent", "file", i + 1))
for i in range(ops.MAX_FILES):
    for j in range(ops.MAX_TEXT_GROUPS):
        locations.append(DiscordLocationData("%# Files Sent", "file", i + 1, j + 1))
for i in range(ops.MAX_POLLS):
    locations.append(DiscordLocationData("%# Polls Run", "poll", i + 1))
for i in range(ops.MAX_POLLS):
    for j in range(ops.MAX_TEXT_GROUPS):
        locations.append(DiscordLocationData("%# Polls Run", "poll", i + 1, j + 1))
for i in range(ops.MAX_VOICE_HOURS):
    locations.append(DiscordLocationData("%# Hours of Voice", "voice-time", i + 1))
for i in range(ops.MAX_VOICE_HOURS):
    for j in range(ops.MAX_VOICE_GROUPS):
        locations.append(DiscordLocationData("%# Hours", "voice-time", i + 1, j + 1))
for i in range(ops.MAX_VOICE_ACTIVITY_HOURS):
    locations.append(
        DiscordLocationData(
            "%# Hours of Voice Activities", "voice-activity-time", i + 1
        )
    )
for i in range(ops.MAX_VOICE_ACTIVITY_HOURS):
    for j in range(ops.MAX_VOICE_GROUPS):
        locations.append(
            DiscordLocationData(
                "%# Hours of Activities", "voice-activity-time", i + 1, j + 1
            )
        )
location_names_to_locations: dict[str, DiscordLocationData] = {
    location.name: location for location in locations
}
location_names_to_ids: dict[str, int] = {
    location.name: i + 1 for i, location in enumerate(locations)
}
location_ids_to_names: dict[int, str] = {v: k for k, v in location_names_to_ids.items()}


if __name__ == "__main__":
    for loc_id, name in location_ids_to_names.items():
        print(f"{loc_id}: {name}")
    print(f"Produced {len(locations)} locations")

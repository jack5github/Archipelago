from dataclasses import dataclass
from Options import DefaultOnToggle, OptionGroup, PerGameCommonOptions, Range, Toggle

MAX_TEXT_GROUPS: int = 15  # WARNING: This being high can cause slow generation
MAX_VOICE_GROUPS: int = 10
MAX_TEAMS: int = MAX_TEXT_GROUPS
MAX_NEW_MEMBERS: int = 1000
MAX_TRIGGER_WORDS: int = 100
MAX_BUTTONS: int = 1000
MAX_GAME_HOURS: int = 10000
MAX_SPOTIFY_HOURS: int = 10000
MAX_MESSAGES: int = 50000  # WARNING: This being high can cause slow generation
MAX_REPLIES: int = 1000
MAX_REPLY_CHAIN_LENGTH: int = 50
MAX_SINGLE_MESSAGE_REACTIONS: int = 200
MAX_SINGLE_REACTIONS: int = 100
MAX_EMOJI_ONLY_MESSAGES: int = 1000
MAX_EMOJI_CHAIN_LENGTH: int = 25
MAX_GIFS: int = 200
MAX_STICKERS: int = 200
MAX_FILES: int = 200
MAX_POLLS: int = 50
MAX_VOICE_HOURS: int = 10000
MAX_VOICE_ACTIVITY_HOURS: int = 1000


class StartWithTextChannelsPercent(Range):
    """
    The percentage of text channels allocated to the Discord bot that will be available for users to view and send messages in at the start of an Archipelago run.

    If 0, no text channels will be available from the start, unless `start_with_voice_channels_percent` is also 0, in which case 1 will be available from the start.
    """

    display_name: str = "Start with Text Channels %"
    range_start: int = 0
    range_end: int = 100
    default: int = 1


class UnusedTextChannelsPercent(Range):
    """
    The percentage of text channels that are allocated to the Discord bot that will be permanently locked for the entirety of an Archipelago run. It will still be possible for users to view these channels should the 'View Channels' item be received.

    If this plus `start_with_text_channels_percent` is greater than 100, this will be decremented until both equate to 100.
    """

    display_name: str = "Unused Text Channels %"
    range_start: int = 0
    range_end: int = 100
    default: int = 0


class TextChannelGroups(Range):
    """
    The number of text channel groups. Each group will contain a roughly equal amount of 0 or more of the text channels that are allocated to the Discord bot. For each group, a 'Text Channel Group #' progression item will be added to the item pool.

    Unused if `start_with_text_channels_percent`, or `start_with_text_channels_percent` plus `unused_text_channels_percent`, equal 100.
    """

    display_name: str = "Text Channel Groups"
    range_start: int = 2
    range_end: int = MAX_TEXT_GROUPS
    default: int = 5


class StartWithVoiceChannelsPercent(Range):
    """
    The percentage of voice channels that are allocated to the Discord bot that will be available for users to view and join at the start of the Archipelago run.
    """

    display_name: str = "Start with Voice Channels %"
    range_start: int = 0
    range_end: int = 100
    default: int = 0


class UnusedVoiceChannelsPercent(Range):
    """
    The percentage of permanently locked voice channels. See `unused_text_channels_percent`.
    """

    display_name: str = "Unused Voice Channels %"
    range_start: int = 0
    range_end: int = 100
    default: int = 0


class VoiceChannelGroups(Range):
    """
    The number of voice channel groups. See `text_channel_groups`.
    """

    display_name: str = "Voice Channel Groups"
    range_start: int = 2
    range_end: int = MAX_VOICE_GROUPS
    default: int = 2


class TeamCount(Range):
    """
    The number of user teams to create from roles allocated to the Discord bot. At the start of an Archipelago run, each text and voice channel will be assigned to one of these teams in equal proportion. Over the course of the run, teams will merge together to form larger teams, until there is only one team left.

    If 1, all users will be able to access all text and voice channels, as they are all in the same team, effectively a teamless run.

    WARNING: The Discord bot will fail to connect to Archipelago if there are more teams than roles allocated to it.
    """

    display_name: str = "Team Count"
    range_start: int = 1
    range_end: int = MAX_TEAMS
    default: int = 1
    option_none: int = 1


class TeamMergeItems(Range):
    """
    The number of 'Progressive Team Merge' items to add to the item pool, which merge teams together to form larger teams.

    If greater than `team_count` + 1, this will be decremented until the condition is satisfied.
    """

    display_name: str = "Team Merge Items"
    range_start: int = 1
    range_end: int = MAX_TEAMS
    default: int = 5


class MaxSlowdown(Range):
    """
    The maximum amount of slowdown that is applied to all text channels allocated to the Discord bot.
    """

    display_name: str = "Max Slowdown"
    range_start: int = 0
    range_end: int = 13
    default: int = 5
    option_none: int = 0
    option_5_seconds: int = 1
    option_10_seconds: int = 2
    option_15_seconds: int = 3
    option_30_seconds: int = 4
    option_1_minute: int = 5
    option_2_minutes: int = 6
    option_5_minutes: int = 7
    option_10_minutes: int = 8
    option_15_minutes: int = 9
    option_30_minutes: int = 10
    option_1_hour: int = 11
    option_2_hours: int = 12
    option_6_hours: int = 13


class SlowmodeReductionItems(Range):
    """
    The number of 'Progressive Slowmode Reduction' items to add to the item pool, which reduce the slowdown of all text channels allocated to the Discord bot.

    Unused if `max_slowdown` is 0. If higher than `max_slowdown`, this will be decremented until both options are equal.
    """

    display_name: str = "Slowmode Reduction Items"
    range_start: int = 1
    range_end: int = 13
    default: int = 5


class EmbedLinksItemEnabled(DefaultOnToggle):
    """
    Whether to prevent users from embedding links in text channels allocated to the Discord bot at the start of an Archipelago run, and to add the 'Embed Links' item to the item pool.
    """

    display_name: str = "Embed Links Item Enabled"


class AttachFilesItemEnabled(DefaultOnToggle):
    """
    Whether the 'Attach Files' item can be found. See `embed_links_item_enabled`.
    """

    display_name: str = "Attach Files Item Enabled"


class AddReactionsItemEnabled(DefaultOnToggle):
    """
    Whether the 'Add Reactions' item can be found. See `embed_links_item_enabled`.
    """

    display_name: str = "Add Reactions Item Enabled"


class ReadMessageHistoryItemEnabled(DefaultOnToggle):
    """
    Whether the 'Read Message History' item can be found. See `embed_links_item_enabled`.
    """

    display_name: str = "Read Message History Item Enabled"


class SendTTSMessagesItemEnabled(DefaultOnToggle):
    """
    Whether the 'Send TTS Messages' item can be found. See `embed_links_item_enabled`.
    """

    display_name: str = "Send TTS Messages Item Enabled"


class SendVoiceMessagesItemEnabled(DefaultOnToggle):
    """
    Whether the 'Send Voice Messages' item can be found. See `embed_links_item_enabled`.
    """

    display_name: str = "Send Voice Messages Item Enabled"


class CreatePollsItemEnabled(DefaultOnToggle):
    """
    Whether the 'Create Polls' item can be found. See `embed_links_item_enabled`.
    """

    display_name: str = "Create Polls Item Enabled"


class UseAppCommandsItemEnabled(DefaultOnToggle):
    """
    Whether the 'Use Application Commands' item can be found. See `embed_links_item_enabled`.
    """

    display_name: str = "Use Application Commands Item Enabled"


class UseActivitiesItemEnabled(DefaultOnToggle):
    """
    Whether the 'Use Activities' item can be found. See `embed_links_item_enabled`.
    """

    display_name: str = "Use Activities Item Enabled"


class MaxNewMembers(Range):
    """
    The maximum number of new members that are expected to join the Discord server.

    If 0, locations related to new members joining the Discord server will not be created.
    """

    display_name: str = "Max New Members"
    range_start: int = 0
    range_end: int = MAX_NEW_MEMBERS
    # Off by default as this burden should not be placed on new servers
    default: int = 0
    option_none: int = 0


class NewMembersLocations(Range):
    """
    The number of locations to create in the world that will be checked upon a sufficient number of users joining the Discord server.

    Unused if `max_new_members` is 0. If greater than `max_new_members`, this will be decremented until both options are equal.
    """

    display_name: str = "New Members Locations"
    range_start: int = 1
    range_end: int = MAX_NEW_MEMBERS
    default: int = 5


class TriggerWords(Range):
    """
    The number of trigger words allocated to the Discord bot to randomly assign to new locations in the world. The first time a trigger word is mentioned in a user message, the item in the associated location is released.

    WARNING: The Discord bot will fail to connect to Archipelago if there are more locations than trigger words allocated to it.
    """

    display_name: str = "Trigger Words"
    range_start: int = 0
    range_end: int = MAX_TRIGGER_WORDS
    default: int = 5


class ButtonWidgetsItems(Range):
    """
    The number of 'Button Widgets' items to add to the item pool, which will cause the Discord bot to post several messages in random text channels containing button widgets that release items when clicked.

    If 0, locations related to button widgets will not be created.
    """

    display_name: str = "Button Widgets Items"
    range_start: int = 0
    range_end: int = MAX_BUTTONS
    default: int = 5
    option_none: int = 0


class ButtonWidgetsLocations(Range):
    """
    The number of locations to create in the world that will be checked upon a button widget being clicked.

    If less than `button_widgets_items`, this will be incremented until the condition is satisfied.
    """

    display_name: str = "Button Widgets Locations"
    range_start: int = 1
    range_end: int = MAX_BUTTONS
    default: int = 5


class MaxGameHours(Range):
    """
    The maximum number of hours that are expected for users to collectively play games in the Discord server.

    If 0, locations related to playing games will not be created.
    """

    display_name: str = "Max Game Hours"
    range_start: int = 0
    range_end: int = MAX_GAME_HOURS
    default: int = 5
    option_none: int = 0


class GameHoursLocations(Range):
    """
    The number of locations to create in the world that will be checked upon a sufficient number of users playing games in the Discord server.

    Unused if `max_game_hours` is 0. If greater than `max_game_hours`, this will be decremented until the condition is satisfied.
    """

    display_name: str = "Game Hours Locations"
    range_start: int = 1
    range_end: int = MAX_GAME_HOURS
    default: int = 5


class MaxSpotifyHours(Range):
    """
    The maximum number of hours that are expected for users to collectively listen to Spotify in the Discord server. See `max_game_hours`.
    """

    display_name: str = "Max Spotify Hours"
    range_start: int = 0
    range_end: int = MAX_SPOTIFY_HOURS
    default: int = 10
    option_none: int = 0


class SpotifyHoursLocations(Range):
    """
    The number of locations to create in the world that will be checked upon a sufficient number of users listening to Spotify in the Discord server. See `game_hours_locations`.
    """

    display_name: str = "Spotify Hours Locations"
    range_start: int = 1
    range_end: int = MAX_SPOTIFY_HOURS
    default: int = 5


class SplitTextChannelLocationsIntoGroups(Toggle):
    """
    Whether to duplicate locations related to performing actions in text channels for each text channel group. This will multiply the number of text channel locations by the value of `text_channel_groups`.
    """

    display_name: str = "Split Text Channel Locations into Groups"


class MaxMessages(Range):
    """
    The maximum number of messages that are expected to be sent in the Discord server.

    If 0, locations related to sending messages in text channels will not be created. If `split_text_channel_locations_into_groups` is enabled, this option's value will be equally divided into each text channel group.
    """

    display_name: str = "Max Messages"
    range_start: int = 0
    range_end: int = MAX_MESSAGES
    default: int = 100
    option_none: int = 0


class MessagesLocations(Range):
    """
    The number of locations to create in the world that will be checked upon a sufficient number of messages being sent in text channels.

    Unused if `max_messages` is 0. If `split_text_channel_locations_into_groups` is enabled and this is greater than `text_channel_groups` times `max_messages`, this will be decremented until the condition is satisfied. Otherwise this will be decremented if it is greater than `max_messages`.
    """

    display_name: str = "Messages Locations"
    range_start: int = 1
    range_end: int = MAX_MESSAGES * MAX_TEXT_GROUPS
    default: int = 5


class MaxReplies(Range):
    """
    The maximum number of replies that are expected to be sent in the Discord server. See `max_messages`.
    """

    display_name: str = "Max Replies"
    range_start: int = 0
    range_end: int = MAX_REPLIES
    default: int = 10
    option_none: int = 0


class RepliesLocations(Range):
    """
    The number of locations to create for replies. See `messages_locations`.
    """

    display_name: str = "Replies Locations"
    range_start: int = 1
    range_end: int = MAX_REPLIES * MAX_TEXT_GROUPS
    default: int = 5


class MaxReplyChainLength(Range):
    """
    The maximum length of a reply chain, where at least 2 users reply to each-other's messages repeatedly, that is expected to occur in the Discord server.

    If 1, locations related to the length of reply chains in text channels will not be created. If `split_text_channel_locations_into_groups` is enabled, this option's value minus 1 will be equally divided into each text channel group.
    """

    display_name: str = "Max Reply Chain Length"
    range_start: int = 1
    range_end: int = MAX_REPLY_CHAIN_LENGTH
    default: int = 10
    option_none: int = 1


class ReplyChainLengthLocations(Range):
    """
    The number of locations to create for reply chains. See `messages_locations`.
    """

    display_name: str = "Reply Chain Length Locations"
    range_start: int = 1
    range_end: int = MAX_REPLY_CHAIN_LENGTH * MAX_TEXT_GROUPS
    default: int = 5


class MaxSingleMessageReactions(Range):
    """
    The maximum number of reactions that are expected to be on a single message in the Discord server. See `max_messages`.
    """

    display_name: str = "Max Single Message Reactions"
    range_start: int = 0
    range_end: int = MAX_SINGLE_MESSAGE_REACTIONS
    default: int = 5
    option_none: int = 0


class SingleMessageReactionsLocations(Range):
    """
    The number of locations to create for single message reactions. See `messages_locations`.
    """

    display_name: str = "Single Message Reactions Locations"
    range_start: int = 1
    range_end: int = MAX_SINGLE_MESSAGE_REACTIONS * MAX_TEXT_GROUPS
    default: int = 5


class MaxSingleReactions(Range):
    """
    The maximum number of a single reaction that is expected to be on a single message in the Discord server. See `max_messages`.
    """

    display_name: str = "Max Single Reactions"
    range_start: int = 0
    range_end: int = MAX_SINGLE_REACTIONS
    default: int = 5
    option_none: int = 0


class SingleReactionsLocations(Range):
    """
    The number of locations to create for single reactions. See `messages_locations`.
    """

    display_name: str = "Single Reactions Locations"
    range_start: int = 1
    range_end: int = MAX_SINGLE_REACTIONS * MAX_TEXT_GROUPS
    default: int = 5


class MaxEmojiOnlyMessages(Range):
    """
    The maximum number of emoji-only messages that are expected to be sent in the Discord server. See `max_messages`.
    """

    display_name: str = "Max Emoji-Only Messages"
    range_start: int = 0
    range_end: int = MAX_EMOJI_ONLY_MESSAGES
    default: int = 5
    option_none: int = 0


class EmojiOnlyMessagesLocations(Range):
    """
    The number of locations to create for emoji-only messages. See `messages_locations`.
    """

    display_name: str = "Emoji-Only Messages Locations"
    range_start: int = 1
    range_end: int = MAX_EMOJI_ONLY_MESSAGES * MAX_TEXT_GROUPS
    default: int = 5


class MaxEmojiChainLength(Range):
    """
    The maximum length of an emoji chain, where a message starts with a single emoji and subsequent messages increase the emoji count by 1, that is expected to occur in the Discord server. See `max_reply_chain_length`.
    """

    display_name: str = "Max Emoji Chain Length"
    range_start: int = 1
    range_end: int = MAX_EMOJI_CHAIN_LENGTH
    default: int = 5
    option_none: int = 1


class EmojiChainLengthLocations(Range):
    """
    The number of locations to create for emoji chains. See `messages_locations`.
    """

    display_name: str = "Emoji Chain Length Locations"
    range_start: int = 1
    range_end: int = MAX_EMOJI_CHAIN_LENGTH * MAX_TEXT_GROUPS
    default: int = 5


class MaxGIFs(Range):
    """
    The maximum number of GIFs that are expected to be sent in the Discord server. A message is considered to be a GIF if it contains no text content and it contains a GIF attachment originating from tenor.com. See `max_messages`.
    """

    display_name: str = "Max GIFs"
    range_start: int = 0
    range_end: int = MAX_GIFS
    default: int = 5
    option_none: int = 0


class GIFsLocations(Range):
    """
    The number of locations to create for GIFs. See `messages_locations`.
    """

    display_name: str = "GIFs Locations"
    range_start: int = 1
    range_end: int = MAX_GIFS * MAX_TEXT_GROUPS
    default: int = 5


class MaxStickers(Range):
    """
    The maximum number of stickers that are expected to be sent in the Discord server. See `max_messages`.
    """

    display_name: str = "Max Stickers"
    range_start: int = 0
    range_end: int = MAX_STICKERS
    default: int = 5
    option_none: int = 0


class StickersLocations(Range):
    """
    The number of locations to create for stickers. See `messages_locations`.
    """

    display_name: str = "Stickers Locations"
    range_start: int = 1
    range_end: int = MAX_STICKERS * MAX_TEXT_GROUPS
    default: int = 5


class MaxFiles(Range):
    """
    The maximum number of files that are expected to be sent in the Discord server. See `max_messages`.
    """

    display_name: str = "Max Files"
    range_start: int = 0
    range_end: int = MAX_FILES
    default: int = 10
    option_none: int = 0


class FilesLocations(Range):
    """
    The number of locations to create for files. See `messages_locations`.
    """

    display_name: str = "Files Locations"
    range_start: int = 1
    range_end: int = MAX_FILES * MAX_TEXT_GROUPS
    default: int = 5


class MaxPolls(Range):
    """
    The maximum number of polls that are expected to be sent in the Discord server. See `max_messages`.
    """

    display_name: str = "Max Polls"
    range_start: int = 0
    range_end: int = MAX_POLLS
    default: int = 5
    option_none: int = 0


class PollsLocations(Range):
    """
    The number of locations to create for polls. See `messages_locations`.
    """

    display_name: str = "Polls Locations"
    range_start: int = 1
    range_end: int = MAX_POLLS * MAX_TEXT_GROUPS
    default: int = 5


class SplitVoiceChannelLocationsIntoGroups(Toggle):
    """
    Whether to duplicate locations related to performing actions in voice channels for each voice channel group. See `split_text_channel_locations_into_groups`.
    """

    display_name: str = "Split Voice Channel Locations into Groups"


class MaxVoiceHours(Range):
    """
    The maximum number of hours that are expected for users to collectively spend in voice channels in the Discord server.

    If 0, locations related to spending time in voice channels will not be created. If `split_voice_channel_locations_into_groups` is enabled, this option's value will be equally divided into each voice channel group.
    """

    display_name: str = "Max Voice Hours"
    range_start: int = 0
    range_end: int = MAX_VOICE_HOURS
    default: int = 10
    option_none: int = 0


class VoiceHoursLocations(Range):
    """
    The number of locations to create in the world that will be checked upon a sufficient number of hours spent in voice channels.

    Unused if `max_voice_hours` is 0. If `split_voice_channel_locations_into_groups` is enabled and this is greater than `voice_channel_groups` times `max_voice_hours`, this will be decremented until the condition is satisfied. Otherwise this will be decremented if it is greater than `max_voice_hours`.
    """

    display_name: str = "Voice Hours Locations"
    range_start: int = 1
    range_end: int = MAX_VOICE_HOURS * MAX_VOICE_GROUPS
    default: int = 5


class MaxVoiceActivityHours(Range):
    """
    The maximum number of hours that are expected for users to collectively spend in activities within voice channels in the Discord server. See `max_voice_hours`.
    """

    display_name: str = "Max Voice Activity Hours"
    range_start: int = 0
    range_end: int = MAX_VOICE_ACTIVITY_HOURS
    default: int = 5
    option_none: int = 0


class VoiceActivityHoursLocations(Range):
    """
    The number of locations to create in the world that will be checked upon a sufficient number of hours spent in activities within voice channels. See `voice_hours_locations`.
    """

    display_name: str = "Voice Activity Hours Locations"
    range_start: int = 1
    range_end: int = MAX_VOICE_ACTIVITY_HOURS * MAX_VOICE_GROUPS
    default: int = 5


class UsefulItemsPercent(Range):
    """
    The percentage of filler items that will be useful, e.g. 'Open Season' and 'Trigger Word Reveal'.
    """

    display_name: str = "Useful Items %"
    range_start: int = 0
    range_end: int = 100
    default: int = 33


class OpenSeasonItemWeight(Range):
    """
    The weight of the useful 'Open Season' item, which will unlock and relax all permissions of a random locked channel for 1 minute, allowing users to release items in locations that would otherwise be out of logic.

    If 0, the 'Open Season' item will not appear in the item pool.
    """

    display_name: str = "Open Season Item Weight"
    range_start: int = 0
    range_end: int = 100
    # Off by default due to this option breaking logic
    default: int = 0


class TriggerWordRevealItemWeight(Range):
    """
    The weight of the useful 'Trigger Word Reveal' item, which will cause the Discord bot to post a message containing one of its trigger words, potentially allowing users to release the item in that trigger word's location.

    If 0, the 'Trigger Word Reveal' item will not appear in the item pool.
    """

    display_name: str = "Trigger Word Reveal Item Weight"
    range_start: int = 0
    range_end: int = 100
    default: int = 50


class TrapItemsPercent(Range):
    """
    The percentage of filler items that will be traps, e.g. 'Lockdown' and 'Kick Random User'.

    If this plus `useful_items_percent` is greater than 100, this will be decremented until both equate to 100.
    """

    display_name: str = "Trap Items %"
    range_start: int = 0
    range_end: int = 100
    # Off by default as traps are not a good first experience for users
    default: int = 0


class LockdownTrapWeight(Range):
    """
    The weight of the trap 'Lockdown', which will cause all text and voice channels allocated to the Discord bot to be locked and completely inaccessible for 1 minute.
    """

    display_name: str = "Lockdown Trap Weight"
    range_start: int = 0
    range_end: int = 100
    default: int = 50


class KickRandomUserTrapWeight(Range):
    """
    The weight of the trap 'Kick Random User', which will cause a random user in the Discord server to be kicked. Only users that are not administrators, are participating in the Archipelago run and have been active recently will be eligible to be kicked. If no eligible users are found when the trap is triggered, it will have no effect.
    """

    display_name: str = "Kick Random User Trap Weight"
    range_start: int = 0
    range_end: int = 100
    # Off by default as kicking users is an extreme trap only for those who agree to it
    default: int = 0


class DeathLink(Toggle):
    """
    Whether to enable sending and receiving Death Link events to and from Archipelago. A Death Link event is sent when a user in the Discord server is kicked, banned, or otherwise punished through Discord permissions. When a Death Link event is received, all text and voice channels allocated to the Discord bot will be locked and completely inaccessible for 1 minute.
    """

    display_name: str = "Death Link"


class EnergyLink(Toggle):
    """
    Whether to enable sending and receiving Joules (J) from Energy Link events to and from Archipelago. Joules are earned by users when they perform actions in the Discord server. Joules can be spent to reveal clues that will assist users in completing locations in the world, or used in other worlds in the multiworld.
    """

    display_name: str = "Energy Link"


discord_option_groups: list[OptionGroup] = [
    OptionGroup(
        "Channels",
        [
            StartWithTextChannelsPercent,
            UnusedTextChannelsPercent,
            TextChannelGroups,
            StartWithVoiceChannelsPercent,
            UnusedVoiceChannelsPercent,
            VoiceChannelGroups,
        ],
    ),
    OptionGroup("Teams", [TeamCount, TeamMergeItems]),
    OptionGroup("Slowdown", [MaxSlowdown, SlowmodeReductionItems]),
    OptionGroup(
        "Permissions",
        [
            EmbedLinksItemEnabled,
            AttachFilesItemEnabled,
            AddReactionsItemEnabled,
            ReadMessageHistoryItemEnabled,
            SendTTSMessagesItemEnabled,
            SendVoiceMessagesItemEnabled,
            CreatePollsItemEnabled,
            UseAppCommandsItemEnabled,
            UseActivitiesItemEnabled,
        ],
        start_collapsed=True,
    ),
    OptionGroup(
        "Global Locations",
        [
            MaxNewMembers,
            NewMembersLocations,
            TriggerWords,
            ButtonWidgetsItems,
            ButtonWidgetsLocations,
            MaxGameHours,
            GameHoursLocations,
            MaxSpotifyHours,
            SpotifyHoursLocations,
        ],
    ),
    OptionGroup(
        "Text Channel Locations",
        [
            SplitTextChannelLocationsIntoGroups,
            MaxMessages,
            MessagesLocations,
            MaxMessages,
            MessagesLocations,
            MaxReplies,
            RepliesLocations,
            MaxReplyChainLength,
            ReplyChainLengthLocations,
            MaxSingleMessageReactions,
            SingleMessageReactionsLocations,
            MaxSingleReactions,
            SingleReactionsLocations,
            MaxEmojiOnlyMessages,
            EmojiOnlyMessagesLocations,
            MaxEmojiChainLength,
            EmojiChainLengthLocations,
            MaxGIFs,
            GIFsLocations,
            MaxStickers,
            StickersLocations,
            MaxFiles,
            FilesLocations,
            MaxPolls,
            PollsLocations,
        ],
    ),
    OptionGroup(
        "Voice Channel Locations",
        [
            SplitVoiceChannelLocationsIntoGroups,
            MaxVoiceHours,
            VoiceHoursLocations,
            MaxVoiceActivityHours,
            VoiceActivityHoursLocations,
        ],
    ),
    OptionGroup(
        "Useful Items",
        [UsefulItemsPercent, OpenSeasonItemWeight, TriggerWordRevealItemWeight],
    ),
    OptionGroup(
        "Trap Items", [TrapItemsPercent, LockdownTrapWeight, KickRandomUserTrapWeight]
    ),
    OptionGroup("Archipelago Links", [DeathLink, EnergyLink]),
]


@dataclass
class DiscordOptions(PerGameCommonOptions):
    start_with_text_channels_percent: StartWithTextChannelsPercent
    unused_text_channels_percent: UnusedTextChannelsPercent
    text_channel_groups: TextChannelGroups
    start_with_voice_channels_percent: StartWithVoiceChannelsPercent
    unused_voice_channels_percent: UnusedVoiceChannelsPercent
    voice_channel_groups: VoiceChannelGroups
    team_count: TeamCount
    team_merge_items: TeamMergeItems
    max_slowdown: MaxSlowdown
    slowmode_reduction_items: SlowmodeReductionItems
    embed_links_item_enabled: EmbedLinksItemEnabled
    attach_files_item_enabled: AttachFilesItemEnabled
    add_reactions_item_enabled: AddReactionsItemEnabled
    read_message_history_item_enabled: ReadMessageHistoryItemEnabled
    send_tts_messages_item_enabled: SendTTSMessagesItemEnabled
    send_voice_messages_item_enabled: SendVoiceMessagesItemEnabled
    create_polls_item_enabled: CreatePollsItemEnabled
    use_app_commands_item_enabled: UseAppCommandsItemEnabled
    use_activities_item_enabled: UseActivitiesItemEnabled
    max_new_members: MaxNewMembers
    new_members_locations: NewMembersLocations
    trigger_words: TriggerWords
    button_widgets_items: ButtonWidgetsItems
    button_widgets_locations: ButtonWidgetsLocations
    max_game_hours: MaxGameHours
    game_hours_locations: GameHoursLocations
    max_spotify_hours: MaxSpotifyHours
    spotify_hours_locations: SpotifyHoursLocations
    split_text_channel_locations_into_groups: SplitTextChannelLocationsIntoGroups
    max_messages: MaxMessages
    messages_locations: MessagesLocations
    max_replies: MaxReplies
    replies_locations: RepliesLocations
    max_reply_chain_length: MaxReplyChainLength
    reply_chain_length_locations: ReplyChainLengthLocations
    max_single_messsage_reactions: MaxSingleMessageReactions
    single_message_reactions_locations: SingleMessageReactionsLocations
    max_single_reactions: MaxSingleReactions
    single_reactions_locations: SingleReactionsLocations
    max_emoji_only_messages: MaxEmojiOnlyMessages
    emoji_only_messages_locations: EmojiOnlyMessagesLocations
    max_emoji_chain_length: MaxEmojiChainLength
    emoji_chain_length_locations: EmojiChainLengthLocations
    max_gifs: MaxGIFs
    gifs_locations: GIFsLocations
    max_stickers: MaxStickers
    stickers_locations: StickersLocations
    max_files: MaxFiles
    files_locations: FilesLocations
    max_polls: MaxPolls
    polls_locations: PollsLocations
    split_voice_channel_locations_into_groups: SplitVoiceChannelLocationsIntoGroups
    max_voice_hours: MaxVoiceHours
    voice_hours_locations: VoiceHoursLocations
    max_voice_activity_hours: MaxVoiceActivityHours
    voice_activity_hours_locations: VoiceActivityHoursLocations
    useful_items_percent: UsefulItemsPercent
    open_season_item_weight: OpenSeasonItemWeight
    trigger_word_reveal_item_weight: TriggerWordRevealItemWeight
    trap_items_percent: TrapItemsPercent
    lockdown_trap_weight: LockdownTrapWeight
    kick_random_user_trap_weight: KickRandomUserTrapWeight
    death_link: DeathLink
    energy_link: EnergyLink

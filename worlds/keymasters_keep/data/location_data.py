from typing import Any, Dict, List, NamedTuple, Optional, Tuple, Union

from ..enums import (
    KeymastersKeepLocations,
    KeymastersKeepRegions,
    KeymastersKeepTags,
    KeymastersKeepTrials,
)


class KeymastersKeepLocationData(NamedTuple):
    name: str
    archipelago_id: Optional[int]
    region: KeymastersKeepRegions
    tags: Optional[Tuple[KeymastersKeepTags, ...]] = None


location_data: Dict[
    KeymastersKeepLocations,
    Union[KeymastersKeepLocationData, List[KeymastersKeepLocationData]],
] = {
    # Door Unlocks
    KeymastersKeepLocations.THE_ARCANE_DOOR_UNLOCK: KeymastersKeepLocationData(
        name=KeymastersKeepLocations.THE_ARCANE_DOOR_UNLOCK.value,
        archipelago_id=201,
        region=KeymastersKeepRegions.KEYMASTERS_KEEP,
        tags=(KeymastersKeepTags.DOOR_UNLOCKS,),
    ),
    KeymastersKeepLocations.THE_ARCANE_PASSAGE_UNLOCK: KeymastersKeepLocationData(
        name=KeymastersKeepLocations.THE_ARCANE_PASSAGE_UNLOCK.value,
        archipelago_id=1,
        region=KeymastersKeepRegions.KEYMASTERS_KEEP,
        tags=(KeymastersKeepTags.DOOR_UNLOCKS,),
    ),
    KeymastersKeepLocations.THE_ARCANE_THRESHOLD_UNLOCK: KeymastersKeepLocationData(
        name=KeymastersKeepLocations.THE_ARCANE_THRESHOLD_UNLOCK.value,
        archipelago_id=2,
        region=KeymastersKeepRegions.KEYMASTERS_KEEP,
        tags=(KeymastersKeepTags.DOOR_UNLOCKS,),
    ),
    KeymastersKeepLocations.THE_CLANDESTINE_PASSAGE_UNLOCK: KeymastersKeepLocationData(
        name=KeymastersKeepLocations.THE_CLANDESTINE_PASSAGE_UNLOCK.value,
        archipelago_id=3,
        region=KeymastersKeepRegions.KEYMASTERS_KEEP,
        tags=(KeymastersKeepTags.DOOR_UNLOCKS,),
    ),
    KeymastersKeepLocations.THE_CLOAKED_ENTRANCE_UNLOCK: KeymastersKeepLocationData(
        name=KeymastersKeepLocations.THE_CLOAKED_ENTRANCE_UNLOCK.value,
        archipelago_id=4,
        region=KeymastersKeepRegions.KEYMASTERS_KEEP,
        tags=(KeymastersKeepTags.DOOR_UNLOCKS,),
    ),
    KeymastersKeepLocations.THE_CLOAKED_THRESHOLD_UNLOCK: KeymastersKeepLocationData(
        name=KeymastersKeepLocations.THE_CLOAKED_THRESHOLD_UNLOCK.value,
        archipelago_id=5,
        region=KeymastersKeepRegions.KEYMASTERS_KEEP,
        tags=(KeymastersKeepTags.DOOR_UNLOCKS,),
    ),
    KeymastersKeepLocations.THE_CLOAKED_VAULT_UNLOCK: KeymastersKeepLocationData(
        name=KeymastersKeepLocations.THE_CLOAKED_VAULT_UNLOCK.value,
        archipelago_id=6,
        region=KeymastersKeepRegions.KEYMASTERS_KEEP,
        tags=(KeymastersKeepTags.DOOR_UNLOCKS,),
    ),
    KeymastersKeepLocations.THE_CONCEALED_THRESHOLD_UNLOCK: KeymastersKeepLocationData(
        name=KeymastersKeepLocations.THE_CONCEALED_THRESHOLD_UNLOCK.value,
        archipelago_id=7,
        region=KeymastersKeepRegions.KEYMASTERS_KEEP,
        tags=(KeymastersKeepTags.DOOR_UNLOCKS,),
    ),
    KeymastersKeepLocations.THE_CONCEALED_VAULT_UNLOCK: KeymastersKeepLocationData(
        name=KeymastersKeepLocations.THE_CONCEALED_VAULT_UNLOCK.value,
        archipelago_id=8,
        region=KeymastersKeepRegions.KEYMASTERS_KEEP,
        tags=(KeymastersKeepTags.DOOR_UNLOCKS,),
    ),
    KeymastersKeepLocations.THE_CRYPTIC_CHAMBER_UNLOCK: KeymastersKeepLocationData(
        name=KeymastersKeepLocations.THE_CRYPTIC_CHAMBER_UNLOCK.value,
        archipelago_id=9,
        region=KeymastersKeepRegions.KEYMASTERS_KEEP,
        tags=(KeymastersKeepTags.DOOR_UNLOCKS,),
    ),
    KeymastersKeepLocations.THE_CRYPTIC_GATEWAY_UNLOCK: KeymastersKeepLocationData(
        name=KeymastersKeepLocations.THE_CRYPTIC_GATEWAY_UNLOCK.value,
        archipelago_id=10,
        region=KeymastersKeepRegions.KEYMASTERS_KEEP,
        tags=(KeymastersKeepTags.DOOR_UNLOCKS,),
    ),
    KeymastersKeepLocations.THE_CRYPTIC_VAULT_UNLOCK: KeymastersKeepLocationData(
        name=KeymastersKeepLocations.THE_CRYPTIC_VAULT_UNLOCK.value,
        archipelago_id=11,
        region=KeymastersKeepRegions.KEYMASTERS_KEEP,
        tags=(KeymastersKeepTags.DOOR_UNLOCKS,),
    ),
    KeymastersKeepLocations.THE_DISGUISED_GATEWAY_UNLOCK: KeymastersKeepLocationData(
        name=KeymastersKeepLocations.THE_DISGUISED_GATEWAY_UNLOCK.value,
        archipelago_id=12,
        region=KeymastersKeepRegions.KEYMASTERS_KEEP,
        tags=(KeymastersKeepTags.DOOR_UNLOCKS,),
    ),
    KeymastersKeepLocations.THE_ECHOING_PASSAGE_UNLOCK: KeymastersKeepLocationData(
        name=KeymastersKeepLocations.THE_ECHOING_PASSAGE_UNLOCK.value,
        archipelago_id=13,
        region=KeymastersKeepRegions.KEYMASTERS_KEEP,
        tags=(KeymastersKeepTags.DOOR_UNLOCKS,),
    ),
    KeymastersKeepLocations.THE_ELUSIVE_DOOR_UNLOCK: KeymastersKeepLocationData(
        name=KeymastersKeepLocations.THE_ELUSIVE_DOOR_UNLOCK.value,
        archipelago_id=14,
        region=KeymastersKeepRegions.KEYMASTERS_KEEP,
        tags=(KeymastersKeepTags.DOOR_UNLOCKS,),
    ),
    KeymastersKeepLocations.THE_ENCHANTED_GATEWAY_UNLOCK: KeymastersKeepLocationData(
        name=KeymastersKeepLocations.THE_ENCHANTED_GATEWAY_UNLOCK.value,
        archipelago_id=15,
        region=KeymastersKeepRegions.KEYMASTERS_KEEP,
        tags=(KeymastersKeepTags.DOOR_UNLOCKS,),
    ),
    KeymastersKeepLocations.THE_ENCHANTED_PASSAGE_UNLOCK: KeymastersKeepLocationData(
        name=KeymastersKeepLocations.THE_ENCHANTED_PASSAGE_UNLOCK.value,
        archipelago_id=16,
        region=KeymastersKeepRegions.KEYMASTERS_KEEP,
        tags=(KeymastersKeepTags.DOOR_UNLOCKS,),
    ),
    KeymastersKeepLocations.THE_ENIGMATIC_PORTAL_UNLOCK: KeymastersKeepLocationData(
        name=KeymastersKeepLocations.THE_ENIGMATIC_PORTAL_UNLOCK.value,
        archipelago_id=17,
        region=KeymastersKeepRegions.KEYMASTERS_KEEP,
        tags=(KeymastersKeepTags.DOOR_UNLOCKS,),
    ),
    KeymastersKeepLocations.THE_ENIGMATIC_THRESHOLD_UNLOCK: KeymastersKeepLocationData(
        name=KeymastersKeepLocations.THE_ENIGMATIC_THRESHOLD_UNLOCK.value,
        archipelago_id=18,
        region=KeymastersKeepRegions.KEYMASTERS_KEEP,
        tags=(KeymastersKeepTags.DOOR_UNLOCKS,),
    ),
    KeymastersKeepLocations.THE_FADED_GATEWAY_UNLOCK: KeymastersKeepLocationData(
        name=KeymastersKeepLocations.THE_FADED_GATEWAY_UNLOCK.value,
        archipelago_id=19,
        region=KeymastersKeepRegions.KEYMASTERS_KEEP,
        tags=(KeymastersKeepTags.DOOR_UNLOCKS,),
    ),
    KeymastersKeepLocations.THE_FAINT_DOORWAY_UNLOCK: KeymastersKeepLocationData(
        name=KeymastersKeepLocations.THE_FAINT_DOORWAY_UNLOCK.value,
        archipelago_id=20,
        region=KeymastersKeepRegions.KEYMASTERS_KEEP,
        tags=(KeymastersKeepTags.DOOR_UNLOCKS,),
    ),
    KeymastersKeepLocations.THE_FAINT_PATH_UNLOCK: KeymastersKeepLocationData(
        name=KeymastersKeepLocations.THE_FAINT_PATH_UNLOCK.value,
        archipelago_id=21,
        region=KeymastersKeepRegions.KEYMASTERS_KEEP,
        tags=(KeymastersKeepTags.DOOR_UNLOCKS,),
    ),
    KeymastersKeepLocations.THE_FAINT_THRESHOLD_UNLOCK: KeymastersKeepLocationData(
        name=KeymastersKeepLocations.THE_FAINT_THRESHOLD_UNLOCK.value,
        archipelago_id=22,
        region=KeymastersKeepRegions.KEYMASTERS_KEEP,
        tags=(KeymastersKeepTags.DOOR_UNLOCKS,),
    ),
    KeymastersKeepLocations.THE_FORBIDDEN_ENTRANCE_UNLOCK: KeymastersKeepLocationData(
        name=KeymastersKeepLocations.THE_FORBIDDEN_ENTRANCE_UNLOCK.value,
        archipelago_id=23,
        region=KeymastersKeepRegions.KEYMASTERS_KEEP,
        tags=(KeymastersKeepTags.DOOR_UNLOCKS,),
    ),
    KeymastersKeepLocations.THE_FORGOTTEN_DOOR_UNLOCK: KeymastersKeepLocationData(
        name=KeymastersKeepLocations.THE_FORGOTTEN_DOOR_UNLOCK.value,
        archipelago_id=24,
        region=KeymastersKeepRegions.KEYMASTERS_KEEP,
        tags=(KeymastersKeepTags.DOOR_UNLOCKS,),
    ),
    KeymastersKeepLocations.THE_FORGOTTEN_GATEWAY_UNLOCK: KeymastersKeepLocationData(
        name=KeymastersKeepLocations.THE_FORGOTTEN_GATEWAY_UNLOCK.value,
        archipelago_id=25,
        region=KeymastersKeepRegions.KEYMASTERS_KEEP,
        tags=(KeymastersKeepTags.DOOR_UNLOCKS,),
    ),
    KeymastersKeepLocations.THE_FORGOTTEN_PORTAL_UNLOCK: KeymastersKeepLocationData(
        name=KeymastersKeepLocations.THE_FORGOTTEN_PORTAL_UNLOCK.value,
        archipelago_id=26,
        region=KeymastersKeepRegions.KEYMASTERS_KEEP,
        tags=(KeymastersKeepTags.DOOR_UNLOCKS,),
    ),
    KeymastersKeepLocations.THE_FORGOTTEN_THRESHOLD_UNLOCK: KeymastersKeepLocationData(
        name=KeymastersKeepLocations.THE_FORGOTTEN_THRESHOLD_UNLOCK.value,
        archipelago_id=27,
        region=KeymastersKeepRegions.KEYMASTERS_KEEP,
        tags=(KeymastersKeepTags.DOOR_UNLOCKS,),
    ),
    KeymastersKeepLocations.THE_GHOSTED_PASSAGEWAY_UNLOCK: KeymastersKeepLocationData(
        name=KeymastersKeepLocations.THE_GHOSTED_PASSAGEWAY_UNLOCK.value,
        archipelago_id=28,
        region=KeymastersKeepRegions.KEYMASTERS_KEEP,
        tags=(KeymastersKeepTags.DOOR_UNLOCKS,),
    ),
    KeymastersKeepLocations.THE_GHOSTLY_PASSAGE_UNLOCK: KeymastersKeepLocationData(
        name=KeymastersKeepLocations.THE_GHOSTLY_PASSAGE_UNLOCK.value,
        archipelago_id=29,
        region=KeymastersKeepRegions.KEYMASTERS_KEEP,
        tags=(KeymastersKeepTags.DOOR_UNLOCKS,),
    ),
    KeymastersKeepLocations.THE_HIDDEN_ARCHWAY_UNLOCK: KeymastersKeepLocationData(
        name=KeymastersKeepLocations.THE_HIDDEN_ARCHWAY_UNLOCK.value,
        archipelago_id=30,
        region=KeymastersKeepRegions.KEYMASTERS_KEEP,
        tags=(KeymastersKeepTags.DOOR_UNLOCKS,),
    ),
    KeymastersKeepLocations.THE_HIDDEN_CHAMBER_UNLOCK: KeymastersKeepLocationData(
        name=KeymastersKeepLocations.THE_HIDDEN_CHAMBER_UNLOCK.value,
        archipelago_id=31,
        region=KeymastersKeepRegions.KEYMASTERS_KEEP,
        tags=(KeymastersKeepTags.DOOR_UNLOCKS,),
    ),
    KeymastersKeepLocations.THE_HIDDEN_DOORWAY_UNLOCK: KeymastersKeepLocationData(
        name=KeymastersKeepLocations.THE_HIDDEN_DOORWAY_UNLOCK.value,
        archipelago_id=32,
        region=KeymastersKeepRegions.KEYMASTERS_KEEP,
        tags=(KeymastersKeepTags.DOOR_UNLOCKS,),
    ),
    KeymastersKeepLocations.THE_HIDDEN_ENTRANCE_UNLOCK: KeymastersKeepLocationData(
        name=KeymastersKeepLocations.THE_HIDDEN_ENTRANCE_UNLOCK.value,
        archipelago_id=33,
        region=KeymastersKeepRegions.KEYMASTERS_KEEP,
        tags=(KeymastersKeepTags.DOOR_UNLOCKS,),
    ),
    KeymastersKeepLocations.THE_HIDDEN_KEYHOLE_UNLOCK: KeymastersKeepLocationData(
        name=KeymastersKeepLocations.THE_HIDDEN_KEYHOLE_UNLOCK.value,
        archipelago_id=34,
        region=KeymastersKeepRegions.KEYMASTERS_KEEP,
        tags=(KeymastersKeepTags.DOOR_UNLOCKS,),
    ),
    KeymastersKeepLocations.THE_HIDDEN_PASSAGEWAY_UNLOCK: KeymastersKeepLocationData(
        name=KeymastersKeepLocations.THE_HIDDEN_PASSAGEWAY_UNLOCK.value,
        archipelago_id=35,
        region=KeymastersKeepRegions.KEYMASTERS_KEEP,
        tags=(KeymastersKeepTags.DOOR_UNLOCKS,),
    ),
    KeymastersKeepLocations.THE_HIDDEN_PATH_UNLOCK: KeymastersKeepLocationData(
        name=KeymastersKeepLocations.THE_HIDDEN_PATH_UNLOCK.value,
        archipelago_id=36,
        region=KeymastersKeepRegions.KEYMASTERS_KEEP,
        tags=(KeymastersKeepTags.DOOR_UNLOCKS,),
    ),
    KeymastersKeepLocations.THE_HIDDEN_REACH_UNLOCK: KeymastersKeepLocationData(
        name=KeymastersKeepLocations.THE_HIDDEN_REACH_UNLOCK.value,
        archipelago_id=37,
        region=KeymastersKeepRegions.KEYMASTERS_KEEP,
        tags=(KeymastersKeepTags.DOOR_UNLOCKS,),
    ),
    KeymastersKeepLocations.THE_HIDDEN_VAULT_UNLOCK: KeymastersKeepLocationData(
        name=KeymastersKeepLocations.THE_HIDDEN_VAULT_UNLOCK.value,
        archipelago_id=38,
        region=KeymastersKeepRegions.KEYMASTERS_KEEP,
        tags=(KeymastersKeepTags.DOOR_UNLOCKS,),
    ),
    KeymastersKeepLocations.THE_INCONSPICUOUS_DOOR_UNLOCK: KeymastersKeepLocationData(
        name=KeymastersKeepLocations.THE_INCONSPICUOUS_DOOR_UNLOCK.value,
        archipelago_id=39,
        region=KeymastersKeepRegions.KEYMASTERS_KEEP,
        tags=(KeymastersKeepTags.DOOR_UNLOCKS,),
    ),
    KeymastersKeepLocations.THE_INVISIBLE_DOORWAY_UNLOCK: KeymastersKeepLocationData(
        name=KeymastersKeepLocations.THE_INVISIBLE_DOORWAY_UNLOCK.value,
        archipelago_id=40,
        region=KeymastersKeepRegions.KEYMASTERS_KEEP,
        tags=(KeymastersKeepTags.DOOR_UNLOCKS,),
    ),
    KeymastersKeepLocations.THE_KEYMASTERS_CHALLENGE_CHAMBER_UNLOCK: KeymastersKeepLocationData(
        name=KeymastersKeepLocations.THE_KEYMASTERS_CHALLENGE_CHAMBER_UNLOCK.value,
        archipelago_id=41,
        region=KeymastersKeepRegions.KEYMASTERS_KEEP,
        tags=(KeymastersKeepTags.DOOR_UNLOCKS,),
    ),
    KeymastersKeepLocations.THE_LOCKED_DOORWAY_UNLOCK: KeymastersKeepLocationData(
        name=KeymastersKeepLocations.THE_LOCKED_DOORWAY_UNLOCK.value,
        archipelago_id=42,
        region=KeymastersKeepRegions.KEYMASTERS_KEEP,
        tags=(KeymastersKeepTags.DOOR_UNLOCKS,),
    ),
    KeymastersKeepLocations.THE_LOCKED_GATEWAY_UNLOCK: KeymastersKeepLocationData(
        name=KeymastersKeepLocations.THE_LOCKED_GATEWAY_UNLOCK.value,
        archipelago_id=43,
        region=KeymastersKeepRegions.KEYMASTERS_KEEP,
        tags=(KeymastersKeepTags.DOOR_UNLOCKS,),
    ),
    KeymastersKeepLocations.THE_LOST_ARCHWAY_UNLOCK: KeymastersKeepLocationData(
        name=KeymastersKeepLocations.THE_LOST_ARCHWAY_UNLOCK.value,
        archipelago_id=44,
        region=KeymastersKeepRegions.KEYMASTERS_KEEP,
        tags=(KeymastersKeepTags.DOOR_UNLOCKS,),
    ),
    KeymastersKeepLocations.THE_LOST_PORTAL_UNLOCK: KeymastersKeepLocationData(
        name=KeymastersKeepLocations.THE_LOST_PORTAL_UNLOCK.value,
        archipelago_id=45,
        region=KeymastersKeepRegions.KEYMASTERS_KEEP,
        tags=(KeymastersKeepTags.DOOR_UNLOCKS,),
    ),
    KeymastersKeepLocations.THE_LOST_THRESHOLD_UNLOCK: KeymastersKeepLocationData(
        name=KeymastersKeepLocations.THE_LOST_THRESHOLD_UNLOCK.value,
        archipelago_id=46,
        region=KeymastersKeepRegions.KEYMASTERS_KEEP,
        tags=(KeymastersKeepTags.DOOR_UNLOCKS,),
    ),
    KeymastersKeepLocations.THE_MYSTERIOUS_ARCH_UNLOCK: KeymastersKeepLocationData(
        name=KeymastersKeepLocations.THE_MYSTERIOUS_ARCH_UNLOCK.value,
        archipelago_id=47,
        region=KeymastersKeepRegions.KEYMASTERS_KEEP,
        tags=(KeymastersKeepTags.DOOR_UNLOCKS,),
    ),
    KeymastersKeepLocations.THE_MYSTERIOUS_DOORWAY_UNLOCK: KeymastersKeepLocationData(
        name=KeymastersKeepLocations.THE_MYSTERIOUS_DOORWAY_UNLOCK.value,
        archipelago_id=48,
        region=KeymastersKeepRegions.KEYMASTERS_KEEP,
        tags=(KeymastersKeepTags.DOOR_UNLOCKS,),
    ),
    KeymastersKeepLocations.THE_MYSTERIOUS_PASSAGE_UNLOCK: KeymastersKeepLocationData(
        name=KeymastersKeepLocations.THE_MYSTERIOUS_PASSAGE_UNLOCK.value,
        archipelago_id=49,
        region=KeymastersKeepRegions.KEYMASTERS_KEEP,
        tags=(KeymastersKeepTags.DOOR_UNLOCKS,),
    ),
    KeymastersKeepLocations.THE_MYSTERIOUS_VAULT_UNLOCK: KeymastersKeepLocationData(
        name=KeymastersKeepLocations.THE_MYSTERIOUS_VAULT_UNLOCK.value,
        archipelago_id=50,
        region=KeymastersKeepRegions.KEYMASTERS_KEEP,
        tags=(KeymastersKeepTags.DOOR_UNLOCKS,),
    ),
    KeymastersKeepLocations.THE_MYSTICAL_PASSAGE_UNLOCK: KeymastersKeepLocationData(
        name=KeymastersKeepLocations.THE_MYSTICAL_PASSAGE_UNLOCK.value,
        archipelago_id=51,
        region=KeymastersKeepRegions.KEYMASTERS_KEEP,
        tags=(KeymastersKeepTags.DOOR_UNLOCKS,),
    ),
    KeymastersKeepLocations.THE_OBSCURED_ARCH_UNLOCK: KeymastersKeepLocationData(
        name=KeymastersKeepLocations.THE_OBSCURED_ARCH_UNLOCK.value,
        archipelago_id=52,
        region=KeymastersKeepRegions.KEYMASTERS_KEEP,
        tags=(KeymastersKeepTags.DOOR_UNLOCKS,),
    ),
    KeymastersKeepLocations.THE_OBSCURED_DOORWAY_UNLOCK: KeymastersKeepLocationData(
        name=KeymastersKeepLocations.THE_OBSCURED_DOORWAY_UNLOCK.value,
        archipelago_id=53,
        region=KeymastersKeepRegions.KEYMASTERS_KEEP,
        tags=(KeymastersKeepTags.DOOR_UNLOCKS,),
    ),
    KeymastersKeepLocations.THE_OBSCURED_PORTAL_UNLOCK: KeymastersKeepLocationData(
        name=KeymastersKeepLocations.THE_OBSCURED_PORTAL_UNLOCK.value,
        archipelago_id=54,
        region=KeymastersKeepRegions.KEYMASTERS_KEEP,
        tags=(KeymastersKeepTags.DOOR_UNLOCKS,),
    ),
    KeymastersKeepLocations.THE_OBSCURED_VAULT_UNLOCK: KeymastersKeepLocationData(
        name=KeymastersKeepLocations.THE_OBSCURED_VAULT_UNLOCK.value,
        archipelago_id=55,
        region=KeymastersKeepRegions.KEYMASTERS_KEEP,
        tags=(KeymastersKeepTags.DOOR_UNLOCKS,),
    ),
    KeymastersKeepLocations.THE_OBSCURE_PASSAGE_UNLOCK: KeymastersKeepLocationData(
        name=KeymastersKeepLocations.THE_OBSCURE_PASSAGE_UNLOCK.value,
        archipelago_id=56,
        region=KeymastersKeepRegions.KEYMASTERS_KEEP,
        tags=(KeymastersKeepTags.DOOR_UNLOCKS,),
    ),
    KeymastersKeepLocations.THE_PHANTOM_PASSAGE_UNLOCK: KeymastersKeepLocationData(
        name=KeymastersKeepLocations.THE_PHANTOM_PASSAGE_UNLOCK.value,
        archipelago_id=57,
        region=KeymastersKeepRegions.KEYMASTERS_KEEP,
        tags=(KeymastersKeepTags.DOOR_UNLOCKS,),
    ),
    KeymastersKeepLocations.THE_PHANTOM_VAULT_UNLOCK: KeymastersKeepLocationData(
        name=KeymastersKeepLocations.THE_PHANTOM_VAULT_UNLOCK.value,
        archipelago_id=58,
        region=KeymastersKeepRegions.KEYMASTERS_KEEP,
        tags=(KeymastersKeepTags.DOOR_UNLOCKS,),
    ),
    KeymastersKeepLocations.THE_QUIET_ARCHWAY_UNLOCK: KeymastersKeepLocationData(
        name=KeymastersKeepLocations.THE_QUIET_ARCHWAY_UNLOCK.value,
        archipelago_id=59,
        region=KeymastersKeepRegions.KEYMASTERS_KEEP,
        tags=(KeymastersKeepTags.DOOR_UNLOCKS,),
    ),
    KeymastersKeepLocations.THE_QUIET_THRESHOLD_UNLOCK: KeymastersKeepLocationData(
        name=KeymastersKeepLocations.THE_QUIET_THRESHOLD_UNLOCK.value,
        archipelago_id=60,
        region=KeymastersKeepRegions.KEYMASTERS_KEEP,
        tags=(KeymastersKeepTags.DOOR_UNLOCKS,),
    ),
    KeymastersKeepLocations.THE_SEALED_CHAMBER_UNLOCK: KeymastersKeepLocationData(
        name=KeymastersKeepLocations.THE_SEALED_CHAMBER_UNLOCK.value,
        archipelago_id=61,
        region=KeymastersKeepRegions.KEYMASTERS_KEEP,
        tags=(KeymastersKeepTags.DOOR_UNLOCKS,),
    ),
    KeymastersKeepLocations.THE_SEALED_GATEWAY_UNLOCK: KeymastersKeepLocationData(
        name=KeymastersKeepLocations.THE_SEALED_GATEWAY_UNLOCK.value,
        archipelago_id=62,
        region=KeymastersKeepRegions.KEYMASTERS_KEEP,
        tags=(KeymastersKeepTags.DOOR_UNLOCKS,),
    ),
    KeymastersKeepLocations.THE_SEALED_THRESHOLD_UNLOCK: KeymastersKeepLocationData(
        name=KeymastersKeepLocations.THE_SEALED_THRESHOLD_UNLOCK.value,
        archipelago_id=63,
        region=KeymastersKeepRegions.KEYMASTERS_KEEP,
        tags=(KeymastersKeepTags.DOOR_UNLOCKS,),
    ),
    KeymastersKeepLocations.THE_SECRETED_DOOR_UNLOCK: KeymastersKeepLocationData(
        name=KeymastersKeepLocations.THE_SECRETED_DOOR_UNLOCK.value,
        archipelago_id=64,
        region=KeymastersKeepRegions.KEYMASTERS_KEEP,
        tags=(KeymastersKeepTags.DOOR_UNLOCKS,),
    ),
    KeymastersKeepLocations.THE_SECRETIVE_DOOR_UNLOCK: KeymastersKeepLocationData(
        name=KeymastersKeepLocations.THE_SECRETIVE_DOOR_UNLOCK.value,
        archipelago_id=65,
        region=KeymastersKeepRegions.KEYMASTERS_KEEP,
        tags=(KeymastersKeepTags.DOOR_UNLOCKS,),
    ),
    KeymastersKeepLocations.THE_SECRET_ARCHWAY_UNLOCK: KeymastersKeepLocationData(
        name=KeymastersKeepLocations.THE_SECRET_ARCHWAY_UNLOCK.value,
        archipelago_id=66,
        region=KeymastersKeepRegions.KEYMASTERS_KEEP,
        tags=(KeymastersKeepTags.DOOR_UNLOCKS,),
    ),
    KeymastersKeepLocations.THE_SECRET_PASSAGEWAY_UNLOCK: KeymastersKeepLocationData(
        name=KeymastersKeepLocations.THE_SECRET_PASSAGEWAY_UNLOCK.value,
        archipelago_id=67,
        region=KeymastersKeepRegions.KEYMASTERS_KEEP,
        tags=(KeymastersKeepTags.DOOR_UNLOCKS,),
    ),
    KeymastersKeepLocations.THE_SECRET_THRESHOLD_UNLOCK: KeymastersKeepLocationData(
        name=KeymastersKeepLocations.THE_SECRET_THRESHOLD_UNLOCK.value,
        archipelago_id=68,
        region=KeymastersKeepRegions.KEYMASTERS_KEEP,
        tags=(KeymastersKeepTags.DOOR_UNLOCKS,),
    ),
    KeymastersKeepLocations.THE_SECRET_VAULT_UNLOCK: KeymastersKeepLocationData(
        name=KeymastersKeepLocations.THE_SECRET_VAULT_UNLOCK.value,
        archipelago_id=69,
        region=KeymastersKeepRegions.KEYMASTERS_KEEP,
        tags=(KeymastersKeepTags.DOOR_UNLOCKS,),
    ),
    KeymastersKeepLocations.THE_SHADOWED_PORTAL_UNLOCK: KeymastersKeepLocationData(
        name=KeymastersKeepLocations.THE_SHADOWED_PORTAL_UNLOCK.value,
        archipelago_id=70,
        region=KeymastersKeepRegions.KEYMASTERS_KEEP,
        tags=(KeymastersKeepTags.DOOR_UNLOCKS,),
    ),
    KeymastersKeepLocations.THE_SHADOWED_THRESHOLD_UNLOCK: KeymastersKeepLocationData(
        name=KeymastersKeepLocations.THE_SHADOWED_THRESHOLD_UNLOCK.value,
        archipelago_id=71,
        region=KeymastersKeepRegions.KEYMASTERS_KEEP,
        tags=(KeymastersKeepTags.DOOR_UNLOCKS,),
    ),
    KeymastersKeepLocations.THE_SHADOWY_PASSAGE_UNLOCK: KeymastersKeepLocationData(
        name=KeymastersKeepLocations.THE_SHADOWY_PASSAGE_UNLOCK.value,
        archipelago_id=72,
        region=KeymastersKeepRegions.KEYMASTERS_KEEP,
        tags=(KeymastersKeepTags.DOOR_UNLOCKS,),
    ),
    KeymastersKeepLocations.THE_SHIMMERING_PASSAGE_UNLOCK: KeymastersKeepLocationData(
        name=KeymastersKeepLocations.THE_SHIMMERING_PASSAGE_UNLOCK.value,
        archipelago_id=73,
        region=KeymastersKeepRegions.KEYMASTERS_KEEP,
        tags=(KeymastersKeepTags.DOOR_UNLOCKS,),
    ),
    KeymastersKeepLocations.THE_SHROUDED_GATEWAY_UNLOCK: KeymastersKeepLocationData(
        name=KeymastersKeepLocations.THE_SHROUDED_GATEWAY_UNLOCK.value,
        archipelago_id=74,
        region=KeymastersKeepRegions.KEYMASTERS_KEEP,
        tags=(KeymastersKeepTags.DOOR_UNLOCKS,),
    ),
    KeymastersKeepLocations.THE_SHROUDED_PORTAL_UNLOCK: KeymastersKeepLocationData(
        name=KeymastersKeepLocations.THE_SHROUDED_PORTAL_UNLOCK.value,
        archipelago_id=75,
        region=KeymastersKeepRegions.KEYMASTERS_KEEP,
        tags=(KeymastersKeepTags.DOOR_UNLOCKS,),
    ),
    KeymastersKeepLocations.THE_SILENT_ARCHWAY_UNLOCK: KeymastersKeepLocationData(
        name=KeymastersKeepLocations.THE_SILENT_ARCHWAY_UNLOCK.value,
        archipelago_id=76,
        region=KeymastersKeepRegions.KEYMASTERS_KEEP,
        tags=(KeymastersKeepTags.DOOR_UNLOCKS,),
    ),
    KeymastersKeepLocations.THE_SILENT_PASSAGE_UNLOCK: KeymastersKeepLocationData(
        name=KeymastersKeepLocations.THE_SILENT_PASSAGE_UNLOCK.value,
        archipelago_id=77,
        region=KeymastersKeepRegions.KEYMASTERS_KEEP,
        tags=(KeymastersKeepTags.DOOR_UNLOCKS,),
    ),
    KeymastersKeepLocations.THE_SILENT_THRESHOLD_UNLOCK: KeymastersKeepLocationData(
        name=KeymastersKeepLocations.THE_SILENT_THRESHOLD_UNLOCK.value,
        archipelago_id=78,
        region=KeymastersKeepRegions.KEYMASTERS_KEEP,
        tags=(KeymastersKeepTags.DOOR_UNLOCKS,),
    ),
    KeymastersKeepLocations.THE_SILENT_VAULT_UNLOCK: KeymastersKeepLocationData(
        name=KeymastersKeepLocations.THE_SILENT_VAULT_UNLOCK.value,
        archipelago_id=79,
        region=KeymastersKeepRegions.KEYMASTERS_KEEP,
        tags=(KeymastersKeepTags.DOOR_UNLOCKS,),
    ),
    KeymastersKeepLocations.THE_UNFATHOMABLE_DOOR_UNLOCK: KeymastersKeepLocationData(
        name=KeymastersKeepLocations.THE_UNFATHOMABLE_DOOR_UNLOCK.value,
        archipelago_id=80,
        region=KeymastersKeepRegions.KEYMASTERS_KEEP,
        tags=(KeymastersKeepTags.DOOR_UNLOCKS,),
    ),
    KeymastersKeepLocations.THE_UNKNOWN_ARCH_UNLOCK: KeymastersKeepLocationData(
        name=KeymastersKeepLocations.THE_UNKNOWN_ARCH_UNLOCK.value,
        archipelago_id=81,
        region=KeymastersKeepRegions.KEYMASTERS_KEEP,
        tags=(KeymastersKeepTags.DOOR_UNLOCKS,),
    ),
    KeymastersKeepLocations.THE_UNKNOWN_GATEWAY_UNLOCK: KeymastersKeepLocationData(
        name=KeymastersKeepLocations.THE_UNKNOWN_GATEWAY_UNLOCK.value,
        archipelago_id=82,
        region=KeymastersKeepRegions.KEYMASTERS_KEEP,
        tags=(KeymastersKeepTags.DOOR_UNLOCKS,),
    ),
    KeymastersKeepLocations.THE_UNMARKED_PASSAGE_UNLOCK: KeymastersKeepLocationData(
        name=KeymastersKeepLocations.THE_UNMARKED_PASSAGE_UNLOCK.value,
        archipelago_id=83,
        region=KeymastersKeepRegions.KEYMASTERS_KEEP,
        tags=(KeymastersKeepTags.DOOR_UNLOCKS,),
    ),
    KeymastersKeepLocations.THE_UNMARKED_VAULT_UNLOCK: KeymastersKeepLocationData(
        name=KeymastersKeepLocations.THE_UNMARKED_VAULT_UNLOCK.value,
        archipelago_id=84,
        region=KeymastersKeepRegions.KEYMASTERS_KEEP,
        tags=(KeymastersKeepTags.DOOR_UNLOCKS,),
    ),
    KeymastersKeepLocations.THE_UNRAVELED_DOOR_UNLOCK: KeymastersKeepLocationData(
        name=KeymastersKeepLocations.THE_UNRAVELED_DOOR_UNLOCK.value,
        archipelago_id=85,
        region=KeymastersKeepRegions.KEYMASTERS_KEEP,
        tags=(KeymastersKeepTags.DOOR_UNLOCKS,),
    ),
    KeymastersKeepLocations.THE_UNSEEN_ARCHWAY_UNLOCK: KeymastersKeepLocationData(
        name=KeymastersKeepLocations.THE_UNSEEN_ARCHWAY_UNLOCK.value,
        archipelago_id=86,
        region=KeymastersKeepRegions.KEYMASTERS_KEEP,
        tags=(KeymastersKeepTags.DOOR_UNLOCKS,),
    ),
    KeymastersKeepLocations.THE_UNSEEN_DOOR_UNLOCK: KeymastersKeepLocationData(
        name=KeymastersKeepLocations.THE_UNSEEN_DOOR_UNLOCK.value,
        archipelago_id=87,
        region=KeymastersKeepRegions.KEYMASTERS_KEEP,
        tags=(KeymastersKeepTags.DOOR_UNLOCKS,),
    ),
    KeymastersKeepLocations.THE_UNSEEN_PASSAGE_UNLOCK: KeymastersKeepLocationData(
        name=KeymastersKeepLocations.THE_UNSEEN_PASSAGE_UNLOCK.value,
        archipelago_id=88,
        region=KeymastersKeepRegions.KEYMASTERS_KEEP,
        tags=(KeymastersKeepTags.DOOR_UNLOCKS,),
    ),
    KeymastersKeepLocations.THE_UNSEEN_PORTAL_UNLOCK: KeymastersKeepLocationData(
        name=KeymastersKeepLocations.THE_UNSEEN_PORTAL_UNLOCK.value,
        archipelago_id=89,
        region=KeymastersKeepRegions.KEYMASTERS_KEEP,
        tags=(KeymastersKeepTags.DOOR_UNLOCKS,),
    ),
    KeymastersKeepLocations.THE_UNSPOKEN_GATE_UNLOCK: KeymastersKeepLocationData(
        name=KeymastersKeepLocations.THE_UNSPOKEN_GATE_UNLOCK.value,
        archipelago_id=90,
        region=KeymastersKeepRegions.KEYMASTERS_KEEP,
        tags=(KeymastersKeepTags.DOOR_UNLOCKS,),
    ),
    KeymastersKeepLocations.THE_UNTOLD_GATEWAY_UNLOCK: KeymastersKeepLocationData(
        name=KeymastersKeepLocations.THE_UNTOLD_GATEWAY_UNLOCK.value,
        archipelago_id=91,
        region=KeymastersKeepRegions.KEYMASTERS_KEEP,
        tags=(KeymastersKeepTags.DOOR_UNLOCKS,),
    ),
    KeymastersKeepLocations.THE_UNTRACEABLE_PATH_UNLOCK: KeymastersKeepLocationData(
        name=KeymastersKeepLocations.THE_UNTRACEABLE_PATH_UNLOCK.value,
        archipelago_id=92,
        region=KeymastersKeepRegions.KEYMASTERS_KEEP,
        tags=(KeymastersKeepTags.DOOR_UNLOCKS,),
    ),
    KeymastersKeepLocations.THE_VANISHING_ARCHWAY_UNLOCK: KeymastersKeepLocationData(
        name=KeymastersKeepLocations.THE_VANISHING_ARCHWAY_UNLOCK.value,
        archipelago_id=93,
        region=KeymastersKeepRegions.KEYMASTERS_KEEP,
        tags=(KeymastersKeepTags.DOOR_UNLOCKS,),
    ),
    KeymastersKeepLocations.THE_VANISHING_DOOR_UNLOCK: KeymastersKeepLocationData(
        name=KeymastersKeepLocations.THE_VANISHING_DOOR_UNLOCK.value,
        archipelago_id=94,
        region=KeymastersKeepRegions.KEYMASTERS_KEEP,
        tags=(KeymastersKeepTags.DOOR_UNLOCKS,),
    ),
    KeymastersKeepLocations.THE_VAULT_OF_WHISPERS_UNLOCK: KeymastersKeepLocationData(
        name=KeymastersKeepLocations.THE_VAULT_OF_WHISPERS_UNLOCK.value,
        archipelago_id=95,
        region=KeymastersKeepRegions.KEYMASTERS_KEEP,
        tags=(KeymastersKeepTags.DOOR_UNLOCKS,),
    ),
    KeymastersKeepLocations.THE_VEILED_PASSAGE_UNLOCK: KeymastersKeepLocationData(
        name=KeymastersKeepLocations.THE_VEILED_PASSAGE_UNLOCK.value,
        archipelago_id=96,
        region=KeymastersKeepRegions.KEYMASTERS_KEEP,
        tags=(KeymastersKeepTags.DOOR_UNLOCKS,),
    ),
    KeymastersKeepLocations.THE_VEILED_PATH_UNLOCK: KeymastersKeepLocationData(
        name=KeymastersKeepLocations.THE_VEILED_PATH_UNLOCK.value,
        archipelago_id=97,
        region=KeymastersKeepRegions.KEYMASTERS_KEEP,
        tags=(KeymastersKeepTags.DOOR_UNLOCKS,),
    ),
    KeymastersKeepLocations.THE_WHISPERED_PORTAL_UNLOCK: KeymastersKeepLocationData(
        name=KeymastersKeepLocations.THE_WHISPERED_PORTAL_UNLOCK.value,
        archipelago_id=98,
        region=KeymastersKeepRegions.KEYMASTERS_KEEP,
        tags=(KeymastersKeepTags.DOOR_UNLOCKS,),
    ),
    KeymastersKeepLocations.THE_WHISPERED_THRESHOLD_UNLOCK: KeymastersKeepLocationData(
        name=KeymastersKeepLocations.THE_WHISPERED_THRESHOLD_UNLOCK.value,
        archipelago_id=99,
        region=KeymastersKeepRegions.KEYMASTERS_KEEP,
        tags=(KeymastersKeepTags.DOOR_UNLOCKS,),
    ),
    KeymastersKeepLocations.THE_WHISPERING_DOOR_UNLOCK: KeymastersKeepLocationData(
        name=KeymastersKeepLocations.THE_WHISPERING_DOOR_UNLOCK.value,
        archipelago_id=100,
        region=KeymastersKeepRegions.KEYMASTERS_KEEP,
        tags=(KeymastersKeepTags.DOOR_UNLOCKS,),
    ),
}

# Trials & Completions
location_data[KeymastersKeepLocations.THE_KEYMASTERS_CHALLENGE_CHAMBER_VICTORY] = KeymastersKeepLocationData(
    name=KeymastersKeepLocations.THE_KEYMASTERS_CHALLENGE_CHAMBER_VICTORY.value,
    archipelago_id=999,
    region=KeymastersKeepRegions.THE_KEYMASTERS_CHALLENGE_CHAMBER,
    tags=(KeymastersKeepTags.TRIALS,),
)

trials: List[Any] = sorted([trial.value for trial in KeymastersKeepTrials])
trial_count: int = len(trials)

for index, (region, trial_location, completion_location, trials_tag) in enumerate([
    (KeymastersKeepRegions.THE_ARCANE_DOOR, KeymastersKeepLocations.THE_ARCANE_DOOR_TRIAL, KeymastersKeepLocations.THE_ARCANE_DOOR_COMPLETE, KeymastersKeepTags.TRIALS_THE_ARCANE_DOOR),
    (KeymastersKeepRegions.THE_ARCANE_PASSAGE, KeymastersKeepLocations.THE_ARCANE_PASSAGE_TRIAL, KeymastersKeepLocations.THE_ARCANE_PASSAGE_COMPLETE, KeymastersKeepTags.TRIALS_THE_ARCANE_PASSAGE),
    (KeymastersKeepRegions.THE_ARCANE_THRESHOLD, KeymastersKeepLocations.THE_ARCANE_THRESHOLD_TRIAL, KeymastersKeepLocations.THE_ARCANE_THRESHOLD_COMPLETE, KeymastersKeepTags.TRIALS_THE_ARCANE_THRESHOLD),
    (KeymastersKeepRegions.THE_CLANDESTINE_PASSAGE, KeymastersKeepLocations.THE_CLANDESTINE_PASSAGE_TRIAL, KeymastersKeepLocations.THE_CLANDESTINE_PASSAGE_COMPLETE, KeymastersKeepTags.TRIALS_THE_CLANDESTINE_PASSAGE),
    (KeymastersKeepRegions.THE_CLOAKED_ENTRANCE, KeymastersKeepLocations.THE_CLOAKED_ENTRANCE_TRIAL, KeymastersKeepLocations.THE_CLOAKED_ENTRANCE_COMPLETE, KeymastersKeepTags.TRIALS_THE_CLOAKED_ENTRANCE),
    (KeymastersKeepRegions.THE_CLOAKED_THRESHOLD, KeymastersKeepLocations.THE_CLOAKED_THRESHOLD_TRIAL, KeymastersKeepLocations.THE_CLOAKED_THRESHOLD_COMPLETE, KeymastersKeepTags.TRIALS_THE_CLOAKED_THRESHOLD),
    (KeymastersKeepRegions.THE_CLOAKED_VAULT, KeymastersKeepLocations.THE_CLOAKED_VAULT_TRIAL, KeymastersKeepLocations.THE_CLOAKED_VAULT_COMPLETE, KeymastersKeepTags.TRIALS_THE_CLOAKED_VAULT),
    (KeymastersKeepRegions.THE_CONCEALED_THRESHOLD, KeymastersKeepLocations.THE_CONCEALED_THRESHOLD_TRIAL, KeymastersKeepLocations.THE_CONCEALED_THRESHOLD_COMPLETE, KeymastersKeepTags.TRIALS_THE_CONCEALED_THRESHOLD),
    (KeymastersKeepRegions.THE_CONCEALED_VAULT, KeymastersKeepLocations.THE_CONCEALED_VAULT_TRIAL, KeymastersKeepLocations.THE_CONCEALED_VAULT_COMPLETE, KeymastersKeepTags.TRIALS_THE_CONCEALED_VAULT),
    (KeymastersKeepRegions.THE_CRYPTIC_CHAMBER, KeymastersKeepLocations.THE_CRYPTIC_CHAMBER_TRIAL, KeymastersKeepLocations.THE_CRYPTIC_CHAMBER_COMPLETE, KeymastersKeepTags.TRIALS_THE_CRYPTIC_CHAMBER),
    (KeymastersKeepRegions.THE_CRYPTIC_GATEWAY, KeymastersKeepLocations.THE_CRYPTIC_GATEWAY_TRIAL, KeymastersKeepLocations.THE_CRYPTIC_GATEWAY_COMPLETE, KeymastersKeepTags.TRIALS_THE_CRYPTIC_GATEWAY),
    (KeymastersKeepRegions.THE_CRYPTIC_VAULT, KeymastersKeepLocations.THE_CRYPTIC_VAULT_TRIAL, KeymastersKeepLocations.THE_CRYPTIC_VAULT_COMPLETE, KeymastersKeepTags.TRIALS_THE_CRYPTIC_VAULT),
    (KeymastersKeepRegions.THE_DISGUISED_GATEWAY, KeymastersKeepLocations.THE_DISGUISED_GATEWAY_TRIAL, KeymastersKeepLocations.THE_DISGUISED_GATEWAY_COMPLETE, KeymastersKeepTags.TRIALS_THE_DISGUISED_GATEWAY),
    (KeymastersKeepRegions.THE_ECHOING_PASSAGE, KeymastersKeepLocations.THE_ECHOING_PASSAGE_TRIAL, KeymastersKeepLocations.THE_ECHOING_PASSAGE_COMPLETE, KeymastersKeepTags.TRIALS_THE_ECHOING_PASSAGE),
    (KeymastersKeepRegions.THE_ELUSIVE_DOOR, KeymastersKeepLocations.THE_ELUSIVE_DOOR_TRIAL, KeymastersKeepLocations.THE_ELUSIVE_DOOR_COMPLETE, KeymastersKeepTags.TRIALS_THE_ELUSIVE_DOOR),
    (KeymastersKeepRegions.THE_ENCHANTED_GATEWAY, KeymastersKeepLocations.THE_ENCHANTED_GATEWAY_TRIAL, KeymastersKeepLocations.THE_ENCHANTED_GATEWAY_COMPLETE, KeymastersKeepTags.TRIALS_THE_ENCHANTED_GATEWAY),
    (KeymastersKeepRegions.THE_ENCHANTED_PASSAGE, KeymastersKeepLocations.THE_ENCHANTED_PASSAGE_TRIAL, KeymastersKeepLocations.THE_ENCHANTED_PASSAGE_COMPLETE, KeymastersKeepTags.TRIALS_THE_ENCHANTED_PASSAGE),
    (KeymastersKeepRegions.THE_ENIGMATIC_PORTAL, KeymastersKeepLocations.THE_ENIGMATIC_PORTAL_TRIAL, KeymastersKeepLocations.THE_ENIGMATIC_PORTAL_COMPLETE, KeymastersKeepTags.TRIALS_THE_ENIGMATIC_PORTAL),
    (KeymastersKeepRegions.THE_ENIGMATIC_THRESHOLD, KeymastersKeepLocations.THE_ENIGMATIC_THRESHOLD_TRIAL, KeymastersKeepLocations.THE_ENIGMATIC_THRESHOLD_COMPLETE, KeymastersKeepTags.TRIALS_THE_ENIGMATIC_THRESHOLD),
    (KeymastersKeepRegions.THE_FADED_GATEWAY, KeymastersKeepLocations.THE_FADED_GATEWAY_TRIAL, KeymastersKeepLocations.THE_FADED_GATEWAY_COMPLETE, KeymastersKeepTags.TRIALS_THE_FADED_GATEWAY),
    (KeymastersKeepRegions.THE_FAINT_DOORWAY, KeymastersKeepLocations.THE_FAINT_DOORWAY_TRIAL, KeymastersKeepLocations.THE_FAINT_DOORWAY_COMPLETE, KeymastersKeepTags.TRIALS_THE_FAINT_DOORWAY),
    (KeymastersKeepRegions.THE_FAINT_PATH, KeymastersKeepLocations.THE_FAINT_PATH_TRIAL, KeymastersKeepLocations.THE_FAINT_PATH_COMPLETE, KeymastersKeepTags.TRIALS_THE_FAINT_PATH),
    (KeymastersKeepRegions.THE_FAINT_THRESHOLD, KeymastersKeepLocations.THE_FAINT_THRESHOLD_TRIAL, KeymastersKeepLocations.THE_FAINT_THRESHOLD_COMPLETE, KeymastersKeepTags.TRIALS_THE_FAINT_THRESHOLD),
    (KeymastersKeepRegions.THE_FORBIDDEN_ENTRANCE, KeymastersKeepLocations.THE_FORBIDDEN_ENTRANCE_TRIAL, KeymastersKeepLocations.THE_FORBIDDEN_ENTRANCE_COMPLETE, KeymastersKeepTags.TRIALS_THE_FORBIDDEN_ENTRANCE),
    (KeymastersKeepRegions.THE_FORGOTTEN_DOOR, KeymastersKeepLocations.THE_FORGOTTEN_DOOR_TRIAL, KeymastersKeepLocations.THE_FORGOTTEN_DOOR_COMPLETE, KeymastersKeepTags.TRIALS_THE_FORGOTTEN_DOOR),
    (KeymastersKeepRegions.THE_FORGOTTEN_GATEWAY, KeymastersKeepLocations.THE_FORGOTTEN_GATEWAY_TRIAL, KeymastersKeepLocations.THE_FORGOTTEN_GATEWAY_COMPLETE, KeymastersKeepTags.TRIALS_THE_FORGOTTEN_GATEWAY),
    (KeymastersKeepRegions.THE_FORGOTTEN_PORTAL, KeymastersKeepLocations.THE_FORGOTTEN_PORTAL_TRIAL, KeymastersKeepLocations.THE_FORGOTTEN_PORTAL_COMPLETE, KeymastersKeepTags.TRIALS_THE_FORGOTTEN_PORTAL),
    (KeymastersKeepRegions.THE_FORGOTTEN_THRESHOLD, KeymastersKeepLocations.THE_FORGOTTEN_THRESHOLD_TRIAL, KeymastersKeepLocations.THE_FORGOTTEN_THRESHOLD_COMPLETE, KeymastersKeepTags.TRIALS_THE_FORGOTTEN_THRESHOLD),
    (KeymastersKeepRegions.THE_GHOSTED_PASSAGEWAY, KeymastersKeepLocations.THE_GHOSTED_PASSAGEWAY_TRIAL, KeymastersKeepLocations.THE_GHOSTED_PASSAGEWAY_COMPLETE, KeymastersKeepTags.TRIALS_THE_GHOSTED_PASSAGEWAY),
    (KeymastersKeepRegions.THE_GHOSTLY_PASSAGE, KeymastersKeepLocations.THE_GHOSTLY_PASSAGE_TRIAL, KeymastersKeepLocations.THE_GHOSTLY_PASSAGE_COMPLETE, KeymastersKeepTags.TRIALS_THE_GHOSTLY_PASSAGE),
    (KeymastersKeepRegions.THE_HIDDEN_ARCHWAY, KeymastersKeepLocations.THE_HIDDEN_ARCHWAY_TRIAL, KeymastersKeepLocations.THE_HIDDEN_ARCHWAY_COMPLETE, KeymastersKeepTags.TRIALS_THE_HIDDEN_ARCHWAY),
    (KeymastersKeepRegions.THE_HIDDEN_CHAMBER, KeymastersKeepLocations.THE_HIDDEN_CHAMBER_TRIAL, KeymastersKeepLocations.THE_HIDDEN_CHAMBER_COMPLETE, KeymastersKeepTags.TRIALS_THE_HIDDEN_CHAMBER),
    (KeymastersKeepRegions.THE_HIDDEN_DOORWAY, KeymastersKeepLocations.THE_HIDDEN_DOORWAY_TRIAL, KeymastersKeepLocations.THE_HIDDEN_DOORWAY_COMPLETE, KeymastersKeepTags.TRIALS_THE_HIDDEN_DOORWAY),
    (KeymastersKeepRegions.THE_HIDDEN_ENTRANCE, KeymastersKeepLocations.THE_HIDDEN_ENTRANCE_TRIAL, KeymastersKeepLocations.THE_HIDDEN_ENTRANCE_COMPLETE, KeymastersKeepTags.TRIALS_THE_HIDDEN_ENTRANCE),
    (KeymastersKeepRegions.THE_HIDDEN_KEYHOLE, KeymastersKeepLocations.THE_HIDDEN_KEYHOLE_TRIAL, KeymastersKeepLocations.THE_HIDDEN_KEYHOLE_COMPLETE, KeymastersKeepTags.TRIALS_THE_HIDDEN_KEYHOLE),
    (KeymastersKeepRegions.THE_HIDDEN_PASSAGEWAY, KeymastersKeepLocations.THE_HIDDEN_PASSAGEWAY_TRIAL, KeymastersKeepLocations.THE_HIDDEN_PASSAGEWAY_COMPLETE, KeymastersKeepTags.TRIALS_THE_HIDDEN_PASSAGEWAY),
    (KeymastersKeepRegions.THE_HIDDEN_PATH, KeymastersKeepLocations.THE_HIDDEN_PATH_TRIAL, KeymastersKeepLocations.THE_HIDDEN_PATH_COMPLETE, KeymastersKeepTags.TRIALS_THE_HIDDEN_PATH),
    (KeymastersKeepRegions.THE_HIDDEN_REACH, KeymastersKeepLocations.THE_HIDDEN_REACH_TRIAL, KeymastersKeepLocations.THE_HIDDEN_REACH_COMPLETE, KeymastersKeepTags.TRIALS_THE_HIDDEN_REACH),
    (KeymastersKeepRegions.THE_HIDDEN_VAULT, KeymastersKeepLocations.THE_HIDDEN_VAULT_TRIAL, KeymastersKeepLocations.THE_HIDDEN_VAULT_COMPLETE, KeymastersKeepTags.TRIALS_THE_HIDDEN_VAULT),
    (KeymastersKeepRegions.THE_INCONSPICUOUS_DOOR, KeymastersKeepLocations.THE_INCONSPICUOUS_DOOR_TRIAL, KeymastersKeepLocations.THE_INCONSPICUOUS_DOOR_COMPLETE, KeymastersKeepTags.TRIALS_THE_INCONSPICUOUS_DOOR),
    (KeymastersKeepRegions.THE_INVISIBLE_DOORWAY, KeymastersKeepLocations.THE_INVISIBLE_DOORWAY_TRIAL, KeymastersKeepLocations.THE_INVISIBLE_DOORWAY_COMPLETE, KeymastersKeepTags.TRIALS_THE_INVISIBLE_DOORWAY),
    (KeymastersKeepRegions.THE_LOCKED_DOORWAY, KeymastersKeepLocations.THE_LOCKED_DOORWAY_TRIAL, KeymastersKeepLocations.THE_LOCKED_DOORWAY_COMPLETE, KeymastersKeepTags.TRIALS_THE_LOCKED_DOORWAY),
    (KeymastersKeepRegions.THE_LOCKED_GATEWAY, KeymastersKeepLocations.THE_LOCKED_GATEWAY_TRIAL, KeymastersKeepLocations.THE_LOCKED_GATEWAY_COMPLETE, KeymastersKeepTags.TRIALS_THE_LOCKED_GATEWAY),
    (KeymastersKeepRegions.THE_LOST_ARCHWAY, KeymastersKeepLocations.THE_LOST_ARCHWAY_TRIAL, KeymastersKeepLocations.THE_LOST_ARCHWAY_COMPLETE, KeymastersKeepTags.TRIALS_THE_LOST_ARCHWAY),
    (KeymastersKeepRegions.THE_LOST_PORTAL, KeymastersKeepLocations.THE_LOST_PORTAL_TRIAL, KeymastersKeepLocations.THE_LOST_PORTAL_COMPLETE, KeymastersKeepTags.TRIALS_THE_LOST_PORTAL),
    (KeymastersKeepRegions.THE_LOST_THRESHOLD, KeymastersKeepLocations.THE_LOST_THRESHOLD_TRIAL, KeymastersKeepLocations.THE_LOST_THRESHOLD_COMPLETE, KeymastersKeepTags.TRIALS_THE_LOST_THRESHOLD),
    (KeymastersKeepRegions.THE_MYSTERIOUS_ARCH, KeymastersKeepLocations.THE_MYSTERIOUS_ARCH_TRIAL, KeymastersKeepLocations.THE_MYSTERIOUS_ARCH_COMPLETE, KeymastersKeepTags.TRIALS_THE_MYSTERIOUS_ARCH),
    (KeymastersKeepRegions.THE_MYSTERIOUS_DOORWAY, KeymastersKeepLocations.THE_MYSTERIOUS_DOORWAY_TRIAL, KeymastersKeepLocations.THE_MYSTERIOUS_DOORWAY_COMPLETE, KeymastersKeepTags.TRIALS_THE_MYSTERIOUS_DOORWAY),
    (KeymastersKeepRegions.THE_MYSTERIOUS_PASSAGE, KeymastersKeepLocations.THE_MYSTERIOUS_PASSAGE_TRIAL, KeymastersKeepLocations.THE_MYSTERIOUS_PASSAGE_COMPLETE, KeymastersKeepTags.TRIALS_THE_MYSTERIOUS_PASSAGE),
    (KeymastersKeepRegions.THE_MYSTERIOUS_VAULT, KeymastersKeepLocations.THE_MYSTERIOUS_VAULT_TRIAL, KeymastersKeepLocations.THE_MYSTERIOUS_VAULT_COMPLETE, KeymastersKeepTags.TRIALS_THE_MYSTERIOUS_VAULT),
    (KeymastersKeepRegions.THE_MYSTICAL_PASSAGE, KeymastersKeepLocations.THE_MYSTICAL_PASSAGE_TRIAL, KeymastersKeepLocations.THE_MYSTICAL_PASSAGE_COMPLETE, KeymastersKeepTags.TRIALS_THE_MYSTICAL_PASSAGE),
    (KeymastersKeepRegions.THE_OBSCURED_ARCH, KeymastersKeepLocations.THE_OBSCURED_ARCH_TRIAL, KeymastersKeepLocations.THE_OBSCURED_ARCH_COMPLETE, KeymastersKeepTags.TRIALS_THE_OBSCURED_ARCH),
    (KeymastersKeepRegions.THE_OBSCURED_DOORWAY, KeymastersKeepLocations.THE_OBSCURED_DOORWAY_TRIAL, KeymastersKeepLocations.THE_OBSCURED_DOORWAY_COMPLETE, KeymastersKeepTags.TRIALS_THE_OBSCURED_DOORWAY),
    (KeymastersKeepRegions.THE_OBSCURED_PORTAL, KeymastersKeepLocations.THE_OBSCURED_PORTAL_TRIAL, KeymastersKeepLocations.THE_OBSCURED_PORTAL_COMPLETE, KeymastersKeepTags.TRIALS_THE_OBSCURED_PORTAL),
    (KeymastersKeepRegions.THE_OBSCURED_VAULT, KeymastersKeepLocations.THE_OBSCURED_VAULT_TRIAL, KeymastersKeepLocations.THE_OBSCURED_VAULT_COMPLETE, KeymastersKeepTags.TRIALS_THE_OBSCURED_VAULT),
    (KeymastersKeepRegions.THE_OBSCURE_PASSAGE, KeymastersKeepLocations.THE_OBSCURE_PASSAGE_TRIAL, KeymastersKeepLocations.THE_OBSCURE_PASSAGE_COMPLETE, KeymastersKeepTags.TRIALS_THE_OBSCURE_PASSAGE),
    (KeymastersKeepRegions.THE_PHANTOM_PASSAGE, KeymastersKeepLocations.THE_PHANTOM_PASSAGE_TRIAL, KeymastersKeepLocations.THE_PHANTOM_PASSAGE_COMPLETE, KeymastersKeepTags.TRIALS_THE_PHANTOM_PASSAGE),
    (KeymastersKeepRegions.THE_PHANTOM_VAULT, KeymastersKeepLocations.THE_PHANTOM_VAULT_TRIAL, KeymastersKeepLocations.THE_PHANTOM_VAULT_COMPLETE, KeymastersKeepTags.TRIALS_THE_PHANTOM_VAULT),
    (KeymastersKeepRegions.THE_QUIET_ARCHWAY, KeymastersKeepLocations.THE_QUIET_ARCHWAY_TRIAL, KeymastersKeepLocations.THE_QUIET_ARCHWAY_COMPLETE, KeymastersKeepTags.TRIALS_THE_QUIET_ARCHWAY),
    (KeymastersKeepRegions.THE_QUIET_THRESHOLD, KeymastersKeepLocations.THE_QUIET_THRESHOLD_TRIAL, KeymastersKeepLocations.THE_QUIET_THRESHOLD_COMPLETE, KeymastersKeepTags.TRIALS_THE_QUIET_THRESHOLD),
    (KeymastersKeepRegions.THE_SEALED_CHAMBER, KeymastersKeepLocations.THE_SEALED_CHAMBER_TRIAL, KeymastersKeepLocations.THE_SEALED_CHAMBER_COMPLETE, KeymastersKeepTags.TRIALS_THE_SEALED_CHAMBER),
    (KeymastersKeepRegions.THE_SEALED_GATEWAY, KeymastersKeepLocations.THE_SEALED_GATEWAY_TRIAL, KeymastersKeepLocations.THE_SEALED_GATEWAY_COMPLETE, KeymastersKeepTags.TRIALS_THE_SEALED_GATEWAY),
    (KeymastersKeepRegions.THE_SEALED_THRESHOLD, KeymastersKeepLocations.THE_SEALED_THRESHOLD_TRIAL, KeymastersKeepLocations.THE_SEALED_THRESHOLD_COMPLETE, KeymastersKeepTags.TRIALS_THE_SEALED_THRESHOLD),
    (KeymastersKeepRegions.THE_SECRETED_DOOR, KeymastersKeepLocations.THE_SECRETED_DOOR_TRIAL, KeymastersKeepLocations.THE_SECRETED_DOOR_COMPLETE, KeymastersKeepTags.TRIALS_THE_SECRETED_DOOR),
    (KeymastersKeepRegions.THE_SECRETIVE_DOOR, KeymastersKeepLocations.THE_SECRETIVE_DOOR_TRIAL, KeymastersKeepLocations.THE_SECRETIVE_DOOR_COMPLETE, KeymastersKeepTags.TRIALS_THE_SECRETIVE_DOOR),
    (KeymastersKeepRegions.THE_SECRET_ARCHWAY, KeymastersKeepLocations.THE_SECRET_ARCHWAY_TRIAL, KeymastersKeepLocations.THE_SECRET_ARCHWAY_COMPLETE, KeymastersKeepTags.TRIALS_THE_SECRET_ARCHWAY),
    (KeymastersKeepRegions.THE_SECRET_PASSAGEWAY, KeymastersKeepLocations.THE_SECRET_PASSAGEWAY_TRIAL, KeymastersKeepLocations.THE_SECRET_PASSAGEWAY_COMPLETE, KeymastersKeepTags.TRIALS_THE_SECRET_PASSAGEWAY),
    (KeymastersKeepRegions.THE_SECRET_THRESHOLD, KeymastersKeepLocations.THE_SECRET_THRESHOLD_TRIAL, KeymastersKeepLocations.THE_SECRET_THRESHOLD_COMPLETE, KeymastersKeepTags.TRIALS_THE_SECRET_THRESHOLD),
    (KeymastersKeepRegions.THE_SECRET_VAULT, KeymastersKeepLocations.THE_SECRET_VAULT_TRIAL, KeymastersKeepLocations.THE_SECRET_VAULT_COMPLETE, KeymastersKeepTags.TRIALS_THE_SECRET_VAULT),
    (KeymastersKeepRegions.THE_SHADOWED_PORTAL, KeymastersKeepLocations.THE_SHADOWED_PORTAL_TRIAL, KeymastersKeepLocations.THE_SHADOWED_PORTAL_COMPLETE, KeymastersKeepTags.TRIALS_THE_SHADOWED_PORTAL),
    (KeymastersKeepRegions.THE_SHADOWED_THRESHOLD, KeymastersKeepLocations.THE_SHADOWED_THRESHOLD_TRIAL, KeymastersKeepLocations.THE_SHADOWED_THRESHOLD_COMPLETE, KeymastersKeepTags.TRIALS_THE_SHADOWED_THRESHOLD),
    (KeymastersKeepRegions.THE_SHADOWY_PASSAGE, KeymastersKeepLocations.THE_SHADOWY_PASSAGE_TRIAL, KeymastersKeepLocations.THE_SHADOWY_PASSAGE_COMPLETE, KeymastersKeepTags.TRIALS_THE_SHADOWY_PASSAGE),
    (KeymastersKeepRegions.THE_SHIMMERING_PASSAGE, KeymastersKeepLocations.THE_SHIMMERING_PASSAGE_TRIAL, KeymastersKeepLocations.THE_SHIMMERING_PASSAGE_COMPLETE, KeymastersKeepTags.TRIALS_THE_SHIMMERING_PASSAGE),
    (KeymastersKeepRegions.THE_SHROUDED_GATEWAY, KeymastersKeepLocations.THE_SHROUDED_GATEWAY_TRIAL, KeymastersKeepLocations.THE_SHROUDED_GATEWAY_COMPLETE, KeymastersKeepTags.TRIALS_THE_SHROUDED_GATEWAY),
    (KeymastersKeepRegions.THE_SHROUDED_PORTAL, KeymastersKeepLocations.THE_SHROUDED_PORTAL_TRIAL, KeymastersKeepLocations.THE_SHROUDED_PORTAL_COMPLETE, KeymastersKeepTags.TRIALS_THE_SHROUDED_PORTAL),
    (KeymastersKeepRegions.THE_SILENT_ARCHWAY, KeymastersKeepLocations.THE_SILENT_ARCHWAY_TRIAL, KeymastersKeepLocations.THE_SILENT_ARCHWAY_COMPLETE, KeymastersKeepTags.TRIALS_THE_SILENT_ARCHWAY),
    (KeymastersKeepRegions.THE_SILENT_PASSAGE, KeymastersKeepLocations.THE_SILENT_PASSAGE_TRIAL, KeymastersKeepLocations.THE_SILENT_PASSAGE_COMPLETE, KeymastersKeepTags.TRIALS_THE_SILENT_PASSAGE),
    (KeymastersKeepRegions.THE_SILENT_THRESHOLD, KeymastersKeepLocations.THE_SILENT_THRESHOLD_TRIAL, KeymastersKeepLocations.THE_SILENT_THRESHOLD_COMPLETE, KeymastersKeepTags.TRIALS_THE_SILENT_THRESHOLD),
    (KeymastersKeepRegions.THE_SILENT_VAULT, KeymastersKeepLocations.THE_SILENT_VAULT_TRIAL, KeymastersKeepLocations.THE_SILENT_VAULT_COMPLETE, KeymastersKeepTags.TRIALS_THE_SILENT_VAULT),
    (KeymastersKeepRegions.THE_UNFATHOMABLE_DOOR, KeymastersKeepLocations.THE_UNFATHOMABLE_DOOR_TRIAL, KeymastersKeepLocations.THE_UNFATHOMABLE_DOOR_COMPLETE, KeymastersKeepTags.TRIALS_THE_UNFATHOMABLE_DOOR),
    (KeymastersKeepRegions.THE_UNKNOWN_ARCH, KeymastersKeepLocations.THE_UNKNOWN_ARCH_TRIAL, KeymastersKeepLocations.THE_UNKNOWN_ARCH_COMPLETE, KeymastersKeepTags.TRIALS_THE_UNKNOWN_ARCH),
    (KeymastersKeepRegions.THE_UNKNOWN_GATEWAY, KeymastersKeepLocations.THE_UNKNOWN_GATEWAY_TRIAL, KeymastersKeepLocations.THE_UNKNOWN_GATEWAY_COMPLETE, KeymastersKeepTags.TRIALS_THE_UNKNOWN_GATEWAY),
    (KeymastersKeepRegions.THE_UNMARKED_PASSAGE, KeymastersKeepLocations.THE_UNMARKED_PASSAGE_TRIAL, KeymastersKeepLocations.THE_UNMARKED_PASSAGE_COMPLETE, KeymastersKeepTags.TRIALS_THE_UNMARKED_PASSAGE),
    (KeymastersKeepRegions.THE_UNMARKED_VAULT, KeymastersKeepLocations.THE_UNMARKED_VAULT_TRIAL, KeymastersKeepLocations.THE_UNMARKED_VAULT_COMPLETE, KeymastersKeepTags.TRIALS_THE_UNMARKED_VAULT),
    (KeymastersKeepRegions.THE_UNRAVELED_DOOR, KeymastersKeepLocations.THE_UNRAVELED_DOOR_TRIAL, KeymastersKeepLocations.THE_UNRAVELED_DOOR_COMPLETE, KeymastersKeepTags.TRIALS_THE_UNRAVELED_DOOR),
    (KeymastersKeepRegions.THE_UNSEEN_ARCHWAY, KeymastersKeepLocations.THE_UNSEEN_ARCHWAY_TRIAL, KeymastersKeepLocations.THE_UNSEEN_ARCHWAY_COMPLETE, KeymastersKeepTags.TRIALS_THE_UNSEEN_ARCHWAY),
    (KeymastersKeepRegions.THE_UNSEEN_DOOR, KeymastersKeepLocations.THE_UNSEEN_DOOR_TRIAL, KeymastersKeepLocations.THE_UNSEEN_DOOR_COMPLETE, KeymastersKeepTags.TRIALS_THE_UNSEEN_DOOR),
    (KeymastersKeepRegions.THE_UNSEEN_PASSAGE, KeymastersKeepLocations.THE_UNSEEN_PASSAGE_TRIAL, KeymastersKeepLocations.THE_UNSEEN_PASSAGE_COMPLETE, KeymastersKeepTags.TRIALS_THE_UNSEEN_PASSAGE),
    (KeymastersKeepRegions.THE_UNSEEN_PORTAL, KeymastersKeepLocations.THE_UNSEEN_PORTAL_TRIAL, KeymastersKeepLocations.THE_UNSEEN_PORTAL_COMPLETE, KeymastersKeepTags.TRIALS_THE_UNSEEN_PORTAL),
    (KeymastersKeepRegions.THE_UNSPOKEN_GATE, KeymastersKeepLocations.THE_UNSPOKEN_GATE_TRIAL, KeymastersKeepLocations.THE_UNSPOKEN_GATE_COMPLETE, KeymastersKeepTags.TRIALS_THE_UNSPOKEN_GATE),
    (KeymastersKeepRegions.THE_UNTOLD_GATEWAY, KeymastersKeepLocations.THE_UNTOLD_GATEWAY_TRIAL, KeymastersKeepLocations.THE_UNTOLD_GATEWAY_COMPLETE, KeymastersKeepTags.TRIALS_THE_UNTOLD_GATEWAY),
    (KeymastersKeepRegions.THE_UNTRACEABLE_PATH, KeymastersKeepLocations.THE_UNTRACEABLE_PATH_TRIAL, KeymastersKeepLocations.THE_UNTRACEABLE_PATH_COMPLETE, KeymastersKeepTags.TRIALS_THE_UNTRACEABLE_PATH),
    (KeymastersKeepRegions.THE_VANISHING_ARCHWAY, KeymastersKeepLocations.THE_VANISHING_ARCHWAY_TRIAL, KeymastersKeepLocations.THE_VANISHING_ARCHWAY_COMPLETE, KeymastersKeepTags.TRIALS_THE_VANISHING_ARCHWAY),
    (KeymastersKeepRegions.THE_VANISHING_DOOR, KeymastersKeepLocations.THE_VANISHING_DOOR_TRIAL, KeymastersKeepLocations.THE_VANISHING_DOOR_COMPLETE, KeymastersKeepTags.TRIALS_THE_VANISHING_DOOR),
    (KeymastersKeepRegions.THE_VAULT_OF_WHISPERS, KeymastersKeepLocations.THE_VAULT_OF_WHISPERS_TRIAL, KeymastersKeepLocations.THE_VAULT_OF_WHISPERS_COMPLETE, KeymastersKeepTags.TRIALS_THE_VAULT_OF_WHISPERS),
    (KeymastersKeepRegions.THE_VEILED_PASSAGE, KeymastersKeepLocations.THE_VEILED_PASSAGE_TRIAL, KeymastersKeepLocations.THE_VEILED_PASSAGE_COMPLETE, KeymastersKeepTags.TRIALS_THE_VEILED_PASSAGE),
    (KeymastersKeepRegions.THE_VEILED_PATH, KeymastersKeepLocations.THE_VEILED_PATH_TRIAL, KeymastersKeepLocations.THE_VEILED_PATH_COMPLETE, KeymastersKeepTags.TRIALS_THE_VEILED_PATH),
    (KeymastersKeepRegions.THE_WHISPERED_PORTAL, KeymastersKeepLocations.THE_WHISPERED_PORTAL_TRIAL, KeymastersKeepLocations.THE_WHISPERED_PORTAL_COMPLETE, KeymastersKeepTags.TRIALS_THE_WHISPERED_PORTAL),
    (KeymastersKeepRegions.THE_WHISPERED_THRESHOLD, KeymastersKeepLocations.THE_WHISPERED_THRESHOLD_TRIAL, KeymastersKeepLocations.THE_WHISPERED_THRESHOLD_COMPLETE, KeymastersKeepTags.TRIALS_THE_WHISPERED_THRESHOLD),
    (KeymastersKeepRegions.THE_WHISPERING_DOOR, KeymastersKeepLocations.THE_WHISPERING_DOOR_TRIAL, KeymastersKeepLocations.THE_WHISPERING_DOOR_COMPLETE, KeymastersKeepTags.TRIALS_THE_WHISPERING_DOOR),
]):
    location_data[trial_location] = list()

    i: int
    for i in range(trial_count):
        location_data[trial_location].append(
            KeymastersKeepLocationData(
                name=trial_location.value.replace("TRIAL_NAME", trials[i]),
                archipelago_id=1000 + (index * 100) + i,
                region=region,
                tags=(KeymastersKeepTags.TRIALS, trials_tag),
            )
        )
    location_data[completion_location] = KeymastersKeepLocationData(
        name=completion_location.value,
        archipelago_id=100000 + index,
        region=region,
        tags=(KeymastersKeepTags.COMPLETIONS, trials_tag),
    )

# Shop Items
location_data[KeymastersKeepLocations.SHOP_ABYSSFORGE_CURIOS_ITEM] = list()

i: int
for i in range(5):
    location_data[KeymastersKeepLocations.SHOP_ABYSSFORGE_CURIOS_ITEM].append(
        KeymastersKeepLocationData(
            name=KeymastersKeepLocations.SHOP_ABYSSFORGE_CURIOS_ITEM.value.replace("ITEM_NUMBER", str(i + 1)),
            archipelago_id=20000 + i,
            region=KeymastersKeepRegions.SHOP_ABYSSFORGE_CURIOS,
            tags=(KeymastersKeepTags.SHOP_ITEM, KeymastersKeepTags.SHOP_ABYSSFORGE_CURIOS),
        )
    )

location_data[KeymastersKeepLocations.SHOP_ARCANE_LANTERN_WORKSHOP_ITEM] = list()

i: int
for i in range(5):
    location_data[KeymastersKeepLocations.SHOP_ARCANE_LANTERN_WORKSHOP_ITEM].append(
        KeymastersKeepLocationData(
            name=KeymastersKeepLocations.SHOP_ARCANE_LANTERN_WORKSHOP_ITEM.value.replace("ITEM_NUMBER", str(i + 1)),
            archipelago_id=20100 + i,
            region=KeymastersKeepRegions.SHOP_ARCANE_LANTERN_WORKSHOP,
            tags=(KeymastersKeepTags.SHOP_ITEM, KeymastersKeepTags.SHOP_ARCANE_LANTERN_WORKSHOP),
        )
    )

location_data[KeymastersKeepLocations.SHOP_ASTRAL_ECHO_ATELIER_ITEM] = list()

i: int
for i in range(5):
    location_data[KeymastersKeepLocations.SHOP_ASTRAL_ECHO_ATELIER_ITEM].append(
        KeymastersKeepLocationData(
            name=KeymastersKeepLocations.SHOP_ASTRAL_ECHO_ATELIER_ITEM.value.replace("ITEM_NUMBER", str(i + 1)),
            archipelago_id=20200 + i,
            region=KeymastersKeepRegions.SHOP_ASTRAL_ECHO_ATELIER,
            tags=(KeymastersKeepTags.SHOP_ITEM, KeymastersKeepTags.SHOP_ASTRAL_ECHO_ATELIER),
        )
    )

location_data[KeymastersKeepLocations.SHOP_ASTRALGLOW_COLLECTION_ITEM] = list()

i: int
for i in range(5):
    location_data[KeymastersKeepLocations.SHOP_ASTRALGLOW_COLLECTION_ITEM].append(
        KeymastersKeepLocationData(
            name=KeymastersKeepLocations.SHOP_ASTRALGLOW_COLLECTION_ITEM.value.replace("ITEM_NUMBER", str(i + 1)),
            archipelago_id=20300 + i,
            region=KeymastersKeepRegions.SHOP_ASTRALGLOW_COLLECTION,
            tags=(KeymastersKeepTags.SHOP_ITEM, KeymastersKeepTags.SHOP_ASTRALGLOW_COLLECTION),
        )
    )

location_data[KeymastersKeepLocations.SHOP_ASTRALHELM_ARMORY_ITEM] = list()

i: int
for i in range(5):
    location_data[KeymastersKeepLocations.SHOP_ASTRALHELM_ARMORY_ITEM].append(
        KeymastersKeepLocationData(
            name=KeymastersKeepLocations.SHOP_ASTRALHELM_ARMORY_ITEM.value.replace("ITEM_NUMBER", str(i + 1)),
            archipelago_id=20400 + i,
            region=KeymastersKeepRegions.SHOP_ASTRALHELM_ARMORY,
            tags=(KeymastersKeepTags.SHOP_ITEM, KeymastersKeepTags.SHOP_ASTRALHELM_ARMORY),
        )
    )

location_data[KeymastersKeepLocations.SHOP_BLOODROSE_ATELIER_ITEM] = list()

i: int
for i in range(5):
    location_data[KeymastersKeepLocations.SHOP_BLOODROSE_ATELIER_ITEM].append(
        KeymastersKeepLocationData(
            name=KeymastersKeepLocations.SHOP_BLOODROSE_ATELIER_ITEM.value.replace("ITEM_NUMBER", str(i + 1)),
            archipelago_id=20500 + i,
            region=KeymastersKeepRegions.SHOP_BLOODROSE_ATELIER,
            tags=(KeymastersKeepTags.SHOP_ITEM, KeymastersKeepTags.SHOP_BLOODROSE_ATELIER),
        )
    )

location_data[KeymastersKeepLocations.SHOP_CELESTIAL_CODEX_CURIOS_ITEM] = list()

i: int
for i in range(5):
    location_data[KeymastersKeepLocations.SHOP_CELESTIAL_CODEX_CURIOS_ITEM].append(
        KeymastersKeepLocationData(
            name=KeymastersKeepLocations.SHOP_CELESTIAL_CODEX_CURIOS_ITEM.value.replace("ITEM_NUMBER", str(i + 1)),
            archipelago_id=20600 + i,
            region=KeymastersKeepRegions.SHOP_CELESTIAL_CODEX_CURIOS,
            tags=(KeymastersKeepTags.SHOP_ITEM, KeymastersKeepTags.SHOP_CELESTIAL_CODEX_CURIOS),
        )
    )

location_data[KeymastersKeepLocations.SHOP_DAWNSHARD_DEPOT_ITEM] = list()

i: int
for i in range(5):
    location_data[KeymastersKeepLocations.SHOP_DAWNSHARD_DEPOT_ITEM].append(
        KeymastersKeepLocationData(
            name=KeymastersKeepLocations.SHOP_DAWNSHARD_DEPOT_ITEM.value.replace("ITEM_NUMBER", str(i + 1)),
            archipelago_id=20700 + i,
            region=KeymastersKeepRegions.SHOP_DAWNSHARD_DEPOT,
            tags=(KeymastersKeepTags.SHOP_ITEM, KeymastersKeepTags.SHOP_DAWNSHARD_DEPOT),
        )
    )

location_data[KeymastersKeepLocations.SHOP_DRAGONBONE_BAZAAR_ITEM] = list()

i: int
for i in range(5):
    location_data[KeymastersKeepLocations.SHOP_DRAGONBONE_BAZAAR_ITEM].append(
        KeymastersKeepLocationData(
            name=KeymastersKeepLocations.SHOP_DRAGONBONE_BAZAAR_ITEM.value.replace("ITEM_NUMBER", str(i + 1)),
            archipelago_id=20800 + i,
            region=KeymastersKeepRegions.SHOP_DRAGONBONE_BAZAAR,
            tags=(KeymastersKeepTags.SHOP_ITEM, KeymastersKeepTags.SHOP_DRAGONBONE_BAZAAR),
        )
    )

location_data[KeymastersKeepLocations.SHOP_DREAMSHARD_COLLECTION_ITEM] = list()

i: int
for i in range(5):
    location_data[KeymastersKeepLocations.SHOP_DREAMSHARD_COLLECTION_ITEM].append(
        KeymastersKeepLocationData(
            name=KeymastersKeepLocations.SHOP_DREAMSHARD_COLLECTION_ITEM.value.replace("ITEM_NUMBER", str(i + 1)),
            archipelago_id=20900 + i,
            region=KeymastersKeepRegions.SHOP_DREAMSHARD_COLLECTION,
            tags=(KeymastersKeepTags.SHOP_ITEM, KeymastersKeepTags.SHOP_DREAMSHARD_COLLECTION),
        )
    )

location_data[KeymastersKeepLocations.SHOP_DREAMLIGHT_DEPOT_ITEM] = list()

i: int
for i in range(5):
    location_data[KeymastersKeepLocations.SHOP_DREAMLIGHT_DEPOT_ITEM].append(
        KeymastersKeepLocationData(
            name=KeymastersKeepLocations.SHOP_DREAMLIGHT_DEPOT_ITEM.value.replace("ITEM_NUMBER", str(i + 1)),
            archipelago_id=21000 + i,
            region=KeymastersKeepRegions.SHOP_DREAMLIGHT_DEPOT,
            tags=(KeymastersKeepTags.SHOP_ITEM, KeymastersKeepTags.SHOP_DREAMLIGHT_DEPOT),
        )
    )

location_data[KeymastersKeepLocations.SHOP_ECHOCHIME_PARLOR_ITEM] = list()

i: int
for i in range(5):
    location_data[KeymastersKeepLocations.SHOP_ECHOCHIME_PARLOR_ITEM].append(
        KeymastersKeepLocationData(
            name=KeymastersKeepLocations.SHOP_ECHOCHIME_PARLOR_ITEM.value.replace("ITEM_NUMBER", str(i + 1)),
            archipelago_id=21100 + i,
            region=KeymastersKeepRegions.SHOP_ECHOCHIME_PARLOR,
            tags=(KeymastersKeepTags.SHOP_ITEM, KeymastersKeepTags.SHOP_ECHOCHIME_PARLOR),
        )
    )

location_data[KeymastersKeepLocations.SHOP_ECLIPSEGEAR_EMPORIUM_ITEM] = list()

i: int
for i in range(5):
    location_data[KeymastersKeepLocations.SHOP_ECLIPSEGEAR_EMPORIUM_ITEM].append(
        KeymastersKeepLocationData(
            name=KeymastersKeepLocations.SHOP_ECLIPSEGEAR_EMPORIUM_ITEM.value.replace("ITEM_NUMBER", str(i + 1)),
            archipelago_id=21200 + i,
            region=KeymastersKeepRegions.SHOP_ECLIPSEGEAR_EMPORIUM,
            tags=(KeymastersKeepTags.SHOP_ITEM, KeymastersKeepTags.SHOP_ECLIPSEGEAR_EMPORIUM),
        )
    )

location_data[KeymastersKeepLocations.SHOP_EMBERHEART_FORGE_AND_FINDS_ITEM] = list()

i: int
for i in range(5):
    location_data[KeymastersKeepLocations.SHOP_EMBERHEART_FORGE_AND_FINDS_ITEM].append(
        KeymastersKeepLocationData(
            name=KeymastersKeepLocations.SHOP_EMBERHEART_FORGE_AND_FINDS_ITEM.value.replace("ITEM_NUMBER", str(i + 1)),
            archipelago_id=21300 + i,
            region=KeymastersKeepRegions.SHOP_EMBERHEART_FORGE_AND_FINDS,
            tags=(KeymastersKeepTags.SHOP_ITEM, KeymastersKeepTags.SHOP_EMBERHEART_FORGE_AND_FINDS),
        )
    )

location_data[KeymastersKeepLocations.SHOP_EMBERWING_EMPORIUM_ITEM] = list()

i: int
for i in range(5):
    location_data[KeymastersKeepLocations.SHOP_EMBERWING_EMPORIUM_ITEM].append(
        KeymastersKeepLocationData(
            name=KeymastersKeepLocations.SHOP_EMBERWING_EMPORIUM_ITEM.value.replace("ITEM_NUMBER", str(i + 1)),
            archipelago_id=21400 + i,
            region=KeymastersKeepRegions.SHOP_EMBERWING_EMPORIUM,
            tags=(KeymastersKeepTags.SHOP_ITEM, KeymastersKeepTags.SHOP_EMBERWING_EMPORIUM),
        )
    )

location_data[KeymastersKeepLocations.SHOP_ETHERHOLLOW_COLLECTION_ITEM] = list()

i: int
for i in range(5):
    location_data[KeymastersKeepLocations.SHOP_ETHERHOLLOW_COLLECTION_ITEM].append(
        KeymastersKeepLocationData(
            name=KeymastersKeepLocations.SHOP_ETHERHOLLOW_COLLECTION_ITEM.value.replace("ITEM_NUMBER", str(i + 1)),
            archipelago_id=21500 + i,
            region=KeymastersKeepRegions.SHOP_ETHERHOLLOW_COLLECTION,
            tags=(KeymastersKeepTags.SHOP_ITEM, KeymastersKeepTags.SHOP_ETHERHOLLOW_COLLECTION),
        )
    )

location_data[KeymastersKeepLocations.SHOP_FIRESONG_FORGE_ITEM] = list()

i: int
for i in range(5):
    location_data[KeymastersKeepLocations.SHOP_FIRESONG_FORGE_ITEM].append(
        KeymastersKeepLocationData(
            name=KeymastersKeepLocations.SHOP_FIRESONG_FORGE_ITEM.value.replace("ITEM_NUMBER", str(i + 1)),
            archipelago_id=21600 + i,
            region=KeymastersKeepRegions.SHOP_FIRESONG_FORGE,
            tags=(KeymastersKeepTags.SHOP_ITEM, KeymastersKeepTags.SHOP_FIRESONG_FORGE),
        )
    )

location_data[KeymastersKeepLocations.SHOP_FROSTLIGHT_CABINET_ITEM] = list()

i: int
for i in range(5):
    location_data[KeymastersKeepLocations.SHOP_FROSTLIGHT_CABINET_ITEM].append(
        KeymastersKeepLocationData(
            name=KeymastersKeepLocations.SHOP_FROSTLIGHT_CABINET_ITEM.value.replace("ITEM_NUMBER", str(i + 1)),
            archipelago_id=21700 + i,
            region=KeymastersKeepRegions.SHOP_FROSTLIGHT_CABINET,
            tags=(KeymastersKeepTags.SHOP_ITEM, KeymastersKeepTags.SHOP_FROSTLIGHT_CABINET),
        )
    )

location_data[KeymastersKeepLocations.SHOP_FROSTWIND_FRONTIER_ITEM] = list()

i: int
for i in range(5):
    location_data[KeymastersKeepLocations.SHOP_FROSTWIND_FRONTIER_ITEM].append(
        KeymastersKeepLocationData(
            name=KeymastersKeepLocations.SHOP_FROSTWIND_FRONTIER_ITEM.value.replace("ITEM_NUMBER", str(i + 1)),
            archipelago_id=21800 + i,
            region=KeymastersKeepRegions.SHOP_FROSTWIND_FRONTIER,
            tags=(KeymastersKeepTags.SHOP_ITEM, KeymastersKeepTags.SHOP_FROSTWIND_FRONTIER),
        )
    )

location_data[KeymastersKeepLocations.SHOP_IRONBLOOM_BAZAAR_ITEM] = list()

i: int
for i in range(5):
    location_data[KeymastersKeepLocations.SHOP_IRONBLOOM_BAZAAR_ITEM].append(
        KeymastersKeepLocationData(
            name=KeymastersKeepLocations.SHOP_IRONBLOOM_BAZAAR_ITEM.value.replace("ITEM_NUMBER", str(i + 1)),
            archipelago_id=21900 + i,
            region=KeymastersKeepRegions.SHOP_IRONBLOOM_BAZAAR,
            tags=(KeymastersKeepTags.SHOP_ITEM, KeymastersKeepTags.SHOP_IRONBLOOM_BAZAAR),
        )
    )

location_data[KeymastersKeepLocations.SHOP_IRONSHARD_ARMORY_ITEM] = list()

i: int
for i in range(5):
    location_data[KeymastersKeepLocations.SHOP_IRONSHARD_ARMORY_ITEM].append(
        KeymastersKeepLocationData(
            name=KeymastersKeepLocations.SHOP_IRONSHARD_ARMORY_ITEM.value.replace("ITEM_NUMBER", str(i + 1)),
            archipelago_id=22000 + i,
            region=KeymastersKeepRegions.SHOP_IRONSHARD_ARMORY,
            tags=(KeymastersKeepTags.SHOP_ITEM, KeymastersKeepTags.SHOP_IRONSHARD_ARMORY),
        )
    )

location_data[KeymastersKeepLocations.SHOP_LUMINSPIRE_WORKSHOP_ITEM] = list()

i: int
for i in range(5):
    location_data[KeymastersKeepLocations.SHOP_LUMINSPIRE_WORKSHOP_ITEM].append(
        KeymastersKeepLocationData(
            name=KeymastersKeepLocations.SHOP_LUMINSPIRE_WORKSHOP_ITEM.value.replace("ITEM_NUMBER", str(i + 1)),
            archipelago_id=22100 + i,
            region=KeymastersKeepRegions.SHOP_LUMINSPIRE_WORKSHOP,
            tags=(KeymastersKeepTags.SHOP_ITEM, KeymastersKeepTags.SHOP_LUMINSPIRE_WORKSHOP),
        )
    )

location_data[KeymastersKeepLocations.SHOP_MOONLIT_RELIQUARY_ITEM] = list()

i: int
for i in range(5):
    location_data[KeymastersKeepLocations.SHOP_MOONLIT_RELIQUARY_ITEM].append(
        KeymastersKeepLocationData(
            name=KeymastersKeepLocations.SHOP_MOONLIT_RELIQUARY_ITEM.value.replace("ITEM_NUMBER", str(i + 1)),
            archipelago_id=22200 + i,
            region=KeymastersKeepRegions.SHOP_MOONLIT_RELIQUARY,
            tags=(KeymastersKeepTags.SHOP_ITEM, KeymastersKeepTags.SHOP_MOONLIT_RELIQUARY),
        )
    )

location_data[KeymastersKeepLocations.SHOP_MOONREIGN_PARLOR_ITEM] = list()

i: int
for i in range(5):
    location_data[KeymastersKeepLocations.SHOP_MOONREIGN_PARLOR_ITEM].append(
        KeymastersKeepLocationData(
            name=KeymastersKeepLocations.SHOP_MOONREIGN_PARLOR_ITEM.value.replace("ITEM_NUMBER", str(i + 1)),
            archipelago_id=22300 + i,
            region=KeymastersKeepRegions.SHOP_MOONREIGN_PARLOR,
            tags=(KeymastersKeepTags.SHOP_ITEM, KeymastersKeepTags.SHOP_MOONREIGN_PARLOR),
        )
    )

location_data[KeymastersKeepLocations.SHOP_MOONSTONE_MARKET_ITEM] = list()

i: int
for i in range(5):
    location_data[KeymastersKeepLocations.SHOP_MOONSTONE_MARKET_ITEM].append(
        KeymastersKeepLocationData(
            name=KeymastersKeepLocations.SHOP_MOONSTONE_MARKET_ITEM.value.replace("ITEM_NUMBER", str(i + 1)),
            archipelago_id=22400 + i,
            region=KeymastersKeepRegions.SHOP_MOONSTONE_MARKET,
            tags=(KeymastersKeepTags.SHOP_ITEM, KeymastersKeepTags.SHOP_MOONSTONE_MARKET),
        )
    )

location_data[KeymastersKeepLocations.SHOP_MYTHRIL_MIRROR_MARKET_ITEM] = list()

i: int
for i in range(5):
    location_data[KeymastersKeepLocations.SHOP_MYTHRIL_MIRROR_MARKET_ITEM].append(
        KeymastersKeepLocationData(
            name=KeymastersKeepLocations.SHOP_MYTHRIL_MIRROR_MARKET_ITEM.value.replace("ITEM_NUMBER", str(i + 1)),
            archipelago_id=22500 + i,
            region=KeymastersKeepRegions.SHOP_MYTHRIL_MIRROR_MARKET,
            tags=(KeymastersKeepTags.SHOP_ITEM, KeymastersKeepTags.SHOP_MYTHRIL_MIRROR_MARKET),
        )
    )

location_data[KeymastersKeepLocations.SHOP_NETHERGLOW_WORKSHOP_ITEM] = list()

i: int
for i in range(5):
    location_data[KeymastersKeepLocations.SHOP_NETHERGLOW_WORKSHOP_ITEM].append(
        KeymastersKeepLocationData(
            name=KeymastersKeepLocations.SHOP_NETHERGLOW_WORKSHOP_ITEM.value.replace("ITEM_NUMBER", str(i + 1)),
            archipelago_id=22600 + i,
            region=KeymastersKeepRegions.SHOP_NETHERGLOW_WORKSHOP,
            tags=(KeymastersKeepTags.SHOP_ITEM, KeymastersKeepTags.SHOP_NETHERGLOW_WORKSHOP),
        )
    )

location_data[KeymastersKeepLocations.SHOP_NIGHTSPIRE_NOOK_ITEM] = list()

i: int
for i in range(5):
    location_data[KeymastersKeepLocations.SHOP_NIGHTSPIRE_NOOK_ITEM].append(
        KeymastersKeepLocationData(
            name=KeymastersKeepLocations.SHOP_NIGHTSPIRE_NOOK_ITEM.value.replace("ITEM_NUMBER", str(i + 1)),
            archipelago_id=22700 + i,
            region=KeymastersKeepRegions.SHOP_NIGHTSPIRE_NOOK,
            tags=(KeymastersKeepTags.SHOP_ITEM, KeymastersKeepTags.SHOP_NIGHTSPIRE_NOOK),
        )
    )

location_data[KeymastersKeepLocations.SHOP_OBSIDIANFLARE_OUTPOST_ITEM] = list()

i: int
for i in range(5):
    location_data[KeymastersKeepLocations.SHOP_OBSIDIANFLARE_OUTPOST_ITEM].append(
        KeymastersKeepLocationData(
            name=KeymastersKeepLocations.SHOP_OBSIDIANFLARE_OUTPOST_ITEM.value.replace("ITEM_NUMBER", str(i + 1)),
            archipelago_id=22800 + i,
            region=KeymastersKeepRegions.SHOP_OBSIDIANFLARE_OUTPOST,
            tags=(KeymastersKeepTags.SHOP_ITEM, KeymastersKeepTags.SHOP_OBSIDIANFLARE_OUTPOST),
        )
    )

location_data[KeymastersKeepLocations.SHOP_OPALINE_RELIQUARY_ITEM] = list()

i: int
for i in range(5):
    location_data[KeymastersKeepLocations.SHOP_OPALINE_RELIQUARY_ITEM].append(
        KeymastersKeepLocationData(
            name=KeymastersKeepLocations.SHOP_OPALINE_RELIQUARY_ITEM.value.replace("ITEM_NUMBER", str(i + 1)),
            archipelago_id=22900 + i,
            region=KeymastersKeepRegions.SHOP_OPALINE_RELIQUARY,
            tags=(KeymastersKeepTags.SHOP_ITEM, KeymastersKeepTags.SHOP_OPALINE_RELIQUARY),
        )
    )

location_data[KeymastersKeepLocations.SHOP_RADIANTCORE_GALLERY_ITEM] = list()

i: int
for i in range(5):
    location_data[KeymastersKeepLocations.SHOP_RADIANTCORE_GALLERY_ITEM].append(
        KeymastersKeepLocationData(
            name=KeymastersKeepLocations.SHOP_RADIANTCORE_GALLERY_ITEM.value.replace("ITEM_NUMBER", str(i + 1)),
            archipelago_id=23000 + i,
            region=KeymastersKeepRegions.SHOP_RADIANTCORE_GALLERY,
            tags=(KeymastersKeepTags.SHOP_ITEM, KeymastersKeepTags.SHOP_RADIANTCORE_GALLERY),
        )
    )

location_data[KeymastersKeepLocations.SHOP_RUNEBOUND_REPOSITORY_ITEM] = list()

i: int
for i in range(5):
    location_data[KeymastersKeepLocations.SHOP_RUNEBOUND_REPOSITORY_ITEM].append(
        KeymastersKeepLocationData(
            name=KeymastersKeepLocations.SHOP_RUNEBOUND_REPOSITORY_ITEM.value.replace("ITEM_NUMBER", str(i + 1)),
            archipelago_id=23100 + i,
            region=KeymastersKeepRegions.SHOP_RUNEBOUND_REPOSITORY,
            tags=(KeymastersKeepTags.SHOP_ITEM, KeymastersKeepTags.SHOP_RUNEBOUND_REPOSITORY),
        )
    )

location_data[KeymastersKeepLocations.SHOP_RUNEBROOK_EXCHANGE_ITEM] = list()

i: int
for i in range(5):
    location_data[KeymastersKeepLocations.SHOP_RUNEBROOK_EXCHANGE_ITEM].append(
        KeymastersKeepLocationData(
            name=KeymastersKeepLocations.SHOP_RUNEBROOK_EXCHANGE_ITEM.value.replace("ITEM_NUMBER", str(i + 1)),
            archipelago_id=23200 + i,
            region=KeymastersKeepRegions.SHOP_RUNEBROOK_EXCHANGE,
            tags=(KeymastersKeepTags.SHOP_ITEM, KeymastersKeepTags.SHOP_RUNEBROOK_EXCHANGE),
        )
    )

location_data[KeymastersKeepLocations.SHOP_RUNECROWN_BOUTIQUE_ITEM] = list()

i: int
for i in range(5):
    location_data[KeymastersKeepLocations.SHOP_RUNECROWN_BOUTIQUE_ITEM].append(
        KeymastersKeepLocationData(
            name=KeymastersKeepLocations.SHOP_RUNECROWN_BOUTIQUE_ITEM.value.replace("ITEM_NUMBER", str(i + 1)),
            archipelago_id=23300 + i,
            region=KeymastersKeepRegions.SHOP_RUNECROWN_BOUTIQUE,
            tags=(KeymastersKeepTags.SHOP_ITEM, KeymastersKeepTags.SHOP_RUNECROWN_BOUTIQUE),
        )
    )

location_data[KeymastersKeepLocations.SHOP_SHADEWOOD_TROVE_ITEM] = list()

i: int
for i in range(5):
    location_data[KeymastersKeepLocations.SHOP_SHADEWOOD_TROVE_ITEM].append(
        KeymastersKeepLocationData(
            name=KeymastersKeepLocations.SHOP_SHADEWOOD_TROVE_ITEM.value.replace("ITEM_NUMBER", str(i + 1)),
            archipelago_id=23400 + i,
            region=KeymastersKeepRegions.SHOP_SHADEWOOD_TROVE,
            tags=(KeymastersKeepTags.SHOP_ITEM, KeymastersKeepTags.SHOP_SHADEWOOD_TROVE),
        )
    )

location_data[KeymastersKeepLocations.SHOP_SHADOWMANTLE_MARKET_ITEM] = list()

i: int
for i in range(5):
    location_data[KeymastersKeepLocations.SHOP_SHADOWMANTLE_MARKET_ITEM].append(
        KeymastersKeepLocationData(
            name=KeymastersKeepLocations.SHOP_SHADOWMANTLE_MARKET_ITEM.value.replace("ITEM_NUMBER", str(i + 1)),
            archipelago_id=23500 + i,
            region=KeymastersKeepRegions.SHOP_SHADOWMANTLE_MARKET,
            tags=(KeymastersKeepTags.SHOP_ITEM, KeymastersKeepTags.SHOP_SHADOWMANTLE_MARKET),
        )
    )

location_data[KeymastersKeepLocations.SHOP_SHATTERSTONE_TROVE_ITEM] = list()

i: int
for i in range(5):
    location_data[KeymastersKeepLocations.SHOP_SHATTERSTONE_TROVE_ITEM].append(
        KeymastersKeepLocationData(
            name=KeymastersKeepLocations.SHOP_SHATTERSTONE_TROVE_ITEM.value.replace("ITEM_NUMBER", str(i + 1)),
            archipelago_id=23600 + i,
            region=KeymastersKeepRegions.SHOP_SHATTERSTONE_TROVE,
            tags=(KeymastersKeepTags.SHOP_ITEM, KeymastersKeepTags.SHOP_SHATTERSTONE_TROVE),
        )
    )

location_data[KeymastersKeepLocations.SHOP_SILVERDAWN_SUNDRIES_ITEM] = list()

i: int
for i in range(5):
    location_data[KeymastersKeepLocations.SHOP_SILVERDAWN_SUNDRIES_ITEM].append(
        KeymastersKeepLocationData(
            name=KeymastersKeepLocations.SHOP_SILVERDAWN_SUNDRIES_ITEM.value.replace("ITEM_NUMBER", str(i + 1)),
            archipelago_id=23700 + i,
            region=KeymastersKeepRegions.SHOP_SILVERDAWN_SUNDRIES,
            tags=(KeymastersKeepTags.SHOP_ITEM, KeymastersKeepTags.SHOP_SILVERDAWN_SUNDRIES),
        )
    )

location_data[KeymastersKeepLocations.SHOP_SILVERQUARTZ_EXCHANGE_ITEM] = list()

i: int
for i in range(5):
    location_data[KeymastersKeepLocations.SHOP_SILVERQUARTZ_EXCHANGE_ITEM].append(
        KeymastersKeepLocationData(
            name=KeymastersKeepLocations.SHOP_SILVERQUARTZ_EXCHANGE_ITEM.value.replace("ITEM_NUMBER", str(i + 1)),
            archipelago_id=23800 + i,
            region=KeymastersKeepRegions.SHOP_SILVERQUARTZ_EXCHANGE,
            tags=(KeymastersKeepTags.SHOP_ITEM, KeymastersKeepTags.SHOP_SILVERQUARTZ_EXCHANGE),
        )
    )

location_data[KeymastersKeepLocations.SHOP_SPIRITCHIME_BOUTIQUE_ITEM] = list()

i: int
for i in range(5):
    location_data[KeymastersKeepLocations.SHOP_SPIRITCHIME_BOUTIQUE_ITEM].append(
        KeymastersKeepLocationData(
            name=KeymastersKeepLocations.SHOP_SPIRITCHIME_BOUTIQUE_ITEM.value.replace("ITEM_NUMBER", str(i + 1)),
            archipelago_id=23900 + i,
            region=KeymastersKeepRegions.SHOP_SPIRITCHIME_BOUTIQUE,
            tags=(KeymastersKeepTags.SHOP_ITEM, KeymastersKeepTags.SHOP_SPIRITCHIME_BOUTIQUE),
        )
    )

location_data[KeymastersKeepLocations.SHOP_STARBOUND_STUDIO_ITEM] = list()

i: int
for i in range(5):
    location_data[KeymastersKeepLocations.SHOP_STARBOUND_STUDIO_ITEM].append(
        KeymastersKeepLocationData(
            name=KeymastersKeepLocations.SHOP_STARBOUND_STUDIO_ITEM.value.replace("ITEM_NUMBER", str(i + 1)),
            archipelago_id=24000 + i,
            region=KeymastersKeepRegions.SHOP_STARBOUND_STUDIO,
            tags=(KeymastersKeepTags.SHOP_ITEM, KeymastersKeepTags.SHOP_STARBOUND_STUDIO),
        )
    )

location_data[KeymastersKeepLocations.SHOP_STARROOT_REPOSITORY_ITEM] = list()

i: int
for i in range(5):
    location_data[KeymastersKeepLocations.SHOP_STARROOT_REPOSITORY_ITEM].append(
        KeymastersKeepLocationData(
            name=KeymastersKeepLocations.SHOP_STARROOT_REPOSITORY_ITEM.value.replace("ITEM_NUMBER", str(i + 1)),
            archipelago_id=24100 + i,
            region=KeymastersKeepRegions.SHOP_STARROOT_REPOSITORY,
            tags=(KeymastersKeepTags.SHOP_ITEM, KeymastersKeepTags.SHOP_STARROOT_REPOSITORY),
        )
    )

location_data[KeymastersKeepLocations.SHOP_STARWEAVE_ARMORY_ITEM] = list()

i: int
for i in range(5):
    location_data[KeymastersKeepLocations.SHOP_STARWEAVE_ARMORY_ITEM].append(
        KeymastersKeepLocationData(
            name=KeymastersKeepLocations.SHOP_STARWEAVE_ARMORY_ITEM.value.replace("ITEM_NUMBER", str(i + 1)),
            archipelago_id=24200 + i,
            region=KeymastersKeepRegions.SHOP_STARWEAVE_ARMORY,
            tags=(KeymastersKeepTags.SHOP_ITEM, KeymastersKeepTags.SHOP_STARWEAVE_ARMORY),
        )
    )

location_data[KeymastersKeepLocations.SHOP_STORMHOLLOW_GEARWORKS_ITEM] = list()

i: int
for i in range(5):
    location_data[KeymastersKeepLocations.SHOP_STORMHOLLOW_GEARWORKS_ITEM].append(
        KeymastersKeepLocationData(
            name=KeymastersKeepLocations.SHOP_STORMHOLLOW_GEARWORKS_ITEM.value.replace("ITEM_NUMBER", str(i + 1)),
            archipelago_id=24300 + i,
            region=KeymastersKeepRegions.SHOP_STORMHOLLOW_GEARWORKS,
            tags=(KeymastersKeepTags.SHOP_ITEM, KeymastersKeepTags.SHOP_STORMHOLLOW_GEARWORKS),
        )
    )

location_data[KeymastersKeepLocations.SHOP_SUNFORGE_SUNDRIES_ITEM] = list()

i: int
for i in range(5):
    location_data[KeymastersKeepLocations.SHOP_SUNFORGE_SUNDRIES_ITEM].append(
        KeymastersKeepLocationData(
            name=KeymastersKeepLocations.SHOP_SUNFORGE_SUNDRIES_ITEM.value.replace("ITEM_NUMBER", str(i + 1)),
            archipelago_id=24400 + i,
            region=KeymastersKeepRegions.SHOP_SUNFORGE_SUNDRIES,
            tags=(KeymastersKeepTags.SHOP_ITEM, KeymastersKeepTags.SHOP_SUNFORGE_SUNDRIES),
        )
    )

location_data[KeymastersKeepLocations.SHOP_THORNBLOOM_CRAFTWORKS_ITEM] = list()

i: int
for i in range(5):
    location_data[KeymastersKeepLocations.SHOP_THORNBLOOM_CRAFTWORKS_ITEM].append(
        KeymastersKeepLocationData(
            name=KeymastersKeepLocations.SHOP_THORNBLOOM_CRAFTWORKS_ITEM.value.replace("ITEM_NUMBER", str(i + 1)),
            archipelago_id=24500 + i,
            region=KeymastersKeepRegions.SHOP_THORNBLOOM_CRAFTWORKS,
            tags=(KeymastersKeepTags.SHOP_ITEM, KeymastersKeepTags.SHOP_THORNBLOOM_CRAFTWORKS),
        )
    )

location_data[KeymastersKeepLocations.SHOP_THORNVALE_WORKSHOP_ITEM] = list()

i: int
for i in range(5):
    location_data[KeymastersKeepLocations.SHOP_THORNVALE_WORKSHOP_ITEM].append(
        KeymastersKeepLocationData(
            name=KeymastersKeepLocations.SHOP_THORNVALE_WORKSHOP_ITEM.value.replace("ITEM_NUMBER", str(i + 1)),
            archipelago_id=24600 + i,
            region=KeymastersKeepRegions.SHOP_THORNVALE_WORKSHOP,
            tags=(KeymastersKeepTags.SHOP_ITEM, KeymastersKeepTags.SHOP_THORNVALE_WORKSHOP),
        )
    )

location_data[KeymastersKeepLocations.SHOP_THUNDERSHARD_TROVE_ITEM] = list()

i: int
for i in range(5):
    location_data[KeymastersKeepLocations.SHOP_THUNDERSHARD_TROVE_ITEM].append(
        KeymastersKeepLocationData(
            name=KeymastersKeepLocations.SHOP_THUNDERSHARD_TROVE_ITEM.value.replace("ITEM_NUMBER", str(i + 1)),
            archipelago_id=24700 + i,
            region=KeymastersKeepRegions.SHOP_THUNDERSHARD_TROVE,
            tags=(KeymastersKeepTags.SHOP_ITEM, KeymastersKeepTags.SHOP_THUNDERSHARD_TROVE),
        )
    )

location_data[KeymastersKeepLocations.SHOP_VINEWHISPER_VAULT_ITEM] = list()

i: int
for i in range(5):
    location_data[KeymastersKeepLocations.SHOP_VINEWHISPER_VAULT_ITEM].append(
        KeymastersKeepLocationData(
            name=KeymastersKeepLocations.SHOP_VINEWHISPER_VAULT_ITEM.value.replace("ITEM_NUMBER", str(i + 1)),
            archipelago_id=24800 + i,
            region=KeymastersKeepRegions.SHOP_VINEWHISPER_VAULT,
            tags=(KeymastersKeepTags.SHOP_ITEM, KeymastersKeepTags.SHOP_VINEWHISPER_VAULT),
        )
    )

location_data[KeymastersKeepLocations.SHOP_VOIDSPIRE_VAULT_ITEM] = list()

i: int
for i in range(5):
    location_data[KeymastersKeepLocations.SHOP_VOIDSPIRE_VAULT_ITEM].append(
        KeymastersKeepLocationData(
            name=KeymastersKeepLocations.SHOP_VOIDSPIRE_VAULT_ITEM.value.replace("ITEM_NUMBER", str(i + 1)),
            archipelago_id=24900 + i,
            region=KeymastersKeepRegions.SHOP_VOIDSPIRE_VAULT,
            tags=(KeymastersKeepTags.SHOP_ITEM, KeymastersKeepTags.SHOP_VOIDSPIRE_VAULT),
        )
    )

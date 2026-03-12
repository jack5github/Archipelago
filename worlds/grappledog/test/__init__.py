from typing import Any, ClassVar, Dict, Iterable, List, Mapping, Union

from BaseClasses import CollectionState, Entrance, Item, Location, Region

from test.bases import WorldTestBase
from test.general import gen_steps, setup_multiworld
from test.multiworld.test_multiworlds import MultiworldTestBase

from .. import GrappleDogWorld
from .. import options as ops


class GrappleDogTestBase(WorldTestBase):
    game = "GrappleDog"
    world: GrappleDogWorld


class TestLevelLockedBosses(GrappleDogTestBase):
    options: dict[str, Any] = {
        "boss_level_unlock": ops.BossLevelUnlock.option_level
    }

    def test_optional_gems_are_filler(self) -> None:
        self.world_setup()
        gems: list[Item] = self.get_items_by_name("Gem")
        self.assertGreaterEqual(len(gems), 1)
        for gem in gems:
            self.assertFalse(gem.advancement)
            self.assertTrue(gem.filler)


if __name__ == "__main__":
    import unittest

    unittest.main()

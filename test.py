import unittest
from core.item import *
from core.cha


class Test(unittest.TestCase):
  

    def test_item(self):
        item = RoomItems("Magic Potion", "Boosts player abilities")
        self.assertEqual(item.name, "Magic Potion")
        self.assertEqual(item.description, "Boosts player abilities")

    def test_character(self):
        character = Character(
            "Jordan", 55, 45, 40, "Agile player with high speed and power"
        )

        self.assertEqual(character.name, "Jordan")
        self.assertEqual(character.health, 55)
        self.assertEqual(character.power, 45)
        self.assertEqual(character.defence, 40)
        self.assertEqual(
            character.about_character, "Agile player with high speed and power"
        )


if __name__ == "__main__":
    unittest.main()



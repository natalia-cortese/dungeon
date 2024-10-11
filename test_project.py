import unittest
from project import Player, Enemy, find_treasure


class TestGameFunctions(unittest.TestCase):
    """
    Let's do some testing
    """
    def setUp(self):
        """Setup a player and an enemy for tests."""
        self.player = Player("Hero")
        self.enemy = Enemy("Goblin", health=30, strength=10)

    def test_player_attack(self):
        """Test if the player can attack."""
        damage = self.player.attack()
        self.assertTrue(5 <= damage <= 15, "Player attack damage should be between 5 and 15.")

    def test_enemy_attack(self):
        """Test if the enemy can attack."""
        damage = self.enemy.attack()
        self.assertTrue(self.enemy.strength - 5 <= damage <= self.enemy.strength, "Enemy attack damage should be within the expected range.")

    def test_player_take_damage(self):
        """Test if the player takes damage correctly."""
        initial_health = self.player.health
        self.player.take_damage(10)
        self.assertEqual(self.player.health, initial_health - 10, "Player's health should decrease by the damage taken.")

    def test_enemy_take_damage(self):
        """Test if the enemy takes damage correctly."""
        initial_health = self.enemy.health
        self.enemy.take_damage(15)
        self.assertEqual(self.enemy.health, initial_health - 15, "Enemy's health should decrease by the damage taken.")

    def test_find_treasure(self):
        """Test if finding treasure increases player's health."""
        initial_health = self.player.health
        find_treasure(self.player)
        self.assertGreater(self.player.health, initial_health, "Player's health should increase after finding treasure.")

    def test_player_alive(self):
        """Test if player status is alive."""
        self.assertTrue(self.player.is_alive(), "Player should be alive initially.")
        self.player.take_damage(100)  # Deal lethal damage
        self.assertFalse(self.player.is_alive(), "Player should not be alive after taking lethal damage.")

    def test_enemy_alive(self):
        """Test if enemy status is alive."""
        self.assertTrue(self.enemy.is_alive(), "Enemy should be alive initially.")
        self.enemy.take_damage(100)  # Deal lethal damage
        self.assertFalse(self.enemy.is_alive(), "Enemy should not be alive after taking lethal damage.")

if __name__ == '__main__':
    unittest.main()

import unittest
from core.board import Board

class TestBoard(unittest.TestCase):

    def setUp(self):
        self.board = Board()

    def test_initial_setup(self):
        # Jugador 1 tiene 15 fichas
        total_p1 = sum(len(p) for p in self.board._Board__points__ if p and p[0] == "player1")
        self.assertEqual(total_p1, 15)

        # Jugador 2 tiene 15 fichas
        total_p2 = sum(len(p) for p in self.board._Board__points__ if p and p[0] == "player2")
        self.assertEqual(total_p2, 15)

    def test_get_point_valid(self):
        # El punto 0 deberia tener 2 fichas de player1
        point = self.board.get_point(0)
        self.assertEqual(len(point), 2)
        self.assertTrue(all(p == "player1" for p in point))

    def test_get_point_invalid(self):
        # Indice fuera de rango debe levantar error
        with self.assertRaises(ValueError):
            self.board.get_point(30)

    def test_valid_move(self):
        # Mover ficha de player1 del punto 0 al punto 3
        moved = self.board.move_checker("player1", 0, 3)
        self.assertTrue(moved)
        self.assertIn("player1", self.board.get_point(3))

    def test_invalid_move_wrong_player(self):
        # Player2 no puede mover desde punto 0 porque solo hay fichas de player1
        moved = self.board.move_checker("player2", 0, 3)
        self.assertFalse(moved)

if __name__ == "__main__":
    unittest.main()


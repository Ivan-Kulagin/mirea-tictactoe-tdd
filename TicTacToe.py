import unittest


class Tictac:

    ST_OK = 0 # Игра не завершена
    
    def __init__(self, players=2, size=3):
        self.size = size
        self.players = players
        self.current_player = 0
        self.empty = set([(i % size, i // size) for i in range(size * size)])
        self.moves = [set([]) for player in range(players)]
        self.state = Tictac.ST_OK
        self.winner = None
    
    
class TictacTests(unittest.TestCase):

    def test_game_start_checks(self):
        # Начать новую игру
        t = Tictac()

        # Проверяет, что игровое поле 3х3 по умолчанию
        self.assertEqual(t.size, 3)
        # Проверяет, что в игре участвуют два игрока по умолчанию
        self.assertEqual(t.players, 2)
        # Проверить, что первый игрок - игрок 0
        self.assertEqual(t.current_player, 0)
        # Проверить, что все ячейки (3х3) пусты
        self.assertEqual(len(t.empty), 9)
        # Проверить, что ячейка (2, 2) пуста
        self.assertTrue((2, 2) in t.empty)
        # Проверить, что игроки ещё не делали ни одного хода
        self.assertEqual(t.moves, [set([]), set([])])
        # Проверить, что игра не завершена
        self.assertEqual(t.state, Tictac.ST_OK)
        # Проверить, что победитель отсутствует (т.е. это ничья)
        self.assertEqual(t.winner, None)

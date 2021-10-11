import unittest


class Tictac:

    ST_OK = 0 # Игра не завершена
    
    MV_OK = 0  # Корректный ход
    MV_BAD = 1  # Некорректный ход, выход за границы или не пустая клетка
    
    def __init__(self, players=2, size=3):
        self.size = size
        self.players = players
        self.current_player = 0
        self.empty = set([(i % size, i // size) for i in range(size * size)])
        self.moves = [set([]) for player in range(players)]
        self.state = Tictac.ST_OK
        self.winner = None

    def move(self, cell):
        # Проверить, что игра не завершена
        if self.state != Tictac.ST_OK:
            return Tictac.MV_GAMEOVER

        # Проверить, что ячейка пуста
        if cell not in self.empty:
            return Tictac.MV_BAD

        # Переместить ячейку из пустого набора в набор ходов конкретного игрока
        self.empty.remove(cell)
        self.moves[self.current_player].add(cell)

        # Проверяет победителя и завершает игру
        if self.check_winner(self.current_player):
            self.state = Tictac.ST_END
            self.winner = self.current_player
            # Завершить ход
            return Tictac.MV_OK

        # Если нет победителя, проверяем ничью
        if not self.empty:
            # Это последний ход
            self.state = Tictac.ST_END
            return Tictac.MV_OK

        # Переключиться на следующего игрока
        self.current_player = self.next_player(self.current_player)

        return Tictac.MV_OK
    
    def next_player(self, player):
        # Переход к следующему игроку
        return (player + 1) % self.players

    
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

    def test_make_a_move(self):
        # Начать новую игру
        t = Tictac()
        # Первый ход, ячейка (0, 0)
        cell = (0, 0)

        # Проверить, что результат хода успешен
        self.assertEqual(t.move(cell), Tictac.MV_OK)

        # Проверить, что эта ячейка больше не пуста
        self.assertTrue(cell not in t.empty)
        # Проверить, что ячейка находится в наборе ходов игрока 0
        self.assertTrue(cell in t.moves[0])
        # Проверить, что текущий игрок - игрок 1
        self.assertEqual(t.current_player, 1)
        # Проверить, что результат хода в ту же ячейку вернёт ошибку
        self.assertEqual(t.move(cell), Tictac.MV_BAD)
        
    def test_next_player_helping_function(self):
        # Начать новую игру с тремя игроками
        t = Tictac(players=3)

        # Проверить, что следующий после игрока 0 - игрок 1
        self.assertEqual(t.next_player(0), 1)
        # Проверить, что следующий после игрока 2 - игрок 0
        self.assertEqual(t.next_player(2), 0)
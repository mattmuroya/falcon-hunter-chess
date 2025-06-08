import unittest
from ChessVar import ChessVar, ChessPiece


class TestGradescope(unittest.TestCase):
    """ChessVar unit tests from Gradescope."""
    def test_basic(self):
        """Tests game, pawn moves, game state."""
        game = ChessVar()

        self.assertFalse(game.make_move("e7", "e5"))
        self.assertFalse(game.make_move("a2", "a5"))

        self.assertTrue(game.make_move("a2", "a4"))

        self.assertFalse(game.make_move("b2", "b4"))
        self.assertTrue(game.make_move("a7", "a6"))

        self.assertEqual(game.get_game_state(), "UNFINISHED")

    def test_pawn(self):
        """Tests basic pawn movement."""
        game = ChessVar()

        self.assertTrue(game.make_move("a2", "a4"))
        self.assertTrue(game.make_move("a7", "a6"))
        self.assertTrue(game.make_move("a4", "a5"))


        self.assertFalse(game.make_move("a6", "a5"))
        self.assertFalse(game.make_move("a6", "b5"))
        self.assertFalse(game.make_move("a6", "b6"))
        self.assertFalse(game.make_move("a6", "a7"))

        self.assertTrue(game.make_move("b7", "b6"))
        self.assertTrue(game.make_move("a5", "b6"))

        self.assertEqual(game.get_game_state(), "UNFINISHED")

    def test_rook_pawn(self):
        """Tests basic pawn and rook movement."""
        game = ChessVar()

        self.assertTrue(game.make_move("a2", "a4"))
        self.assertTrue(game.make_move("h7", "h5"))

        self.assertFalse(game.make_move("a1", "a5"))

        self.assertTrue(game.make_move("a1", "a3"))

        self.assertFalse(game.make_move("h8", "f6"))
        self.assertFalse(game.make_move("h8", "g6"))
        self.assertFalse(game.make_move("h8", "h9"))

        self.assertTrue(game.make_move("h8", "h6"))
        self.assertTrue(game.make_move("a3", "e3"))
        self.assertTrue(game.make_move("h6", "h7"))
        self.assertTrue(game.make_move("e3", "e5"))

        self.assertFalse(game.make_move("e7", "e5"))

        self.assertTrue(game.make_move("e7", "e6"))
        self.assertTrue(game.make_move("h2", "h4"))

        self.assertFalse(game.make_move("h7", "h5"))

        self.assertTrue(game.make_move("h7", "h6"))

        self.assertFalse(game.make_move("h4", "h5"))

        self.assertTrue(game.make_move("h1", "h3"))

        self.assertFalse(game.make_move("h6", "e6"))

        self.assertEqual(game.get_game_state(), "UNFINISHED")

    def test_knight(self):
        """Tests basic knight movement."""
        game = ChessVar()

        self.assertTrue(game.make_move("b1", "c3"))
        self.assertTrue(game.make_move("g8", "h6"))

        self.assertFalse(game.make_move("c3", "a5"))

        self.assertTrue(game.make_move("c3", "b5"))
        self.assertTrue(game.make_move("h6", "f5"))

        self.assertFalse(game.make_move("b5", "b7"))

        self.assertTrue(game.make_move("b5", "c7"))
        self.assertTrue(game.make_move("f5", "d6"))

        self.assertEqual(game.get_game_state(), "UNFINISHED")

    def test_bishop(self):
        """Tests basic bishop movement."""
        game = ChessVar()

        self.assertTrue(game.make_move("d2", "d4"))
        self.assertTrue(game.make_move("e7", "e5"))

        self.assertFalse(game.make_move("c1", "a3"))

        self.assertTrue(game.make_move("c1", "h6"))
        self.assertTrue(game.make_move("f8", "c5"))
        self.assertTrue(game.make_move("d4", "c5"))
        self.assertTrue(game.make_move("b7", "b5"))
        self.assertTrue(game.make_move("h6", "g7"))
        self.assertTrue(game.make_move("c8", "b7"))
        self.assertTrue(game.make_move("g2", "g3"))
        self.assertTrue(game.make_move("b7", "h1"))

        self.assertEqual(game.get_game_state(), "UNFINISHED")

    def test_queen(self):
        """Tests basic queen movement."""
        game = ChessVar()

        self.assertTrue(game.make_move("e2", "e4"))
        self.assertTrue(game.make_move("d7", "d5"))

        self.assertFalse(game.make_move("d1", "d4"))

        self.assertTrue(game.make_move("d1", "g4"))

        self.assertFalse(game.make_move("d8", "f6"))

        self.assertTrue(game.make_move("d8", "d6"))
        self.assertTrue(game.make_move("g4", "c8"))
        self.assertTrue(game.make_move("d6", "b4"))
        self.assertTrue(game.make_move("c8", "c7"))

        self.assertFalse(game.make_move("b4", "b1"))

        self.assertTrue(game.make_move("b4", "e4"))

        self.assertEqual(game.get_game_state(), "UNFINISHED")

    def test_king(self):
        """Tests basic king movement."""
        game = ChessVar()

        self.assertTrue(game.make_move("e2", "e4"))
        self.assertTrue(game.make_move("e7", "e5"))

        self.assertFalse(game.make_move("e1", "e3"))
        self.assertFalse(game.make_move("e1", "f1"))

        self.assertTrue(game.make_move("e1", "e2"))

        self.assertFalse(game.make_move("e8", "d7"))

        self.assertTrue(game.make_move("e8", "e7"))
        self.assertTrue(game.make_move("e2", "f3"))
        self.assertTrue(game.make_move("e7", "e8"))
        self.assertTrue(game.make_move("f3", "f4"))

        self.assertEqual(game.get_game_state(), "UNFINISHED")

    def test_black_win(self):
        """Tests black win."""
        game = ChessVar()

        self.assertTrue(game.make_move("e2", "e4"))
        self.assertTrue(game.make_move("e7", "e5"))

        self.assertFalse(game.make_move("e1", "e3"))
        self.assertFalse(game.make_move("e1", "f1"))

        self.assertTrue(game.make_move("e1", "e2"))

        self.assertFalse(game.make_move("e8", "d7"))

        self.assertTrue(game.make_move("e8", "e7"))
        self.assertTrue(game.make_move("e2", "f3"))
        self.assertTrue(game.make_move("e7", "e8"))
        self.assertTrue(game.make_move("f3", "f4"))
        self.assertTrue(game.make_move("e5", "f4"))

        self.assertEqual(game.get_game_state(), "BLACK_WON")

        self.assertFalse(game.make_move("a2", "a4"))
        self.assertEqual(game.get_current_player().get_color(), "black")

    def test_white_win(self):
        """Tests white win."""
        game = ChessVar()

        self.assertTrue(game.make_move("e2", "e4"))
        self.assertTrue(game.make_move("e7", "e5"))

        self.assertFalse(game.make_move("e1", "e3"))
        self.assertFalse(game.make_move("e1", "f1"))

        self.assertTrue(game.make_move("e1", "e2"))

        self.assertFalse(game.make_move("e8", "d7"))

        self.assertTrue(game.make_move("e8", "e7"))
        self.assertTrue(game.make_move("e2", "f3"))
        self.assertTrue(game.make_move("e7", "e6"))
        self.assertTrue(game.make_move("f3", "f4"))
        self.assertTrue(game.make_move("e6", "f5"))
        self.assertTrue(game.make_move("f4", "f5"))

        self.assertEqual(game.get_game_state(), "WHITE_WON")

        self.assertFalse(game.make_move("a7", "a6"))
        self.assertEqual(game.get_current_player().get_color(), "white")


class TestFairyEntry(unittest.TestCase):
    """Tests fairy entry eligibility."""
    def test_white_fairies(self):
        """Tests white fairy entries."""
        game = ChessVar()

        _ = None

        game._board._grid = [
            [_, _, _, _, _, _, _, _],
            [_, _, _, _, _, _, _, _],
            [_, _, _, _, _, _, _, _],
            [_, _, _, _, _, _, _, _],
            [_, _, _, _, _, _, _, _],
            [_, _, _, _, _, _, _, _],
            [_, _, _, _, _, _, _, _],
            [_, _, _, _, _, _, _, _],
        ]

        self.assertFalse(game.enter_fairy_piece("f", "a1" )) # wrong color
        self.assertFalse(game.enter_fairy_piece("F", "a1")) # not enough points
        game._white.increment_fairy_points()
        self.assertFalse(game.enter_fairy_piece("F", "a3")) # not in home ranks
        self.assertTrue(game.enter_fairy_piece("F", "b2")) # good

        game._change_turn() # switch back to white

        self.assertFalse(game.enter_fairy_piece("H", "e1")) # not enough points
        game._white.increment_fairy_points()
        self.assertTrue(game.enter_fairy_piece("H", "e1"))

    def test_black_fairies(self):
        """Tests black fairy entries."""
        game = ChessVar()
        game._change_turn()

        _ = None

        game._board._grid = [
            [_, _, _, _, _, _, _, _],
            [_, _, _, _, _, _, _, _],
            [_, _, _, _, _, _, _, _],
            [_, _, _, _, _, _, _, _],
            [_, _, _, _, _, _, _, _],
            [_, _, _, _, _, _, _, _],
            [_, _, _, _, _, _, _, _],
            [_, _, _, _, _, _, _, _],
        ]

        self.assertFalse(game.enter_fairy_piece("F", "d8" )) # wrong color
        self.assertFalse(game.enter_fairy_piece("f", "d8")) # not enough points
        game._black.increment_fairy_points()
        self.assertFalse(game.enter_fairy_piece("f", "6")) # not in home ranks
        self.assertTrue(game.enter_fairy_piece("f", "d7")) # good


class TestChessVarEnterFairy(unittest.TestCase):
    """ChessVar enter fairy unit tests."""

    def test_falcon_entry(self):
        """Tests falcon entry."""
        game = ChessVar()

        game.make_move("d2", "d4")
        game.make_move("g7", "g6")

        # Unable to play fairy on wrong turn
        self.assertFalse(game.enter_fairy_piece("f", "g7"))
        self.assertFalse(game.enter_fairy_piece("h", "g7"))

        game.make_move("c1", "h6")

        # Unable to enter fairy with 0 points
        self.assertFalse(game.enter_fairy_piece("f", 'g7'))
        self.assertFalse(game.enter_fairy_piece("h", "g7"))

        game.make_move("b8", "c6")
        game.make_move("h6", "f8") # white caps black, 1 point

        # 1 point but wrong player's home rank
        self.assertFalse(game.enter_fairy_piece("f", "d2"))

        # 1 point but wrong color
        self.assertFalse(game.enter_fairy_piece("F", "g7"))

        # able to enter fairy after 1 point
        self.assertTrue(game.enter_fairy_piece("f", "g7"))

        game.make_move("d1", "d3")

        # Unable to repeat falcon
        self.assertFalse(game.enter_fairy_piece("f", "b8"))

        # Unable to play hunter without another point
        self.assertFalse(game.enter_fairy_piece("h", "b8"))


class TestFairyMoves(unittest.TestCase):
    """Fairy movement unit tests."""
    def setUp(self):
        """Setup test data."""
        self.P1 = ChessPiece("pawn", "white")
        self.P2 = ChessPiece("pawn", "white")
        self.P3 = ChessPiece("pawn", "white")
        self.P4 = ChessPiece("pawn", "white")
        self.P5 = ChessPiece("pawn", "white")
        self.P6 = ChessPiece("pawn", "white")
        self.P7 = ChessPiece("pawn", "white")
        self.P8 = ChessPiece("pawn", "white")
        self.R1 = ChessPiece("rook", "white")
        self.R2 = ChessPiece("rook", "white")
        self.B1 = ChessPiece("bishop", "white")
        self.B2 = ChessPiece("bishop", "white")
        self.N1 = ChessPiece("knight", "white")
        self.N2 = ChessPiece("knight", "white")
        self.K = ChessPiece("king", "white")
        self.Q = ChessPiece("queen", "white")

        self.p1 = ChessPiece("pawn", "black")
        self.p2 = ChessPiece("pawn", "black")
        self.p3 = ChessPiece("pawn", "black")
        self.p4 = ChessPiece("pawn", "black")
        self.p5 = ChessPiece("pawn", "black")
        self.p6 = ChessPiece("pawn", "black")
        self.p7 = ChessPiece("pawn", "black")
        self.p8 = ChessPiece("pawn", "black")
        self.r1 = ChessPiece("rook", "black")
        self.r2 = ChessPiece("rook", "black")
        self.b1 = ChessPiece("bishop", "black")
        self.b2 = ChessPiece("bishop", "black")
        self.n1 = ChessPiece("knight", "black")
        self.n2 = ChessPiece("knight", "black")
        self.k = ChessPiece("king", "black")
        self.q = ChessPiece("queen", "black")

    def test_falcon_moves(self):
        """Tests falcon movement."""
        game = ChessVar()

        game.make_move("h2", "h4")
        game.make_move("g8", "f6")
        game.make_move("h1", "h3")
        game.make_move("f6", "e4")
        game.make_move("h3", "d3")
        game.make_move("d7", "d5")
        game.make_move("d3", "d5")
        game.make_move("d8", "d5")

        # Enter white falcon
        self.assertTrue(game.enter_fairy_piece("F", "h2"))

        game.make_move("c7", "c5")

        self.assertTrue(game.make_move("h2", "b8"))

        game.make_move("b7", "b5")

        self.assertTrue(game.make_move("b8", "b5"))

        # Play black hunter
        self.assertTrue(game.enter_fairy_piece("h", "b7"))

        # Try to play white hunter
        self.assertFalse(game.enter_fairy_piece("H", 'h1'))

        self.assertTrue(game.make_move("b5", "e8"))

        # Try to play after game won
        # self.assertFalse(game.make_move("a7", "a5"))

        # print(self.p1.get_color())


class TestEnterFairyPieces(unittest.TestCase):
    """Tests fairy piece entry and movement."""
    def test_entry_no_points(self):
        game = ChessVar()
        game.make_move("e2", "e4")
        game.make_move("d7", "d5")
        self.assertFalse(game.enter_fairy_piece("F", "d7"))
        self.assertFalse(game.enter_fairy_piece("H", "d7"))
        self.assertFalse(game.enter_fairy_piece("f", "d7"))
        self.assertFalse(game.enter_fairy_piece("h", "d7"))
        self.assertFalse(game.enter_fairy_piece("test", "d7"))
        self.assertFalse(game.enter_fairy_piece("F", "e2"))
        self.assertFalse(game.enter_fairy_piece("H", "e2"))
        self.assertFalse(game.enter_fairy_piece("f", "e2"))
        self.assertFalse(game.enter_fairy_piece("h", "e2"))
        self.assertFalse(game.enter_fairy_piece("test", "e2"))

    def test_entry_wrong_turn(self):
        game = ChessVar()
        game.make_move("e2", "e4")
        game.make_move("d7", "d5")
        game.make_move("d1", "g4")
        game.make_move("c8", "g4") # black captures white's queen
        self.assertEqual(game._white.get_fairy_points(), 1)

        self.assertFalse(game.enter_fairy_piece("f", "d7"))
        self.assertFalse(game.enter_fairy_piece("h", "d7"))

        self.assertFalse(game.enter_fairy_piece("f", "e2"))
        self.assertFalse(game.enter_fairy_piece("h", "e2"))

        # enter the piece
        self.assertTrue(game.enter_fairy_piece("F", "e2"))

        self.assertNotIn("falcon", game._white.get_reserve())

    def test_entry_wrong_space(self):
        game = ChessVar()
        game.make_move("e2", "e4")
        game.make_move("d7", "d5")
        game.make_move("d1", "g4")
        game.make_move("c8", "g4") # black captures white's queen
        self.assertEqual(game._white.get_fairy_points(), 1)

        self.assertFalse(game.enter_fairy_piece("f", "d7"))
        self.assertFalse(game.enter_fairy_piece("h", "d7"))

        self.assertFalse(game.enter_fairy_piece("f", "e2"))
        self.assertFalse(game.enter_fairy_piece("h", "e2"))

        # invalid spaces
        self.assertFalse(game.enter_fairy_piece("F", "e3"))
        self.assertFalse(game.enter_fairy_piece("F", "e3"))
        self.assertFalse(game.enter_fairy_piece("F", "a3"))
        self.assertFalse(game.enter_fairy_piece("F", "f6"))
        self.assertFalse(game.enter_fairy_piece("F", "b2"))
        self.assertFalse(game.enter_fairy_piece("F", "b1"))
        self.assertFalse(game.enter_fairy_piece("F", "h1"))
        self.assertFalse(game.enter_fairy_piece("F", "i2"))
        self.assertFalse(game.enter_fairy_piece("F", "c9"))
        self.assertFalse(game.enter_fairy_piece("F", "d5"))
        self.assertFalse(game.enter_fairy_piece("F", "d7"))
        self.assertFalse(game.enter_fairy_piece("F", "c8"))

    def test_entry_not_enough_points(self):
        game = ChessVar()
        game.make_move("e2", "e4")
        game.make_move("d7", "d5")
        game.make_move("d1", "g4")
        game.make_move("c8", "g4") # black captures white's queen
        self.assertEqual(game._white.get_fairy_points(), 1)

        self.assertFalse(game.enter_fairy_piece("f", "d7"))
        self.assertFalse(game.enter_fairy_piece("h", "d7"))

        self.assertFalse(game.enter_fairy_piece("f", "e2"))
        self.assertFalse(game.enter_fairy_piece("h", "e2"))

        # enter the piece
        self.assertTrue(game.enter_fairy_piece("F", "e2"))
        self.assertNotIn("falcon", game._white.get_reserve())

        game.make_move("a7", "a6")

        # try to enter second piece
        self.assertFalse(game.enter_fairy_piece("H", "d1"))

    def test_entry_game_over(self):
        game = ChessVar()
        game.make_move("f2", "f3")
        game.make_move("e7", "e5")
        game.make_move("b1", "c3")
        game.make_move("d8", "h4")
        game.make_move("a2", "a3")
        game.make_move("h4", "e1") # black captures white's king

        self.assertFalse(game.make_move("F", "f2"))
        self.assertFalse(game.make_move("H", "f2"))

        game = ChessVar()
        game.make_move("f2", "f3")
        game.make_move("e7", "e5")
        game.make_move("b1", "c3")
        game.make_move("d8", "h4")
        game.make_move("a2", "a3")
        game.make_move("b7", "b5")
        game.make_move("c3", "e4")
        game.make_move("h4", "e4") # black captures white's knight
        game.make_move("e1", "f2")
        game.make_move("f8", "c5")
        game.make_move("h2", "h3")
        game.make_move("c5", "f2") # black captures white's king

        self.assertEqual(game._white.get_fairy_points(), 1)

        self.assertFalse(game.make_move("F", "f2"))
        self.assertFalse(game.make_move("H", "f2"))


class TestMoveFairyPieces(unittest.TestCase):
    """Tests fairy piece movement"""
    game = ChessVar()
    _ = None
    piece = ChessPiece("hunter", "white")

    game._board._grid = [
        [_, _, _, _, _, _, _, _],
        [_, _, _, _, _, _, _, _],
        [_, _, _, _, _, _, _, _],
        [_, _, _, _, _, _, _, _],
        [_, _, _, piece, _, _, _, _],
        [_, _, _, _, _, _, _, _],
        [_, _, _, _, _, _, _, _],
        [_, _, _, _, _, _, _, _],
    ]

    game.print_board()


    game._board._grid = [
        [_, _, _, _, _, _, _, _],
        [ChessPiece("queen", "white"), _, _, _, _, _, _, _],
        [_, _, _, _, _, ChessPiece("queen", "white"), _, _],
        [_, _, _, ChessPiece("queen", "white"), _, _, _, _],
        [ChessPiece("queen", "white"), _, _, piece, _, ChessPiece("queen", "white"), _, _],
        [_, _, _, _, _, _, _, _],
        [_, ChessPiece("queen", "white"), _, ChessPiece("queen", "white"), _, ChessPiece("queen", "white"), _, _],
        [_, _, _, _, _, _, _, _],
    ]

    for row, col in game._board.get_valid_moves(4, 3):
        game._board.set(row, col, ChessPiece("pawn","white"))

    game.print_board()

if __name__ == "__main__":
    unittest.main()

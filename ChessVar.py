# Author:           Matt Muroya
# GitHub username:  mattmuroya
# Date:             2024-03-02
# Description:      ChessVar represents a game of Falcon-Hunter chess comprising
#                   two Player objects, a Board object, and all the standard
#                   ChessPiece objects (plus the Falcon and Hunter). Classes
#                   contain properties and methods for managing game state,
#                   validating moves, and actioning pieces on the board.


class ChessVar:
    """Represents a game of chess comprising two players, a board, and all the
    standard chess pieces plus the falcon and hunter. Handles user input, game
    state and flow, and player move validation.
    """
    def __init__(self) -> None:
        self._white = Player("white")
        self._black = Player("black")

        self._player = self._white
        self._winner = None
        self._board = Board()

        print("\nGame start!")
        self.print_board()
        print("\nWhite's turn")

    def print_board(self) -> None:
        """Prints a graphical representation of the current board state."""
        self._black.print_sideboard()
        self._board.print()
        self._white.print_sideboard()

    def get_current_player(self):
        """Returns the player for the current turn."""
        return self._player

    def get_game_state(self) -> str:
        """Returns a string declaring the game's current win state."""
        if self._winner is self._white:
            return "WHITE_WON"

        if self._winner is self._black:
            return "BLACK_WON"

        return "UNFINISHED"

    def make_move(self, orig: str, dest: str) -> bool:
        """Takes an origin and destination in algebraic notation and validates
        the move based on game state. Calls Board.get_valid_moves() to validate
        if the move based on piece type/board state. If valid, calls Board.set()
        and returns a bool indicating whether the action completed successfully.
        """
        orig = str(orig).lower()
        dest = str(dest).lower()

        player = self._player
        color = player.get_color()

        print(f"\n> {color.capitalize()} plays {orig} to {dest}")

        # Validate game status
        if self._winner is not None:
            print("\nInvalid move; game already won")
            return False

        # Validate coordinates
        orig_coords = self._to_coordinates(orig)
        dest_coords = self._to_coordinates(dest)

        if orig_coords is None or dest_coords is None:
            print("\nInvalid input")
            return False

        # Check origin piece
        piece = self._board.get(*orig_coords)

        if piece is None:
            print("\nInvalid move; no chess piece at origin")
            return False

        if piece.get_color() != color:
            print("\nInvalid move; enemy chess piece at origin")
            return False

        # Validate target space is a valid move
        valid_moves = self._board.get_valid_moves(*orig_coords)

        if dest_coords not in valid_moves:
            print("\nInvalid move; destination not allowed")
            return False

        # Execute move
        captured = self._board.set(*dest_coords, piece)
        self._board.set(*orig_coords, None)

        if captured is not None:
            captured_type = captured.get_type()
            enemy = captured.get_color().capitalize()

            print(f"\n{color.capitalize()} captures {enemy}'s {captured_type}")

            if captured_type == "king":
                self._winner = player
            else:
                self._change_turn()
                if captured_type in {"queen", "rook", "bishop", "knight"}:
                    self._player.increment_fairy_points()
        else:
            self._change_turn()

        self.print_board()

        if self._winner is not None:
            print(f"\n{player.get_color().capitalize()} wins!\n")
        else:
            print(f"\n{self._player.get_color().capitalize()}'s turn")

        return True

    def enter_fairy_piece(self, token: str, pos: str) -> bool:
        """Takes a fairy piece and target position in algebraic notation and
        validates the play; if valid, removes the piece from reserve, plays it,
        and returns a bool indicating whether the action completed successfully.
        """
        pos = str(pos).lower()

        player = self._player
        color = player.get_color()
        fairy = "falcon" if token.lower() == "f" else "hunter"

        print(f"\n> {color.capitalize()} plays {fairy} to {pos}")

        # Validate game status
        if self._winner is not None:
            print("\nInvalid play; game already won")
            return False

        if token not in ("F", "H", "f", "h"):
            print("\nInvalid input")
            return False

        # Validate selected piece matches player color
        if (player is self._white and token.islower()
            or player is self._black and token.isupper()
        ):
            print("\nInvalid play; fairy piece is enemy color")
            return False

        # Validate position is on the board
        pos_coords = self._to_coordinates(pos)

        if pos_coords is None:
            print("\nInvalid input; position not on board")
            return False

        reserve = player.get_reserve()
        points = player.get_fairy_points()

        # Validate fairy in reserve
        if fairy not in reserve:
            print(f"\nInvalid play; {color} {fairy} already played")
            return False

        # If two left, must have 1 point; if 1 left, must have 2 points
        if len(reserve) == 2 and points < 1 or len(reserve) == 1 and points < 2:
            print("\nInvalid play; not enough fairy points")
            return False

        # Validate target space is a valid move
        if (player is self._white and not 6 <= pos_coords[0] <= 7
            or player is self._black and not 0 <= pos_coords[0] <= 1
            or self._board.get(*pos_coords) is not None
        ):
            print("\nInvalid starting space")
            return False

        # Else, execute move
        self._board.set(*pos_coords, ChessPiece(fairy, player.get_color()))
        player.remove_from_reserve(fairy)

        print(f"\n{color.capitalize()}'s {fairy} is now in play")
        self.print_board()

        self._change_turn()
        print(f"\n{self._player.get_color().capitalize()}'s turn")

        return True

    def _change_turn(self) -> None:
        """Changes which player has the current turn."""
        self._player = self._black if self._player is self._white else self._white

    def _to_coordinates(self, pos: str) -> "tuple[int, int] | None":
        """Converts a string in algebraic notation representing a space on the 
        board into a pair of 2D array coordinates returned as a tuple.
        """
        # Validate input
        if not isinstance(pos, str):
            return None

        if len(pos) != 2 or pos[0] not in "abcdefgh" or pos[1] not in "12345678":
            return None

        # Convert to row/col coordinates
        row = 8 - int(pos[1:])
        col = ord(pos[0].lower()) - 97

        return row, col


class Player:
    """Represents a player. Handles player color, fairy pieces in reserve, and
    fairy points (i.e., the number of queens/rooks/bishops/knights lost).
    """
    def __init__(self, color: str) -> None:
        self._color = color
        self._reserve = ["falcon", "hunter"]
        self._fairy_points = 0

    def get_color(self) -> str:
        """Returns the player's color."""
        return self._color

    def get_reserve(self) -> "list[str]":
        """Returns the player's reserve list."""
        return self._reserve

    def get_fairy_points(self) -> int:
        """Returns the player's fairy points."""
        return self._fairy_points

    def remove_from_reserve(self, fairy: str) -> None:
        """Removes the specified fairy piece from the player's reserve."""
        if fairy in self._reserve:
            self._reserve.remove(fairy)

    def increment_fairy_points(self) -> None:
        """Increments the player's fairy points."""
        self._fairy_points += 1

        color = self.get_color().capitalize()
        points = self.get_fairy_points()
        print(f"{color} has {points} fairy point{'s' if points > 1 else ''}")

    def print_sideboard(self) -> None:
        """Prints the player's remaining pieces in reserve and fairy points."""
        key = {
            "falcon": "▽" if self.get_color() == "white" else "▼",
            "hunter": "□" if self.get_color() == "white" else "■"
        }
        col = self.get_color().capitalize()
        rsv = " ".join([key[piece] for piece in self.get_reserve()])
        pts = self.get_fairy_points()

        print(f"\n      {col}: [ {rsv} ], {pts} fairy point{'' if pts == 1 else 's'}")


class Board:
    """Represents the board as a 2D array of ChessPiece objects. Has methods for
    getting/setting board state and printing the board to the terminal.
    """
    def __init__(self) -> None:
        back = ["rook","knight","bishop","queen","king","bishop","knight","rook"]
        front = ["pawn"] * 8
        self._grid = [
            [ChessPiece(type, "black") for type in back],
            [ChessPiece(type, "black") for type in front],
            [None] * 8, [None] * 8, [None] * 8, [None] * 8,
            [ChessPiece(type, "white") for type in front],
            [ChessPiece(type, "white") for type in back]
        ]
        self._key = {
            "white": {
                "king": "♔", "queen": "♕", "rook": "♖", "bishop": "♗",
                "knight": "♘", "pawn": "♙", "falcon": "▽", "hunter": "□"
            },
            "black": {
                "king": "♚", "queen": "♛", "rook": "♜", "bishop": "♝",
                "knight": "♞", "pawn": "♟︎", "falcon": "▼", "hunter": "■"
            }
        }

    def print(self) -> None:
        """Prints a graphical representation of the current board state."""
        print("\n      ╔═══╤═══╤═══╤═══╤═══╤═══╤═══╤═══╗")
        for row in range(8):
            print(f"    {str(8-row)} ║", end="")
            for col in range(8):
                piece = self.get(row, col)
                token = (" " if piece is None
                         else self._key[piece.get_color()][piece.get_type()])
                print(f" {token} {'│' if col < 7 else ''}", end="")
            print("║\n      ╟───┼───┼───┼───┼───┼───┼───┼───╢" if row < 7 else "║")
        print(
            "      ╚═══╧═══╧═══╧═══╧═══╧═══╧═══╧═══╝\n" +
            "        a   b   c   d   e   f   g   h  "
        )

    def get(self, row: int, col: int) -> "ChessPiece | None":
        """Takes a row/col and returns that ChessPiece object, if any."""
        if 0 <= row <= 7 and 0 <= col <=7:
            return self._grid[row][col]

        return None

    def set(self, row: int, col: int, piece: "ChessPiece | None") -> "ChessPiece | None":
        """Takes a row/col and ChessPiece object (or None) and sets the piece to
        that position. Returns the captured ChessPiece object (if any).
        """
        captured = self._grid[row][col]
        self._grid[row][col] = piece

        return captured

    def _scan(self, row: int, col: int, dy: int, dx: int, step_limit: int,
              color: str, can_capture=True, res: "set[tuple[int, int]]"=None
        ) -> "set[tuple[int, int]]":
        """Recursive helper for get_valid_moves() that scans a path. Takes a
        position (row/col), step (dy/dx), step limit, piece color, indicator for
        whether capture is allowed, and a set of valid moves along the path.
        
        Starts at row/col and steps the path indicated by dy and dx. Checks that
        each square is open and continues until (a) out of bounds or (b) hits
        or captures another piece. Returns list of valid moves along the path.
        """
        if res is None:
            res = set()

        # Base case: exceeded step limit
        if step_limit == 0:
            return res

        # Base case: fell off board
        if not 0 <= row <= 7 or not 0 <= col <= 7:
            return res

        # Get contents of space
        space = self.get(row, col)

        # Base case: collision detected
        if space is not None:
            # Add to res only if enemy
            if can_capture and space.get_color() != color:
                res.add((row, col))

            return res

        # Space is empty; add to res and call recursively
        res.add((row, col))

        if step_limit is not None:
            step_limit -= 1

        return self._scan(row+dy, col+dx, dy, dx, step_limit, color, can_capture, res)

    def get_valid_moves(self, row: int, col: int) -> "set[tuple[int, int]]":
        """Takes a row/col coordinate pair and calculates and returns a set of
        valid moves (as row/col coordinates) for the piece in that position.
        """
        valid_moves = set()
        piece = self.get(row, col)

        if piece is None:
            return valid_moves

        color = piece.get_color()
        name = piece.get_type()
        moveset = piece.get_moveset()
        step_limit = piece.get_step_limit()

        if name == "pawn":
            # Scan vertical move
            dy, dx = moveset[0]
            # Limit 2 if home row. If in enemy home, limited to 1 by oob
            step_limit = 2 if row in (1, 6) else 1
            valid_moves.update(self._scan(row+dy, col+dx, dy, dx, step_limit, color, False))

            # Add diagonal move only if enemy present
            for dy, dx in moveset[1:]:
                diagonal = self.get(row+dy, col+dx)

                if diagonal is not None and diagonal.get_color() != color:
                    valid_moves.update({(row+dy, col+dx)})
        else:
            for dy, dx in moveset:
                valid_moves.update(self._scan(row+dy, col+dx, dy, dx, step_limit, color))

        return valid_moves


class ChessPiece:
    """Represents a chess piece. Handles piece type, color, and moveset."""
    def __init__(self, piece_type: str, color: str) -> None:
        self._type = piece_type
        self._color = color
        self._moveset = ()
        self._step_limit = None

        north = (-1, 0)
        south = (1, 0)
        east = (0, 1)
        west = (0, -1)

        northeast = (-1, 1)
        southeast = (1, 1)
        southwest = (1, -1)
        northwest = (-1, -1)

        if piece_type == "pawn":
            # Step limit 2 for first move, else 1; Handled by Board object
            if color == "white":
                self._moveset = (north, northeast, northwest)
            if color == "black":
                self._moveset = (south, southeast, southwest)

        if piece_type == "king":
            self._step_limit = 1
            self._moveset = (north, south, east, west,
                             northeast, southeast, southwest, northwest)

        if piece_type == "queen":
            self._moveset = (north, south, east, west,
                             northeast, southeast, southwest, northwest)

        if piece_type == "rook":
            self._moveset = (north, south, east, west)

        if piece_type == "bishop":
            self._moveset = (northeast, southeast, southwest, northwest)

        if piece_type == "knight":
            self._step_limit = 1
            self._moveset = ((-2, 1), (-1, 2), (-1,-2), (-2, -1), # Quadrant 1/2
                             (2, -1), (1, -2), (1, 2), (2, 1)) # Quadrant 3/4

        if piece_type == "falcon":
            if color == "white":
                self._moveset = (south, northeast, northwest)
            if color == "black":
                self._moveset = (north, southeast, southwest)

        if piece_type == "hunter":
            if color == "white":
                self._moveset = (north, southeast, southwest)
            if color == "black":
                self._moveset = (south, northeast, northwest)

    def get_type(self) -> str:
        """Returns the chess piece's type."""
        return self._type

    def get_color(self) -> str:
        """Returns the chess piece's color."""
        return self._color

    def get_moveset(self) -> "tuple[tuple[int, int]]":
        """Returns the chess piece's moveset."""
        return self._moveset

    def get_step_limit(self) -> "int | None":
        """Returns the chess piece's step limit."""
        return self._step_limit


if __name__ == "__main__":
    print("\n" * 20)
    print(
        r"   _____ _                __      __            " + "\n"
        r"  / ____| |               \ \    / /            " + "\n"
        r" | |    | |__   ___  ___ __\ \  / /_ _ _ __     " + "\n"
        r" | |    | '_ \ / _ \/ __/ __\ \/ / _` | '__|    " + "\n"
        r" | |____| | | |  __/\__ \__ \\  / (_| | |       " + "\n"
        r"  \_____|_| |_|\___||___/___/ \/ \__,_|_|       " + "\n"
        r"                                                " + "\n"
        r"        A Game of Falcon-Hunter Chess           " + "\n"
        r"                                                " + "\n"
        r"                                                " + "\n"
        r"                 How to play:                   " + "\n"
        r"                                                " + "\n"
        r"To make a move, enter the name of an origin and " + "\n"
        r"destination space in algebraic notation.        " + "\n"
        r"                                                " + "\n"
        r"Example:                                        " + "\n"
        r"                                                " + "\n"
        r"> Origin: d2                                    " + "\n"
        r"> Destination: d4                               " + "\n"
        r"                                                " + "\n"
        r"To play your falcon or hunter, enter the name of" + "\n"
        r"the piece for the origin and a starting position" + "\n"
        r"for the destination                             " + "\n"
        r"                                                " + "\n"
        r"Example:                                        " + "\n"
        r"                                                " + "\n"
        r"> Origin: falcon                                " + "\n"
        r"> Destination: d2                               "
    )

    game = ChessVar()

    # MAIN LOOP
    while game.get_game_state() == "UNFINISHED":
        origin = input("\n> Origin: ")
        destination = input("> Destination: ")

        if origin == "falcon":
            origin = "F" if game.get_current_player().get_color() == "white" else "f"
            game.enter_fairy_piece(origin, destination)
        elif origin == "hunter":
            origin = "H" if game.get_current_player().get_color() == "white" else "h"
            game.enter_fairy_piece(origin, destination)
        else:
            game.make_move(origin, destination)

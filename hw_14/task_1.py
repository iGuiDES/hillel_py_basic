import random


class ChessBoard:
    def __init__(self):
        self.board = [[" " for _ in range(8)] for _ in range(8)]
        self.pieces = [
            '♚', '♛', '♜', '♝', '♞', '♟', '♔', '♕', '♖', '♗', '♘', '♙'
        ]
        self.place_kings()

    def place_kings(self):
        bk_row, bk_col = (
            random.randint(0, 7), random.randint(0, 7)
        )
        self.board[bk_row][bk_col] = '♚'
        wk_row, wk_col = (
            random.randint(0, 7), random.randint(0, 7)
        )
        while wk_row == bk_row and wk_col == bk_col:
            wk_row, wk_col = (
                random.randint(0, 7), random.randint(0, 7)
            )
        self.board[wk_row][wk_col] = '♔'

    def place_random_pieces(self):
        self.__init__()
        for _ in range(random.randint(0, 30)):
            piece = random.choice(self.pieces)
            row, col = random.randint(0, 7), random.randint(0, 7)
            while self.board[row][col] != " ":
                row, col = random.randint(0, 7), random.randint(0, 7)
            self.board[row][col] = piece

    def draw_board(self):
        print('    ' + '   '.join(
            ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
        ) + '  ')

        print('   ' + '┌───' * 8 + '┐')

        for row in range(8):
            print(f' {8 - row} │', end="")

            for col in range(8):
                print(f" {self.board[row][col]} │", end="")
            print(f' {8 - row}')
            if row < 7:
                print('   ├' + '───┼' * 7 + '───┤')
        print('   ' + '└───' * 8 + '┘')
        print('    ' + '   '.join(
            ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
        ) + '  ')


board = ChessBoard()

print("\n" + "#"*15 + " Дошка 1 " + "#"*15 + "\n")
board.place_random_pieces()
board.draw_board()

print("\n" + "#"*15 + " Дошка 2 " + "#"*15 + "\n")
board.place_random_pieces()
board.draw_board()

print("\n" + "#"*15 + " Дошка 3 " + "#"*15 + "\n")
board.place_random_pieces()
board.draw_board()

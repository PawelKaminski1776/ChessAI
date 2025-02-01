# Needs friendly and enemy pieces detection

class Movement:
    def __init__(self, chessboard):
        self.board = chessboard

    def checkifSameColor(self, h1, w1, h2, w2):
        if self.board[h1][w1].isupper() == self.board[h2][w2].isupper():
            return True;
        else:
            return False;

    # Definitely needs refactoring
    def queen_moves(self, h, w):
        possible_moves = []
        # Vertical and Horizontal Movement
        i = -8;
        for i in range(8):
            if  i != w:  # Avoid current position
                # Vertical movement
                if self.checkifSameColor(h, w, i, w):
                    if self.board[i][w] == ' ' or not checkifSameColor(h, w, i, w):
                        # Deploy empty position
                        self.board[h][w] == ' '
                        # Move Queen
                        possible_moves.append((i, w))
                    else:
                        break

        i = -8;
        for i in range(8):
            if  i != w:  # Avoid current position
                # Horizontal movement
                if self.checkifSameColor(h, w, h, i):
                    if self.board[h][i] == ' ' or not checkifSameColor(h, w, h, i):
                        # Deploy empty position
                        self.board[h][w] == ' '
                        # Move Queen
                        possible_moves.append((h,i))
                    else:
                        break

        for i in range(-8,8):
            if  i != w and i != h:
                # Top-right diagonal
                if h - i >= 0 and w + i < 8:
                    if self.board[h - i][w + i] == ' ' or not self.checkifSameColor(h, w, h - i, w + i):
                        possible_moves.append((h - i, w + i))  # Add move
                    if self.board[h - i][w + i] != ' ':
                        if not self.checkifSameColor(h, w, h - i, w + i):  # Capture opponent's piece
                            possible_moves.append((h - i, w + i))
                        break  # Stop if there's a piece in the way

        for i in range(-8,8):
            if  i != w and i != h:
                # Bottom-left diagonal
                if h + i < 8 and w - i >= 0:
                    if self.board[h + i][w - i] == ' ' or not self.checkifSameColor(h, w, h + i, w - i):
                        possible_moves.append((h + i, w - i))  # Add move
                    if self.board[h + i][w - i] != ' ':
                        if not self.checkifSameColor(h, w, h + i, w - i):  # Capture opponent's piece
                            possible_moves.append((h + i, w - i))
                        break  # Stop if there's a piece in the way

        for i in range(-8, 8):
            if  i != w and i != h:
                # Top-left diagonal
                if h - i >= 0 and w - i >= 0:
                    if self.board[h - i][w - i] == ' ' or not self.checkifSameColor(h, w, h - i, w - i):
                        possible_moves.append((h - i, w - i))  # Add move
                    if self.board[h - i][w - i] != ' ':
                        if not self.checkifSameColor(h, w, h - i, w - i):  # Capture opponent's piece
                            possible_moves.append((h - i, w - i))
                        break  # Stop if there's a piece in the way
        for i in range(8):
            if  i != w and i != h:
                # Bottom-right diagonal
                if h + i < 8 and w + i < 8:
                    if self.board[h + i][w + i] == ' ' or not self.checkifSameColor(h, w, h + i, w + i):
                        possible_moves.append((h + i, w + i))  # Add move
                    if self.board[h + i][w + i] != ' ':
                        if not self.checkifSameColor(h, w, h + i, w + i):  # Capture opponent's piece
                            possible_moves.append((h + i, w + i))
                        break  # Stop if there's a piece in the way

        return possible_moves


    # knight movement: L-shape
    def knight_moves(self, h, w):
        possible_moves = []

        # List of positions the knight can move to
        knight_moves_list = [
            (h-2, w-1), (h-2, w+1),  # Two squares up, one left or right
            (h-1, w-2), (h-1, w+2),  # One square up, two left or right
            (h+1, w-2), (h+1, w+2),  # One square down, two left or right
            (h+2, w-1), (h+2, w+1)   # Two squares down, one left or right
        ]

        # Check if each move is within board limits (0 <= h, w < 8)
        for move in knight_moves_list:
            nh, nw = move
            if 0 <= nh < 8 and 0 <= nw < 8:
                possible_moves.append((nh, nw))

        # Kill Logic (Except for K)
        return possible_moves

    # bishop movement
    def bishop_moves(self, h, w):
        possible_moves = []
        # Diagonal Movement
        for i in range(0, 8):
            if h + i < 8 and w + i < 8:
                possible_moves.append((h + i, w + i))  # Top-right diagonal
            if h - i >= 0 and w - i >= 0:
                possible_moves.append((h - i, w - i))  # Bottom-left diagonal
            if h + i < 8 and w - i >= 0:
                possible_moves.append((h + i, w - i))  # Top-left diagonal
            if h - i >= 0 and w + i < 8:
                possible_moves.append((h - i, w + i))  # Bottom-right diagonal
        # Kill Logic (Except for K)
        return possible_moves

    def rook_moves(self, h, w):
        possible_moves = []
        # Vertical and Horizontal Movement
        for i in range(8):
            if self.board[i] == ' ':
                if i != h:  # Avoid the current position
                    possible_moves.append((i, w))  # Vertical
                if i != w:  # Avoid the current position
                    possible_moves.append((h, i))  # Horizontal

        # Kill Logic (Except for K)
        return possible_moves


    def pawn_moves(self, h, w):
        possible_moves = []
        # first 2 move for pawn p1
        if h == 1:
            possible_moves.append((h + 2, w))
        # second 2 move for pawn p2
        if h == 6:
            possible_moves.append((h - 2, w))

        # p1
        if self.board[h][w] == 'P':
            possible_moves.append((h + 1, w))

        # p2
        if self.board[h][w] == 'p':
            possible_moves.append((h - 1, w))

        # Kill Logic (Except for K)

        return possible_moves;


    def king_moves(self, h, w):
        possible_moves = []

        # implement king move logic
        # check logic

        return possible_moves;

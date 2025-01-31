# Needs friendly and enemy pieces detection

class Movement:
    def __init__(self, chessboard):
        self.board = chessboard

    # Queen Movement: Diagonal, Vertical, Horizontal
    def queen_moves(self, h, w):
        possible_moves = []

        # Vertical and Horizontal Movement
        for i in range(8):
            if i != h:
                possible_moves.append((i, w))
            if i != w:
                possible_moves.append((h, i))

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
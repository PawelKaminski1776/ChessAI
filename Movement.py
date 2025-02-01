# Needs friendly and enemy pieces detection

class Movement:
    def __init__(self, chessboard):
        self.board = chessboard
        self.check = False

    def checkifSameColor(self, h1, w1, h2, w2):
        if self.board[h1][w1].isupper() == self.board[h2][w2].isupper():
            return True;

        else:
            return False;

    def rook_moves(self, h, w):
        possible_moves = []
        # Vertical Check Down
        for i in range(h+1,len(self.board),1):
            if i != h:
                # Vertical movement - WORKS NOW
                if self.board[i][w] == ' ':
                    # Add Move
                    possible_moves.append((i, w))
                if self.board[i][w] != ' ' and not self.checkifSameColor(h, w, i, w):
                    # Add Move
                    possible_moves.append((i, w))
                    print(i,w)
                    break;
                if self.board[i][w] != ' ' and self.checkifSameColor(h, w, i, w):
                    break

        # Vertical Check Up
        for i in range(h-1,-1,-1):
            if i != h:
                # Vertical movement - WORKS NOW
                if self.board[i][w] == ' ':
                    # Add Move
                    possible_moves.append((i, w))
                if self.board[i][w] != ' ' and not self.checkifSameColor(h, w, i, w):
                    # Add Move
                    possible_moves.append((i, w))
                    break
                if self.board[i][w] != ' ' and self.checkifSameColor(h, w, i, w):
                    break


        # Horizontal Check Right
        for i in range(w,len(self.board)):
            if i != w:
                # Horizontal movement - WORKS NOW
                if self.board[h][i] == ' ':
                    # Add Move
                    possible_moves.append((h,i))
                if self.board[h][i] != ' ' and not self.checkifSameColor(h, w, h, i):
                    # Add Move
                    possible_moves.append((h,i))
                    break;
                if self.board[h][i] != ' ' and self.checkifSameColor(h, w, h, i):
                    break

        # Horizontal Check Left
        for i in range(w,-1,-1):
            if i != w:
                # Horizontal movement - WORKS NOW
                if self.board[h][i] == ' ':
                    # Add Move
                    possible_moves.append((h,i))
                if self.board[h][i] != ' ' and not self.checkifSameColor(h, w, h, i):
                    # Add Move
                    possible_moves.append((h,i))
                    break;
                if self.board[h][i] != ' ' and self.checkifSameColor(h, w, h, i):
                    break
        return possible_moves

    def bishop_moves(self, h, w):
        possible_moves = []
        # Top-right diagonal
        k = w;
        for i in range(h-1,-1,-1):
            k = k + 1
            if self.board[i][k] == ' ':
                possible_moves.append((i,k))
            if self.board[i][k] != ' ' and not self.checkifSameColor(h, w, i, k):
                possible_moves.append((i,k))
                break;
            if self.board[i][k] != ' ' and self.checkifSameColor(h, w, i, k):
                break;

        # Top-left diagonal
        k = w;
        for i in range(h-1,-1,-1):
            k = k - 1
            if self.board[i][k] == ' ':
                possible_moves.append((i,k))
            if self.board[i][k] != ' ' and not self.checkifSameColor(h, w, i, k):
                possible_moves.append((i,k))
                break;
            if self.board[i][k] != ' ' and self.checkifSameColor(h, w, i, k):
                break;

        # Bottom-right diagonal
        k = w;
        for i in range(h+1,len(self.board),1):
            k = k + 1
            if self.board[i][k] == ' ':
                possible_moves.append((i,k))
            if self.board[i][k] != ' ' and not self.checkifSameColor(h, w, i, k):
                possible_moves.append((i,k))
                break;
            if self.board[i][k] != ' ' and self.checkifSameColor(h, w, i, k):
                break;

                # Botton-Left diagonal
        k = w;
        for i in range(h+1,len(self.board),1):
            k = k - 1
            if self.board[i][k] == ' ':
                possible_moves.append((i,k))
            if self.board[i][k] != ' ' and not self.checkifSameColor(h, w, i, k):
                possible_moves.append((i,k))
                break;
            if self.board[i][k] != ' ' and self.checkifSameColor(h, w, i, k):
                break;
        return possible_moves

    # Definitely needs refactoring
    def queen_moves(self, h, w):
        possible_moves = []
        # Vertical Movement

        # Vertical Check Down
        for i in range(h+1,len(self.board),1):
            if i != h:
                # Vertical movement - WORKS NOW
                if self.board[i][w] == ' ':
                    # Add Move
                    possible_moves.append((i, w))
                if self.board[i][w] != ' ' and not self.checkifSameColor(h, w, i, w):
                    # Add Move
                    possible_moves.append((i, w))
                    print(i,w)
                    break;
                if self.board[i][w] != ' ' and self.checkifSameColor(h, w, i, w):
                    break

        # Vertical Check Up
        for i in range(h-1,-1,-1):
            if i != h:
                # Vertical movement - WORKS NOW
                if self.board[i][w] == ' ':
                    # Add Move
                    possible_moves.append((i, w))
                if self.board[i][w] != ' ' and not self.checkifSameColor(h, w, i, w):
                    # Add Move
                    possible_moves.append((i, w))
                    break
                if self.board[i][w] != ' ' and self.checkifSameColor(h, w, i, w):
                    break


        # Horizontal Check Right
        for i in range(w,len(self.board)):
            if i != w:
                # Horizontal movement - WORKS NOW
                if self.board[h][i] == ' ':
                    # Add Move
                    possible_moves.append((h,i))
                if self.board[h][i] != ' ' and not self.checkifSameColor(h, w, h, i):
                    # Add Move
                    possible_moves.append((h,i))
                    break;
                if self.board[h][i] != ' ' and self.checkifSameColor(h, w, h, i):
                    break

        # Horizontal Check Left
        for i in range(w,-1,-1):
            if i != w:
                # Horizontal movement - WORKS NOW
                if self.board[h][i] == ' ':
                    # Add Move
                    possible_moves.append((h,i))
                if self.board[h][i] != ' ' and not self.checkifSameColor(h, w, h, i):
                    # Add Move
                    possible_moves.append((h,i))
                    break;
                if self.board[h][i] != ' ' and self.checkifSameColor(h, w, h, i):
                    break


        # Top-right diagonal
        k = w;
        for i in range(h-1,-1,-1):
            k = k + 1
            if self.board[i][k] == ' ':
                possible_moves.append((i,k))
            if self.board[i][k] != ' ' and not self.checkifSameColor(h, w, i, k):
                possible_moves.append((i,k))
                break;
            if self.board[i][k] != ' ' and self.checkifSameColor(h, w, i, k):
                break;

        # Top-left diagonal
        k = w;
        for i in range(h-1,-1,-1):
            k = k - 1
            if self.board[i][k] == ' ':
                possible_moves.append((i,k))
            if self.board[i][k] != ' ' and not self.checkifSameColor(h, w, i, k):
                possible_moves.append((i,k))
                break;
            if self.board[i][k] != ' ' and self.checkifSameColor(h, w, i, k):
                break;

        # Bottom-right diagonal
        k = w;
        for i in range(h+1,len(self.board),1):
            k = k + 1
            if self.board[i][k] == ' ':
                possible_moves.append((i,k))
            if self.board[i][k] != ' ' and not self.checkifSameColor(h, w, i, k):
                possible_moves.append((i,k))
                break;
            if self.board[i][k] != ' ' and self.checkifSameColor(h, w, i, k):
                break;

                # Botton-Left diagonal
        k = w;
        for i in range(h+1,len(self.board),1):
            k = k - 1
            if self.board[i][k] == ' ':
                possible_moves.append((i,k))
            if self.board[i][k] != ' ' and not self.checkifSameColor(h, w, i, k):
                possible_moves.append((i,k))
                break;
            if self.board[i][k] != ' ' and self.checkifSameColor(h, w, i, k):
                break;

        return possible_moves

    # knight movement: L-shape
    def knight_moves(self, h, w):
        possible_moves = []

        # List of positions the knight can move to
        knight_moves_list = [
            (h-2, w-1), (h-2, w+1),
            (h-1, w-2), (h-1, w+2),
            (h+1, w-2), (h+1, w+2),
            (h+2, w-1), (h+2, w+1)
        ]

        # Check if each move is within board limits (0 <= h, w < 8)
        for move in knight_moves_list:
            nh, nw = move
            if 0 <= nh < 8 and 0 <= nw < 8:
                if self.board[nh][nw] == ' ' or not self.checkifSameColor(h,w,nh,nw):
                    possible_moves.append((nh, nw))

        return possible_moves

    def pawn_moves(self, h, w):
        possible_moves = []
        Pawn_moves_kill_list_p1 = [
            (h-1, w-1),(h-1, w+1)
        ]

        Pawn_moves_kill_list_p2 = [
            (h+1, w+1),(h+1, w-1)
        ]
        # p1
        if self.board[h][w] == 'P':
            if self.board[h + 1][w] == ' ':
                if h == 1:
                    possible_moves.append((h + 2, w))
                possible_moves.append((h + 1, w))

            for move in Pawn_moves_kill_list_p1:
                nh, nw = move
                if 0 <= nh < 8 and 0 <= nw < 8:
                    if not self.checkifSameColor(h,w,nh,nw):
                        possible_moves.append((nh, nw))


        # p2
        if self.board[h][w] == 'p':
            if self.board[h - 1][w] == ' ':
                if h == 6:
                    possible_moves.append((h - 2, w))
                possible_moves.append((h - 1, w))

            for move in Pawn_moves_kill_list_p2:
                nh, nw = move
                if 0 <= nh < 8 and 0 <= nw < 8:
                    if not self.checkifSameColor(h,w,nh,nw):
                        possible_moves.append((nh, nw))

        # change to queen logic

        # Kill Logic

        return possible_moves;
    def king_moves(self, h, w):
        possible_moves = []
        king_moves = [
            # Vertical and Horizontal:
            (h-1, w),(h+1, w),
            (h, w-1),(h, w+1),

            # Diagonal:
            (h+1, w+1),(h+1, w-1),
            (h-1, w+1),(h-1, w-1),
        ]

        for move in king_moves:
            nh, nw = move
            if 0 <= nh < 8 and 0 <= nw < 8:
                if not self.checkifSameColor(h,w,nh,nw):
                    possible_moves.append((nh, nw))
        return possible_moves


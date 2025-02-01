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
   
import Movement;

chessboard = [
    ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R'],  # Black back rank
    ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],  # Black pawns
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],  # Empty row
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],  # Empty row
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],  # Empty row
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],  # Empty row
    ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],  # White pawns
    ['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r']]


movement = Movement(chessboard)
possible_moves = []

for i in range(7):
    for k in range(7):
        if chessboard[i][k] == 'P':
            possible_moves += movement.pawn_moves(i,k)
        if chessboard[i][k] == 'R':
            possible_moves += movement.rook_moves(i,k)
        if chessboard[i][k] == 'N':
            possible_moves += movement.knight_moves(i,k)
        if chessboard[i][k] == 'B':
            possible_moves += movement.bishop_moves(i,k)
        if chessboard[i][k] == 'Q':
            possible_moves += movement.queen_moves(i,k)
        if chessboard[i][k] == 'K':
            possible_moves += movement.king_moves(i,k)

print(len(possible_moves))
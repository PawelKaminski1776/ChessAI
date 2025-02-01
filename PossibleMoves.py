chessboard = [
    ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R'],  # Black back rank
    ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],  # Black pawns
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],  # Empty row
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],  # Empty row
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],  # Empty row
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],  # Empty row
    ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],  # White pawns
    ['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r']]  # White back rank


movement = Movement(chessboard)
possible_moves = []

for i in range(0,8):
    for k in range(0,8):
        if chessboard[i][k] == 'P':
            possible_moves += movement.pawn_moves(i,k)
        if chessboard[i][k] == 'R':
            possible_moves += movement.rook_moves(i,k)
        if chessboard[i][k] == 'N':
            possible_moves += movement.knight_moves(i,k)
        if chessboard[i][k] == 'B':
            possible_moves += movement.bishop_moves(i,k)
        if chessboard[i][k] == 'K':
            possible_moves += movement.king_moves(i,k)
        if chessboard[i][k] == 'Q':
            possible_moves += movement.queen_moves(i,k)



# Show Start Possible moves for testing
for num1, num2 in possible_moves:
    chessboard[num1][num2] = '*'

print(len(possible_moves))
for row in chessboard:
    print(row)

## Testing method for checking if pieces are the same
## print(movement.checkColor(0,0,1,1))

##print(len(chessboard))
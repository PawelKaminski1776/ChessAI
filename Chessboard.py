# Generate Chessboard
chessboard = [
    ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R'],  # Black back rank
    ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],  # Black pawns
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],  # Empty row
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],  # Empty row
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],  # Empty row
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],  # Empty row
    ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],  # White pawns
    ['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r']   # White back rank
]


for row in chessboard:
    print(row)
print("Mohd Jawwad Ali Farooqui,USN:1AY24AI070,SEC:O")
def isValidChessBoard(board):
    valid_positions = {f"{r}{c}" for r in range(1, 9) for c in "abcdefgh"}
    valid_pieces = {'pawn', 'knight', 'bishop', 'rook', 'queen', 'king'}
    piece_count = {'w': 0, 'b': 0}
    king_count = {'wking': 0, 'bking': 0}
    pawn_count = {'w': 0, 'b': 0}
    for position, piece in board.items():
        # Check if position is valid
        if position not in valid_positions:
            return False
        if len(piece) < 2 or piece[0] not in 'wb' or piece[1:] not in valid_pieces:
            return False
        color = piece[0]
        piece_type = piece[1:]
        piece_count[color] += 1
        if piece_type == 'king':
            king_count[piece] += 1
        if piece_type == 'pawn':
            pawn_count[color] += 1
    if king_count['wking'] != 1 or king_count['bking'] != 1:
        return False
    if piece_count['w'] > 16 or piece_count['b'] > 16:
        return False
    if pawn_count['w'] > 8 or pawn_count['b'] > 8:
        return False
    return True

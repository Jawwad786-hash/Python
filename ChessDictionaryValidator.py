print("Mohd Jawwad Ali Farooqui, USN:1AY24AI070, SEC:O")
def create_chess_dictionary():
    chess_pieces = {
        "King": {
            "abbreviation": "K",
            "movement": "Moves one square in any direction."
        },
        "Queen": {
            "abbreviation": "Q",
            "movement": "Moves any number of squares in any direction."
        },
        "Rook": {
            "abbreviation": "R",
            "movement": "Moves any number of squares vertically or horizontally."
        },
        "Bishop": {
            "abbreviation": "B",
            "movement": "Moves any number of squares diagonally."
        },
        "Knight": {
            "abbreviation": "N",
            "movement": "Moves in an L-shape: two squares in one direction and then one square perpendicular."
        },
        "Pawn": {
            "abbreviation": "P",
            "movement": "Moves forward one square, but captures diagonally. On first move, can advance two squares."
        }
    }
    return chess_pieces
def display_chess_dictionary(chess_dict):
    print("\n--- Chess Dictionary ---\n")
    for piece, details in chess_dict.items():
        print(f"Piece: {piece}")
        print(f"  Abbreviation: {details['abbreviation']}")
        print(f"  Movement: {details['movement']}\n")
if __name__ == "__main__":
    chess_dict = create_chess_dictionary()
    display_chess_dictionary(chess_dict)

   

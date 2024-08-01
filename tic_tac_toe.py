
def print_intro_art():
    '''
    Prints intro art for the game. In Stick Letters.
    '''
    print('''___    __     ___       __     ___  __   ___ 
 |  | /  ` __  |   /\  /  ` __  |  /  \ |__  
 |  | \__,     |  /~~\ \__,     |  \__/ |___ 
                                             ''')
    
def create_board():
    '''
    This creates a blank board that has 9 empty spaces.
    '''
    return [" " for _ in range(9)]


def print_board(board):
    print("\n")
    for i in range(3):
        print(" " + " | ".join(board[i*3:(i+1)*3]))
        if i < 2:
            print("---|---|---")
    print("\n")


def get_move(player):
    while True:
        try:
            move = int(input(f"Player {player}, enter your move (1-9): ")) - 1
            if move >= 0 and move < 9:
                return move
            else:
                print("Invalid move. Please enter a number between 1 and 9.")
        except ValueError:
            print("Invalid input. Please enter a number.")


def is_winner(board, player):
    win_positions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows       0 1 2 
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns    3 4 5
        [0, 4, 8], [2, 4, 6]              # Diagonals  6 7 8
    ]
    for pos in win_positions:
        if all(board[i] == player for i in pos):
            return True
    return False


def is_draw(board):
    return all(space != " " for space in board)


def print_game_list():
    """
    This function prints the list of games and returns the number of games that are available.
    """       
    try:
        with open('game_list.txt', 'r') as file:
            game_list = [line.strip() for line in file]
            
            for game in game_list:
                print(game)
                
        print("\n")
        game_count = len(game_list)
        print(f"Number of available games: {game_count}")
        
        return game_count

    except FileNotFoundError:
        print("Error: The file 'game_list.txt' was not found.")
        return 0
    except IOError:
        print("Error: An error occurred while reading the file 'game_list.txt'.")
        return 0


def main():
    print_intro_art()
    
    while True:
        board = create_board()
        current_player = "X"

        while True:
            print_board(board)
            move = get_move(current_player)
            
            if board[move] == " ":
                board[move] = current_player
            else:
                print("The position is already occupied. Try again.")
                continue
            
            if is_winner(board, current_player):
                print_board(board)
                print(f"Player {current_player} wins!")
                break

            if is_draw(board):
                print_board(board)
                print("It's a draw!")
                break

            current_player = "O" if current_player == "X" else "X"

        play_again = input("Do you want to play again? (y/n): ").lower()
        if play_again != "y":
            break


if __name__ == "__main__":
    main()
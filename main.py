import sys
import time
import tic_tac_toe

# Color reset
RESET = "\033[0m"

# Regular colors
BLACK = "\033[30m"
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
MAGENTA = "\033[35m"
CYAN = "\033[36m"
WHITE = "\033[37m"

# Background colors
BG_BLACK = "\033[40m"
BG_RED = "\033[41m"
BG_GREEN = "\033[42m"
BG_YELLOW = "\033[43m"
BG_BLUE = "\033[44m"
BG_MAGENTA = "\033[45m"
BG_CYAN = "\033[46m"
BG_WHITE = "\033[47m"

def print_game_list():
    '''
    This function prints the list of games and returns the number of games that are available. 
    '''       
    try:
        with open('game_list.txt', 'r') as file:
            game_list = file.readlines()
            for game in range(len(game_list)):
                print(f"{game + 1}. {game_list[game].strip()}")
    except FileNotFoundError:
        print("Error: The file 'game_list.txt' was not found.")
    except IOError:
        print("Error: An error occurred while reading the file 'game_list.txt'.")
    except Exception as e:
        print(f"Error: An unexpected error occurred: {e}")
    
    print(f"{RED}0. Exit{RESET}")
    return len(game_list)
    

def print_intro_art():
    '''
    This function prints ascii art when this program is run.     
    '''
    print('''\n\n███╗   ███╗██╗███╗   ██╗██╗       ██████╗  █████╗ ███╗   ███╗███████╗███████╗
████╗ ████║██║████╗  ██║██║      ██╔════╝ ██╔══██╗████╗ ████║██╔════╝██╔════╝
██╔████╔██║██║██╔██╗ ██║██║█████╗██║  ███╗███████║██╔████╔██║█████╗  ███████╗
██║╚██╔╝██║██║██║╚██╗██║██║╚════╝██║   ██║██╔══██║██║╚██╔╝██║██╔══╝  ╚════██║
██║ ╚═╝ ██║██║██║ ╚████║██║      ╚██████╔╝██║  ██║██║ ╚═╝ ██║███████╗███████║
╚═╝     ╚═╝╚═╝╚═╝  ╚═══╝╚═╝       ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝╚══════╝
                                                                             ''')
    print("-" * 78 + "\n")

def validate_input(min_range, max_range, input_type, user_input):
    '''
    This function validates user input. 
    The min_range and max_range parameters are used to set a range for numerical inputs [Inclusive].
    The input_type parameter is used specify and validate the type of input.
    The user_input parameter is the user input that needs to be validated.
    '''

    if input_type == "int":
        try:
            user_input = int(user_input)
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            return False
        
        if user_input == 0:
            print(f"{RED}Exiting the program...{RESET}")
            sys.exit()
            
        if user_input < min_range or user_input > max_range:
            print("Invalid input. Please enter a valid number.")
            return False
        
        return True

def print_loading_bar(duration=3, length=30):
    for i in range(length + 1):
        percent = int((i / length) * 100)
        bar = '█' * i + '-' * (length - i)
        sys.stdout.write(f"\r|{bar}| {percent}%")
        sys.stdout.flush()
        time.sleep(duration / length)
    print()  # Move to the next line after completion

def initiate_game(user_input):
    '''
    This function initiates the game that the user has selected by calling the related function.
    '''
    try:
        with open('game_list.txt', 'r') as file:
            game_list = file.readlines()
            game = game_list[int(user_input) - 1].strip()
            print(f"{MAGENTA}\n{game} was chosen! {RESET}")
            print(f"{YELLOW}Initializing the game...{RESET}\n")
            print_loading_bar()
            print()

            if game == "Tic-tac-toe":
                tic_tac_toe.main()                

    except FileNotFoundError:
        print("Error: The file 'game_list.txt' was not found.")
    except IOError:
        print("Error: An error occurred while reading the file 'game_list.txt'.")
    except Exception as e:
        print(f"Error: An unexpected error occurred: {e}")
    
    main()

def main():
    print_intro_art()
    number_of_games = print_game_list()
    user_input = input("Enter the number of the game you want to play: ")        
    check = validate_input(0, number_of_games, "int", user_input)

    if check == True:
        initiate_game(user_input)



if __name__ == "__main__":
    main()
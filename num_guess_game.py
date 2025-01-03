from random import randint

Welcome_intro = r"""
Welcome to the number guessing game!!

                                                       _             
 _ __  _   _ _ __ ___         __ _ _   _  ___  ___ ___(_)_ __   __ _ 
| '_ \| | | | '_ ` _ \ _____ / _` | | | |/ _ \/ __/ __| | '_ \ / _` |
| | | | |_| | | | | | |_____| (_| | |_| |  __/\__ \__ \ | | | | (_| |
|_| |_|\__,_|_| |_| |_|      \__, |\__,_|\___||___/___/_|_| |_|\__, |
                             |___/_                            |___/ 
  __ _  __ _ _ __ ___   ___  | | | |                                 
 / _` |/ _` | '_ ` _ \ / _ \ | | | |                                 
| (_| | (_| | | | | | |  __/ |_|_|_|                                 
 \__, |\__,_|_| |_| |_|\___| (_|_|_)                                 
 |___/                   

"""

you_win = r"""

CORRECT GUESS!!!

__   _____  _   _  __        _____ _   _ 
\ \ / / _ \| | | | \ \      / /_ _| \ | |
 \ V / | | | | | |  \ \ /\ / / | ||  \| |
  | || |_| | |_| |   \ V  V /  | || |\  |
  |_| \___/ \___/     \_/\_/  |___|_| \_|

"""

you_lose = r"""

NO MORE GUESSES LEFT!!!

__     ______  _    _   _      ____   _____ ______ 
\ \   / / __ \| |  | | | |    / __ \ / ____|  ____|
 \ \_/ / |  | | |  | | | |   | |  | | (___ | |__   
  \   /| |  | | |  | | | |   | |  | |\___ \|  __|  
   | | | |__| | |__| | | |___| |__| |____) | |____ 
   |_|  \____/ \____/  |______\____/|_____/|______|
                                                  


"""

thanks_for_playing = r"""

 _____ _   _    _    _   _ _  ______    _____ ___  ____  
|_   _| | | |  / \  | \ | | |/ / ___|  |  ___/ _ \|  _ \ 
  | | | |_| | / _ \ |  \| | ' /\___ \  | |_ | | | | |_) |
  | | |  _  |/ ___ \| |\  | . \ ___) | |  _|| |_| |  _ < 
  |_| |_| |_/_/   \_\_| \_|_|\_\____/  |_|   \___/|_| \_\
                                                         
 ____  _        _ __   _____ _   _  ____                 
|  _ \| |      / \\ \ / /_ _| \ | |/ ___|                
| |_) | |     / _ \\ V / | ||  \| | |  _                 
|  __/| |___ / ___ \| |  | || |\  | |_| |                
|_|   |_____/_/   \_\_| |___|_| \_|\____|                


"""

def num_guess_game():
    print(Welcome_intro)
    print("Instructions: number should be a valid integer between 1 and 100 inclusively.")
    num_of_guess = 7
    number = randint(1, 100)

    while num_of_guess > 0:
        try:
            guess_number = int(input("Enter the number to guess: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        if guess_number == number:
            print(f"The number was {guess_number}")
            print(you_win)
            break  # Exit the loop on a win
        elif guess_number < number:
            print("TOO LOW!")
        else:
            print("TOO HIGH!")

        num_of_guess -= 1
        print(f"Guesses left: {num_of_guess}")

    if num_of_guess == 0:
        print(f"The number was {number}")
        print(you_lose)

def play_again():
    while True:
        again = input("Do you want to play again? (yes/no): ").strip().lower()
        if again in ('yes', 'y'):
            num_guess_game()
        elif again in ('no', 'n'):
            print(thanks_for_playing)
            break
        else:
            print("Please enter 'yes' or 'no'.")

if __name__=="__main__":
    num_guess_game()
    play_again()
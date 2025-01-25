import random

rps = r"""

█▀█ █▀█ █▀▀ █▄▀  
█▀▄ █▄█ █▄▄ █░█  

█▀█ ▄▀█ █▀█ █▀▀ █▀█  
█▀▀ █▀█ █▀▀ ██▄ █▀▄  

█▀ █▀▀ █ █▀ █▀ █▀█ █▀█ █▀
▄█ █▄▄ █ ▄█ ▄█ █▄█ █▀▄ ▄█

"""
# ASCII Arts for rock, paper, and scissors by Veronica Karlsson
ascii_art_list ={
    "rock" : '''  
    _______
---'   ____)  
      (_____)  
      (_____)  
      (____)
---.__(___)  
''',

"paper" : '''  
    _______
---'   ____)____  
          ______)  
          _______)  
         _______)
---.__________)  
''',

"scissors" : '''  
    _______
---'   ____)____  
          ______)  
       __________)  
      (____)
---.__(___)  
'''  
}

you_win = r"""

__   _____  _   _  __        _____ _   _ 
\ \ / / _ \| | | | \ \      / /_ _| \ | |
 \ V / | | | | | |  \ \ /\ / / | ||  \| |
  | || |_| | |_| |   \ V  V /  | || |\  |
  |_| \___/ \___/     \_/\_/  |___|_| \_|

"""

you_lose = r"""

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

def win_condition(comp_guess, your_guess):
    if comp_guess == your_guess:
        print("It's a tie!")
    elif (comp_guess == "rock" and your_guess == "paper") or \
         (comp_guess == "paper" and your_guess == "scissors") or \
         (comp_guess == "scissors" and your_guess == "rock"):
        print(you_win)
    else:
        print(you_lose)

def play_game():
    print(rps)
    print("Welcome to the rock paper scissors game\n\n")
    guesses = ["rock", "paper", "scissors"]
    while True:
        comp_guess = random.choice(guesses)
        your_guess = input("Enter rock paper or scissors as your option below:-\n")
        if your_guess in guesses:
            print(f"Your guess : {your_guess}")
            print(ascii_art_list[your_guess])
            print(f"Computer guess : {comp_guess}")
            print(ascii_art_list[comp_guess])
            win_condition(comp_guess,your_guess)
            break
        else:
            print("ERROR!!! incorrect option\n")
            

def play_again():
    while True:
        again = input("Do you want to play again? (yes/no): ").strip().lower()
        if again in ('yes', 'y'):
            play_game()
        elif again in ('no', 'n'):
            print(thanks_for_playing)
            break
        else:
            print("Please enter 'yes' or 'no'.")


if __name__=="__main__":
    play_game()
    play_again()

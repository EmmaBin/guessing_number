"""A number-guessing game."""
from random import randint
best_score = 101
def guessingGame():
    low_num = int(input('Pick a low number to start with.'))
    high_num = int(input('Now pick a high number.'))
    secret_num = randint(low_num, high_num)
    print(secret_num)
    print(f"{name}, I'm thinking of a number between {low_num} and {high_num}.")

    guess_count = 0
    while True:
        while True:
            user_guess = input("Guess a number: ")
            try:
                int(user_guess)
            except:
                print("ERROR: Please input a number.")
            else:
                user_guess = int(user_guess)

                if user_guess < low_num or user_guess > high_num:
                    print(f"ERROR: Please choose a number between {low_num} and {high_num}.")
                else:
                    break
        guess_count += 1
        if user_guess == secret_num:        
            print(f'Well done, {name} you guessed the correct number in {guess_count} tries!')
            return guess_count
            break
        elif user_guess > secret_num:
            print('Your guess is too high, try again!')  
        else:
            print('Your guess is too low, try again!')

        if guess_count == 10:
            print('Too many tries!')
            # set guess_count = 0
            return guess_count
            break
            


def com_vs_human():
    human_num= int(input("Please think about a number: "))
    start_num = int(input("Set a low number for computer: "))
    end_num=int(input("Set a high number for computer: "))
    com_guess= randint(start_num,end_num)
    while True:
        print(f"The computer guessed {com_guess}." )
        user_response= input("Answer 'Too high' 'Too low' or 'You won': ").lower()
        if user_response == "too high":
            end_num = com_guess-1
            com_guess=randint(start_num,end_num)
        elif user_response == "too low":
            start_num = com_guess+1
            com_guess=randint(start_num,end_num)
        else:
            print("You won!!!")
            break

        

print('Howdy, what is your name?')
name = input('type in your name: ')
print("We're going to play a number guessing game! Do you want to guess the computer's number, or do you want the computer to guess your number?")

play_again = True
while play_again: 
    who_plays = input('Type A if you would like to guess. Type B if you would like the computer to guess: ')
    if who_plays == 'A':
        guess_count = guessingGame()
        if guess_count < best_score:
            best_score = guess_count
            print(f'Congratulations, you have a new best score {best_score}!')
        else:
            print(f'You still have not beaten your best score of {best_score}, try again!')    
    else:
        com_vs_human()
    player_choice = input('Would you like to play again? y/n: ')
    if player_choice == 'n':
        play_again = False
    


        


# loop
    # ask user for guess number
    #check if it's an integer and if it's within the range
        # if invalid input: print error message and prompt again
        # if valid: 
#count the guess 
#compare the guess number from the user with the real secret number every time and print 
    # if too high:
    # if too low: 
    # if correct: exit loop
# increase the number of guesses
# print well done 






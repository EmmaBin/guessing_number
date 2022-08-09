"""A number-guessing game."""
from random import randint
print('Howdy, what is your name?')
name = input('type in your name: ')
secret_num = randint(1, 100)
print(f"{name}, I'm thinking of a number between 1 and 100.")

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

            if user_guess < 1 or user_guess > 100:
                print("ERROR: Please choose a number between 1 and 100.")
            else:
                break
    guess_count += 1
    if user_guess == secret_num:        
        print(f'Well done, {name} you guessed the correct number in {guess_count} tries!')
        break
    elif user_guess > secret_num:
        print('Your guess is too high, try again!')  
    else:
        print('Your guess is too low, try again!')




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
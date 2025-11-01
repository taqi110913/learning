import random
number = random.randint(1, 100)
number_of_guesses = 0
max_guesses = 10
while number_of_guesses < max_guesses:
    print("Guess a number between 1 and 100:")
    guess = int(input())
    number_of_guesses += 1
    if guess == number:
        print(f"Yes! That's the magic number! You found it in {number_of_guesses} guesses!")
        break
    else:
        if guess < number:
            print("Your guess is too low.")
        else:
            print("Your guess is too high.")
        print(f"Darn, that wasn't the right number. You have {max_guesses - number_of_guesses} guesses left to guess the magic number!")
if number_of_guesses == max_guesses:
    print(f"Aww, you ran out of guesses. The magic number was {number}.")
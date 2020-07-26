import random

play_game = 'y'

while play_game == 'y':
    answer = random.randint(1, 100)
    try_number = input("Guess a number between 1 to 100 : ")
    try_number = int(try_number)
    counter = 1

    while try_number != answer:
        if try_number > answer:
            print("Your number is too large.")
        elif try_number < answer:
            print("Your number is too small.")
        try_number = int(input("Guess a number between 1 to 100 : "))
        counter += 1
    print(f"You got it. You tried {counter} times !!")
    play_game = input("Continue ? Please enter y or n : ")

print("\nThank you for playing with us !")
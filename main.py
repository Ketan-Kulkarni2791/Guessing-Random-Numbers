import random

flag = True
while flag:
    num = input("Please enter the number of upper limit : ")

    # If we put negative no. i.e. -7, technically - is not digit. So it won't accept it.
    if num.isdigit():
        print("Let's Play !")
        num = int(num)
        flag = False
    else:
        print("Invalid input ! Please Try again !")

secret = random.randint(1, num)

guess = None
count = 1

while guess != secret:
    guess = input(f"Please type a number between 1 and {num} : ")
    if guess.isdigit():
        guess = int(guess)

    if guess == secret:
        print("You have guessed correct number.")
    else:
        print("Sorry, not a correct number ! Please try again.")
        count += 1

print(f"It took you {count} number of count to guess the correct number.")


from random import randint as rand
num = rand(1, 9)
guess = 0
attempts = 0

while guess != num:
    guess = int(input("Guess: "))
    print(guess)
    if guess > num:
        print("Too high!")
        attempts += 1
    elif guess < num:
        print("Too low!")
        attempts += 1
print(f"Well done after {attempts} attempts! Play again? ")

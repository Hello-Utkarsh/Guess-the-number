import random
number = random.randint(0, 100)
print("The computer has thought of a number, can you guess it?")
for i in range(1,9):
    n = int(input("Enter the number\n"))
    if n==number:
        print("You Got That Right!")
        break
    elif n>number:
        print("High")
    else:
        print("Low")
    print(f"You got {8-i} turns left")
    if i == 8:
        print("Better Luck Next Time!")
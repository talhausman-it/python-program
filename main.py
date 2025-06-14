import random

print("1 for snake (s)")
print("-1 for water (w)")
print("0 for gun (g)")

youdic = {'s': 1, 'w': -1, 'g': 0}
reversdic = {1: 's', -1: 'w', 0: 'g'}

compter = random.choice([1, -1, 0])
youstr = input("Enter your choice (s/w/g): ")

if youstr not in youdic:
    print("Invalid input! Choose s, w, or g.")
else:
    you = youdic[youstr]
    print(f"You chose: {reversdic[you]} | Computer chose: {reversdic[compter]}")

    if compter == you:
        print("Draw")
    elif (compter == 1 and you == 0) or (compter == 0 and you == -1) or (compter == -1 and you == 1):
        print("You lose")
    else:
        print("You win")
  


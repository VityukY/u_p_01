import random

rock = """
    ______
---'   ___)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    ______
---'   ___)_____
          ______)
       __________)
      (___)
---.__(__)
"""
main_rules = """
1/ Rock wins against scissors.
2/ Scissors win against paper.
3/ Paper wins against rock.
"""
signs = [rock, paper, scissors]

while True:
    user_choise = int(
        input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n")
    )
    print(f"Your choise is:\n{signs[user_choise]}")
    pc_chose = random.randint(0, 2)
    print(f"PC choise is:\n{signs[pc_chose]}")
    if user_choise == pc_chose:
        print("That draw. Try again")
        continue
    if (
        user_choise == 0
        and pc_chose == 1
        or user_choise == 1
        and pc_chose == 2
        or user_choise == 2
        and pc_chose == 0
    ):
        print("You lose")
    else:
        print("You win!")

    cont = input("Do you wanna play again Yes or No\n").lower()
    if cont == "no":
        print("Game over. Thx")
        break

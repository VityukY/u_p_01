print("The Love Calculator is calculating your score...")
name1 = "Pierre Curie"  # What is your name? #switched to input
name2 = "Marie Curie"  # What is their name? #switched to input
# 🚨 Don't change the code above 👆
# Write your code below this line 👇


score1 = 0
score2 = 0
true_list = ["t", "r", "u", "e"]
love_list = ["l", "o", "v", "e"]
name1, name2 = name1.lower(), name2.lower()

for char in true_list:
    score1 += name1.count(char)
    score1 += name2.count(char)
for char in love_list:
    score2 += name1.count(char)
    score2 += name2.count(char)

total_score = str(score1) + str(score2)
if 39 < int(total_score) < 51:
    print(f"Your score is {total_score}, you are alright together.")
elif int(total_score) > 89 or int(total_score) < 11:
    print(f"Your score is {total_score}, you go together like coke and mentos.")
else:
    print(f"Your score is {total_score}.")

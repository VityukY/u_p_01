line1 = ["⬜️", "️⬜️", "️⬜️"]
line2 = ["⬜️", "⬜️", "️⬜️"]
line3 = ["⬜️️", "⬜️️", "⬜️️"]
map = [line1, line2, line3]
print("Hiding your treasure! X marks the spot.")
position = "B3".upper()  # Where do you want to put the treasure? #example
# 🚨 Don't change the code above 👆
# Write your code below this row 👇
ind_1 = position[0]
ind_2 = int(position[1]) - 1

abc = ["A,", "B", "C"]
letter_index = abc.index(ind_1)


map[ind_2][letter_index] = "X"

# Write your code above this row 👆
# 🚨 Don't change the code below 👇

print(f"{line1}\n{line2}\n{line3}")

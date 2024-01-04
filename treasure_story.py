StoryTelling = True
while StoryTelling:
    print(
        '''
   *******************************************************************************
            |                   |                  |                     |
   _________|________________.=""_;=.______________|_____________________|_______
   |                   |  ,-"_,=""     `"=.|                  |
   |___________________|__"=._o`"-._        `"=.______________|___________________
            |                `"=._o`"=._      _`"=._                     |
   _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
   |                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
   |___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
            |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
   _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
   |                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
   |___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
   ____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
   /______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
   ____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
   /______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
   ____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
   /______/______/______/______/______/______/______/______/______/______/_____ /
   *******************************************************************************
   '''
    )
    print("Welcome to Treasure Island.")
    print("Your mission is to find the treasure.")
    print("You're at a crossroad. Where do you want to go? Type 'left' or 'right'")
    answ = input().lower()
    if answ == "right":
        print("Fall in a hole. Game over")
        StoryTelling = False
        break
    print(
        "You've come to a lake. There is an island in the middle of the lake. Type 'wait' to wait for a boat. Type 'swim' to swim across."
    )
    answ = input().lower()
    if answ == "swim":
        print(
            '''
                                        ,-
                                    ,'::|
                                    /::::|
                                    ,'::::o\                                      _..
                ____........-------,..::?88b                                  ,-' /
        _.--"""". . . .      .   .  .  .  ""`-._                           ,-' .;'
        <. - :::::o......  ...   . . .. . .  .  .""--._                  ,-'. .;'
        `-._  ` `":`:`:`::||||:::::::::::::::::.:. .  ""--._ ,'|     ,-'.  .;'
            """_=--       //'doo.. ````:`:`::::::::::.:.:.:. .`-`._-'.   .;'
                ""--.__     P(       \               ` ``:`:``:::: .   .;'
                        "\""--.:-.     `.                             .:/
                        \. /    `-._   `.""-----.,-..::(--"".\""`.  `:\
                        `P         `-._ \          `-:\          `. `:\
                                        ""            "            `-._)  -Seal


'''
        )
        print("Attacked by trout. Game over")
        StoryTelling = False
        break
    print(
        "You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose?"
    )
    answ = input().lower()
    if answ == "red":
        print(
            """               (  .      )
                )           (              )
                        .  '   .   '  .  '  .
                (    , )       (.   )  (   ',    )
                .' ) ( . )    ,  ( ,     )   ( .
            ). , ( .   (  ) ( , ')  .' (  ,    )
            (_,) . ), ) _) _,')  (, ) '. )  ,. (' )
        jgs^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
        """
        )
        print("Burned by fire. Game over")
        StoryTelling = False
    if answ == "blue":
        print("Eaten by Beasts. Game over")
        StoryTelling = False
    if answ == "Yellow":
        print("Died in dessert. Game over")
        StoryTelling = False
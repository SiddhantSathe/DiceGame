import random

list = [1,2,3,4,5,6]
player1 = input("Player1, Enter your name: ")
player2 = input("Player2, Enter your name: ")
print("Hi " + player1 + " & "+ player2 +" Welcome to the game of dice.")
print("""Rules:
       Player will roll dice untill player gets number 1.
       When player receives 1 his chance to roll terminates and next player start to roll.
       Player can leave the game anytime by pressing any key except y.
       At the end of the game the total score of each player will be displayed.
       The player with the highest number wins.
       !!!ALL THE BEST!!!""")
def roll():
    total=0
    print("do you want to roll? Press y for yes:")
    consent=input()
    while consent == "y":
        number = random.choice(list)
        if number != 1:
            print("the dice roll is {}".format(number))
            total =total + number
            print("YOUR TOTAL IS {}".format(total))
            print("do you want to roll? Press y for yes:")
            consent = input()
        else:
            print("the dice roll is {}".format(number))
            print("your turn is over")
            break
    return total
print("Its {}'s turn".format(player1))
p1=roll()
print("FINAL SCORE OF {} is {}".format(player1,p1))
print("Now its {}'s turn".format(player2))
p2=roll()
print("FINAL SCORE OF {} is {}".format(player2,p2))
if p1>p2:
    print("{} wins".format(player1))
elif p2>p1:
    print("{} wins".format(player2))
else:
    print("Its a tie")    

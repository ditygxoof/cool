import random
suits = ["clubs", "diamonds", "hearts", "spades"]
faces = ["two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "jack", "queen", "king", "ace"]
computer_points = 0
player_points = 0
amountofrounds = 0
keep_going = True
while keep_going:
    my_face = random.choice(faces)
    my_suit = random.choice(suits)
    your_face = random.choice(faces)
    your_suit = random.choice(suits)
    print("I have the", my_face, "of", your_suit)
    print("You have the", your_face, "of", your_suit)
    if faces.index(my_face) > faces.index(your_face):
        print("I win!")
        computer_points+= 1
        amountofrounds+= 1
        
        
    elif faces.index(my_face) < faces.index(your_face):
        print("You win!")
        player_points+= 1
        amountofrounds+= 1
    else:
        print("It's a tie!")
        amountofrounds+= 1
    answer = input("Hit [Enter] to keep going, any key to exit.")
    print("Computer points: ", computer_points, "Your points:", player_points, "Amount of rounds:", amountofrounds)
    if player_points == computer_points:
         print("Tie")
    elif player_points > computer_points:
         print("Player Winning")
    else:
         print("Computer Winning")
    
   
    
    keep_going = (answer == "")
              

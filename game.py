import time
import random 

# the places in which the user can be present
place = ["FARM", "STORAGE", "FACTORY",]
user_place = random.choice(place)

# action when the user is in the farm
def farm_exploration(score):
    print("After you woke up, you found yourself very wet because there was a severe storm last night. You decided to explore the farm.")
    time.sleep(2)
    print("You found the farm's door.")
    time.sleep(2)
    print("Do you enter?")
    time.sleep(2)
    print("1. YES")
    time.sleep(2)
    print("OR")
    time.sleep(2)
    print("2. NO")

    choice = input("1 OR 2: ")

    while choice not in ["1", "2"]:
        print("CHOOSE THE NUMBER 1 OR 2 ONLY")
        choice = input("1 OR 2: ")

    if choice == "1":
        score += 100
        print("Your score is:", score)
        time.sleep(3)
        print("You find a strange man.")
        time.sleep(2)
        print("He seems to be the owner of the farm.")
        time.sleep(2)
        print("You try to get closer, but he looks a little scary. You don't know his intentions. You tap him on the shoulder, and he turns to you and raises a gun at you. He asks who you are. What do you do?")
        time.sleep(2)
        print("1. Talk to him and tell him your story.")
        time.sleep(2)
        print("OR")
        time.sleep(2)
        print("2. Run away.")
        time.sleep(2)


        choice = input("1 OR 2: ")

        while choice not in ["1", "2"]:
            print("CHOOSE THE NUMBER 1 OR 2 ONLY")
            choice = input("1 OR 2: ")

        if choice == "1":
            score += 100
            print("Your score is:", score)
            time.sleep(2)
            print("You are really brave.")
            time.sleep(2)
            print("The man understood your situation, apologized,") 
            time.sleep(2)
            print("and helped you reach the police station and get home.")
            time.sleep(2)
            print("Hooray, you did it!")


        elif choice == "2":
            score = 0
            print("Your score is:", score)
            time.sleep(3)
            print("You lose your SOUL and your SCORE.")
            print("When you decided to escape and run away,")
            print("the man shot you. He thought you were a thief or a harmful person,")
            print("and your escape confirmed his suspicion.")


    elif choice == "2":
        score = 0
        print("Your score is:", score)
        time.sleep(2)
        print("You have decided not to enter the farm gate. But what will you do?")
        time.sleep(2)
        print("Will you remain like that? ")
        print("..........")
        time.sleep(2)
        print("Not trying to go to the cars or even enter the farm?")
        time.sleep(3)
        print("Relief will not come to you without effort.")
        time.sleep(2)
        print("The game has ended ")
        print("you LOSE because you did not try to save yourself.")
        time.sleep(2)

    return score




def main():
    score = 0

    # Introduction part
    print("You suddenly woke up in fear.")
    time.sleep(2)
    print("You found yourself in an unknown place.")
    time.sleep(2)
    print("And you don't even know where you are!!!")
    time.sleep(2)
    print("But it seems like ...")
    time.sleep(2)
    print(user_place)
    time.sleep(2)
    print("Now ....")
    time.sleep(2)
    print("Then you found a very bright white light.")
    time.sleep(3)
    print("Will you go to it....?")
    time.sleep(2)
    print("You have 2 options, choose just one.")
    time.sleep(4)
    print("1. YES")
    time.sleep(3)
    print("       OR ....")
    time.sleep(3)
    print("2. NO")

    # Get the player's first choice
    choice1 = input("1 OR 2: ")

    # Directly validate the choice
    while choice1 not in ["1", "2"]:
        print("CHOOSE THE NUMBER 1 OR 2 ONLY")
        choice1 = input("1 OR 2: ")

    # Handling the first choice
    if choice1 == "1":
        score += 100
        print("Your score is:", score)
        print("Will you try to go to the cars, but they are very far away?")
        time.sleep(2)
        print("OR")
        time.sleep(2)
        print("Will you try to discover this farm until the morning?")

        # Get the player's second choice
        choice2 = input("1 OR 2: ")

        # Directly validate the choice
        while choice2 not in ["1", "2"]:
            print("CHOOSE THE NUMBER 1 OR 2 ONLY")
            choice2 = input("1 OR 2: ")


        # Handling the second choice
        if choice2 == "1":
            score += 100
            print("Your score is:", score)
            print("After you got closer and closer,")
            time.sleep(2)
            print("you found that it was a highway.")
            time.sleep(2)
            print("The cars were moving at very high speeds.")
            time.sleep(2)
            print("It was very dark around you.")
            time.sleep(2)
            print("You will try to stop a vehicle to help you.")
            time.sleep(2)
            print("1. With the risk that cars will not see you and you will wait a very long time with the small number of passing cars?")
            time.sleep(2)
            print("OR")
            time.sleep(2)
            print("2. You wait in the morning for the cars to see you and for you to rest a little?")




            # Get the player's third choice
            choice3 = input("1 OR 2: ")

            # Directly validate the choice
            while choice3 not in ["1", "2"]:
                print("CHOOSE THE NUMBER 1 OR 2 ONLY")
                choice3 = input("1 OR 2: ")

            if choice3 == "1":
                print("You decided to take the risk and try to stop a car.")
                time.sleep(2)
                print("and NOW .....")
                time.sleep(2)
                print(".....")
                time.sleep(2)
                print("Hurray, you did it and finally")
                time.sleep(2)
                print("They will take you to the nearest police station to help you find your location and reach your home.")

            elif choice3 == "2":
                score += 50
                print("Your score is:", score)
                print("but ...")
                time.sleep(2)
                print("This was a great waste of time.")
                time.sleep(2)
                print("You decided to wait until morning to increase your chances of being seen.")
                time.sleep(2)
                print("After you woke up,")
                time.sleep(2)
                print("someone was waking you up. You found yourself very wet from the winter that happened while you were sleeping. When you woke up, you found a broken-down car near you. The driver woke you up to help you and actually took you to the nearest police station to help you find your home.")
                time.sleep(2)
                print("Finally, they will take you to the nearest police station to help you find your location and reach your home.")
       

        elif choice2 == "2":
            score += 50
            print("Your score is:", score)
            score = farm_exploration(score)
       

    elif choice1 == "2":
        score += 50
        print("Your score is:", score)
        print("You chose to stay on the farm until morning. It was a wise choice.")
        time.sleep(2)
        score = farm_exploration(score)


    final_score(score)
    play_again()

def final_score(score):
    print("Your final score is:", score)
    if score == 0:
        print("YOU LOSE!")
    else:
        print("YOU WIN!")

    print("")
    print("DO YOU WANT TO PLAY AGAIN?")
    print("1. YES")
    print("2. NO")

def play_again():
    choice = input("1 OR 2: ")

    # Asking the player to play again y/n
    while choice not in ["1", "2"]:
        print("CHOOSE THE NUMBER 1 OR 2 ONLY")
        choice = input("1 OR 2: ")

    if choice == "1":
        main()
    elif choice == "2":
        print("Good game, see you later")

if __name__ == "__main__":
    main()

import random
while True:
    health=200
    print("="*90)
    print(" ⚔️ MONSTER BATTLE ⚔️".center(90))
    print("="*90)
    print(' Defeat the Boss "SUPERMAN" to Save the Kingdom!'.center(90))
    print("Kill The Boss Without Dying To Win".center(90))
    boss_health=650
    print("="*90)
    character=["Goblin", "Skeleton", "Zombie", "Dragon"]
    print("The characters are: ", character)
    choice=input("Do you want to choose your character or let the computer choose for you? (y/n): ")
    print()
    if choice.upper()=="N":
        random_character=random.choice(character)
        print("The computer has chosen: ", random_character)
    elif choice.upper()=="Y":
        user_character=input("Which character do you want to choose?(1/2/3/4)? ")
        print("You have chosen: ", character[int(user_character)-1])
    else:
        print("Invalid choice")
        exit()
    print("Health of your character is: ", health,"❤️")
    print("-"*90)
    print("The Boss has appeared!".center(90))
    print(f"Boss Health: {boss_health}".center(90))
    print("-"*90)
    while health>0 and boss_health>0:
        option=["Attack","Heal","your status","Run"]
        for i in range(len(option)):
            print(i+1, option[i])
        move=input("What do you want to do? (1/2/3/4): ")
        print("-"*90)
        if move=="1":
            boss_health-=52
            print("You attacked the Superman!")
            print("damage dealt: 52")
            print(f"Superman's HP: {boss_health}")
            print()
            if boss_health<=0:
                break
            print("superman attacks you!")
            health-=18
            print(f"your health: {health}")
            print("-"*90)
            print(f"Boss Health: {boss_health}".center(90))
            print("-"*90)
        elif move=="2":
            if health>=200:
                print("You are already at full health!")
                print(f"your health: {health}")
                print("-"*90)
            else:
                health+=50
                print("You healed yourself!")
                if health>200:
                    health=200
                print(f"your health: {health}")
                print()
                print("superman attacks you!")
                health-=10
                print(f"your health is now: {health}")
                print("-"*90)
        elif move=="3":
            print("="*90)
            print("YOUR STATUS".center(90))
            print()
            print(f"Health Of Your Character: {health}/200")   
            print()
            print()
            print("BOSS STATUS".center(90))
            print()
            print("Boss: Superman")
            print(f"health: {boss_health}/650")
            print("="*90)
        elif move=="4":
            print("You ran away from the battle!")
            print()
            print("#"*90)
            print("GAME OVER".center(90))
            print("#"*90)
            print("You ran away from the battle and lost the game!")
            print("Superman has taken over the kingdom and you have failed to save it!") 
            print("-"*90)
            exit()
        else:
            print("Invalid option! Choose 1, 2, 3, or 4.")
    if health<=0:
        print()
        print("#"*90)
        print("GAME OVER".center(90))
        print("#"*90)
        print()
        print("superman has defeated you and taken over the kingdom!")
        print("You have failed to save the kingdom!")
        print("Better luck next time!")
    elif boss_health<=0:
        print()
        print("#"*90)
        print("YOU WIN!".center(90))
        print("#"*90)
        print()
        print("You have defeated the boss and saved the kingdom!")
        print("Congratulations!")
        print("You are a true hero!")
        print("Thank you for playing the game!")
    break
    
    




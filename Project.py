#Hana Parcell

#April 13, 2022

#Py Fighter Project



import random, time


START = input("Would you like to play Py Fighter? Y/N: ").upper()



while START == "Y" or START == "N":

    
    

    if START == "Y": 

        P1_Strength = int(input("Player 1, what level strength are you? From 1-50"))
        P1_Armor = int(input("Player 1, how much armor do you yield? From 1-50"))

        if P1_Strength < 0 or P1_Strength > 50:
            print("Cheater. You lost. L")
            break

        if P1_Armor < 0 or P1_Armor > 50:
            print("Cheater. You lost. L")
            break
        

        #P2 strength + armor

        P2_Strength = int(input("Player 2, what level strength are you? From 1-50"))
        P2_Armor = int(input("Player 2, how much armor do you yield? From 1-50"))

        if P2_Strength < 0 or P2_Strength > 50:
            print("Cheater. You lost. L")
            break

        if P2_Armor < 0 or P2_Armor > 50:
            print("Cheater. You lost. L")
            break

        #P1 dices
        while P1_Strength > 0 or P2_Strength > 0: 
            P1_Turn = input("Player 1, would you like to roll your dice? Y/N >").upper()

            if P1_Turn == "Y":
                P1_Dice = round(P1_Strength / 10)

                print("Player 1, you have", P1_Dice, "dice.")
            else:
                print("Why would you do that? you lost. L")
                break 

            #P2 Dices   

            P2_Turn = input("Player 2, would you like to roll your dice? Y/N >").upper()

            if P2_Turn == "Y":
                P2_Dice = round(P2_Strength / 10)

                print("Player 2, you have", P2_Dice, "dice.")
            else:
                print("Why would you do that? you lost. L")
                break 



            #PLAYER 1 DICE ROLL

            P1_Total = 0
            dice_num = P1_Dice
            sides = 6
            P1_DiceRoll = [random.randint(1, sides) for _ in range(dice_num)]

            for ele in range(0, len(P1_DiceRoll)):
                P1_Total = P1_Total + P1_DiceRoll[ele]


            print("PLayer 1, you rolled a", P1_Total)
            P1_Strength = P1_Total

            #PLAYER 2 DICE ROLL

            P2_Total = 0
            dice_num = P2_Dice
            sides = 6
            P2_DiceRoll = [random.randint(1, sides) for _ in range(dice_num)]

            for ele in range(0, len(P2_DiceRoll)):
                P2_Total = P2_Total + P2_DiceRoll[ele]

            print("Player 2, you rolled a", P2_Total)
            P2_Strength = P2_Total


            print("Ready... Set... Fight!")

            time.sleep(1)

            
            #Damage

            if P1_Strength > P2_Strength:
                damage = P1_Strength - P2_Strength
                print("Oh no! Player 2, you have been dealt", damage, "damage!")
                print("Player 1, your health is now", P1_Strength)
                print("Player 1, your health is now", P2_Strength)
                

            else:
                damage = P2_Strength - P1_Strength
                print("Oh no! Player 1, you have been dealt ", damage, "damage!")
                print("Player 1, your health is now", P1_Strength)
                print("Player 2, your health is now", P2_Strength)


            if P1_Strength <= 0:
                print("Player 1, you have been defeated. L.")
                break

            else:
                if P2_Strength <= 0:
                    print("Player 2, you have been defeated. L.")
                    break

        START = input("Would you like to play Py Fighter? Y/N: ").upper()
    
    else:

        START = input("Would you like to play Py Fighter? Y/N: ").upper()





            

    

            
            

    

    
    
    





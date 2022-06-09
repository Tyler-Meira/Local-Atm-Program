

# Assignment 04 
# Tyler Meira
# Humber Atm

# This assignment was designed to simulate the basic functions of real atm, 
# storing values locally, using different concepts went over in class.

#The first section of this code is the pin system the program askes you to 


counter = 0;
pinOk = False
userPin = 1111
userBalance = 100

while 1 == 1:
    print(" ")
    print("Welcome to the Humber Atm")
    print(" ")
    while 1 == 1:
        pinInput = int(input("Please Enter Your 4 Digit Pin: "))

        if(pinInput == userPin):
            print("Welcome!")
            pinOk = True
            break;
        else: 
            if(counter >= 2):
                print("You have entered the wrong pin too many times!")
                break
            else:
                print("Invalid pin")
                counter = counter + 1;
                continue

    if(pinOk == True):
        # do nothing
        print(" ")
    else:
        break
         
    while 1 == 1:
        
        print("Please Press 1 For Your Balance")
        print("Please Press 2 To Make A Withdrawl")
        print("Please Press 3 To Pay In")
        print("Please Press 4 To Return Card")
        print(" ")

        userInput = int(input("Please Select An Option: "))

        if(userInput == 1):
            print(userBalance)
            print(" ")

                
            goBack = input("Would You Like To Go Back? : ")

            if(goBack == 'no'):
                break
            elif(goBack == 'yes'):
                print("")
                continue

        elif(userInput == 2):
            print("How Much Would you like to withdraw")
            print("$10")
            print("$20")
            print("$40")
            print("$60")
            print("$80")
            print("$100")
            
            userWithdraw = int(input("For other enter 1: "))
            
            if(userWithdraw == 10):
                if(userWithdraw > userBalance):
                    print("Invalid Ammount")
                else:
                    userBalance = userBalance - userWithdraw
                    print("Your Balance Is Now $ ", userBalance)
            elif(userWithdraw == 20):
                if(userWithdraw > userBalance):
                    print("Invalid Ammount")
                else:
                    userBalance = userBalance - userWithdraw
                    print("Your Balance Is Now $ ", userBalance)
            elif(userWithdraw == 40):
                if(userWithdraw > userBalance):
                    print("Invalid Ammount")
                else:
                    userBalance = userBalance - userWithdraw
                    print("Your Balance Is Now $ ", userBalance)
            elif(userWithdraw == 60):
                if(userWithdraw > userBalance):
                    print("Invalid Ammount")
                else:
                    userBalance = userBalance - userWithdraw
                    print("Your Balance Is Now $ ", userBalance)
            elif(userWithdraw == 80):
                if(userWithdraw > userBalance):
                    print("Invalid Ammount")
                else:
                    userBalance = userBalance - userWithdraw
                    print("Your Balance Is Now $ ", userBalance)
            elif(userWithdraw == 100):
                if(userWithdraw > userBalance):
                    print("Invalid Ammount")
                else:
                    userBalance = userBalance - userWithdraw
                    print("Your Balance Is Now $ ", userBalance)
            elif(userWithdraw == 1):
                userWithdrawCustom = int(input("Please Enter Desired Amount: "))
                if(userWithdrawCustom > userBalance):
                    print("Invalid Ammount")
                else:
                    print(userBalance)
                    userBalance = userBalance - userWithdraw
                    print("Your Balance Is Now $ ", userBalance)
                
            
            goBack = input("Would You Like To Go Back? : ")

            if(goBack == 'no'):
                break
            elif(goBack == 'yes'):
                print("")
                continue
            else:
                print(" ")
            
        elif(userInput == 3):
            
            userDeposit = int(input("How Much Would You Like to Deposit?"))
            userBalance = userBalance + userDeposit
            
            print("")
            print("Your new Balance is : $", userBalance)
            
            goBack = input("Would You Like To Go Back? : ")

            if(goBack == 'no'):
                break
            elif(goBack == 'yes'):
                print("")
                continue
            else:
                print(" ")
            
        elif(userInput == 4):
            print("Please wait whilst your card is Returned...")
            print("")
            print("Thank You!, Good Bye.")
            break
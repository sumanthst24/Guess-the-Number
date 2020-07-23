import random
import sys


def number_generation():
    generated_number=int(random.randrange(1,20))
    #print(generated_number)
    return generated_number

    

def startGame():
    print("A number is being generated ...")
    generated_number=number_generation()
    number_of_chances=3
    current_chance=1
    guessed_number=0
    while(current_chance<=3):
        print("Guess the number")
        guessed_number=int(input())
        if(guessed_number==generated_number and current_chance==1):
            print("WOW! You got it right in your first guess itself")
            print("Enter 1 if you want to play again or 2 to exit")
            break
        elif(guessed_number>generated_number):
            print("The number is less than "+str(guessed_number))
            current_chance+=1
            print("You lost a chance")
            print("You have "+str(number_of_chances-current_chance+1)+" chances remaining")
        elif(guessed_number<generated_number):
            print("The number is greater than "+str(guessed_number))
            current_chance+=1
            print("You lost a chance")
            print("You have "+str(number_of_chances-current_chance+1)+" chances remaining")
        elif(guessed_number==generated_number and current_chance<=3):
            print("Yes!You guessed it right")
            print("Enter 1 if you want to play again or 2 to exit")
            break
        if(current_chance==4):
            print("---   GAME OVER   ---")
            print("You couldn't make it")
            print("The number is generated is "+str(generated_number))
            print("Enter 1 if you want to play again or 2 to exit")
            break
            
    
    

print("============   Welcome to the game Guess the Number   ============")
print("A number is generated in between 1 and 20 inclusive")
print("You need to guess the exact number in less than 3 chances")
while(1):
    print("Choose your option")
    print("1.Start the game")
    print("2.Exit the game")
    n=(input())
    if(int(n)<1 and int(n)>2):
        print("Invalid Option")
        sys.exit()
    elif(n=='1'):
        startGame()
    elif(n=='2'):
            print("Thank you for playing !")
            print("Hope you had fun")
            sys.exit()
    else:
        print("You selected an invalid option")
        sys.exit()

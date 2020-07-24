import random#import random to generate random number
import sys#to exit from the program


def number_generation():
    generated_number=int(random.randrange(1,20))#randrange generates a random number between 1 and 20
    #print(generated_number)
    return generated_number

    

def startGame():
    print("A number is being generated ...")
    generated_number=number_generation()#return from the function call
    number_of_chances=3#number of chances
    current_chance=1#tracking the current chance
    guessed_number=0
    while(current_chance<=3):
        print("Guess the number")
        guessed_number=int(input())#take input from the number
        if(guessed_number==generated_number and current_chance==1):#if its the first and correct guess
            print("WOW! You got it right in your first guess itself")#print that guess is correct
            print("Enter 1 if you want to play again or 2 to exit")#ask if the user want to play again
            break
        elif(guessed_number>generated_number):#if the number guessed is greater than the number generated
            print("The number is less than "+str(guessed_number))#print the number generated is less than number guessed
            current_chance+=1#increment the chances used by 1
            print("You lost a chance")
            print("You have "+str(number_of_chances-current_chance+1)+" chances remaining")#display remaining chances
        elif(guessed_number<generated_number):#if the number guessed is lesser than the number generated
            print("The number is greater than "+str(guessed_number))#print the number generated is greater than number guessed
            current_chance+=1#increment the chances used by 1
            print("You lost a chance")
            print("You have "+str(number_of_chances-current_chance+1)+" chances remaining")#display remaining chances
        elif(guessed_number==generated_number and current_chance<=3):#if the guess is right within 3 chances
            print("Yes!You guessed it right")#display that guess is correct
            print("Enter 1 if you want to play again or 2 to exit")#ask if the user want to play again
            break
        if(current_chance==4):
            print("---   GAME OVER   ---")
            print("You couldn't make it")
            print("The number is generated is "+str(generated_number))#display the generated number
            print("Enter 1 if you want to play again or 2 to exit")#ask if the user want to play again
            break
            
    
    

print("============   Welcome to the game Guess the Number   ============")#display the game title
print("A number is generated in between 1 and 20 inclusive")#display the rules
print("You need to guess the exact number in less than 3 chances")
while(1):
    print("Choose your option")#display the options
    print("1.Start the game")
    print("2.Exit the game")
    n=(input())#read the input
    if(int(n)<1 and int(n)>2):#invalid choice
        print("Invalid Option")
        sys.exit()
    elif(n=='1'):
        startGame()#call startGame() function
    elif(n=='2'):
            print("Thank you for playing !")
            print("Hope you had fun")
            sys.exit()#exit
    else:
        print("You selected an invalid option")
        sys.exit()#exit

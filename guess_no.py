# Guess the number between 0 to 20 if the user guesses the number true then return success otherwise chck whether the the guess ws close or not+-*+++++++
import random                                                       
print("welcome to 'guess the number game': ")
b=True
while b:
    num=int(input("Enter a number between 0 to 20 : "))
    guess=random.randint(0,20)
    if num==guess:
        print("whooo! YOu got it man")

    elif num<int(guess)-3 or num>int(guess)+3:
        print("you lost it man")

    elif num<guess or num>guess:
        for i in range(1,4):
            if (num+i)==guess or (num-i)==guess:
                print("oops you were close")
                break
    
    print(f"original number: {guess}")
    print(f"guessed number : {num}")
    replay=input("Do u wanna play it again yes/no: ")
    if replay=="yes":
        b=True
    elif replay=="no":
        b=False
    else:
        print("Wrong entry :")
        b=False

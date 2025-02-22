print("Hey! Welcome to Guessing Game ")
score = 0
player = input("IF you don't Mind Can you Type Your Name : ")
print(f"Hi, {player} It's Pleasure ")
play = input("Do you want to Start the Games If your answer is Yes Please type yes or NO to cancel : ").lower()

if play == "yes":
    print("Your First Question ")


    while True:
        guess = input("what is the Capital of INDIA : ").lower()
        

        if guess == "delhi":
            print("That is Correct")
            score+=1
            print(f"Awesome ! Your Score is {score}")
        else:
            print("That's a wrong Answer")

        
        guess2 = input("What is the Capital of Japan : ").lower()
        if guess2 == "tokyo":
            print("That is Correct")
            score+=1
            print(f"Awesome ! Your Score is {score}")
        else:
            print("That's a wrong Answer")

        guess3 = input("What is the capital of Germany : ").lower()
        if guess3 == "berlin":
            print("Nice , That is the Correct Answer, You won the Game")
            score+=1
            print(f"Your Current Score is {score}")
        
        else:
            print("Answer Is Wrong . Try Again")
        print(f"You'r total score is {score}")
        break
else:
    print('Thanks for Visiting ! Goodbye')
    exit()

   


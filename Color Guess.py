import random, turtle, tkinter

def guess_game():

    def color(guess_x,guess_y,randvalue_x,randvalue_y):
        turtle.setpos(guess_x,guess_y)
        turtle.fillcolor(guess)
        turtle.begin_fill()
        turtle.circle(100)
        turtle.end_fill()

        turtle.setpos(randvalue_x,randvalue_y)
        turtle.fillcolor(randvalue)
        turtle.begin_fill()
        turtle.circle(100)
        turtle.end_fill()


    print("GUESS THE COLOR FROM THE LIST PROVIDED\n")
    print(colors)
    print("\nLet's Start The Game")
    print("(There are only 3 chances)\n")

    
    guess_x=-250
    guess_y=50

    randvalue_x=-250
    randvalue_y=-200

    for i in range(1,4):
        print("Enter your guess: ")
        guess=input().capitalize()

        input_screen = turtle.Turtle()
        turtle.setup(width=750, height=600)
        input_screen.screen.bgcolor("black")
        turtle.title("COLOR GUESS")
        turtle.pen(pencolor=None)
 
        randvalue=random.choice(colors)

        color(guess_x,guess_y,randvalue_x,randvalue_y)

        if (guess==randvalue):
            print("Your guess is right! \nYOU WON ")
            print("THANK YOU")
            break

        else:
            if(i==3):
                print("Sorry, You lost!\n")
                print("Enter '1' to try again")
                tryagain=int(input())

                if(tryagain==1):
                    turtle.clear()
                    guess_game()
                else:
                    print("THANK YOU")
                    exit()

            print("\nOhh Sorry\nYou are left with '" +str(3-i)+ "' chance/s\n")
            guess_x += 250
            randvalue_x += 250

    
colors= ['Blue','Red','Orange','Violet','Green','Yellow','White','Aqua','Gray','Pink','Brown','Purple','Maroon','Indigo','Magenta','Silver','Gold']
guess_game()


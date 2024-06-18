from tkinter import *

screen = Tk()  # Tk() class importing -creating object of Tk()
screen.geometry("500x500")
screen.title("ROCK PAPER SCISSOR")


"""
     python logic is here

"""

from random import choice

gameList=["ROCK","PAPER","SCISSOR"]


userchoicevar= StringVar()
userchoicevar.set("PENDING")

computerchoicevar=StringVar()
computerchoicevar.set("PENDING")

userScore=IntVar()
userScore.set(0)
computerScore=IntVar()
computerScore.set(0)
finalval=StringVar()

c_score=0
u_score=0
game_chance=0
def game(userChoice):
    global c_score,u_score,game_chance
    if game_chance==5:
        if u_score>c_score:
            finalval.set("User won the game")
        else:
            finalval.set("Computer won the game")
    else:            
    #print(userChoice)
        userchoicevar.set(userChoice)
        computer = choice(gameList)     # randomly generate value
        computerchoicevar.set(computer)
        if userChoice=="ROCK" and computer=="PAPER" or userChoice=="PAPER" and computer=="SCISSOR" or userChoice=="SCISSOR" and computer=="ROCK":
            c_score+=1
            computerScore.set(c_score)

        elif userChoice=="ROCK" and computer=="SCISSOR" or userChoice=="PAPER" and computer=="ROCK" or userChoice=="SCISSOR" and computer=="PAPER":
            u_score+=1
            userScore.set(u_score)     

        else:
            print("It's a TIE.....")    
        
        game_chance+=1


lbl= Label(screen,text="WELCOME TO ROCK PAPER SCISSOR GAME",font=("Arial",16,"bold"))
lbl.place(x=10,y=10)

btn = Button(screen,text="ROCK",font=("Arial",16,"bold"),bg="blue",fg="white",command=lambda : game("ROCK"))
btn.place(x=50,y=60)

btn = Button(screen,text="PAPER",font=("Arial",16,"bold"),bg="blue",fg="white",command=lambda : game("PAPER"))
btn.place(x=200,y=60)

btn = Button(screen,text="SCISSOR",font=("Arial",16,"bold"),bg="blue",fg="white",command=lambda : game("SCISSOR"))
btn.place(x=350,y=60)


# for user score section
lbl = Label(screen,text="USER",font=("Arial",16,"bold"))
lbl.place(x=30,y=160)

btn = Button(screen,textvariable=userchoicevar,font=("Arial",16,"bold"),bg="green",fg="white")
btn.place(x=200,y=150)

btn = Button(screen,textvariable=userScore,font=("Arial",16,"bold"),bg="cyan",fg="black")
btn.place(x=350,y=150)

# for computer score section 

lbl = Label(screen,text="COMPUTER",font=("Arial",16,"bold"))
lbl.place(x=30,y=220)

btn = Button(screen,textvariable=computerchoicevar,font=("Arial",16,"bold"),bg="green",fg="white")
btn.place(x=200,y=220)

btn = Button(screen,textvariable=computerScore,font=("Arial",16,"bold"),bg="cyan",fg="black")
btn.place(x=350,y=220)

#for final winner

lb1=Label(screen,textvariable=finalval,font=("Arial",16,"bold"),fg="red")
lb1.place(x=130,y=300)
screen.mainloop()
       
        
            

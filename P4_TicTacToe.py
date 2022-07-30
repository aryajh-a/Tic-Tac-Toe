from faulthandler import disable
from tkinter import *
# creating 1st window (menu)
root=Tk()
root.geometry("550x600")
root.configure(bg='lavender')
root.title("MENU")

class TicTacToe :

    turn=0                                              # to track which player's turn it is
     
    def click1(self):                                   # when 1st button is clicked
        if self.btn1.cget('text')=="":                  # so that button won't work more than once
            self.turn+=1
            if self.turn%2==0:
                self.btn1.config(text='X', font=('Times', 9, 'bold'), padx=41, fg='white')
            else:
                self.btn1.config(text='O', font=('Times', 10, 'bold'), padx=40, fg='yellow')
            self.checkifwon()
            self.playerturn()

    def click2(self):
        if self.btn2.cget('text')=="":
            self.turn+=1
            if self.turn%2==0:
                self.btn2.config(text='X', font=('Times', 9, 'bold'), padx=41, fg='white')
            else:
                self.btn2.config(text='O', font=('Times', 10, 'bold'), padx=40, fg='yellow')
            self.checkifwon()
            self.playerturn()

    def click3(self):
        if self.btn3.cget('text')=="":
            self.turn+=1
            if self.turn%2==0:
                self.btn3.config(text='X', font=('Times', 9, 'bold'), padx=41, fg='white')
            else:
                self.btn3.config(text='O', font=('Times', 10, 'bold'), padx=40, fg='yellow')
            self.checkifwon()
            self.playerturn()

    def click4(self):
        if self.btn4.cget('text')=="":
            self.turn+=1
            if self.turn%2==0:
                self.btn4.config(text='X', font=('Times', 9, 'bold'), padx=41, fg='white')
            else:
                self.btn4.config(text='O', font=('Times', 10, 'bold'), padx=40, fg='yellow')
            self.checkifwon()
            self.playerturn()

    def click5(self):
        if self.btn5.cget('text')=="":
            self.turn+=1
            if self.turn%2==0:
                self.btn5.config(text='X', font=('Times', 9, 'bold'), padx=41, fg='white')
            else:
                self.btn5.config(text='O', font=('Times', 10, 'bold'), padx=40, fg='yellow')
            self.checkifwon()
            self.playerturn()

    def click6(self):
        if self.btn6.cget('text')=="":
            self.turn+=1
            if self.turn%2==0:
                self.btn6.config(text='X', font=('Times', 9, 'bold'), padx=41, fg='white')
            else:
                self.btn6.config(text='O', font=('Times', 10, 'bold'), padx=40, fg='yellow')
            self.checkifwon()
            self.playerturn()

    def click7(self):
        if self.btn7.cget('text')=="":
            self.turn+=1
            if self.turn%2==0:
                self.btn7.config(text='X', font=('Times', 9, 'bold'), padx=41, fg='white')
            else:
                self.btn7.config(text='O', font=('Times', 10, 'bold'), padx=40, fg='yellow')
            self.checkifwon()
            self.playerturn()

    def click8(self):
        if self.btn8.cget('text')=="":
            self.turn+=1
            if self.turn%2==0:
                self.btn8.config(text='X', font=('Times', 9, 'bold'), padx=41, fg='white')
            else:
                self.btn8.config(text='O', font=('Times', 10, 'bold'), padx=40, fg='yellow')
            self.checkifwon()
            self.playerturn()

    def click9(self):
        if self.btn9.cget('text')=="":
            self.turn+=1
            if self.turn%2==0:
                self.btn9.config(text='X', font=('Times', 9, 'bold'), padx=41, fg='white')
            else:
                self.btn9.config(text='O', font=('Times', 10, 'bold'), padx=40, fg='yellow')
            self.checkifwon()
            self.playerturn()


    def playerturn(self):                       # to show which player's turn it is on a label after each move
        if(self.turn%2==0):
            
            self.mylabel.config(text=self.p1_name.get()+"'s Turn", font=('Seoge print', 10, 'bold'))
        else:
            self.mylabel.config(text=self.p2_name.get()+"'s Turn", font=('Seoge print', 10, 'bold'))


    def start(self):

        self.top=Toplevel()                     # 2nd window for the game
        self.top.geometry("350x500")
        self.top.configure(bg='lavender')
        self.top.title("TIC-TAC-TOE")

        # creating all the buttons
        self.btn1= Button(self.top, padx=45, pady=30,text="", bg='firebrick', fg='white', command= self.click1)
        self.btn1.grid(row=0, column=0, pady=(30,0), padx=(25,0))
        self.btn2= Button(self.top, padx=45, pady=30,text="", bg='firebrick', fg='white', command= self.click2)
        self.btn2.grid(row=0, column=1,pady=(30,0))
        self.btn3= Button(self.top, padx=45, pady=30,text="", bg='firebrick', fg='white', command= self.click3)
        self.btn3.grid(row=0, column=2,pady=(30,0))
        self.btn4= Button(self.top, padx=45, pady=30,text="", bg='firebrick', fg='white', command= self.click4)
        self.btn4.grid(row=1, column=0, padx=(25,0))
        self.btn5= Button(self.top, padx=45, pady=30,text="", bg='firebrick', fg='white', command= self.click5)
        self.btn5.grid(row=1, column=1)
        self.btn6= Button(self.top, padx=45, pady=30,text="", bg='firebrick', fg='white', command= self.click6)
        self.btn6.grid(row=1, column=2)
        self.btn7= Button(self.top, padx=45, pady=30,text="", bg='firebrick', fg='white', command= self.click7)
        self.btn7.grid(row=2, column=0, padx=(25,0))
        self.btn8= Button(self.top, padx=45, pady=30,text="", bg='firebrick', fg='white', command= self.click8)
        self.btn8.grid(row=2, column=1)
        self.btn9= Button(self.top, padx=45, pady=30,text="", bg='firebrick', fg='white', command= self.click9)
        self.btn9.grid(row=2, column=2)

        # creating label to show which player's turn it is
        self.mylabel= Label(self.top, text=self.p1_name.get() +"'s Turn" , padx=90, pady=10, bg='lavender', font=('Seoge print', 10, 'bold'))
        self.mylabel.grid(row=4, column=0, columnspan=3, pady=(5,0))

        # creating quit buttton
        quitbtn= Button(self.top, padx=35, pady=20,text="Quit Game", bg='gold3', fg='black', command=quit)
        quitbtn.grid(row=7, column=0, columnspan=3, pady=(10,0), padx=(10,0))


    def __init__(self, main):
        self.p1_name=Entry(main, width=40 )                 # taking players' name as input
        self.p1_name.grid(row=1, column=1, pady=(20,0))
        self.p2_name=Entry(main, width=40 )
        self.p2_name.grid(row=2, column=1, pady=(20,0))

        game_Label=Label(main, text="TIC-TAC-TOE", font=('Segoe print', 40,'bold'), fg='brown', bg='lavender')
        game_Label.grid(row=0, column=0, columnspan=2, pady=(10,10), padx=70)
        p1_nameLabel=Label(main,text="PLAYER 1 :", font=('Times', 15, 'bold'), bg='lavender')
        p1_nameLabel.grid(row=1, column=0, pady=(20,0))
        p2_nameLabel=Label(main, text="PLAYER 2 :", font=('Times', 15, 'bold'), bg='lavender')
        p2_nameLabel.grid(row=2, column=0, pady=(20,0))
        
        # start game button
        startbtn=Button(main, text="START GAME", padx=10, pady=15, command=lambda: self.start(), font=("Times", 20,"bold", "italic"), bg='gold1')
        startbtn.grid(row=4, column=0, columnspan=2,padx=50, pady=40)

    
    # creating function which disable all buttons
    def disable(self):    
        self.btn1.config(state=DISABLED)
        self.btn2.config(state=DISABLED)
        self.btn3.config(state=DISABLED)
        self.btn4.config(state=DISABLED)
        self.btn5.config(state=DISABLED)
        self.btn6.config(state=DISABLED)
        self.btn7.config(state=DISABLED)
        self.btn8.config(state=DISABLED)
        self.btn9.config(state=DISABLED)

    # to continuously check if someone has won the game
    def checkifwon(self):
        if self.turn%2==0:
                name=self.p2_name.get()
        else :
                name=self.p1_name.get()    

        won=0
        draw=0

        if (self.btn2.cget('text')=="X" or self.btn2.cget('text')=='O') and self.btn1.cget('text')==self.btn2.cget('text') and self.btn2.cget('text') == self.btn3.cget('text') :
            won=1
                
        elif (self.btn4.cget('text')=='X' or self.btn4.cget('text')=='O') and self.btn1.cget('text')==self.btn4.cget('text') and self.btn4.cget('text') == self.btn7.cget('text'):
            won=1

        elif (self.btn5.cget('text')=='X' or self.btn5.cget('text')=='O') and self.btn1.cget('text')==self.btn5.cget('text') and self.btn5.cget('text') == self.btn9.cget('text'):
            won=1
            
        elif (self.btn8.cget('text')=='X' or self.btn8.cget('text')=='O') and self.btn9.cget('text')==self.btn8.cget('text') and self.btn8.cget('text') == self.btn7.cget('text'):
            won=1
            
        elif (self.btn6.cget('text')=='X' or self.btn6.cget('text')=='O') and self.btn9.cget('text')==self.btn6.cget('text') and self.btn6.cget('text') == self.btn3.cget('text'):
            won=1
            
        elif (self.btn5.cget('text')=='X' or self.btn5.cget('text')=='O') and self.btn3.cget('text')==self.btn5.cget('text') and self.btn5.cget('text') == self.btn7.cget('text'):
            won=1
            
        elif (self.btn5.cget('text')=='X' or self.btn5.cget('text')=='O') and self.btn2.cget('text')==self.btn5.cget('text') and self.btn5.cget('text') == self.btn8.cget('text'):
            won=1
            
        elif (self.btn5.cget('text')=='X' or self.btn5.cget('text')=='O') and self.btn4.cget('text')==self.btn5.cget('text') and self.btn5.cget('text') == self.btn6.cget('text'):
            won=1

        elif (self.btn1.cget('text')!="" and self.btn2.cget('text')!="" and self.btn3.cget('text')!="" and self.btn4.cget('text')!="" and self.btn5.cget('text')!="" and self.btn6.cget('text')!="" and self.btn7.cget('text')!="" and self.btn8.cget('text')!="" and self.btn9.cget('text')!=""   ):
            draw=1                          # when match draws

        if draw == 1 :              # check if match draws
            winlabel = Label(self.top, text="GAME  DRAW ", font=('Times', 20, 'bold'), bg='gold', padx=30)
            winlabel.grid(row=1, column=0, columnspan=3, ipadx=20, padx=(25,0))
            self.disable()               # disable all the buttons when game is over

        elif won==1 :               # check if someone won
            winlabel = Label(self.top, text=name + " WON", font=('Times', 20, 'bold'), bg='gold')
            winlabel.grid(row=1, column=0, columnspan=3, ipadx=60)
            self.disable()               # disable all the buttons once somebody wins


        
e=TicTacToe(root)
root.mainloop()
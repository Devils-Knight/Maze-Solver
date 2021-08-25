from tkinter import *
from MazeSolver import MazeSolver

class gui:
    def __init__(self,master):
        self.win=master
        self.ms=MazeSolver('maze_boards/4.txt')
        self.board=self.ms.board
        self.canvas = Canvas(self.win,height=470, width=650,bg="#fff")
        self.canvas.pack()
        self.canvas.create_rectangle(20, 10, 630, 460,outline="#fff",fill="#0ff")
        self.displayboard(self.board)
        
    def update(self):
        self.ms.solve()
        self.board=self.ms.board
        x,y=40,25
        for i in self.board:
            for j in i:
                if j=="*":
                    self.canvas.create_rectangle(x+2, y+5, x+17,y+29,outline="#00f",fill="#00f")
                x+=19
            y+=34
            x=40

    def displayboard(self,board):
        x,y=40,25
        for i in self.board:
            for j in i:
                if j=="#":
                    self.canvas.create_rectangle(x, y, x+19,y+34,outline="#fb0",fill="#fb0")
                if j=="x":
                    self.canvas.create_rectangle(x+2, y+5, x+17,y+29,outline="#0f0",fill="#0f0")
                if j=="o":
                    self.canvas.create_rectangle(x+2, y+5, x+17,y+29,outline="#f00",fill="#f00")
                if j=="*":
                    self.canvas.create_rectangle(x+2, y+5, x+17,y+29,outline="#00f",fill="#00f")
                x+=19
            y+=34
            x=40
        btn = Button(
        self.win,
        text='Mazesolver',
        font="Times 12",
        command=self.update
        )
        btn.pack(side="bottom")


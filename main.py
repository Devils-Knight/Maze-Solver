from gui import *

def main():
    win = Tk()
    win.title("maze solver")
    win.geometry("650x520")
    win.config(bg="#345")
    gui(win)
    win.mainloop()
main()
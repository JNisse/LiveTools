from tkinter import *
from tkinter import ttk
from pgn import read_pgn, format_pgn
fil='exempel.pgn'

def pgn_win():
    pgnfil=[]
    pgn_window=Toplevel(window,width=30 ,height=30,takefocus=True)
    pgn_window.title("PGN window")
    info=Label(pgn_window,text="Information om PGN")
    info.grid()
    listbox=Listbox(pgn_window,width=75,height=50)
    listbox.grid()
    pgn=read_pgn(fil)
    for x in pgn:
        listbox.insert(END,x)
    pgnfil.append(format_pgn(pgn))

 

def setup_board():
    global buttons
    for button in buttons[1]:
        button.config(image=pb)
    for button in buttons[6]:
        button.config(image=pw)
    buttons[0][0].config(image=rb)
    buttons[0][1].config(image=nb)
    buttons[0][2].config(image=bb)
    buttons[0][3].config(image=qb)
    buttons[0][4].config(image=kb)
    buttons[0][5].config(image=bb)
    buttons[0][6].config(image=nb)
    buttons[0][7].config(image=rb)
    buttons[7][0].config(image=rw)
    buttons[7][1].config(image=nw)
    buttons[7][2].config(image=bw)
    buttons[7][3].config(image=qw)
    buttons[7][4].config(image=kw)
    buttons[7][5].config(image=bw)
    buttons[7][6].config(image=nw)
    buttons[7][7].config(image=rw)

window=Tk()
window.title("Analysbräde")
#mainframe = ttk.Frame(window, padding="3 3 12 12")
bb=PhotoImage(file=r"C:\Users\Jpani\Documents\USSSpy\analysis_board\images\bishop.png")
bw=PhotoImage(file=r"C:\Users\Jpani\Documents\USSSpy\analysis_board\images\bishopW.png")
nb=PhotoImage(file=r"C:\Users\Jpani\Documents\USSSpy\analysis_board\images\Knight.png")
nw=PhotoImage(file=r"C:\Users\Jpani\Documents\USSSpy\analysis_board\images\KnightW.png")
rb=PhotoImage(file=r"C:\Users\Jpani\Documents\USSSpy\analysis_board\images\Rook.png")
rw=PhotoImage(file=r"C:\Users\Jpani\Documents\USSSpy\analysis_board\images\RookW.png")
qb=PhotoImage(file=r"C:\Users\Jpani\Documents\USSSpy\analysis_board\images\Queen.png")
qw=PhotoImage(file=r"C:\Users\Jpani\Documents\USSSpy\analysis_board\images\QueenW.png")
kb=PhotoImage(file=r"C:\Users\Jpani\Documents\USSSpy\analysis_board\images\King.png")
kw=PhotoImage(file=r"C:\Users\Jpani\Documents\USSSpy\analysis_board\images\KingW.png")
pb=PhotoImage(file=r"C:\Users\Jpani\Documents\USSSpy\analysis_board\images\Pawn.png")
pw=PhotoImage(file=r"C:\Users\Jpani\Documents\USSSpy\analysis_board\images\PawnW.png")
non=PhotoImage(file=r"C:\Users\Jpani\Documents\USSSpy\analysis_board\images\empty1.png")
black=[pb,nb,bb,rb,qb,kb]
white=[pw,nw,bw,rw,qw,kw]
to_move=True # True=white to move
current_piece=non
current_piece2=non
buttons=[]
def move_piece(i,j):
    global buttons
    global current_piece
    global current_piece2
    
    if (current_piece2==non):
        current_piece=buttons[i][j].cget('image')
    buttons[i][j].config(image=current_piece2)
    current_piece2=current_piece
    current_piece=non
def add_piece(i,is_white):
    global current_piece2
    
    if is_white:
        current_piece2=white[i]
    else:
        current_piece2=black[i]  

extras=[]
def board():
    for i in range(len(white)):
        extras.append(Button(window,image=white[i],command=lambda i=i:add_piece(i,True)))
        extras.append(Button(window,image=black[i],command=lambda i=i: add_piece(i,False)))
        extras[2*i].grid(row=i,column=9)
        extras[2*i+1].grid(row=i,column=10)
    for i in range(8):
        buttons.append([])

        for j in range(8):
        
            buttons[i].append(Button(window,image=non))
            buttons[i][j].config(command= lambda i=i, j=j: move_piece(i,j))
            if ((i+j)%2)==1:
                buttons[i][j].config(bg='brown')
            buttons[i][j].grid(row=i,column=j)
    
pgn_window_button=Button(window,text="PGN fönster",command=pgn_win)
pgn_window_button.grid(row=8,column=8)


board()
setup_board()

window.mainloop()

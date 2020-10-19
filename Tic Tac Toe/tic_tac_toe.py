from tkinter import * 
import tkinter.messagebox
tk = Tk()
tk.title("Tic Tac Toe")
flag=1
count=0

def btnClick(btn):
	global flag,count
	if btn['text']==' ' and flag==1:
		btn['text']="X"
		flag=0
	elif btn['text']==' ' and flag==0:
		btn['text']='O'
		flag=1
	else:
		pass
	count=count+1
	checkForWin()

def clear():
	global count
	button1['text']=' '
	button2['text']=' '
	button3['text']=' '
	button4['text']=' '
	button5['text']=' '
	button6['text']=' '
	button7['text']=' '
	button8['text']=' '
	button9['text']=' '
	count=0

def checkForWin():
    if (button1['text'] == 'X' and button2['text'] == 'X' and button3['text'] == 'X' or
        button4['text'] == 'X' and button5['text'] == 'X' and button6['text'] == 'X' or
        button7['text'] =='X' and button8['text'] == 'X' and button9['text'] == 'X' or
        button1['text'] == 'X' and button5['text'] == 'X' and button9['text'] == 'X' or
        button3['text'] == 'X' and button5['text'] == 'X' and button7['text'] == 'X' or
        button1['text'] == 'X' and button2['text'] == 'X' and button3['text'] == 'X' or
        button1['text'] == 'X' and button4['text'] == 'X' and button7['text'] == 'X' or
        button2['text'] == 'X' and button5['text'] == 'X' and button8['text'] == 'X' or
        button7['text'] == 'X' and button6['text'] == 'X' and button9['text'] == 'X'):
    	tkinter.messagebox.showinfo("Tic-Tac-Toe","X WINS :)")
    	clear()
   

    elif (button1['text'] == 'O' and button2['text'] == 'O' and button3['text'] == 'O' or
          button4['text'] == 'O' and button5['text'] == 'O' and button6['text'] == 'O' or
          button7['text'] == 'O' and button8['text'] == 'O' and button9['text'] == 'O' or
          button1['text'] == 'O' and button5['text'] == 'O' and button9['text'] == 'O' or
          button3['text'] == 'O' and button5['text'] == 'O' and button7['text'] == 'O' or
          button1['text'] == 'O' and button2['text'] == 'O' and button3['text'] == 'O' or
          button1['text'] == 'O' and button4['text'] == 'O' and button7['text'] == 'O' or
          button2['text'] == 'O' and button5['text'] == 'O' and button8['text'] == 'O' or
          button7['text'] == 'O' and button6['text'] == 'O' and button9['text'] == 'O'):
    	tkinter.messagebox.showinfo("Tic-Tac-Toe","O WINS :)")
    	clear()

    elif count==9:
    	tkinter.messagebox.showinfo("Tic-Tac-Toe","GAME DRAW TRY AGAIN")
    	clear()

button1 = Button(tk, text=" ", font='Times 15 bold', bg='indian red', fg='gold', height=4, width=8, command=lambda: btnClick(button1))
button1.grid(row=3, column=0)

button2 = Button(tk, text=' ', font='Times 15 bold', bg='indian red', fg='gold', height=4, width=8, command=lambda: btnClick(button2))
button2.grid(row=3, column=1)

button3 = Button(tk, text=' ',font='Times 15 bold', bg='indian red', fg='gold', height=4, width=8, command=lambda: btnClick(button3))
button3.grid(row=3, column=2)

button4 = Button(tk, text=' ', font='Times 15 bold', bg='indian red', fg='gold', height=4, width=8, command=lambda: btnClick(button4))
button4.grid(row=4, column=0)

button5 = Button(tk, text=' ', font='Times 15 bold', bg='indian red', fg='gold', height=4, width=8, command=lambda: btnClick(button5))
button5.grid(row=4, column=1)

button6 = Button(tk, text=' ', font='Times 15 bold', bg='indian red', fg='gold', height=4, width=8, command=lambda: btnClick(button6))
button6.grid(row=4, column=2)

button7 = Button(tk, text=' ', font='Times 15 bold', bg='indian red', fg='gold', height=4, width=8, command=lambda: btnClick(button7))
button7.grid(row=5, column=0)

button8 = Button(tk, text=' ', font='Times 15 bold', bg='indian red', fg='gold', height=4, width=8, command=lambda: btnClick(button8))
button8.grid(row=5, column=1)

button9 = Button(tk, text=' ', font='Times 15 bold', bg='indian red', fg='gold', height=4, width=8, command=lambda: btnClick(button9))
button9.grid(row=5, column=2)

tk.mainloop()
#tkinter is a module(toolbox) that 
#holds code that you can use
#by using as tk we just are shorting the name 
import tkinter as tk
#root is a variable that holds the information 
#about the main window. That is the window 
#with th e close, min, max buttons in the top left
#tk.TK() go in the tk tool box and use the function Tk()
root = tk.Tk()

#if we want to better posistion the elements we use 
#the grid geomtry manager, not the pack 
ent = tk.Entry(root)
ent.grid(row = 0, column = 0)

btn = tk.Button(root, text = "Press Me")
btn.grid(row = 0, column = 1)

labl = tk.Label(root, text = "...")
labl.grid(row = 1, column = 0, columnspan = 2)


#sets up your program in an infinit loop waiting for
#the userto do something. This is an EVENT DRIVE PROGRAM
#This means a function is called when we "do something" 
root.mainloop()
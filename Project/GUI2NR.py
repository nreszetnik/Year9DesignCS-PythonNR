 #This imports the tkinter "tool box" this conains
#all the support material to make GUI elements
#by including "as tk" we are giving a short name to use.
import tkinter as tk

root = tk.Tk()
#**********************WIDGET 1***********
#Three stages to build elements/objects
#1, construct the object: We build and configure
#2, Configure the object: We specify behaviours and settings
#3, Pack the object: Put it in the window
titleLabel = tk.Label(root, text = "PASSWORD GENERATOR", font=("Helvetica", 16))
#ordered parameters: The order we send them matters. (COMMON)
#named parameters: JvaScript and Python specific
titleLabel.grid(row = 0, column = 0, columnspan = 2)

#Widget 2: Text***************
output = tk.Text(root, heigh = 10, width = 50)
output.config(state = "disable")
output.grid(row = 1, column = 0, columnspan = 2)



#Widget 3: Labels************************
word1Label = tk.Label(root, text = "Word 1", background  = "red", foreground = "blue")
word1Label.grid(row = 2, column = 0, sticky  = "NESW")

word1Label = tk.Label(root, text = "Word 2", background  = "red", foreground = "blue")
word1Label.grid(row = 3, column = 0)


word1Label = tk.Label(root, text = "Word 3")
word1Label.grid(row = 4, column = 0)

#Widget 4: Entry*************
ent1 = tk.Entry(root)
ent1.grid(row = 2, column = 1)

ent2 = tk.Entry(root)
ent2.grid(row = 3, column = 1)

ent3 = tk.Entry(root)
ent3.grid(row = 4, column = 1)

#Widget 5: Buttons*********
btnGo = tk.Button(root, text = "GENERATE")
btnGo.grid(row = 5, column = 1)

#We are writing an event drive program.
#Build the GUI
#Strat it running
#Wait for "Event"
root.mainloop() #Starts the program"
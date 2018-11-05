import tkinter as tk

def change(*args):
	print("running change")


root  = tk.Tk() #Constructs our man window

#List of strings
#My list is called options there are three elements with index 0 to 2
#print(OPTIONS [2])
OPTIONS = [

"eggs",
"bunny",
"chicken",
]

var =tk.StringVar(root) #This is creating a variable that tracks something
var.set(OPTIONS[0])
var.trace("w",change)

dropDownMenu = tk.OptionMenu(root,var, OPTIONS[0],OPTIONS[1],OPTIONS[2])
dropDownMenu.pack()

root.mainloop()
print("End program")
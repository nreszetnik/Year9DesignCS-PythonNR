
import tkinter as tk

def on_entry_click(event):
   print(event.widget)
   event.widget.delete(0, "end") # delete all the text in the entry
   event.widget.insert(0, '') #Insert blank for user input
   event.widget.config(fg = "black") #The inserted text becomes black

def on_focusout1(event):
	if ent1.get() == "":
		ent1.insert(0, "Enter Amount of Money You Have; i.e $30,000")
		ent1.config(fg = "grey")
		ent1.grid(row = 7, column = 0)

def change(*args):
	print("running change")
	print(metalType.get())

root = tk.Tk()

titleLabel = tk.Label(root, text = "Commodity Program", font = ("Helvetica", 20))
titleLabel.grid(row = 0, column = 0, columnspan = 2, sticky = "NESW")

word1Label = tk.Label(root, text = "Metal Type")
word1Label.grid(row = 1, column = 0, columnspan = 2, sticky = "NESW" )

MetalOPTIONS = [

"Gold",
"Silver",
"Platnium",
"Palladium",
]

metalType=tk.StringVar(root) 
metalType.set(MetalOPTIONS[0])
metalType.trace("w",change)

dropDownMenu = tk.OptionMenu(root,metalType, MetalOPTIONS[0],MetalOPTIONS[1],MetalOPTIONS[2])
dropDownMenu.grid(row = 2, column = 0, rowspan = 2, columnspan = 2, sticky = "NESW")

cbHighContrast = tk.Checkbutton(root,text = "High Contrast")
cbHighContrast.grid(row = 2, column = 2, sticky = "NESW")

cbFontsize= tk.Checkbutton(root,text = "Font Size")
cbFontsize.grid(row = 3, column = 2, sticky = "NESW")

word1Label = tk.Label(root, text = "Measurement Type")
word1Label.grid(row = 4, column = 0, columnspan = 2, sticky = "NESW")

MeasurementOPTIONS = [

"Grams",
"Kilograms",
"Ounces",
]

measurementType=tk.StringVar(root)
measurementType.set(MeasurementOPTIONS[0])
measurementType.trace("w",change)

dropDownMenu2 = tk.OptionMenu(root,measurementType, MeasurementOPTIONS[0],MeasurementOPTIONS[1],MeasurementOPTIONS[2])
dropDownMenu2.grid(row = 5, column = 0, columnspan = 2, sticky = "NESW")


word1Label = tk.Label(root, text = "Amount of Money You Have To Spend")
word1Label.grid(row = 6, column = 0, columnspan = 2, sticky = "NESW")

root.title("GUI Entry")
entry1 = tk.Entry(root)
entry1.grid(row = 7, column = 0, columnspan = 2, sticky = "NESW")

ent1 = tk.Entry(root)
ent1.insert(0, "Enter rhr ; i.e 80")
ent1.bind("<FocusIn>", on_entry_click)
ent1.bind("<FocusOut1>", on_focusout1)
ent1.config(fg = "grey")
ent1.grid(row = 2, column = 1)


root.title("Commodity GUI Program")
btn1 = tk.Button(root, text = "Submit")
btn1.grid(row = 8, column = 0, columnspan = 2, sticky = "NESW")

root.mainloop()
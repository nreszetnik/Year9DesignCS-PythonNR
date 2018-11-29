
import tkinter as tk

def change(*args):
	print("running change")
	print(metalType.get())
	if metalType.get() == "Silver":
		dropDownMenu.config(background = "#C0C0C0")

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
dropDownMenu.config(background = "#FFD700")
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

root.title("PROGRAM")
btn1 = tk.Button(root, text = "Submit")
btn1.grid(row = 8, column = 0, columnspan = 2, sticky = "NESW")

root.mainloop()
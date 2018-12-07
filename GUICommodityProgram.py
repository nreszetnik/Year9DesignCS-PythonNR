
import tkinter as tk

def on_entry_click(event):
   print(event.widget)
   event.widget.delete(0, "end") # delete all the text in the entry
   event.widget.insert(0, '') #Insert blank for user input
   event.widget.config(fg = "black") #The inserted text becomes black

def on_focusout1(event):
	print("%%%%%%%%%%%%%%%%%%%%%%%")
	if event.widget.get() == "":
		event.widget.insert(0, "i.e $30,000")
		
		event.widget.config(fg = "grey")
		
def change(*args):
	print("running change")
	print(metalType.get())
	if metalType.get() == "Gold":
		dropDownMenu.config(background = "#FFD700")
	elif metalType.get() == "Silver":
		dropDownMenu.config(background = "#C0C0C0")
	elif metalType.get() == "Platnium":
		dropDownMenu.config(background  = "#e5e4e2")

def changeHighContrast(*args):
	print("Change Contrast")
	print(contrast.get())

	if contrast.get() == 0:
		if var1.get() == 1:
			root.config(bg = "black")
			cbHighContrast.config(bg = "black", fg = "yellow")
		if var1.get() == 0:
			root.config(bg = "white")
			cbHighContrast.config(bg = "white",fg = "black")
	else:
		print("do something else")
root = tk.Tk()

root.config( bg = "grey")

titleLabel = tk.Label(root, text = "Commodity Program", font = ("Helvetica", 20), bg = "grey")
titleLabel.grid(row = 0, column = 0, columnspan = 2, sticky = "NESW")

word1Label = tk.Label(root, text = "Metal Type", font = ("Helvetica"),bg = "grey")
word1Label.grid(row = 1, column = 0, columnspan = 2,sticky = "NESW", padx = 5, pady = 5)

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
dropDownMenu.config(bg = "#FFD700")
dropDownMenu.grid(row = 2, column = 0, rowspan = 2, columnspan = 2, sticky = "NESW", padx = 5, pady = 5)


var1 = tk.IntVar()
contrast = tk.IntVar()
contrast.trace("w",changeHighContrast)
#check1 = tk.Checkbutton(root, text="High Contrast On/Off", variable=var1)
#check1.config(font=("Courier", 16))
#check1.grid()
cbHighContrast = tk.Checkbutton(root,text = "High Contrast", bg = "grey",variable = contrast)
cbHighContrast.grid(row = 2, column = 2, sticky = "NESW")


 
cbFontsize= tk.Checkbutton(root,text = "Font Size", bg = "grey")
cbFontsize.grid(row = 3, column = 2, sticky = "NESW")

word1Label = tk.Label(root, text = "Measurement Type",font = ("Helvetica"), bg = "grey")
word1Label.grid(row = 4, column = 0, columnspan = 2, sticky = "NESW", padx = 5, pady = 5)

MeasurementOPTIONS = [

"Grams",
"Kilograms",
"Ounces",
]

measurementType=tk.StringVar(root)
measurementType.set(MeasurementOPTIONS[0])
measurementType.trace("w",change)

dropDownMenu2 = tk.OptionMenu(root,measurementType, MeasurementOPTIONS[0],MeasurementOPTIONS[1],MeasurementOPTIONS[2])
dropDownMenu2.grid(row = 5, column = 0, columnspan = 2, sticky = "NESW", padx = 5, pady = 5)


word1Label = tk.Label(root, text = "Amount of Money You Have To Spend", font = ("Helvetica"), bg = "grey")
word1Label.grid(row = 6, column = 0, columnspan = 2, sticky = "NESW", padx = 5, pady = 5)

root.title("GUI Entry")
entry1 = tk.Entry(root)
entry1.grid(row = 7, column = 0, columnspan = 2, sticky = "NESW", padx = 5, pady = 5)
entry1.insert(0, "i.e $30,000")
entry1.bind("<FocusIn>", on_entry_click)
entry1.bind("<FocusOut>", on_focusout1)
entry1.config(fg = "grey")



root.title("Commodity GUI Program")
btn1 = tk.Button(root, text = "Submit")
btn1.grid(row = 8, column = 0, columnspan = 2, sticky = "NESW",padx = 20, pady = 20)

root.mainloop()
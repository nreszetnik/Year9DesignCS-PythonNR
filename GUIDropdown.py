import tkinter as tk

def change(*args):
	print("running change")


root  = tk.Tk() #Constructs our man window

#List of strings
#My list is called options there are three elements with index 0 to 2
#print(OPTIONS [2])
MeasurementOPTIONS = [

"Grams",
"Kilograms",
"Ounces",
]

measurementType=tk.StringVar(root)
measurementType.set(MeasurementOPTIONS[0])
measurementType.trace("w",change)

dropDownMenu = tk.OptionMenu(root,measurementType, MeasurementOPTIONS[0],MeasurementOPTIONS[1],MeasurementOPTIONS[2])
dropDownMenu.pack()

root.mainloop()
print("End program")
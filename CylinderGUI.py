import tkinter as tk
def submit():

	print("Submit pressed")
	r = float(entr.get())
	h = float(enth.get())

	v = math.pi*r*r*h
	v = round (v,3)

	output.insert
	
root = tk.Tk()
root.configure(background = 'red')
root.title("Volume of a Cylinder")

labr = tk.Label(root, text="radius")
labr.pack()

entr = tk.Entry(root)
entr.pack()

labh = tk.Label(root, text="height")
labh.configure(background = 'red')
labh.pack()

enth = tk.Entry(root)
enth.pack()

btn = tk.Button(root, text="Submit", command=submit)
btn.pack()

output = tk.Text(root, width=50, height=10, borderwidth=3, relief=tk.GROOVE)
output.pack()







root.mainloop()
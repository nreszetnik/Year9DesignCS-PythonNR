import tkinter as tk
import math

def submit():

	print("Submit pressed")
	r = float(slide1.get())
	h = float(slide2.get())

	v = math.pi*r*r*h
	v = round (v,3)

	output.config(state="normal")

	outputValue = "Given\nradius:"+str(r)+"units\nheight:"+str(h)+"units\nThe volume is:"+str(v)+"units\n\n"

	output.delete(1.0,tk.END)
	output.insert(tk.INSERT,outputValue)
	output.config(state="disable")

root = tk.Tk()
root.configure(background="red")
root.title("Volume of a Cylinder")

labr = tk.Label(root, text="radius", background="red")
labr.pack()

slide1 = tk.Scale(root, from_=0, to=100, resolution=1, orient=tk.HORIZONTAL, background="red")
slide1.pack()

labh = tk.Label(root, text="height")
labh.configure(background="red")
labh.pack()

slide2 = tk.Scale(root, from_=0, to=100, resolution=1, orient=tk.HORIZONTAL, background="red")
slide2.pack()

btn = tk.Button(root, text="Submit", command=submit, background="red")
btn.pack()

output = tk.Text(root, width=50, height=10, borderwidth=3, relief=tk.GROOVE)
output.config(state="disabled")
output.pack()

root.mainloop()
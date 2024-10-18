from tkinter import*
from tkinter import ttk
root=Tk()
root.title("Conversion Table")
root.geometry("1200x800+0+0")
lf_bg='Gray70'
rf_bg='Gray57'
frame_font=('Courier',14)

unit = Label(root, text="UNIT CONVERTER", font=("Times New Roman",20, "bold"), bg="black", fg="white")
unit.pack(side=TOP,fill=X)



def convert2():
	global combo1, combo2, e1, ans1
	value = float(e1.get())
	x=combo1.get()
	y=combo2.get()
	
	if x=="Kgs" and y=="lbs":
		res = round(value * 2.20462,2)

		result = str(value) +" " +x+ "  = " + str(res) +" "+ y
		ans2.config(text=result)
	elif x=="lbs" and y=="Kgs":
		res = round(value * 0.4539,2)
		result = str(value) +" " +x+ "  = " + str(res) +" "+ y
		ans2.config(text=result)
	else:
		result = str(value) + x + "  = " + str(value) + y
		ans2.config(text=result)



left_frame = Frame(root,bg=lf_bg)
right_frame = Frame(root,bg=rf_bg)

left_frame.place(relx=0,relheight=1,y=40,relwidth=0.5)
right_frame.place(relx=0.5,relheight=1,y=40,relwidth=0.5)

def convert1():
	global combo1, combo2, e1, ans2
	
	x=combo1.get()
	y=combo2.get()

	value = float(e1.get())
	
	if x== "Km" and y=="Miles":
		res = round(value * 0.621371,2)
		result = str(value) +" " +x+ "  = " + str(res) +" "+ y
		
		ans1.config(text=result)
	elif x== "Miles" and y=="Km":
		res = round(value * 1.60934,2)
		result = str(value) +" " +x+ "  = " + str(res) +" "+ y
		
		ans1.config(text=result)
	else:
		result = str(value) + x + "  = " + str(value) + y
		ans1.config(text=result)



def convert3():
	global combo1,combo2,el,ans3
	
	x=combo1.get()
	y=combo2.get()
	value=float(e1.get())
	
	if x=="Fahrenheit" and y=="Celsius":
		res=round(value * (32)*5/9,2)
		result = str(value) +" " +x+ "  = " + str(res) +" "+ y
		ans3.config(text=result)
	elif x=="Celsius" and y=="Fahrenheit":
		res=round(value * 1.8+32,2)
		result = str(value) +" " +x+ "  = " + str(res) +" "+ y
		ans3.config(text=result)
	elif x=="Celsius" and y=="Kelvin":
		res=round(value +273.15,2)
		result = str(value) +" " +x+ "  = " + str(res) +" "+ y
		ans3.config(text=result)
	elif x=="Kelvin" and y=="Celsius":
		res=round(value -273.15,2)
		result = str(value) +" " +x+ "  = " + str(res) +" "+ y
		ans3.config(text=result)
	elif x=="Fahrenheit" and y=="Kelvin":
		res=round((value -32)*5/9+273.15,2)
		result = str(value) +" " +x+ "  = " + str(res) +" "+ y
		ans3.config(text=result)
	elif x=="Kelvin" and y=="Fahrenheit":
		res=round((value-273.15)*5/9+32,2)
		result = str(value) +" " +x+ "  = " + str(res) +" "+ y
		ans3.config(text=result)
	else:
		result = str(value) +" "+ x + "  = " + str(value) + " "+y
		ans3.config(text=result)

		



def cmd_length():
	global combo1, combo2, e1, ans1, ans2, ans3
	ans2.destroy()
	ans3.destroy()
	l1=Label(right_frame,text="Length",width=15,font=frame_font, bg=rf_bg)
	l1.place(relx=0.1, rely=0.1)
	combo1=ttk.Combobox(right_frame,values=["Km","Miles"], width = 26)
	combo1.place(relx=0.22,rely=0.22)
	e1 = Entry(right_frame, width=28)
	e1.place(relx=0.22, rely=0.32)
	combo2=ttk.Combobox(right_frame,values=["Km","Miles"], width = 26)
	combo2.place(relx=0.22,rely=0.42)
	convert=Button(right_frame,text="Convert",width=17,font=("Courier",12), command = convert1)
	convert.place(relx=0.22,rely=0.52)
	ans1=Label(right_frame,text="",font=frame_font, bg=rf_bg)
	ans1.place(relx=0.3, rely=0.62)

def cmd_weight():
	global combo1, combo2, e1, ans2, ans1, ans3
	ans1.destroy()
	ans3.destroy()
	l2=Label(right_frame,text="Weight",width=15,font=frame_font,bg=rf_bg)
	l2.place(relx=0.1,rely=0.1)
	combo1=ttk.Combobox(right_frame,values=["Kgs","lbs"],width=26)
	combo1.place(relx=0.22,rely=0.22)
	e1=Entry(right_frame, width=28)
	e1.place(relx=0.22, rely=0.32)
	combo2=ttk.Combobox(right_frame,values=["Kgs","lbs"], width = 26)
	combo2.place(relx=0.22,rely=0.42)
	convert=Button(right_frame,text="Convert",width=17,font=("Courier",12), command = convert2)
	convert.place(relx=0.22,rely=0.52)
	ans2=Label(right_frame,text="",font=frame_font, bg=rf_bg)
	ans2.place(relx=0.23, rely=0.62)

def cmd_temperature():
	global combo1, combo2, e1, ans3, ans1, ans2
	ans1.destroy()
	ans2.destroy()
	l3=Label(right_frame,text="Temperature",width=15,font=frame_font,bg=rf_bg)
	l3.place(relx=0.1,rely=0.1)
	combo1=ttk.Combobox(right_frame,values=["Celsius","Fahrenheit","Kelvin"],width=26)
	combo1.place(relx=0.22,rely=0.22)
	e1=Entry(right_frame, width=28)
	e1.place(relx=0.22, rely=0.32)
	combo2=ttk.Combobox(right_frame,values=["Celsius","Fahrenheit","Kelvin"], width = 26)
	combo2.place(relx=0.22,rely=0.42)
	convert=Button(right_frame,text="Convert",width=17,font=("Courier",12), command = convert3)
	convert.place(relx=0.22,rely=0.52)
	ans3=Label(right_frame,text="",font=frame_font, bg=rf_bg)
	ans3.place(relx=0.23, rely=0.62)


b1=Button(left_frame,text="Length",width=20,font=("Courier",12),command=cmd_length)		
b2=Button(left_frame,text="Weight",width=20,font=("Courier",12),command=cmd_weight)
b3=Button(left_frame,text="Temperature",width=20,font=("Courier",12),command=cmd_temperature)

b1.place(relx=0.2,rely=0.2)
b2.place(relx=0.2,rely=0.3)
b3.place(relx=0.2,rely=0.4)
ans1=Label(right_frame,text="",font=frame_font, bg=rf_bg)
ans2=Label(right_frame,text="",font=frame_font, bg=rf_bg)
ans3=Label(right_frame,text="",font=frame_font, bg=rf_bg)	


mainloop()

from Tkinter import *



root = Tk()
root.title("welcome to login")
root.geometry('900x600')
root.configure(background='orange')


#led = 4


def login():
	username = 'admin'
	password =  e2.get()

	if username == password:
		print("welcome to next level")

################## New window open to do anther function #############

		newWindow = Toplevel(window)
		newWindow.title("control allaicance")
		newWindow.geometry('600x500')

#################################### first led =4 light up ##################################################################

		def lightup():
			if led.is_lit:
				led.off()
				ledButton["text"]= "Turn led on"

			else:
				ledButton["text"] ="Turn led off"
 
		ledButton = Button(newWindow, text="turn on led", font = ('arial', 20,'bold'),command=lightup)
		ledButton.grid(row=0,column=1)

##########################################################################################################################




#		def lightup2():
			













	else:
		print("plz enter valid uerid and pass")





l1 = Label(window,text="Username", font =('arial',20,'bold'))
l2 = Label(window,text="Password", font = ('arial',20,'bold'))


e1 = Entry(window,font=('arial',20,'bold'))
e2 = Entry(window,font=('arial',20,'bold'),show='*')


button1 = Button(window,text="Login", font = ('arial',20,'bold'),command=login)
button2 = Button(window,text="cancel", font = ('arial',20,'bold'),command=quit)


l1.grid(row=0,column=0)
e1.grid(row=0,column=1)

l2.grid(row=1,column=0)
e2.grid(row=1,column=1)


button1.grid(row=3,column=0)
button2.grid(row=3,column=1)


root.mainloop()


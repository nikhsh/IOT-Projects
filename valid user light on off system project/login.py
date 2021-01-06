from tkinter import *
#import RPi.GPIO
#RPi.GPIO.setmode(RPi.GPIO.BCM)



#led = 4
#led2 = 8


window = Tk()
window.title("welcome to login")
window.geometry('900x600')
window.configure(background='orange')

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




		def lightup2():
			if led2.is_lit:
				led2.off()
				ledButton["text"] = "Turn on second led"

			else:
				ledButton["text"] = "Trun off "
		ledButton = Button(newWindow, text="turn on led", font= ('arial',20,'bold'),command=lightup2)
		ledButton.grid(row=3,column=2)



###################################################################################################################











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


window.mainloop()

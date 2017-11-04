from Tkinter import *
from driver.Driver import Driver
from driver.Driver import DummyRPMDriver
from driver.Driver import Dummy2RPMDriver
from driver.Driver import DummyConnectedDriver

c = Driver(DummyRPMDriver())
d = Driver(Dummy2RPMDriver())
e = Driver(DummyConnectedDriver())

root = Tk()
root["bg"] = "black"
root.overrideredirect(True)
root.overrideredirect(False)
root.attributes('-fullscreen',True)

lab = Label(root)
lab.pack()
lab2 = Label(root)
lab2.pack()

lab.config(font=("Arial", 44))
lab2.config(font=("Arial", 44))

connection = e.getConnection()

if connection == 1:
    logo = PhotoImage(file="connected.pgm")
    w1 = Label(root, image=logo, borderwidth=0, highlightthickness=0)
    w1.pack()

else:
    logo = PhotoImage(file="disconnected2.pgm")
    w1 = Label(root, image=logo, borderwidth=0, highlightthickness=0)
    w1.pack()

def clock():

    time = c.getRPM()
    lab.config(text=time, fg="white", bg="black")
    time2 = d.getRPM()
    lab2.config(text=time2, fg="white", bg="black")
    root.after(1000, clock) # run itself again after 1000 ms

# run first time
clock()
root.mainloop()

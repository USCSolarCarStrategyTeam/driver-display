from Tkinter import *  # This interface allow us to draw windows



from Tkinter import *
from driver.Driver import Driver
from driver.Driver import DummyRPMDriver
from driver.Driver import Dummy2RPMDriver
import threading
import time

c = Driver(DummyRPMDriver())
d = Driver(Dummy2RPMDriver())

root = Tk()
#root["bg"] = "black"
#root.overrideredirect(True)
#root.overrideredirect(False)
#root.attributes('-fullscreen',True)
logo = PhotoImage(file="driver-display/connected.pgm")
w1 = Label(root, image=logo)
w1.pack()
root.mainloop()


def total():
    threading.Timer(5.0, total).start()
    w = Label(root, text = c.getRPM(), fg="white", bg="black")
    w.pack()
    g = Label(root, text = d.getRPM(), fg="white", bg="black")
    g.pack()
    root.mainloop()
# total()




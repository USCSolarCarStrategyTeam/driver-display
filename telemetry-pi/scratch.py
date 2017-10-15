from Tkinter import *  # This interface allow us to draw windows



from Tkinter import *


root = Tk()
root ["bg"] = "black"
root.overrideredirect(True)
root.overrideredirect(False)
root.attributes('-fullscreen',True)
w = Label(root, text = "hello")
w.pack()
root.mainloop()


from tkinter import *

class checkIn(Frame):
    """A GUI for our checkin process."""

    def __init__(self, master):
        """ Initialize the frame"""
        Frame.__init__(self,master)
        self.init_window()

    def init_window(self):
        self.master.title("Check-in Procedures")
        self.pack(fill=BOTH, expand=1)
        quitButton = Button(self, text="quit")
        quitButton.place(x=0,y=0)

##class Cellphone(Frame):
##    """Buttons for Options"""
##    def __init__(self, master):
##        Frame.__init__(self, master)
##        label = Label(self, text = "CELLPHONE")
##        label.pack(pady=10,padx=10)

##        button1 = Button(self, text = "Back", command=lambda: controller.show_frame(checkIn))
##        button1.pack()
            

root = Tk()

root.geometry("400x300")

app = checkIn(root)

root.mainloop()

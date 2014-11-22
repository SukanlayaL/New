##from Tkinter import *        
##from PIL import ImageTk, Image
##
##app_root = Tk()
##
###Setting it up
##img = ImageTk.PhotoImage(Image.open("C:\Users\ºÔÇ\Desktop\hello-002.gif"))
##
###Displaying it
##imglabel = Label(app_root, image=img).grid(row=60, column=10)        
##
##app_root.mainloop()
# label_as_frame.py
from Tkinter import *
root = Tk() #Makes the window
root.wm_title("Window Title") #Makes the title that will appear in the top left
root.config(background = "#FFFFFF") #sets background color to white

#put widgets here
leftFrame = Frame(root, width=500, height = 600)
leftFrame.grid(row=0, column=0, padx=10, pady=2)
newCanvas = Canvas(leftFrame, width=500, height=500, bg='#33CC99')
newCanvas.grid(row=0, column=0, padx=10, pady=2)

firstLabel = Label(leftFrame, text="This is my first label")
firstLabel.grid(row=0, column=100, padx=10, pady=2)

userInput = Entry(leftFrame, width = 10) #the width refers to the number of characters
userInput.grid(row=0, column=0, padx=10, pady=2)

newCanvas = Canvas(leftFrame, width=10, height=100, bg='#99FFCC')
newCanvas.grid(row=0, column=0, padx=10, pady=2)

newText = Text(leftFrame, width=50, height=8, takefocus=0)
newText.grid(row=0, column=0, padx=10, pady=2)

#write to widget
newText.insert(4.6, "Text to insert : ") #0.0 is beginning of widget

#get the text inside of userInput
userInput.get()

root.mainloop() #start monitoring and updating the GUI. Nothing below here runs.


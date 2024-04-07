from tkinter import ttk
from tkinter import *
from spellcheck import SpellCheck
import pytesseract
import re
import cv2
#global keywords
options=['None']
spell_check = SpellCheck('meddata.csv')
#functions

def check():
    global e1
    global e2
    global option_menu
    global notif
    spell_check.check(e1.get())
    options = spell_check.suggestions()
    selected_option = StringVar()
    if e1.get()=='':
        selected_option.set("None")
        notif.config(fg='red', text = 'Invalid Input ')
    else:
        if e1.get() == options[0][0]and e2.get()== options[0][1][1:-1]:
            notif.config(fg='green', text = 'You are good to go ')

        else:
            selected_option.set(options[0])
            option_menu = OptionMenu(Result, selected_option, *options)
            option_menu.grid(column=1, row=4, columnspan=1)
            show_frame(Result)
            
def scan():
    #capture image
    global notif2
    pytesseract.pytesseract.tesseract_cmd = r"C:\Users\rhyth\OneDrive\Documents\Tesseract.exe"
    # cam_port=0
    # cam = cv2.VideoCapture(cam_port)
    # result, image = cam.read()

    out_below = pytesseract.image_to_string("montair-lc.jpg")
    out_below = max(re.findall(r'\b\w+\b', out_below),key=len)

    spell_check.check(out_below)
    #out_below = spell_check.optimise(out_below)
    options = spell_check.suggestions()
    selected_option = StringVar()
    if out_below=='':
        selected_option.set("None")
        notif2.config(fg='red', text = 'Invalid Input ')
    else:
        if len(options)>0:
            if out_below == options[0][0]:
                notif2.config(fg='green', text = 'You are good to go ')

            else:
                selected_option.set(options[0])
                option_menu = OptionMenu(Result, selected_option, *options)
                option_menu.grid(column=1, row=4, columnspan=1)
                show_frame(Result)
        else:
            notif2.config(fg='red', text = 'Please try again')
            
    

#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ window
window = Tk()
# Icon init
# p1 = PhotoImage(file = 'ico.png')
# window.iconphoto(False, p1)
window.title("HEALTHNOX")
window.config(bg = "white")
window.rowconfigure(0, weight=1)
window.columnconfigure(0, weight=1)

#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ 

def show_frame(frame):
   frame.tkraise()

#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

home = Frame(window,bg = "#6be2f9")
Manual = Frame(window,bg = "#6be2f9")
Auto = Frame(window,bg = "#6be2f9")
Result = Frame(window,bg = "#6be2f9")

for frame in (home,Manual,Auto,Result):
    frame.grid(row=0, column=0, sticky='nsew')

show_frame(home)


#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ frame creation and home page

Label(home, text="DEF-CON",font=("Arial Bold", 50), bg = "#ADD8E6").grid(column=0, row=0, columnspan=2)
Label(home, text="SPELL CHECK FOR MEDICAL PURPOSE",font=("Arial Bold", 20),bg = "#ADD8E6").grid(column=0, row=1, columnspan=2)
Label(home, text="   ",font=("Arial Bold", 25),bg = "#6be2f9").grid(column=0, row=2, columnspan=2)

click_btn= PhotoImage(file='log.png')
button= Button(home, image=click_btn,command= lambda:show_frame(Manual),borderwidth=0,height = 100, width = 100).grid(column=0, row=3)

btnimg = PhotoImage(file='med.png')
button1= Button(home, image=btnimg,command= lambda:show_frame(Auto),borderwidth=0,height = 100, width = 100).grid(column=1, row=3)

Label(home, text="Manual",font=("Arial Bold", 15),bg = "#6be2f9").grid(column=0, row=4, columnspan=1)
Label(home, text="Auto",font=("Arial Bold", 15),bg = "#6be2f9").grid(column=1, row=4, columnspan=1)


#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ frame creation and manual

Label(Manual, text="DEF-CON",font=("Arial Bold", 50), bg = "#ADD8E6").grid(column=0, row=0, columnspan=3)
Label(Manual, text="SPELL CHECK FOR MEDICAL PURPOSE",font=("Arial Bold", 25),bg = "#ADD8E6").grid(column=0, row=1, columnspan=3)
Label(Manual, text="   ",font=("Arial Bold", 25),bg = "#6be2f9").grid(column=0, row=2, columnspan=3)

Label(Manual, text="Medicine :",font=("Arial Bold", 15),bg = "#6be2f9").grid(column=0, row=4, columnspan=1)
Label(Manual, text="Salt     :",font=("Arial Bold", 15),bg = "#6be2f9").grid(column=0, row=5, columnspan=1)
e1 = Entry(Manual, font=('Arial', 14))
e1.grid(column=1, row=4, columnspan=2)
e2 = Entry(Manual, font=('Arial', 14))
e2.grid(column=1, row=5, columnspan=2)

button5_man = ttk.Button(
    Manual,
    text='Check',
    command=lambda: check()
)
button5_man.grid(column=1, row=6)

notif = Label(Manual, text="Please Enter Your Medicine Name", font=('Calibri', 11),fg="orange",bg="#6be2f9")
notif.grid(column=0,row=7)

btnhome = PhotoImage(file='home.png')
button4_man= Button(Manual, image=btnhome,command= lambda:show_frame(home),borderwidth=0,height = 50, width = 50).grid(column=3, row=8)

#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ frame creation and Auto

Label(Auto, text="DEF-CON",font=("Arial Bold", 50), bg = "#ADD8E6").grid(column=0, row=0, columnspan=3)
Label(Auto, text="SPELL CHECK FOR MEDICAL PURPOSE",font=("Arial Bold", 25),bg = "#ADD8E6").grid(column=0, row=1, columnspan=3)
Label(Auto, text="   ",font=("Arial Bold", 25),bg = "#6be2f9").grid(column=0, row=2, columnspan=3)

button1_auto = ttk.Button(
    Auto,
    text='Scan',
    command=lambda: scan()
)
button1_auto.grid(column=1, row=6)

notif2 = Label(Auto, text="Click Scan to Scan for medicine", font=('Calibri', 11),fg="orange",bg="#6be2f9")
notif2.grid(column=0,row=7,columnspan=3)

#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ frame creation and result

Label(Result, text="DEF-CON",font=("Arial Bold", 50), bg = "#ADD8E6").grid(column=0, row=0, columnspan=3)
Label(Result, text="SPELL CHECK FOR MEDICAL PURPOSE",font=("Arial Bold", 25),bg = "#ADD8E6").grid(column=0, row=1, columnspan=3)
Label(Result, text="   ",font=("Arial Bold", 25),bg = "#6be2f9").grid(column=0, row=2, columnspan=3)

Label(Result, text="Suggestion :",font=("Arial Bold", 15),bg = "#6be2f9").grid(column=0, row=4, columnspan=1)



btnhome = PhotoImage(file='home.png')
button5 = ttk.Button(
    Manual,
    text='Check',
    command=lambda: check()
)
button5.grid(column=1, row=6)
button4= Button(Result, image=btnhome,command= lambda:show_frame(home),borderwidth=0,height = 50, width = 50).grid(column=3, row=0)


window.mainloop()
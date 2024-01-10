import tkinter as tk
from tkinter import *
from tkinter import messagebox, filedialog
from tkinter.ttk import *

HEIGHT = 700
WIDTH = 800


def elp():
    root = tk.Tk()
    root.title("SNV Krack")
    canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
    canvas.pack()

    # background_image = tk.PhotoImage(file='abc.jpg')
    # background_label = tk.Label(root, image=background_image)
    # background_label.place(relwidth=1, relheight=1)

    checkvar1 = tk.IntVar()
    checkvar2 = tk.IntVar()
    checkvar3 = tk.IntVar()

    frame = tk.Frame(root, bg='white', bd=5)
    frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.2, anchor='n')

    # label = tk.Label(frame, text="The name of the file ", bg='#99d6ff', font=50)
    # label.place(relwidth=0.65, relheight=0.45)

    # button = tk.Button(frame, text="Name of the file", bg='#99d6ff', font=500, command=lambda: leopen())
    button = tk.Button(frame, text="Name of the file", bg='#99d6ff', font=500, command=lambda: leopen(entry))
    button.place(relwidth=0.65, relheight=0.45)

    entry = tk.Entry(frame, font=50, bg='#99d6ff')
    entry.place(rely=0.5, relwidth=0.65, relheight=0.5)

    lower_frame = tk.Frame(root, bg='#99d6ff', bd=10)
    lower_frame.place(relx=0.5, rely=0.35, relwidth=0.75, relheight=0.55, anchor='n')

    pgbar = Progressbar(lower_frame, length=350, orient=VERTICAL, mode='indeterminate')
    pgbar.place(relx=0.9)

    button = tk.Button(frame, text="Find password", bg='yellow', fg='red', font=500,
                       command=lambda: test_function(entry, entry1, checkvar1, checkvar2, checkvar3, pgbar))
    button.place(relx=0.7, relwidth=0.3, relheight=0.5)

    button = tk.Button(frame, text="cancel", bg='yellow', fg='red', font=500, command=lambda: clicked(pgbar))
    button.place(relx=0.7, relwidth=0.3, relheight=0.45, rely=0.55)

    a = tk.Checkbutton(lower_frame, text="0-9  -   numeric digits only", variable=checkvar1, onvalue=1, offvalue=0)
    a.place(relx=0.0, rely=0.15)

    b = tk.Checkbutton(lower_frame, text="a-z -  small alphabets only", variable=checkvar2, onvalue=1, offvalue=0)
    b.place(relx=0.0, rely=0.25)

    c = tk.Checkbutton(lower_frame, text="A-Z capital alphabets only", variable=checkvar3, onvalue=1, offvalue=0)
    c.place(relx=0.0, rely=0.35)

    label = tk.Label(lower_frame, text="Hints about the password", bg='yellow')
    label.place(relwidth=0.8, relheight=0.1)

    label = tk.Label(lower_frame, text="length of the password ", bg='yellow')
    label.place(rely=0.45, relwidth=0.35, relheight=0.1)

    label = tk.Label(lower_frame, text="current word", bg='yellow')
    label.place(rely=0.45, relwidth=0.5, relheight=0.1, relx=0.38)

    entry1 = tk.Entry(lower_frame, font=50, bg='white')
    entry1.place(rely=0.6, relwidth=0.35, relheight=0.1)

    label = tk.Label(lower_frame, text="...", bg='white')
    label.place(rely=0.6, relwidth=0.5, relheight=0.1, relx=0.38)

    label = tk.Label(lower_frame, text="Possible string in the password", bg='yellow')
    label.place(rely=0.75, relwidth=0.8, relheight=0.1)

    # labelfinal = tk.Label(lower_frame, text="...", bg='white')
    # labelfinal.place(rely=0.9, relwidth=0.8, relheight=0.1)

    entrywhy = tk.Entry(lower_frame, bg='white')
    entrywhy.place(rely=0.9, relwidth=0.8, relheight=0.1)

    root.mainloop()


def madat():
    root = tk.Tk()
    root.title("SNV Krack")
    canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
    canvas.pack()

    # background_image = tk.PhotoImage(file='abc.jpg')
    # background_label = tk.Label(root, image=background_image)
    # background_label.place(relwidth=1, relheight=1)

    checkvar1 = tk.IntVar()
    checkvar2 = tk.IntVar()
    checkvar3 = tk.IntVar()

    frame = tk.Frame(root, bg='white', bd=5)
    frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.2, anchor='n')

    # button = tk.Button(frame, text="Name of the file", bg='#99d6ff', font=500, command=lambda: leopen())
    labelllii = tk.Label(frame, text="Enter the Hash Value", bg='yellow')
    labelllii.place(relwidth=0.65, relheight=0.45)

    entry = tk.Entry(frame, font=50, bg='#99d6ff')
    entry.place(rely=0.5, relwidth=0.65, relheight=0.5)

    lower_frame = tk.Frame(root, bg='#99d6ff', bd=10)
    lower_frame.place(relx=0.5, rely=0.35, relwidth=0.75, relheight=0.55, anchor='n')

    pgbar = Progressbar(lower_frame, length=350, orient=VERTICAL, mode='indeterminate')
    pgbar.place(relx=0.9)

    button = tk.Button(frame, text="Crack hash", bg='yellow', fg='red', font=500,
                       command=lambda: test_function(entry, entry1, checkvar1, checkvar2, checkvar3, pgbar))
    button.place(relx=0.7, relwidth=0.3, relheight=0.5)

    button = tk.Button(frame, text="cancel", bg='yellow', fg='red', font=500, command=lambda: clicked(pgbar))
    button.place(relx=0.7, relwidth=0.3, relheight=0.45, rely=0.55)

    a = tk.Checkbutton(lower_frame, text="0-9  -   numeric digits only", variable=checkvar1, onvalue=1, offvalue=0)
    a.place(relx=0.0, rely=0.15)

    b = tk.Checkbutton(lower_frame, text="a-z -  small alphabets only", variable=checkvar2, onvalue=1, offvalue=0)
    b.place(relx=0.0, rely=0.25)

    c = tk.Checkbutton(lower_frame, text="A-Z capital alphabets only", variable=checkvar3, onvalue=1, offvalue=0)
    c.place(relx=0.0, rely=0.35)

    label = tk.Label(lower_frame, text="Hints about the word", bg='yellow')
    label.place(relwidth=0.8, relheight=0.1)

    label = tk.Label(lower_frame, text="length of the word ", bg='yellow')
    label.place(rely=0.45, relwidth=0.35, relheight=0.1)

    label = tk.Label(lower_frame, text="current word", bg='yellow')
    label.place(rely=0.45, relwidth=0.5, relheight=0.1, relx=0.38)

    entry1 = tk.Entry(lower_frame, font=50, bg='white')
    entry1.place(rely=0.6, relwidth=0.35, relheight=0.1)

    label = tk.Label(lower_frame, text="...", bg='white')
    label.place(rely=0.6, relwidth=0.5, relheight=0.1, relx=0.38)

    label = tk.Label(lower_frame, text="Possible string in the word", bg='yellow')
    label.place(rely=0.75, relwidth=0.8, relheight=0.1)

    # labelfinal = tk.Label(lower_frame, text="...", bg='white')
    # labelfinal.place(rely=0.9, relwidth=0.8, relheight=0.1)

    entrywhy = tk.Entry(lower_frame, bg='white')
    entrywhy.place(rely=0.9, relwidth=0.8, relheight=0.1)

    root.mainloop()


def leopen(entry):
    file1 = filedialog.askopenfilename(title='Choose file', filetypes=[('pdf file', '*.pdf'), ("Excel files", ".xlsx")])
    entry.insert(0, file1)


def clicked(pgbar):
    blaa = messagebox.askokcancel("Cracking in progress", "Do you wish to abort")
    if blaa == 1:
        pgbar.stop()


def test_function(entry, entry1, checkvar1, checkvar2, checkvar3, pgbar):
    result = entry.get()
    length1 = entry1.get()
    a1 = checkvar1.get()
    b1 = checkvar2.get()
    c1 = checkvar3.get()
    #   labelfinal.config(text=result)
    length = entry1.get()
    pgbar.start(30)


bla = tk.Tk()

bla.title("SNV Krack")
canvas1 = tk.Canvas(bla, height=HEIGHT, width=WIDTH)
canvas1.pack()

frame2 = tk.Frame(bla, bg='white', bd=5)
frame2.place(relx=0.0, rely=0.0, relwidth=1, relheight=1)

# background_image = tk.PhotoImage(file='abc.jpg')
# background_label = tk.Label(frame2, image=background_image)
# background_label.place(relwidth=1, relheight=1)

buttone = tk.Button(frame2, text="File password cracker", bg='#99d6ff', font=500, command=lambda: elp())
buttone.place(relx=0.1, rely=0.65, relwidth=0.8, relheight=0.1)

buttone1 = tk.Button(frame2, text="Hash cracker", bg='#99d6ff', font=500, command=lambda: madat())
buttone1.place(relx=0.1, rely=0.8, relwidth=0.8, relheight=0.1)

bla.mainloop()
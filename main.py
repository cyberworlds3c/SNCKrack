import hashcracker
import string
import PDFCracker
import Exceltry
import tkinter as tk
from tkinter import *
from tkinter import messagebox, filedialog
from tkinter.ttk import *
from PIL import ImageTk

HEIGHT = 700
WIDTH = 800

zero_to_nine = 0
a_to_z = 0
A_TO_Z = 0


def number():
    global zero_to_nine
    zero_to_nine = 1


def small_alpha():
    global a_to_z
    a_to_z = 1


def cap_alpha():
    global A_TO_Z
    A_TO_Z = 1


def filecrack():
    root = tk.Tk()
    root.title("SNV Krack")
    canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
    canvas.pack()

    frame = tk.Frame(root, bg='#444141', bd=5)
    frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.2, anchor='n')

    button = tk.Button(frame, text="Click here to add file / Name of the file", bg='#54bf74', fg='white', font=500,
                       command=lambda: leopen(entry))
    button.place(relwidth=0.6523, relheight=0.45)

    entry = tk.Entry(frame, font=50, bg='#6ec37b')
    entry.place(rely=0.5, relwidth=0.65, relheight=0.5)

    lower_frame = tk.Frame(root, bg='black', bd=10)
    lower_frame.place(relx=0.5, rely=0.35, relwidth=0.75, relheight=0.55, anchor='n')

    pgbar = Progressbar(lower_frame, length=350, orient=VERTICAL, mode='indeterminate')
    pgbar.place(relx=0.9)

    button = tk.Button(frame, text="cancel", bg='#7cc587', fg='white', font=500, command=lambda: clicked(pgbar))
    button.place(relx=0.7, relwidth=0.3, relheight=0.45, rely=0.55)

    a = tk.Checkbutton(lower_frame, text="0-9  -   numeric digits only", command=lambda: number())
    a.place(relx=0.0, rely=0.15)

    b = tk.Checkbutton(lower_frame, text="a-z -  small alphabets only", command=lambda: small_alpha())
    b.place(relx=0.0, rely=0.25)

    c = tk.Checkbutton(lower_frame, text="A-Z capital alphabets only", command=lambda: cap_alpha())
    c.place(relx=0.0, rely=0.35)

    button = tk.Button(frame, text="Find password", bg='#54bf74', fg='white', font=500,
                       command=lambda: file_crack(entry, entry1, pgbar, possible_string))
    button.place(relx=0.7, relwidth=0.3, relheight=0.5)

    label = tk.Label(lower_frame, text="Hints about the password", bg='blue')
    label.place(relwidth=0.8, relheight=0.1)

    label = tk.Label(lower_frame, text="length of the password ", bg='blue')
    label.place(rely=0.45, relwidth=0.29, relheight=0.1)

    entry1 = tk.Entry(lower_frame, font=50, bg='white')
    entry1.place(rely=0.6, relwidth=0.29, relheight=0.1)


    label = tk.Label(lower_frame, text="Possible string in the password", bg='yellow')
    label.place(rely=0.75, relwidth=0.8, relheight=0.1)

    # labelfinal = tk.Label(lower_frame, text="...", bg='white')
    # labelfinal.place(rely=0.9, relwidth=0.8, relheight=0.1)

    possible_string = tk.Entry(lower_frame, bg='white')
    possible_string.place(rely=0.9, relwidth=0.8, relheight=0.1)

    root.mainloop()


def hashcrack():
    root = tk.Tk()
    root.title("SNV Krack")
    canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
    canvas.pack(expand=YES, fill=BOTH)
    # im = ImageTk.PhotoImage(file="C:/Users/smits/Music/download.png")
    # canvas1.create_image(100, 50, image=im, anchor=NW)

    # background_image = tk.PhotoImage(file='C:\Users\smits\Music\download.jpg')
    # background_label = tk.Label(root, image=background_image)
    # background_label.place(relwidth=1, relheight=1)

    frame = tk.Frame(root, bg='white', bd=5)
    frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.2, anchor='n')

    label1 = tk.Label(frame, text="Enter the Hash Value", bg='yellow')
    label1.place(relwidth=0.65, relheight=0.45)

    # FILE_ENTRY

    given_hash = tk.Entry(frame, font=50, bg='#99d6ff')
    given_hash.place(rely=0.5, relwidth=0.65, relheight=0.5)

    lower_frame = tk.Frame(root, bg='#99d6ff', bd=10)
    lower_frame.place(relx=0.5, rely=0.35, relwidth=0.75, relheight=0.55, anchor='n')

    pgbar = Progressbar(lower_frame, length=350, orient=VERTICAL, mode='indeterminate')
    pgbar.place(relx=0.9)

    button = tk.Button(frame, text="Crack Hash", bg='yellow', fg='red', font=500,
                       command=lambda: hash_crack(given_hash, pass_len, pgbar, possible_string))
    button.place(relx=0.7, relwidth=0.3, relheight=0.5)

    button = tk.Button(frame, text="cancel", bg='yellow', fg='red', font=500, command=lambda: clicked(pgbar))
    button.place(relx=0.7, relwidth=0.3, relheight=0.45, rely=0.55)

    a = tk.Checkbutton(lower_frame, text="0-9  -   numeric digits only", command=lambda: number())
    a.place(relx=0.0, rely=0.15)

    b = tk.Checkbutton(lower_frame, text="a-z -  small alphabets only", command=lambda: small_alpha())
    b.place(relx=0.0, rely=0.25)

    c = tk.Checkbutton(lower_frame, text="A-Z capital alphabets only", command=lambda: cap_alpha())
    c.place(relx=0.0, rely=0.35)

    label1 = tk.Label(lower_frame, text="Hints about the word", bg='yellow')
    label1.place(relwidth=0.8, relheight=0.1)

    label1 = tk.Label(lower_frame, text="length of the word ", bg='yellow')
    label1.place(rely=0.45, relwidth=0.29, relheight=0.1)

    pass_len = tk.Entry(lower_frame, font=50, bg='white')
    pass_len.place(rely=0.6, relwidth=0.29, relheight=0.1)

    label1 = tk.Label(lower_frame, text="Possible string in the word", bg='yellow')
    label1.place(rely=0.75, relwidth=0.8, relheight=0.1)

    possible_string = tk.Entry(lower_frame, bg='white')
    possible_string.place(rely=0.9, relwidth=0.8, relheight=0.1)

    root.mainloop()


def leopen(entry):
    file1 = filedialog.askopenfilename(title='Choose file', filetypes=[('pdf file', '*.pdf'), ("Excel files", ".xlsx")])
    entry.insert(0, file1)


def clicked(pgbar):
    blaa = messagebox.askokcancel("Cracking in progress", "Do you wish to abort")
    if blaa == 1:
        pgbar.stop()


def file_crack(file_entry, len_pass, pgbar, possible_string):
  #  pgbar.start()
    file_name = file_entry.get()
    length = len_pass.get()
    charset = possible_string.get()
    #   labelfinal.config(text=result)

    char = ''

    if charset == '':
        if zero_to_nine == 1:
            char += string.digits

        if a_to_z == 1:
            char += string.ascii_lowercase

        if A_TO_Z == 1:
            char += string.ascii_uppercase

        elif zero_to_nine == 0 and a_to_z == 0 and A_TO_Z == 0:
            char = string.ascii_letters + string.digits + '!#$%&*?@^~'

    else:
        char = charset

    if '.pdf' in file_name:
        if length == '':
            PDFCracker.pdfcracker(file_name, char)
        else:
            length1 = int(len_pass.get())
            PDFCracker.pdfcracker_len(file_name, char, length1)

    elif '.xlsx' in file_name:
        if length == '':
            Exceltry.xlsxcracker(file_name, char)
        else:
            length1 = int(len_pass.get())
            Exceltry.xlsxcracker_len(file_name, char, length1)

    else:
        pgbar.stop()
        messagebox.showerror(0, "Invalide file name")


def hash_crack(hash_entry, pass_len, pgbar, possible_string, ):
    pgbar.start()
    given_hash = hash_entry.get()
    hash = given_hash.lower()
    charset = possible_string.get()

    char = ''

    if charset == '':
        if zero_to_nine == 1:
            char += string.digits

        if a_to_z == 1:
            char += string.ascii_lowercase

        if A_TO_Z == 1:
            char += string.ascii_uppercase

        elif zero_to_nine == 0 and a_to_z == 0 and A_TO_Z == 0:
            char = string.ascii_letters + string.digits + '!#$%&*?@^~'

    else:
        char = charset

    if pass_len.get() == '':

        if len(hash) == 32:
            hashcracker.md5(hash, char)

        elif len(hash) == 64:
            hashcracker.sha256(hash, char)

        elif len(hash) == 128:
            hashcracker.sha512(hash, char)

        else:
            messagebox.showerror(0, "Hash not in our database!!!")

    else:
        length = int(pass_len.get())
        if len(hash) == 32:
            hashcracker.md5_len(hash, char, length)

        elif len(hash) == 64:
            hashcracker.sha256_len(hash, char, length)

        elif len(hash) == 128:
            hashcracker.sha512_len(hash, char, length)

        else:
            messagebox.showerror(0, "Hash not in our database!!!")


if __name__ == '__main__':
    main_screen = tk.Tk()

    main_screen.title("SNV Krack")
    canvas1 = tk.Canvas(main_screen, height=main_screen.winfo_screenwidth() + 100,
                        width=main_screen.winfo_screenwidth(), bg="black")
    canvas1.pack(expand=YES, fill=BOTH)
    image = ImageTk.PhotoImage(file="C:/Users/smits/Music/finall.png")
    canvas1.create_image(100, 50, image=image, anchor=NW)

    frame2 = tk.Frame(main_screen, bg='black')
    frame2.place(relx=0.0, rely=0.55, relwidth=1, relheight=0.3)

    pgbar = Progressbar(frame2, length=1000, orient=HORIZONTAL, mode='indeterminate')
    pgbar.place(relx=0.2)
    pgbar.start()
    # frame2.create_image(10, 10, image=image, anchor=NW)

    buttone = tk.Button(frame2, text="File password cracker", bg='#99d6ff', font=500, command=lambda: filecrack())
    buttone.place(relx=0.1, rely=0.3, relwidth=0.8, relheight=0.3)

    buttone1 = tk.Button(frame2, text="Hash cracker", bg='#99d6ff', font=500, command=lambda: hashcrack())
    buttone1.place(relx=0.1, rely=0.7, relwidth=0.8, relheight=0.3)

    main_screen.mainloop()

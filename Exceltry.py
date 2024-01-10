from tkinter import messagebox


def xlsxcracker(file, char):
    import itertools
    import win32com.client
    import time
    flag = 0
    start = time.time()

    for n in range(1, 16):
        for temp in itertools.product(char, repeat=n):

            print("Testing password:" + ''.join(temp))
            instance = win32com.client.Dispatch("Excel.Application")

            try:
                instance.Workbooks.open(file, True, False, None, ''.join(temp))
                flag = 1
                c = "Password of the ExcelFile is  " + ''.join(temp)
                messagebox.showinfo("Hash decryption found", c)
                print("Password cracked: " + ''.join(temp))
                break

            except:
                pass

        if flag == 1:
            break
    end = time.time()
    t_time = end - start
    print("Total running time : ", t_time, "seconds")


def xlsxcracker_len(file, char, len):
    import itertools
    import win32com.client
    import time

    flag = 0

    start = time.time()

    for n in range(len, len + 1):
        for temp in itertools.product(char, repeat=n):

            print("Testing password:" + ''.join(temp))
            instance = win32com.client.Dispatch("Excel.Application")

            try:
                instance.Workbooks.open(file, True, False, None, ''.join(temp))
                flag = 1
                c = "Password of the ExcelFile is  " + ''.join(temp)
                messagebox.showinfo("Hash decryption found", c)
                print("Password cracked: " + ''.join(temp))
                break

            except:
                pass

        if flag == 1:
            break
    end = time.time()
    t_time = end - start
    print("Total running time : ", t_time, "seconds")

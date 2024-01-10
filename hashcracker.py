# SHA-512 HASH CRACKER WITHOUT LENGTH
from tkinter import messagebox


def sha512(pass_hash, char):
    import hashlib
    import itertools
    import time

    flag = 0
    start = time.time()

    for n in range(1, 16):

        for tryword in itertools.product(char, repeat=n):
            enc_wrd = ''.join(tryword).encode('utf-8')
            digest = hashlib.sha512(enc_wrd.strip()).hexdigest()

            end = time.time()
            t_time = end - start

            print(''.join(tryword))
            print(digest)
            print(pass_hash)

            if digest == pass_hash:
                print("Hash Cracked")
                print("Cracked Hash is " + ''.join(tryword))
                flag = 1
                print("Total running time : ", t_time, "seconds")
                c = "The decrypted word from the input hash= " + ''.join(tryword)
                messagebox.showinfo("Hash decryption found", c)
                time.sleep(10)

                break

    if flag == 0:
        print("Hash is not in the list")


# MD5 HASH CRACKER WITHOUT LENGTH


def md5(pass_hash, char):
    import hashlib
    import time

    import itertools

    flag = 0

    start = time.time()

    for n in range(1, 16):

        for tryword in itertools.product(char, repeat=n):

            enc_wrd = ''.join(tryword).encode('utf-8')
            digest = hashlib.md5(enc_wrd.strip()).hexdigest()

            end = time.time()
            t_time = end - start

            print(''.join(tryword))
            print(digest)
            print(pass_hash)

            if digest == pass_hash:
                print("Hash Cracked")
                print("Cracked Hash is " + ''.join(tryword))
                flag = 1

                print("Total running time : ", t_time, "seconds")
                # time.sleep(10)
                c = "The decrypted word from the input hash= " + ''.join(tryword)
                messagebox.showinfo("Hash decryption found", c)
                time.sleep(10)

                break

        if flag == 1:
            break

    if flag == 0:
        print("Hash is not in the list")


# SHA-256 HASH CRACKER WITHOUT LENGTH


def sha256(pass_hash, char):
    import hashlib
    import itertools
    import time

    flag = 0

    start = time.time()

    for n in range(1, 16):

        for tryword in itertools.product(char, repeat=n):

            enc_wrd = ''.join(tryword).encode('utf-8')
            digest = hashlib.sha256(enc_wrd.strip()).hexdigest()

            end = time.time()
            t_time = end - start

            print(''.join(tryword))
            print(digest)
            print(pass_hash)

            if digest == pass_hash:
                print("Hash Cracked")
                print("Cracked Hash is " + ''.join(tryword))
                flag = 1
                print("Total running time : ", t_time, "seconds")
                c = "The decrypted word from the input hash= " + ''.join(tryword)
                messagebox.showinfo("Hash decryption found", c)
                time.sleep(10)

                break

    if flag == 0:
        print("Hash is not in the list")


# SHA-512 HASH CRACKER WITH LENGTH


def sha512_len(pass_hash, char, len):
    import hashlib
    import itertools
    import time

    flag = 0
    start = time.time()

    for n in range(len, len + 1):

        for tryword in itertools.product(char, repeat=n):

            enc_wrd = ''.join(tryword).encode('utf-8')
            digest = hashlib.sha512(enc_wrd.strip()).hexdigest()

            end = time.time()
            t_time = end - start

            print(''.join(tryword))
            print(digest)
            print(pass_hash)

            if digest == pass_hash:
                print("Hash Cracked")
                print("Cracked Hash is " + ''.join(tryword))
                flag = 1
                print("Total running time : ", t_time, "seconds")
                c = "The decrypted word from the input hash= " + ''.join(tryword)
                messagebox.showinfo("Hash decryption found", c)
                time.sleep(10)

                break

    if flag == 0:
        print("Hash is not in the list")


# MD5 HASH CRACKER WITH LENGTH


def md5_len(pass_hash, char, pass_len):
    import hashlib
    import time
    import itertools

    flag = 0

    start = time.time()

    for n in range(pass_len, pass_len + 1):

        for tryword in itertools.product(char, repeat=n):

            enc_wrd = ''.join(tryword).encode('utf-8')
            digest = hashlib.md5(enc_wrd.strip()).hexdigest()

            end = time.time()
            t_time = end - start

            print(''.join(tryword))
            print(digest)
            print(pass_hash)

            if digest == pass_hash:
                print("Hash Cracked")
                print("Cracked Hash is " + ''.join(tryword))
                flag = 1
                print("Total running time : ", t_time, "seconds")
                c = "The decrypted word from the input hash= " + ''.join(tryword)
                messagebox.showinfo("Hash decryption found", c)
                time.sleep(10)

                break

    if flag == 0:
        print("Hash is not in the list")


# SHA-256 HASH CRACKER WITH LENGTH


def sha256_len(pass_hash, char, len):
    import hashlib
    import itertools
    import time

    flag = 0

    start = time.time()

    for n in range(len, len + 1):

        for tryword in itertools.product(char, repeat=n):

            enc_wrd = ''.join(tryword).encode('utf-8')
            digest = hashlib.sha256(enc_wrd.strip()).hexdigest()

            end = time.time()
            t_time = end - start

            print(''.join(tryword))
            print(digest)
            print(pass_hash)


            if digest == pass_hash:
                print("Hash Cracked")
                print("Cracked Hash is " + ''.join(tryword))
                flag = 1
                print("Total running time : ", t_time, "seconds")
                c = "The decrypted word from the input hash= " + ''.join(tryword)
                assn = ''.join(tryword)
                messagebox.showinfo("Hash decryption found", c)
                time.sleep(10)

                break

    if flag == 0:
        print("Hash is not in the list")

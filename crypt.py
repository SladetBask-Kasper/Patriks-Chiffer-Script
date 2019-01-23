#!/usr/bin/python
# coding=utf-8
from os import system
import collections
from sys import argv

def chunks(l, n): # l = array(string), n = chunksize

    chunk1 = []

    while True:
        try:
            if len(l) == 0:
                break
            chunk1.append(l[:n])
            l = l[n:]
        except IndexError:
            n -= 1
            if len(l) == 0 or n <= 0:
                break
    return chunk1

def crypt(iword = "_NONE_", ikey = "_NONE_", kwargs = "_NONE_"):
    if iword == "_NONE_":
        iword = str(input("Enter Word: "))
    if ikey == "_NONE_":
        ikey = str(input("Enter Key: "))
    key = list(ikey)
    word = list(iword)
    conclution = ""
    y = 0
    x = len(word)
    while y < x:
        for k in key:

            z = int(k)
            try:
                conclution += word[z]
            except IndexError:
                #print("DEBUG: Index error")
                conclution += "x" # add 'x' to end if not char found and if msg is unfit for chunking
                y += 1
            y += 1

        word = iword[y:]

    print("conclution: " + str(conclution))

    if kwargs.lower() == "hold":
        input()
        exit()

def decrypt(iword = "_NONE_", ikey = "_NONE_", kwargs = "_NONE_"):

    if iword == "_NONE_":
        iword = str(input("Enter Word: "))
    if ikey == "_NONE_":
        ikey = str(input("Enter Key: "))

    rev_key = str(ikey)[::-1]
    rev_word = str(iword)[::-1]


    crev_word = chunks(rev_word, len(rev_key))
    crev_word = crev_word[::-1]
    conclution = ""

    for w in crev_word:
        d = {}
        for i in range(len(rev_key)):

            try:
                d[rev_key[i]] = w[i]
            except IndexError:
                if not kwargs.lower() == "quiet": print("ERROR: out of index (Invalid chunk size?)")
        od = collections.OrderedDict(sorted(d.items()))
        for odk in od:
            conclution += od[odk]

    if not kwargs.lower() == "quiet":
        print("conclution: " + str(conclution))

    if kwargs.lower() == "hold":
        input()
        exit()

    return conclution

def bruteforce(iword = "_NONE_", imin = "100", imax = "100000", scanmode = "_NONE_"):

    if iword == "_NONE_":
        iword = str(input("Enter Word: "))

    min = int(imin)
    max = int(imax)

    sfor = "_NONE_"
    if "-search-for:" in scanmode:
        sfor = scanmode[len("-search-for:"):]
        print("Searching for : " + str(sfor))

    try:
        while min <= max:
            tmp = decrypt(iword, str(min), "quiet")
            if len(tmp) == len(iword):
                if scanmode == "--scan-mode":
                    if "hitta" in tmp.lower() or "hon" in tmp.lower() or "hur" in tmp.lower() or "var" in tmp.lower() or "uppgift" in tmp.lower() or "lämna" in tmp.lower() or "bra" in tmp.lower() or "ord" in tmp.lower() or "åtminstonde" in tmp.lower() or "tack" in tmp.lower() or "hur" in tmp.lower() or "kan" in tmp.lower() or "dag" in tmp.lower() or "öga" in tmp.lower() or "väg" in tmp.lower() or "vidrig" in tmp.lower() or "kax" in tmp.lower() or "väg" in tmp.lower() or "och" in tmp.lower() or "vad" in tmp.lower() or "svår" in tmp.lower() or "stop" in tmp.lower() or "jävla" in tmp.lower() or "rikti" in tmp.lower() or "för" in tmp.lower() or "slut" in tmp.lower():
                        print(str(min) + " : " + tmp)
                elif not sfor == "_NONE_":
                    if tmp.lower() == sfor.lower():
                        print(str(min) + " : " + tmp)
                else: print(str(min) + " : " + tmp)
            min += 1
    except KeyboardInterrupt:
        pass
    print("Jobs Done!")
    print("Tested: " + str(min) + " combinations!")
    exit()

# hjälp meny
def help_menu():
    print(" --=^=--- Help menu --=^=--")
    print("python_script.py (arg1) [(arg2) (arg3) (arg4) (arg5)]")
    print("\t(arg1)--decrypt")
    print("\t(arg1)--encrypt")
    print("\t(arg1)--bruteforce")
    print("\t(arg1)--search-for")
    print("--------------------------------")
    print("\t(arg2)msg")
    print("\t(arg3)key (alt: min key)")
    print("\t(arg4)maxkey")
    print("\t(arg5)--scan-mode")

    print("\n=============================\nFor more details, check out Github: \"https://github.com/SladetBask-Kasper/Patriks-Chiffer-Script\"\n=============================\n")

    exit()

def check_arg(argno):
    try:
        if argv[argno]:
            pass
    except:
        return False
    else:
        return True

# Arg parser
if __name__ == "__main__":
    if not check_arg(1):
        print("1: encrypt, 2: decrypt.")
        l = str(input(" > "))
        if l == "1":
            crypt(iword = "_NONE_", ikey = "_NONE_", kwargs = "hold")
        elif l == "2":
            decrypt(iword = "_NONE_", ikey = "_NONE_", kwargs = "hold")
        else:
            print("Error- Invalid input value")
            exit()
    else:
        if check_arg(1):

            if not check_arg(2):
                if argv[1] == "--encrypt": crypt()
                elif argv[1] == "--decrypt": decrypt()
                else: help_menu()
            else:
                x = len(argv) -1 # 0 = 1 otherwise
                if argv[1] == "--encrypt":
                    if check_arg(3): crypt(argv[2], argv[3])
                    else: crypt(argv[2])
                elif argv[1] == "--decrypt":
                    if check_arg(3): decrypt(argv[2], argv[3])
                    else: decrypt(argv[2])
                elif argv[1] == "--bruteforce":
                    if x >= 5: bruteforce(argv[2], argv[3], argv[4], argv[5])
                    elif x == 4: bruteforce(argv[2], argv[3], argv[4])
                    elif x == 3: bruteforce(argv[2], argv[3])
                    elif x == 2: bruteforce(argv[2])
                    elif x == 1: bruteforce()
                elif argv[1] == "--search-for":
                    if x >= 5: bruteforce(argv[2], argv[4], argv[5], "-search-for:" + argv[3])
                    elif x == 4: bruteforce(argv[2], argv[4], "9999999999", "-search-for:" + argv[3])
                    elif x == 3: bruteforce(argv[2], "100", "9999999999", "-search-for:" + argv[3])
                    elif x <= 2:
                        argv2 = "_NONE_"
                        if x == 2:
                            argv2 = argv[2]
                        print("What do you wanna search for?")
                        print("type \"::Exit\" to exit")
                        inp = str(input(" > "))
                        if inp.lower() == "::exit":
                            exit()
                        else: bruteforce(argv2, "100", "9999999999", "-search-for:" + inp)
                else:
                    help_menu()

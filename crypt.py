from os import system
import collections
from sys import argv

def chunks(l, n): # l = array, n = chunksize?

    x = 0
    chunk1 = []

    while True:
        try:
            if len(l) == 0:
                break
            chunk1.append(l[:n])#
            l = l[n:]
        except IndexError:
            n -= 1
            if len(l) == 0 or n <= 0:
                break
    return chunk1

def crypt(iword = "_NONE_", ikey = "_NONE_"):
    if iword == "_NONE_":
        iword = str(input("Enter Word: "))
    if ikey == "_NONE_":
        ikey = str(input("Enter Key: "))
    key = list(ikey)
    word = list(iword)
    #word = ["A", "A", "V", "E", "L", "D", "T", "E", "T", "Ö", "D", "G"]
    #key = ["2", "3", "1", "0", "2", "3", "1", "0"]
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

def decrypt(iword = "_NONE_", ikey = "_NONE_", kwargs = "_NONE_"):

    if iword == "_NONE_":
        iword = str(input("Enter Word: "))
    if ikey == "_NONE_":
        ikey = str(input("Enter Key: "))

    key = list(ikey)
    word = list(iword)
    #key = ["3", "5", "2", "1", "4", "0", "3", "5", "2", "1", "4", "0"]
    #word = ["A", "A", "V", "E", "L", "D", "T", "E", "T", "Ö", "D", "G"]

    converted_key = []

    for i in key:
        converted_key.append(int(i))

    sorted_key = sorted(converted_key)
    sorted_word = sorted(word)

    rev_key = str(ikey)[::-1]
    rev_word = str(iword)[::-1]


    xx = len(rev_key)
    crev_word = chunks(rev_word, xx)
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
    return conclution

def bruteforce(iword = "_NONE_", imin = "100", imax = "100000", scanmode = "_NONE_"):

    if iword == "_NONE_":
        iword = str(input("Enter Word: "))

    min = int(imin)
    max = int(imax)

    while min <= max:
        tmp = decrypt(iword, str(min), "quiet")
        if len(tmp) == len(iword):
            if scanmode == "--scan-mode":
                if "hitta" in tmp.lower() or "hon" in tmp.lower() or "hur" in tmp.lower() or "var" in tmp.lower() or "uppgift" in tmp.lower() or "lämna" in tmp.lower() or "bra" in tmp.lower() or "ord" in tmp.lower() or "åtminstonde" in tmp.lower() or "tack" in tmp.lower() or "hur" in tmp.lower() or "kan" in tmp.lower() or "dag" in tmp.lower() or "öga" in tmp.lower() or "väg" in tmp.lower() or "vidrig" in tmp.lower() or "kax" in tmp.lower() or "väg" in tmp.lower() or "och" in tmp.lower() or "vad" in tmp.lower() or "svår" in tmp.lower() or "stop" in tmp.lower() or "jävla" in tmp.lower() or "rikti" in tmp.lower() or "för" in tmp.lower() or "slut" in tmp.lower():
                    print(str(min) + " : " + tmp)
            else: print(str(min) + " : " + tmp)
        min += 1
    print("Jobs Done!")
    exit()

# hjälp meny
def help_menu():
    print("Help menu isn't working")
    exit()

# Arg parser
if __name__ == "__main__":
    try:
        if argv[1]:
            pass
    except:
        print("1: encrypt, 2: decrypt.")
        l = str(input(" > "))
        if l == "1":
            crypt()
        elif l == "2":
            decrypt()
        else:
            print("Error- Invalid input value")
    else:

        if argv[1] == "--encrypt" or argv[1] == "--decrypt":
            try:
                if argv[2]:
                    pass
            except:
                if argv[1] == "--encrypt":
                    crypt()
                elif argv[1] == "--decrypt":
                    decrypt()
            else:
                try:
                    if argv[3]:
                        pass
                except:
                    if argv[1] == "--encrypt":
                        crypt(argv[2])
                    elif argv[1] == "--decrypt":
                        decrypt(argv[2])
                else:
                    if argv[1] == "--encrypt":
                        crypt(argv[2], argv[3])
                    elif argv[1] == "--decrypt":
                        decrypt(argv[2], argv[3])
        elif argv[1] == "--bruteforce":
            try:
                if argv[2]:
                    pass
            except:
                bruteforce()
            else:
                try:
                    if argv[3]:
                        pass
                except:
                    bruteforce(argv[2])
                else:
                    try:
                        if argv[4]:
                            pass
                    except:
                        bruteforce(argv[2], argv[3])
                    else:
                        try:
                            if argv[5]:
                                pass
                        except:
                            bruteforce(argv[2], argv[3], argv[4])
                        else:
                            bruteforce(argv[2], argv[3], argv[4], argv[5])
        else :
            help_menu()

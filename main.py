from time import sleep as wait
from os import system as cmd
from kerdesek import *
penz = ""
def k1():
    q1()
    startq = input("             ")
    if startq == "c":
        penz = 5000
        k2()
    else:
        print(f"Nem jó válasz! Nyeremény: {penz}")


def k2():
    pass
def main():
    cmd("clear")
    try:
        start()
        startq = input("             ")
        if startq == "a":
            k1()
        else:
            exit()
    except ValueError:
        main()


if __name__ == "__main__":
    main()
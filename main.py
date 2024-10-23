from time import sleep as wait
from os import system as cmd
from kerdesek import *
fix_penz = 0
penz = 0

def k0(kerdes):
    global penz, fix_penz
    q0(kerdes[0])
    startq = input("             ")
    if startq == kerdes[1]:
        penz += kerdes[2]
    elif startq == "s":
        print(f"Kiszálltál! A nyereményed: {penz}Ft")
        re = input(f"Szeretnéd újrakezdeni? igen(a) || nem(b):  ")
        if re == "a":
            return "main"
        else:
            return "exit"
    else:
        print(f"Nem jó válasz! Elbukott Nyeremény: {penz}Ft")
        return "exit"


def main():
    while True:
        cmd("clear")
        try:
            start()
            startq = input("             ")
            if startq == "a":
                for kerdes in fkerdesek():
                    ret=k0(kerdes)
                    if ret == "main":
                        break
                    elif ret == "exit":
                        exit()
            else:
                exit()
            # Ha ide elért mindre válaszolt
            print(f"{bcolors.OKGREEN}Gratulálok!{bcolors.ENDC}\nSikeresen végigvitted. Nyereményed: 40.000.000Ft.")
            uj = input("Szeretnéd újrakezdeni? igen(a) || nem(b):  ")
            if uj == "a":
                return "main"
            else:
                exit()
        except ValueError:
            pass

if __name__ == "__main__":
    main()
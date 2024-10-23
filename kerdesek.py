class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def start():
    print("-----------------------------------------------")
    print("| Legyen ön is milliomos                      |")
    print("| Tájékoztató:                                |")
    print("| - Mindig a, b, c vagy d-vel kell válaszolnia|")
    print("| - A játékmenet során bármikor kiszállhat    |")
    print("|     ha beír egy 's' betűt                   |")
    print("| - A játékmenet során kérhetsz internetes    |")
    print("|     segítséget egyszer ha beírod a 'i' betűt|")
    print("| - A játékmenet során kérhetsz segítséget    |")
    print("|      a közönségtől egyszer ha beírod a      |")
    print("|      'k' betűt                              |")
    print("|                                             |")
    print("|       a.start                               |")
    print("|       b.kilépés                             |")
    print("-----------------------------------------------")
    print("             |           ")

def fkerdesek():
    kerdesek=[
        [
            [
                    "| Hogyan folytatódik ifj.Jojann Strauss ismert operettjének címe. Egy éj ...?        |",
                    "|       a. Esküvő után                                                               |",
                    "|       b. És más semmi                                                   (5.000Ft)  |",
                    "|       c. Velencében                                                                |",
                    "|       d. A Velencei tónál                                                          |"
            ],
            "c",
            5000    
        ],
        [
            [
                "|Az alábbiak közül melyik egy műfaj sejtelmességét kifejező irodalmi stíluselem elnevezése|",
                "|       a. Ódai pompa                                                                     |",
                "|       b. Lírai szikra                                                  (10.000Ft)       |",
                "|       c. Balladai homály                                                                |",
                "|       d. Drámai ború                                                                    |"
            ],
            "c",
            10000
        ],
        [
            [
                "|                     Melyik városban feszítették keresztre jézust?                       |",
                "|       a. Betlehem                                                                       |",
                "|       b. Jeruzsálem                                                    (25.000Ft)       |",
                "|       c. Rómában                                                                        |",
                "|       d. Názáretben                                                                     |"
            ],
            "b",
            25000
        ],
        [
            [
                "| Melyik cízi jármű játszott szerepet 1917-ben a pétervári bolsevik felkelés kitörésekor? |",
                "|       a. A Patyomkin páncélos                                                           |",
                "|       b. Az Auróra cirkáló                                             (50.000Ft)       |",
                "|       c. A Lenin gőzhajó                                                                |",
                "|       d. A Pravada torpedóromboló                                                       |"
            ],
            "b",
            50000
        ],
        [
            [
                "|            Ki volt Szemiramisz, akinek a nevéhez a híres függőkert kapcsolódik          |",
                "|       a. görög istennő                                                                  |",
                f"|       b. Aszír királynő                                                ({bcolors.WARNING}100.000Ft{bcolors.ENDC})      |",
                "|       c. Egyiptomi fáraó                                                                |",
                "|       d. Dávid kegyence                                                                 |",
            ],
            "b",
            100000
        ],
        [
            [
                "|                            Kik jártak a Sóhajok hídján?                                 |",
                "|       a. A bírák                                                                        |",
                "|       b. A szűzleányok                                                (200.000Ft)       |",
                "|       c. Az elítéltek                                                                   |",
                "|       d. A leprások                                                                     |"
            ],
            "c",
            200000
        ],
        [
            [
                "|            Melyik megyében található a sok látogatót vonzó Bugacpuszta?                 |",
                "|       a. Csongrád                                                                       |",
                "|       b. Hajdú-Bihar                                                  (300.000Ft)       |",
                "|       c. Bács-Kiskun                                                                    |",
                "|       d. Pest                                                                           |"
            ],
            "c",
            300000
        ],
        [
            [
                "|                       Ki a hair című musical zeneszerzője?                              |",
                "|       a. Galt McDermot                                                                  |",
                "|       b. Leonard Bernstein                                            (500.000Ft)       |",
                "|       c. Andrew Lioyd Webber                                                            |",
                "|       d. John Kander                                                                    |"
            ],
            "a",
            500000
        ],
        [
            [
                "|          Ki volt Bill clintonrepublikánus ellenlábasa az 1996-os választásokon?         |",
                "|       a. Al Gore                                                                        |",
                "|       b. Ross Perot                                                   (800.000Ft)       |",
                "|       c. Robert Dolo                                                                    |",
                "|       d. Michael Dukakis                                                                |"
            ],
            "c",
            800000
        ],
        [
            [
                "|         Melyik nagy utazónk írta meg a török-tatár nyelvek etimológiai szótárat?        |",
                "|       a. Vámbéry Ármin                                                                  |",
                f"|       b. Hopp Ferenc                                                  ({bcolors.WARNING}1.500.000Ft{bcolors.ENDC})     |",
                "|       c. Kőrösi Csoma Sándor                                                            |",
                "|       d. Germanus Gyula                                                                 |"
            ],
            "a",
            1500000
        ],
        [
            [
                "|                    Az alábbi űrahjósok közül ki nem járt a holdon?                      |",
                "|       a. David Scott                                                                    |",
                "|       b. James Irwin                                                (3.000.000Ft)       |",
                "|       c. Eugene A. Cernan                                                               |",
                "|       d. James Arthur Lowell                                                            |"
            ],
            "d",
            3000000
        ],
        [
            [
                "|            Ki szokott harangozni, ha szegény az eklézsia a közmondás szerint?           |",
                "|       a. Maga a pap                                                                     |",
                "|       b. A templom egere                                            (5.000.000Ft)       |",
                "|       c. A papné                                                                        |",
                "|       d. A szél                                                                         |"
            ],
            "a",
            5000000
        ],
        [
            [
                "|            Melyik folyó felett ível át a híres firenzei Ponte Vecchio híd?              |",
                "|       a. Adige                                                                          |",
                "|       b. Tevere                                                    (10.000.000Ft)       |",
                "|       c. Pó                                                                             |",
                "|       d. Arno                                                                           |"
            ],
            "c",
            10000000
        ],
        [
            [
                "|            Melyik az a fa, melynek levelei élükkel fordulnak a nap felé?                |",
                "|       a. Majomkenyérfa                                                                  |",
                "|       b. Kaucsukfa                                                 (20.000.000Ft)       |",
                "|       c. Eukaliptuszfa                                                                  |",
                "|       d. Tiszafa                                                                        |"
            ],
            "c",
            20000000
        ],
        [
            [
                "|                    Milyen pitypangnak hívják a gyermekláncfüvet?                        |",
                "|       a. Patyolat                                                                       |",
                "|       b. Papucs                                                    (40.000.000Ft)       |",
                "|       c. Pongyola                                                                       |",
                "|       d. Parafa                                                                         |"
            ],
            "c",
            40000000
        ]
    ]
    return kerdesek

def q0(kerdes):
    print("-------------|------------------------------------------------------------------------")
    for sor in kerdes:
        print(sor)
    print("-------------|------------------------------------------------------------------------")
    print("             |                                          ")

def char_to_number(argument):
    switcher = {
        "0": 0,
        "1": 1,
        "2": 2,
        "3": 3,
        "4": 4,
        "5": 5,
        "6": 6,
        "7": 7,
        "8": 8,
        "9": 9,
        "A": 10,
        "B": 11,
        "C": 12,
        "D": 13,
        "E": 14,
        "F": 15,
        "G": 16,
        "H": 17,
        "I": 18,
        "J": 19,
        "K": 20,
        "L": 21,
        "M": 22,
        "N": 23,
        "O": 24,
        "Q": 25,
        "P": 26,
        "R": 27,
        "S": 28,
        "T": 29,
        "U": 30,
        "V": 31,
        "W": 32,
        "X": 33,
        "Y": 34,
        "Z": 35,
        "-": 36,
        ".": 37,
        " ": 38,
        "$": 39,
        "/": 40,
        "+": 41,
        "%": 42,
        "#": 0,
        "&": 0,
        "*": 0,
        "=": 0
    }
    return switcher.get(argument, "invalid")


def number_to_char(argument):
    switcher = {
        0: "0",
        1: "1",
        2: "2",
        3: "3",
        4: "4",
        5: "5",
        6: "6",
        7: "7",
        8: "8",
        9: "9",
        10: "A",
        11: "B",
        12: "C",
        13: "D",
        14: "E",
        15: "F",
        16: "G",
        17: "H",
        18: "I",
        19: "J",
        20: "K",
        21: "L",
        22: "M",
        23: "N",
        24: "O",
        25: "Q",
        26: "P",
        27: "R",
        28: "S",
        29: "T",
        30: "U",
        31: "V",
        32: "W",
        33: "X",
        34: "Y",
        35: "Z",
        36: "-",
        37: ".",
        38: " ",
        39: "$",
        40: "/",
        41: "+",
        42: "%"
    }
    return switcher.get(argument, "invalid")

def znak_kontrolny(znaki):
    suma = 0
    for c in znaki:
        suma = suma + char_to_number(c)
    return number_to_char(suma%43)

rok = int(input("Podaj rok dostawy np:22 : "))
nrdostawy = int(input("Poday nr dostawy: "))
liczba_sztuk = int(input("Liczba dostarczonych sztuk: "))
qr_start="#059103502Q    ###*1T9 PYM"
qr_end="*="
serial_number_start=rok * 10000000 + nrdostawy * 100000
for i in range(liczba_sztuk):
    serial_number = serial_number_start + i
    qr = qr_start + str(serial_number)
    caly_qr = qr + znak_kontrolny(qr) + qr_end
    print(caly_qr)
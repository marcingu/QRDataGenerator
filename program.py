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

def control_char(chars):
    sum = 0
    for c in chars:
        sum = sum + char_to_number(c)
    return number_to_char(sum%43)



part_number = ''
while len(part_number)<11:
    part_number = str(input("Input part number: "))
    part_number = part_number.replace('.','')        
    if len(part_number)<11:             
        while len(part_number)<11:
            part_number+=' '
    elif len(part_number)>11:
        print('Part number too long!!!')

color_code = ''
while len(color_code)<3:
    color_code = str(input("Input color code (or press ENTER if there is none): "))
    if len(color_code)<3:            
        while len(color_code)<3:
            color_code+=' '
    elif len(color_code)>3:
        print('Color code too long!!!')



module_number = str(input("Input BG-Nr - module number (you can find it on drawing): "))
if len(module_number)<3:
    while len(module_number)<3:
        module_number+=' '
elif len(module_number)>3:
    print('Module number too long!!!')
    exit()

manufacturer_code = ''
while len(manufacturer_code)<4:
    manufacturer_code = str(input("Input Manufacturer code: "))
    if len(manufacturer_code)==3:
        manufacturer_code = ' '+manufacturer_code
    elif len(manufacturer_code)>4:
        print("Manufacturer code is too long!")


year = int(input("Supply year [YY] : "))
if year > 2000:
    year -= 2000

supply_number = int(input("Supply batch number in year: "))
nr_of_qr = int(input("How many codes do you need: "))
qr_start="#" + (part_number) + color_code + "###*" + module_number + manufacturer_code
qr_start=qr_start.upper()
qr_end="*="
serial_number_start=year * 10000000 + supply_number * 100000
for i in range(nr_of_qr):
    serial_number = serial_number_start + i
    qr = qr_start + str(serial_number)
    whole_qr = qr + control_char(qr) + qr_end
    print(whole_qr)
    
input()

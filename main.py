ISINGLEFEE, FSINGLEFEE, ASINGLEFEE, LSINGLEFEE = 305.3828, 6.1590, 165.3096, 259.5835
PLOWTAR, PHIGHTAR, RLOWTAR, RHIGHTAR = 191.2220, 282.8414, 48.2187, 113.2271
IDAYFEE, PDAYFEE, RDAYFEE, ADAYFEE = 309.1833, 285.8616, 115.7700, 170.4822
IPEAKFEE, PPEAKFEE, RPEAKFEE, APEAKFEE = 490.9037, 458.8843, 208.3645, 280.0325
INIGHTFEE, PNIGHTFEE, RNIGHTFEE, ANIGHTFEE = 162.5171, 148.1941, 41.7225, 77.1882
IUNITFEE, PUNITFEE, RUNITFEE, FUNITFEE, AUNITFEE, LUNITFEE = 64.7998, 87.8175, 85.883, 58.2521, 72.1579, 84.1099
IECT, OECT, RFAVAT, OVAT = 0.01, 0.05, 0.1, 0.2


def industry(dayu, peaku, nightu, daynum, SM):
    totalu = dayu + peaku + nightu
    Stotalufee = totalu * ISINGLEFEE + totalu * IUNITFEE
    Mtotalufee = dayu * IDAYFEE + peaku * IPEAKFEE + nightu * INIGHTFEE + totalu * IUNITFEE
    if SM == 'S':
        print("Daytime Usage", dayu)
        print("Peaktime Usage", peaku)
        print("Nighttime Usage", nightu)
        print("Total Usage kwh", totalu)
        print("Total usage TL without tax", Stotalufee)
        print("ECT is", Stotalufee * IECT, "VAT is", Stotalufee * OVAT)
        print("Bill is", Stotalufee * IECT * OVAT)
        print("Change type diffrence is", Stotalufee - Mtotalufee)
    else:
        print("Daytime Usage", dayu)
        print("Peaktime Usage", peaku)
        print("Nighttime Usage", nightu)
        print("Total Usage kwh", totalu)
        print("Total usage TL without tax", Mtotalufee)
        print("ECT is", Mtotalufee * IECT, "VAT is", Mtotalufee * OVAT)
        print("Bill is", Mtotalufee * IECT * OVAT)
        print("Change type diffrence is", Stotalufee - Mtotalufee)


def public(dayu, peaku, nightu, daynum, SM):
    print("Yavaş kardeş daha yazmadık")


def residential(dayu, peaku, nightu, daynum, SM, fam):
    totalu = dayu + peaku + nightu
    lowlimit = daynum * 8
    if fam:
        Stotalufee = totalu * FSINGLEFEE + totalu * FUNITFEE
    else:
        if totalu <= lowlimit:
            Stotalufee = totalu * RLOWTAR + totalu * RUNITFEE
        else:
            Stotalufee = lowlimit * RLOWTAR + (totalu - lowlimit) * RHIGHTAR + totalu * RUNITFEE
        Mtotalufee = dayu * RDAYFEE + peaku * RPEAKFEE + nightu * RNIGHTFEE + totalu * RUNITFEE
    if fam or SM == "S":
        print("Daytime Usage", dayu)
        print("Peaktime Usage", peaku)
        print("Nighttime Usage", nightu)
        print("total usage kwh", totalu)
        print("total usage TL without tax", Stotalufee)
        print("ECT is", Stotalufee * OECT, "VAT is", Stotalufee * RFAVAT)
        print("Bill is", Stotalufee * OECT * RFAVAT)
        if SM == "S":
            print("Change type diffrence is", Stotalufee - Mtotalufee)
    else:
        print("Daytime Usage", dayu)
        print("Peaktime Usage", peaku)
        print("Nighttime Usage", nightu)
        print("total usage kwh", totalu)
        print("total usage TL without tax", Mtotalufee)
        print("ECT is", Mtotalufee * OECT, "VAT is", Mtotalufee * RFAVAT)
        print("Bill is", Mtotalufee * OECT * RFAVAT)
        print("Change type diffrence is", Mtotalufee - Stotalufee)


def agricultural(dayu, peaku, nightu, daynum, SM):
    print("Yavaş kardeş daha yazmadık")


def lightning(dayu, peaku, nightu, daynum):
    print("Yavaş kardeş daha yazmadık")


def singmulti():
    type = input("Single or Multi:")
    if type == "s" or type == "S":
        type = "S"
        return type
    elif type == "m" or type == "M":
        type = "M"
        return type


def reader():
    preday = int(input())
    curday = int(input())
    prepeak = int(input())
    curpeak = int(input())
    prenight = int(input())
    curnight = int(input())
    daynumber = int(input())
    totalamoyear = int(input())
    if totalamoyear > 1000:
        freecons = True
    else:
        freecons = False
    return curday - preday, curpeak - prepeak, curnight - prenight, daynumber, freecons


def main():
    while True:
        consno = int(input("Please enter the consumer no"))
        if consno == 0:
            break
        constype = input("Please enter the consumer type")
        dayu, peaku, nightu, daynum, freecons = reader()

        if constype == "I" or constype == "ı":
            SMtype = singmulti()
            industry(dayu, peaku, nightu, daynum, SMtype)
        elif constype == "P" or constype == "p":
            SMtype = singmulti()
            public(dayu, peaku, nightu, daynum, SMtype)
        elif constype == "R" or constype == "r":
            family = input("Are you Family veterans")
            if family == "Y" or family == "y":
                residential(dayu, peaku, nightu, daynum, SMtype, True)
            elif family == "N" or family == "n":
                SMtype = singmulti()
                residential(dayu, peaku, nightu, daynum, SMtype, False)
        elif constype == "A" or constype == "a":
            SMtype = singmulti()
            agricultural(dayu, peaku, nightu, daynum, SMtype)
        elif constype == "L" or constype == "l":
            lightning(dayu, peaku, nightu, daynum)

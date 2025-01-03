"""
We wrote the constant names in 3 parts. The first of these 3 parts is the sector names; I = Industry,
P = Public and Private Services Sector and Other, R = Residential, A = Agricultural Activities, L = Lightning.
The second part is time dependent constants; DAY = Daytime period, PEAK = Peak period, NIGHT = Night period, 
SINGLE = Single-time. The third piece consists of the abbreviations FEE and TARR, which we derived from fee and tarriff.
For there are 2 types of taxes, we put the abbreviations of the sectors in front of the abbreviations when naming the
taxes (I = Industry, RFA = Residential Family Veterans and Agriculture). The abbreviation 'O = Other' means sectors 
other than Industry for ECT; For VAT, sectors except RFA. The abbreviation 'A' means '1 added'. We put it in order not 
to add 1 again when calculating the tax.
"""
ISINGLEFEE, FSINGLEFEE, ASINGLEFEE, LSINGLEFEE = 305.3828, 6.1590, 165.3096, 259.5835
PLOWTAR, PHIGHTAR, RLOWTAR, RHIGHTAR = 191.2220, 282.8414, 48.2187, 113.2271
IDAYFEE, PDAYFEE, RDAYFEE, ADAYFEE = 309.1833, 285.8616, 115.7700, 170.4822
IPEAKFEE, PPEAKFEE, RPEAKFEE, APEAKFEE = 490.9037, 458.8843, 208.3645, 280.0325
INIGHTFEE, PNIGHTFEE, RNIGHTFEE, ANIGHTFEE = 162.5171, 148.1941, 41.7225, 77.1882
IUNITFEE, PUNITFEE, RUNITFEE, FUNITFEE, AUNITFEE, LUNITFEE = 64.7998, 87.8175, 85.883, 58.2521, 72.1579, 84.1099
IECT, OECT, RFAVAT, OVAT = 0.01, 0.05, 0.1, 0.2
IAECT, OAECT, RFAAVAT, OAVAT = 1.01, 1.05, 1.1, 1.2

"""
The printer function is compressed into a single function to increase the readability of outputs printed repeatedly in each sector.
"""


def printer(dayu, peaku, nightu, totalu, totalufee, ECT, VAT, bill):
    print("Daytime period usage (kWh) = ", dayu)
    print("Peak period usage (kWh) = ", peaku)
    print("Night period usage (kWh) = ", nightu)
    print("Total Usage (kWh) = ", totalu)
    print("Total usage TL without tax and distribution fee (TL)= ", round(totalufee, 2))
    print("ECT is (TL)= ", round(ECT, 2), "TL", "VAT is (TL)= ", round(VAT, 2), "TL")
    print("Bill is (TL)= ", round(bill, 2), "TL")


"""
The advantage function is about the difference between the types and consumer advantageous situation
"""


def advantages(Sbill, Mbill, choose):
    if choose == "S":
        if Sbill < Mbill:
            print("Difference between Single-time type and Multi-time type (TL)=", round(Sbill - Mbill, 2),
                  "The consumer chose the advantageous type ")
            return True
        else:
            print("Difference between Single-time type and Multi-time type (TL)=", round(Sbill - Mbill, 2),
                  "The consumer chose the disadvantageous type ")
            return False
    else:
        if Sbill > Mbill:
            print("Difference between Single-time type and Multi-time type (TL)=", round(Sbill - Mbill, 2),
                  "The consumer chose the advantageous type ")
            return True
        else:
            print("Difference between Single-time type and Multi-time type (TL)=", round(Sbill - Mbill, 2),
                  "The consumer chose the disadvantageous type ")
            return False


"""
The five functions below are designed to make separate bill calculations for each sector.
For readability we used the common variables.
the abbreviations as follow : 'u' at the end of the variables = usage, at the beginning of
the variables 'S' = Single time , 'M' = Multi time. 'totalu' = Total usage. 'lowlimit' refers
to the low tariff limit. public = Public and Private Services Sector and Other
"""


def industry(dayu, peaku, nightu, daynum, SM):
    totalu = dayu + peaku + nightu
    Stotalufee = totalu * ISINGLEFEE / 100
    Mtotalufee = (dayu * IDAYFEE + peaku * IPEAKFEE + nightu * INIGHTFEE) / 100
    SECT = Stotalufee * IECT
    MECT = Mtotalufee * IECT
    disturbfee = totalu * IUNITFEE / 100
    Sbill = ((Stotalufee + SECT + disturbfee) * OAVAT)
    Mbill = ((Mtotalufee + MECT + disturbfee) * OAVAT)
    if SM == 'S':
        VAT = Sbill - (Stotalufee + SECT + disturbfee)
        printer(dayu, peaku, nightu, totalu, Stotalufee, SECT, VAT, Sbill)
        advantage = advantages(Sbill, Mbill, "S")
        return totalu, Sbill, totalu / daynum, SECT, VAT, advantage
    else:
        VAT = Mbill - (Mtotalufee + SECT + disturbfee)
        printer(dayu, peaku, nightu, totalu, Mtotalufee, SECT, VAT, Mbill)
        advantage = advantages(Sbill, Mbill, "M")
        return totalu, Mbill, totalu / daynum, MECT, VAT, advantage


def public(dayu, peaku, nightu, daynum, SM):
    totalu = dayu + peaku + nightu
    lowlimit = daynum * 30
    if totalu <= lowlimit:
        Stotalufee = (totalu * PLOWTAR) / 100
    else:
        Stotalufee = (lowlimit * PLOWTAR + (totalu - lowlimit) * PHIGHTAR) / 100
    Mtotalufee = (dayu * PDAYFEE + peaku * PPEAKFEE + nightu * PNIGHTFEE) / 100
    SECT = (Stotalufee * OECT)
    MECT = (Mtotalufee * OECT)
    disturbfee = totalu * PUNITFEE / 100
    Sbill = ((Stotalufee + SECT + disturbfee) * OAVAT)
    Mbill = ((Mtotalufee + MECT + disturbfee) * OAVAT)
    if SM == "S":
        VAT = Sbill - (Stotalufee + SECT + disturbfee)
        printer(dayu, peaku, nightu, totalu, Stotalufee, SECT, VAT, Sbill)
        advantage = advantages(Sbill, Mbill, "S")
        return totalu, Sbill, totalu / daynum, SECT, VAT, advantage
    else:
        VAT = Mbill - (Mtotalufee + SECT + disturbfee)
        printer(dayu, peaku, nightu, totalu, Mtotalufee, MECT, VAT, Mbill)
        advantage = advantages(Sbill, Mbill, "M")
        return totalu, Mbill, totalu / daynum, MECT, VAT, advantage


# The variable 'fam' refers to family of veterans and martrys.
def residential(dayu, peaku, nightu, daynum, SM, fam):
    totalu = dayu + peaku + nightu
    lowlimit = daynum * 8
    if fam:
        Stotalufee = (totalu * FSINGLEFEE) / 100
        disturbfee = totalu * FUNITFEE / 100
    else:
        if totalu <= lowlimit:
            Stotalufee = (totalu * RLOWTAR) / 100
        else:
            Stotalufee = (lowlimit * RLOWTAR + (totalu - lowlimit) * RHIGHTAR) / 100
        Mtotalufee = (dayu * RDAYFEE + peaku * RPEAKFEE + nightu * RNIGHTFEE) / 100
        disturbfee = totalu * RUNITFEE / 100
        MECT = (Mtotalufee * OECT)
        Mbill = ((Mtotalufee + MECT + disturbfee) * RFAAVAT)
    SECT = (Stotalufee * OECT)
    Sbill = ((Stotalufee + SECT + disturbfee) * RFAAVAT)
    if fam or SM == "S":
        VAT = Sbill - (Stotalufee + SECT + disturbfee)
        printer(dayu, peaku, nightu, totalu, Stotalufee, SECT, VAT, Sbill)
        if SM == "S":
            advantage = advantages(Sbill, Mbill, "S")
            return totalu, Sbill, totalu / daynum, SECT, VAT, advantage
        return totalu, Sbill, totalu / daynum, SECT, VAT
    else:
        VAT = Mbill - (Mtotalufee + SECT + disturbfee)
        printer(dayu, peaku, nightu, totalu, Mtotalufee, MECT, VAT, Mbill)
        advantage = advantages(Sbill, Mbill, "M")
        return totalu, Mbill, totalu / daynum, MECT, VAT, advantage


def agricultural(dayu, peaku, nightu, daynum, SM):
    totalu = dayu + peaku + nightu
    Stotalufee = (totalu * ASINGLEFEE) / 100
    Mtotalufee = (dayu * ADAYFEE + peaku * APEAKFEE + nightu * ANIGHTFEE) / 100
    SECT = (Stotalufee * OECT)
    MECT = (Mtotalufee * OECT)
    disturbfee = totalu * AUNITFEE / 100
    Sbill = ((Stotalufee + SECT + disturbfee) * RFAAVAT)
    Mbill = ((Mtotalufee + MECT + disturbfee) * RFAAVAT)
    if SM == 'S':
        VAT = Sbill - (Stotalufee + SECT + disturbfee)
        printer(dayu, peaku, nightu, totalu, Stotalufee, SECT, VAT, Sbill)
        advantage = advantages(Sbill, Mbill, "S")
        return totalu, Sbill, totalu / daynum, SECT, VAT, advantage
    else:
        VAT = Mbill - (Mtotalufee + SECT + disturbfee)
        printer(dayu, peaku, nightu, totalu, Mtotalufee, MECT, VAT, Mbill)
        advantage = advantages(Sbill, Mbill, "M")
        return totalu, Mbill, totalu / daynum, MECT, VAT, advantage


def lightning(dayu, peaku, nightu, daynum):
    totalu = dayu + peaku + nightu
    Stotalufee = (totalu * LSINGLEFEE) / 100
    ECT = Stotalufee * OECT
    disturbfee = totalu * LUNITFEE / 100
    Sbill = ((Stotalufee + ECT + disturbfee) * OAVAT)
    VAT = Sbill - (Stotalufee + ECT + disturbfee)
    printer(dayu, peaku, nightu, totalu, Stotalufee, ECT, VAT, Sbill)
    return totalu, Sbill, totalu / daynum, ECT, VAT


"""
It was written to choose Single-time or Multi-time option.
"""


def singmulti():
    types = input("Enter your type (Single or Multi) (S,s,M,m): ")
    if types == "s" or types == "S":
        types = "S"
        return types
    elif types == "m" or types == "M":
        types = "M"
        return types
    else:
        singmulti()


"""
It has written to take the inputs from user.
"""


def reader():
    preday = int(input("Enter the previous day-time period consumption value (kWh) (bigger than 0): "))
    while preday < 0:
        preday = int(input("Enter the previous day-time period consumption value (kWh) (bigger than 0): "))
    curday = int(input("Enter the current day-time period consumption value (kWh) (bigger than previous day value): "))
    while curday < preday:
        curday = int(
            input("Enter the current day-time period consumption value (kWh) (bigger than previous day value): "))
    prepeak = int(input("Enter the previous peak period consumption value (kWh) (bigger than 0): "))
    while prepeak < 0:
        prepeak = int(input("Enter the previous peak period consumption value (kWh) (bigger than 0): "))
    curpeak = int(input("Enter the current peak period consumption value (kWh) (bigger than previous peak value): "))
    while curpeak < prepeak:
        curpeak = int(
            input("Enter the current peak period consumption value (kWh) (bigger than previous peak value): "))
    prenight = int(input("Enter the previous night period consumption value (kWh) (bigger than 0): "))
    while prenight < 0:
        prenight = int(input("Enter the previous night period consumption value (kWh) (bigger than 0): "))
    curnight = int(input("Enter the current night period consumption value (kWh) (bigger than previous night value): "))
    while curnight < prenight:
        curnight = int(
            input("Enter the current night period consumption value (kWh) (bigger than previous night value): "))
    daynumber = int(input("Enter the number of days electricity was consumed : "))
    while daynumber < 0:
        daynumber = int(input("Enter the number of days electricity was consumed (bigger than 0): "))
    totalamoyear = int(input("Enter total amount of electricity consumed in a year (kWh)(bigger than 0): "))
    while totalamoyear < 0:
        totalamoyear = int(input("Enter total amount of electricity consumed in a year (kWh)(bigger than 0): "))
    return curday - preday, curpeak - prepeak, curnight - prenight, daynumber, totalamoyear


"""
The statistics section was written to reduce the crowding of statistics for each sector.
"""


def consumerdata(ctype, cons, total, kwh):
    print(ctype, "Number is = ", round(cons, 2))
    print(ctype, "Percentage of all consumers = %", round(cons / total * 100, 2))
    print(ctype, "Total kWh usage is = ", round(kwh, 2))
    print(ctype, "Average kWh usage is = ", round(kwh / cons, 2))


def main():
    indcons, agricons, lightcons = 0, 0, 0  # Number of consumers in the sector.
    pubscons, pubmcons = 0, 0  # Number of people choosing single and multi in Public and Private Services Sector and Other.
    frezcons = 0  # Number of families of martyrs and veterans.
    nrezcons = 0  # Number of Non-families of martyrs and veterans residential consumers
    indkwh, pubkwh, rezkwh, agrikwh, lightkwh = 0, 0, 0, 0, 0  # Amount of electricity consumed by sectors.
    Industryhighusers = 0  # Number of Industry users of higher than 10000 kWh or 100000TL bill
    maxrezconsno, maxotherconsno = 0, 0  # Data of Residential and Other users whose maximum statistics are requested.
    maxrezbill, maxotherbill = 0, 0
    maxrezave, maxotherave = 0, 0
    maxothertype=""
    adv = 0  # Number of taking advantage users.
    pubdays = 0  # Total number of days public users used electricity.
    totalect, totalvat, totalbill = 0, 0, 0  # Total bill amount, VAT and ECT data.
    pubsave, pubmave = 0, 0  # Total Public and Private Services Sector and Other single time and multi time consumers averages
    while True:
        consno = int(input("Please enter the consumer no (Enter 0 for exit tho program) ="))
        while consno < 0:
            consno = int(input("Please enter the consumer no (Enter 0 for exit tho program) ="))
        if consno == 0:
            rezcons = frezcons + nrezcons  # Total Residential consumers number
            tpubcons = pubscons + pubmcons  # Total Public and Private Services Sector and Other consumers number
            totalcons = indcons + rezcons + agricons + lightcons + tpubcons  # total consumers number
            totalkwh = indkwh + pubkwh + rezkwh + agrikwh + lightkwh  # total consumption kwh number
            consumerdata("Industry : ", indcons, totalcons, indkwh)
            consumerdata("Public and Private Services Sector and Other : ", tpubcons, totalcons, pubkwh)
            consumerdata("Residential : ", rezcons, totalcons, rezkwh)
            consumerdata("Agricultural Activities : ", agricons, totalcons, agrikwh)
            consumerdata("Lightning : ", lightcons, totalcons, lightkwh)
            print("Bornova's all electric consumption is = ", totalkwh, "kWh")
            print(pubscons, "of Public and Private Services Sector and Other consumers preferred single time.")
            print(pubmcons, "of Public and Private Services Sector and Other consumers preferred multi time.")
            print(round(pubscons / tpubcons * 100, 2),
                  "% percent of Public and Private Services Sector and Other consumers preferred single time.")
            print(round(pubmcons / tpubcons * 100, 2),
                  "% percent of Public and Private Services Sector and Other consumers preferred multi time.")
            print("Public and Private Services Sector and Other consumers preferred single time consumed an average",
                  round(pubsave / pubscons, 2), "kWh per day.")
            print("Public and Private Services Sector and Other consumers preferred multi time consumed an average",
                  round(pubmave / pubmcons, 2), "kWh per day.")
            print("Industry consumers of higher than 10000 kWh or 100000TL bill  number is", Industryhighusers,
                  "These consumers percantage of industry%", round(Industryhighusers / indcons * 100, 2))
            print("Maximum rezidans daily average consumption consumer no is = ", maxrezconsno,
                  "Consumed average of a day is = ", round(maxrezave, 2), "Bill is = ", round(maxrezbill, 2))
            print("Maximum other bill consumer no is = ", maxotherconsno,"Consumer type is",maxothertype, "bill is = ", round(maxotherbill, 2),
                  "max average daily consumption is", round(maxotherave, 2))
            print("GDZ gained = ", round(totalbill - totalvat - totalect, 2), "TL", "The municipality gained",
                  round(totalect, 2), "TL", "The state gained", round(totalvat, 2), "TL")
            print("Advantage gainer consumer's percentage is %",
                  round(adv / (totalcons - lightcons - frezcons) * 100, 2))
            break
        constype = input("Please enter the consumer type (I,i,P,p,R,r,A,a,L,l): ")
        while constype not in ["I", "i", "P", "p", "R", "r", "A", "a", "L", "l"]:
            constype = input("Please enter the consumer type (I,i,P,p,R,r,A,a,L,l): ")
        """
        Data entry, output printing and data retention processes for the statistics section according to consumer type.
        """
        if constype == "I" or constype == "i":
            SMtype = singmulti()
            dayu, peaku, nightu, daynum, totalu = reader()
            print("Consumer No = ", consno)
            print("Consumer type is Industry.")
            usage, bill, average, nowect, nowvat, nowadv = industry(dayu, peaku, nightu, daynum, SMtype)
            indcons += 1
            indkwh += usage
            totalect += nowect
            totalvat += nowvat
            totalbill += bill
            if usage > 10000 or bill > 100000:
                Industryhighusers += 1
            if bill > maxotherbill:
                maxotherbill = bill
                maxotherconsno = consno
                maxotherave = average
                maxothertype= "Industry"
            if nowadv:
                adv += 1
        elif constype == "P" or constype == "p":
            SMtype = singmulti()
            dayu, peaku, nightu, daynum, totalu = reader()
            print("Consumer No = ", consno)
            print("Consumer type is Public and Private Services Sector and Other.")
            usage, bill, average, nowect, nowvat, nowadv = public(dayu, peaku, nightu, daynum, SMtype)
            if SMtype == "S":
                pubscons += 1
                pubsave += average
            else:
                pubmcons += 1
                pubmave += average
            pubkwh += usage
            pubdays += daynum
            totalect += nowect
            totalvat += nowvat
            totalbill += bill
            if bill > maxotherbill:
                maxotherbill = bill
                maxotherconsno = consno
                maxotherave = average
                maxothertype= "Public and Private Services Sector and Other"
            if nowadv:
                adv += 1
        elif constype == "R" or constype == "r":
            family = input("Are you a family of martyrs or veterans? (Y,y,N,n) : ")
            while family not in ["y", "Y", "N", "n"]:
                family = input("Are you a family of martyrs or veterans? (Y,y,N,n) : ")
            if family == "Y" or family == "y":
                dayu, peaku, nightu, daynum, totalu = reader()
                print("Consumer No = ", consno)
                print("Consumer type is Residential (family of martyrs and veterans).")
                usage, bill, average, nowect, nowvat = residential(dayu, peaku, nightu, daynum, "", True)
                frezcons += 1
            elif family == "N" or family == "n":
                SMtype = singmulti()
                dayu, peaku, nightu, daynum, totalu = reader()
                print("Consumer No = ", consno)
                print("Consumer type is Residential.")
                usage, bill, average, nowect, nowvat, nowadv = residential(dayu, peaku, nightu, daynum, SMtype, False)
                if nowadv:
                    adv += 1
                nrezcons += 1
            rezkwh += usage
            totalect += nowect
            totalvat += nowvat
            totalbill += bill
            if average > maxrezave:
                maxrezbill = bill
                maxrezconsno = consno
                maxrezave = average
        elif constype == "A" or constype == "a":
            SMtype = singmulti()
            dayu, peaku, nightu, daynum, totalu = reader()
            print("Consumer No = ", consno)
            print("Consumer type is Agricultural Activities.")
            usage, bill, average, nowect, nowvat, nowadv = agricultural(dayu, peaku, nightu, daynum, SMtype)
            totalect += nowect
            totalvat += nowvat
            totalbill += bill
            agricons += 1
            agrikwh += usage
            if bill > maxotherbill:
                maxotherbill = bill
                maxotherconsno = consno
                maxotherave = average
                maxothertype="Agricultural Activities"
            if nowadv:
                adv += 1
        else:
            dayu, peaku, nightu, daynum, totalu = reader()
            print("Consumer No = ", consno)
            print("Consumer type is Lightning.")
            usage, bill, average, nowect, nowvat = lightning(dayu, peaku, nightu, daynum)
            lightcons += 1
            lightkwh += usage
            totalect += nowect
            totalvat += nowvat
            totalbill += bill
            if bill > maxotherbill:
                maxotherbill = bill
                maxotherconsno = consno
                maxotherave = average
                maxothertype="Lightning"
        if totalu + usage >= 1000:
            print("Total usage in this year is =", totalu + usage, "kWh Consumer is Free.")
        else:
            print("Total usage in this year is =", totalu + usage, "kWh Consumer is not Free.")


main()

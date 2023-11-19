ISINGLEFEE, FSINGLEFEE, ASINGLEFEE, LSINGLEFEE = 305.3828, 6.1590, 165.3096, 259.5835
PLOWTAR, PHIGHTAR, RLOWTAR, RHIGHTAR = 191.2220, 282.8414, 48.2187, 113.2271
IDAYFEE, PDAYFEE, RDAYFEE, ADAYFEE = 309.1833, 285.8616, 115.7700, 170.4822
IPEAKFEE, PPEAKFEE, RPEAKFEE, APEAKFEE = 490.9037, 458.8843, 208.3645, 280.0325
INIGHTFEE, PNIGHTFEE, RNIGHTFEE, ANIGHTFEE = 162.5171, 148.1941, 41.7225, 77.1882
IUNITFEE, PUNITFEE, RUNITFEE, FUNITFEE, AUNITFEE, LUNITFEE = 64.7998, 87.8175, 85.883, 58.2521, 72.1579, 84.1099
IECT, OECT, RFAVAT, OVAT = 0.01, 0.05, 0.1, 0.2
IAECT, OAECT, RFAAVAT, OAVAT = 1.01, 1.05, 1.1, 1.2
def printer(dayu,peaku,nightu,totalu,totalufee,ECT,VAT,bill):
    print("Daytime Usage", dayu)
    print("Peaktime Usage", peaku)
    print("Nighttime Usage", nightu)
    print("Total Usage kwh", totalu)
    print("Total usage TL without tax", totalufee)
    print("ECT is", ECT, "VAT is", VAT)
    print("Bill is", bill)
def industry(dayu, peaku, nightu, daynum, SM):
    totalu = dayu + peaku + nightu
    Stotalufee = (totalu * ISINGLEFEE + totalu * IUNITFEE)/100
    Mtotalufee = (dayu * IDAYFEE + peaku * IPEAKFEE + nightu * INIGHTFEE + totalu * IUNITFEE)/100
    Sbill = (Stotalufee * (IAECT) * (OAVAT))
    Mbill = (Mtotalufee * (IAECT) * (OAVAT))
    if SM == 'S':
        ECT = (Stotalufee * IECT)
        VAT = (Stotalufee * OVAT)
        printer(dayu,peaku,nightu,totalu,Stotalufee,ECT,VAT,Sbill)
        print("Daytime Usage", dayu)
        print("Peaktime Usage", peaku)
        print("Nighttime Usage", nightu)
        print("Total Usage kwh", totalu)
        print("Total usage TL without tax", Stotalufee)
        print("ECT is", ECT, "VAT is", VAT)
        print("Bill is", Sbill)
        print("Change type diffrence is", Sbill - Mbill)
        if Sbill > Mbill:
            advantage = False
        else:
            advantage = True
        return totalu, Sbill, totalu / daynum, ECT, VAT, advantage
    else:
        ECT = (Mtotalufee * IECT)
        VAT = (Mtotalufee * OVAT)
        print("Daytime Usage", dayu)
        print("Peaktime Usage", peaku)
        print("Nighttime Usage", nightu)
        print("Total Usage kwh", totalu)
        print("Total usage TL without tax", Mtotalufee)
        print("ECT is", ECT, "VAT is", VAT)
        print("Bill is", Mbill)
        print("Change type diffrence is", Sbill - Mbill)
        if Sbill > Mbill:
            advantage = True
        else:
            advantage = False
        return totalu, Mbill, totalu / daynum, ECT, VAT, advantage


def public(dayu, peaku, nightu, daynum, SM):
    totalu = dayu + peaku + nightu
    lowlimit = daynum * 30
    if totalu <= lowlimit:
        Stotalufee = (totalu * PLOWTAR + totalu * PUNITFEE)/100
    else:
        Stotalufee = (lowlimit * PLOWTAR + (totalu - lowlimit) * PHIGHTAR + totalu * PUNITFEE)/100
    Mtotalufee = (dayu * PDAYFEE + peaku * PPEAKFEE + nightu * PNIGHTFEE + totalu * PUNITFEE)/100
    Sbill=(Stotalufee * (OAECT) * (OAVAT))
    Mbill=(Mtotalufee * (OAECT) * (OAVAT))
    if SM == "S":
        ECT = Stotalufee * OECT
        VAT = Stotalufee * OVAT
        printer(dayu,peaku,nightu,totalu,Stotalufee,ECT,VAT,Sbill)
        print("Change type diffrence is", Sbill - Mbill)
        if Sbill > Mbill:
            advantage = False
        else:
            advantage = True
        return totalu, Sbill, totalu / daynum, ECT, VAT, advantage
    else:
        ECT = Mtotalufee * OECT
        VAT = Mtotalufee * OVAT
        printer(dayu,peaku,nightu,totalu,Mtotalufee,ECT,VAT,Mbill)
        print("Change type diffrence is", Sbill - Mbill)
        if Sbill > Mbill:
            advantage = True
        else:
            advantage = False
        return totalu, Mbill, totalu / daynum, ECT, VAT, advantage


def residential(dayu, peaku, nightu, daynum, SM, fam):
    totalu = dayu + peaku + nightu
    lowlimit = daynum * 8
    if fam:
        Stotalufee = (totalu * FSINGLEFEE + totalu * FUNITFEE)/100
    else:
        if totalu <= lowlimit:
            Stotalufee = (totalu * RLOWTAR + totalu * RUNITFEE)/100
        else:
            Stotalufee = (lowlimit * RLOWTAR + (totalu - lowlimit) * RHIGHTAR + totalu * RUNITFEE)/100
    Mtotalufee = (dayu * RDAYFEE + peaku * RPEAKFEE + nightu * RNIGHTFEE + totalu * RUNITFEE)/100
    Sbill=(Stotalufee * (OAECT) * (RFAAVAT))
    Mbill=(Mtotalufee * (OAECT) * (RFAAVAT))
    if fam or SM == "S":
        ECT = Stotalufee * OECT
        VAT = Stotalufee * RFAVAT
        printer(dayu,peaku,nightu,totalu,Stotalufee,ECT,VAT,Sbill)
        if SM == "S":
            if Sbill > Mbill:
                advantage = False
            else:
                advantage = True
            print("Change type diffrence is", Sbill - Mbill)
            return totalu, Sbill, totalu / daynum, ECT, VAT, advantage
        return totalu, Sbill, totalu / daynum, ECT, VAT
    else:
        ECT = Mtotalufee * OECT
        VAT = Mtotalufee * RFAVAT
        printer(dayu,peaku,nightu,totalu,Mtotalufee,ECT,VAT,Mbill)
        print("Change type diffrence is", Sbill - Mbill)
        if Sbill > Mbill:
            advantage = True
        else:
            advantage = False
        return totalu, Mbill, totalu / daynum, ECT, VAT, advantage


def agricultural(dayu, peaku, nightu, daynum, SM):
    totalu = dayu + peaku + nightu
    Stotalufee = (totalu * ASINGLEFEE + totalu * AUNITFEE)/100
    Mtotalufee = (dayu * ADAYFEE + peaku * APEAKFEE + nightu * ANIGHTFEE + totalu * AUNITFEE)/100
    Sbill=Stotalufee * (OAECT) * (RFAAVAT)
    Mbill=Mtotalufee * (OAECT) * (RFAAVAT)
    if SM == 'S':
        ECT = Stotalufee * IECT
        VAT = Stotalufee * RFAVAT
        printer(dayu,peaku,nightu,totalu,Stotalufee,ECT,VAT,Sbill)
        print("Change type diffrence is", Sbill - Mbill)
        if Sbill > Mbill:
            advantage = False
        else:
            advantage = True
        return totalu, Sbill, totalu / daynum, ECT, VAT, advantage
    else:
        ECT = Mtotalufee * OECT
        VAT = Mtotalufee * RFAVAT
        printer(dayu,peaku,nightu,totalu,Mtotalufee,ECT,VAT,Mbill)
        print("Change type diffrence is", Sbill - Mbill)
        if Sbill > Mbill:
            advantage = True
        else:
            advantage = False
        return totalu, Mbill, totalu / daynum, ECT, VAT, advantage


def lightning(dayu, peaku, nightu, daynum):
    totalu = dayu + peaku + nightu
    Stotalufee = (totalu * LSINGLEFEE + totalu * LUNITFEE)/100
    ECT = Stotalufee * OECT
    VAT = Stotalufee * OVAT
    Sbill = Stotalufee * (OAECT) * (OAVAT)
    printer(dayu, peaku, nightu, totalu, Stotalufee, ECT, VAT, Sbill)
    return totalu, Sbill, totalu / daynum, ECT, VAT


def singmulti():
    type = input("Single or Multi:")
    if type == "s" or type == "S":
        type = "S"
        return type
    elif type == "m" or type == "M":
        type = "M"
        return type


def reader():
    preday = int(input("preday"))
    while preday <0:
        preday = int(input("preday"))
    curday = int(input("curday"))
    while curday<preday:
        curday = int(input("curday"))
    prepeak = int(input("prepeak"))
    while prepeak <0:
        prepeak = int(input("prepeak"))
    curpeak = int(input("curpeak"))
    while curpeak<prepeak:
        curpeak = int(input("curpeak"))
    prenight = int(input("prenight"))
    while prenight <0:
        prenight = int(input("prenight"))
    curnight = int(input("curnight"))
    while curnight<prenight:
        curnight = int(input("curnight"))
    daynumber = int(input("daynumber"))
    while daynumber<0:
        daynumber=int(input("Day number"))
    totalamoyear = int(input("totalamo year"))
    while totalamoyear<0 or totalamoyear<preday+prenight+prepeak:
        int(input("total amount year"))
    if totalamoyear+curday - preday+ curpeak - prepeak+curnight - prenight > 1000:
        freecons = True
    else:
        freecons = False
    return curday - preday, curpeak - prepeak, curnight - prenight, daynumber, freecons

def consumerdata(ctype,cons,total,kwh):
    print(ctype,"number is",cons)
    print(ctype,"percentage of all consumers",cons/total*100)
    print(ctype,"total kwh usage is",kwh)
    print(ctype,"average kwh usage is",kwh/cons)
def main():
    indcons, rezcons, agricons, lightcons = 0, 0, 0, 0
    pubscons,pubmcons=0,0
    tpubcons=0
    frezcons=0
    indkwh, pubkwh, rezkwh, agrikwh, lightkwh = 0, 0, 0, 0, 0
    freenum = 0
    maxrezconsno,maxotherconsno=0,0
    maxrezbill,maxotherbill=0,0
    maxrezave,maxotherave=0,0
    adv=0
    pubdays=0
    totalect,totalvat,totalbill=0,0,0
    while True:
        consno = int(input("Please enter the consumer no"))
        while consno<0:
            consno = int(input("Please enter the consumer no"))
        if consno == 0:
            totalcons = indcons + rezcons + agricons + lightcons + tpubcons
            consumerdata("Industry",indcons,totalcons,indkwh)
            consumerdata("Public and Private Services Sector and Other", tpubcons, totalcons, pubkwh)
            consumerdata("Residential", rezcons, totalcons, rezkwh)
            consumerdata("Agricultural Activities", agricons, totalcons, agrikwh)
            consumerdata("Lightning", lightcons, totalcons, lightkwh)
            print(pubscons,"of Public and Private Services Sector and Other consumers preferred single time")
            print(pubmcons, "of Public and Private Services Sector and Other consumers preferred multi time")
            print(pubscons/tpubcons*100, "% percent of Public and Private Services Sector and Other consumers preferred single time")
            print(pubmcons / tpubcons * 100,"% percent of Public and Private Services Sector and Other consumers preferred multi time")
            print("Public and Private Services Sector and Other consumers consumed an average",pubkwh/pubdays,"kWh per day")
            #Başkan buraya free cons muhabbeti gelecek ama yanlış anlatılmış pdfte hocaya soracağız
            print("Max rezidans average consumption consumer is",maxrezconsno,"consumed average of a day is",maxrezave,"bill is",maxrezbill)
            print("Max other bill consuemr no is",maxotherconsno,"bill is ",maxotherbill,"max average is",maxotherave)
            print("GDZ gained",totalbill-totalvat-totalect,"The municipality gained",totalect,"The state gained",totalvat)
            print("Advantage gainer is",adv/(totalcons-lightcons-frezcons)*100)
            break
        constype = input("Please enter the consumer type")
        while constype!="I" and constype!="i" and constype!="P" and constype!="p" and constype!="R" and constype!="r" and constype!="A" and constype!="a" and constype!="L" and constype!="l":
            constype = input("Please enter the consumer type")
        dayu, peaku, nightu, daynum,freecons= reader()
        if constype == "I" or constype == "i":
            SMtype = singmulti()
            usage,bill,average,nowect,nowvat,nowadv=industry(dayu, peaku, nightu, daynum, SMtype)
            indcons+=1
            indkwh+=usage
            totalect+=nowect
            totalvat+=nowvat
            totalbill+=bill
            if usage>1000 or bill>100000:
                freenum+=1
            if bill>maxotherbill:
                maxotherbill=bill
                maxotherconsno=consno
                maxotherave=average
            if nowadv:
                adv+=1
        elif constype == "P" or constype == "p":
            SMtype = singmulti()
            usage,bill,average,nowect,nowvat,nowadv=public(dayu, peaku, nightu, daynum, SMtype)
            if SMtype=="S":
                pubscons+=1
            else:
                pubmcons+=0
            pubkwh+=usage
            pubdays+=daynum
            totalect += nowect
            totalvat += nowvat
            totalbill+=bill
            if bill>maxotherbill:
                maxotherbill=bill
                maxotherconsno=consno
                maxotherave=average
            if nowadv:
                adv+=1
        elif constype == "R" or constype == "r":
            family = input("Are you Family veterans")
            if family == "Y" or family == "y":
                usage,bill,average,nowect,nowvat=residential(dayu, peaku, nightu, daynum, SMtype, True)
                frezcons+=1
            elif family == "N" or family == "n":
                SMtype = singmulti()
                usage,bill,average,nowect,nowvat,nowadv=residential(dayu, peaku, nightu, daynum, SMtype, False)
                if nowadv:
                    adv += 1
            rezcons+=1
            rezkwh+=usage
            totalect += nowect
            totalvat += nowvat
            totalbill+=bill
            if average>maxrezave:
                maxrezbill=bill
                maxrezconsno=maxrezconsno
                maxrezave=average
        elif constype == "A" or constype == "a":
            SMtype = singmulti()
            usage,bill,average,nowect,nowvat,nowadv=agricultural(dayu, peaku, nightu, daynum, SMtype)
            totalect += nowect
            totalvat += nowvat
            totalbill+=bill
            agricons+=1
            agrikwh+=usage
            if bill>maxotherbill:
                maxotherbill=bill
                maxotherconsno=consno
                maxotherave=average
            if nowadv:
                adv+=1
        else:
            usage,bill,average,nowect,nowvat=lightning(dayu, peaku, nightu, daynum)
            lightcons+=1
            lightkwh+=usage
            totalect += nowect
            totalvat += nowvat
            totalbill+=bill
            if bill>maxotherbill:
                maxotherbill=bill
                maxotherconsno=consno
                maxotherave=average
        if freecons==True:
            freenum+=1
            print("Consumer is Free")
main()
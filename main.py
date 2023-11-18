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
    Sbill = (Stotalufee * (1 + IECT) * (1 + OVAT))/100
    Mbill = (Mtotalufee * (1 + IECT) * (1 + OVAT))/100
    if SM == 'S':
        ECT = (Stotalufee * IECT) / 100
        VAT = (Stotalufee * OVAT) / 100
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
        ECT = (Mtotalufee * IECT) / 100
        VAT = (Mtotalufee * OVAT) / 100
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
        Stotalufee = totalu * PLOWTAR + totalu * PUNITFEE
    else:
        Stotalufee = lowlimit * PLOWTAR + (totalu - lowlimit) * PHIGHTAR + totalu * PUNITFEE
    Mtotalufee = dayu * PDAYFEE + peaku * PPEAKFEE + nightu * PNIGHTFEE + totalu * PUNITFEE
    Sbill=(Stotalufee * (1+OECT) * (1+OVAT))/100
    Mbill=(Mtotalufee * (1+OECT) * (1+OVAT))/100
    if SM == "S":
        ECT = Stotalufee * OECT / 100
        VAT = Stotalufee * OVAT / 100
        print("Daytime Usage", dayu)
        print("Peaktime Usage", peaku)
        print("Nighttime Usage", nightu)
        print("total usage kwh", totalu)
        print("total usage TL without tax", Stotalufee)
        print("ECT is", ECT, "VAT is", VAT)
        print("Bill is", Sbill)
        print("Change type diffrence is", Sbill - Mbill)
        if Sbill > Mbill:
            advantage = False
        else:
            advantage = True
        return totalu, Sbill, totalu / daynum, ECT, VAT, advantage
    else:
        ECT = Mtotalufee * OECT / 100
        VAT = Mtotalufee * OVAT / 100
        print("Daytime Usage", dayu)
        print("Peaktime Usage", peaku)
        print("Nighttime Usage", nightu)
        print("total usage kwh", totalu)
        print("total usage TL without tax", Mtotalufee)
        print("ECT is", ECT, "VAT is", VAT)
        print("Bill is", Mbill)
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
        Stotalufee = totalu * FSINGLEFEE + totalu * FUNITFEE
    else:
        if totalu <= lowlimit:
            Stotalufee = totalu * RLOWTAR + totalu * RUNITFEE
        else:
            Stotalufee = lowlimit * RLOWTAR + (totalu - lowlimit) * RHIGHTAR + totalu * RUNITFEE
    Mtotalufee = dayu * RDAYFEE + peaku * RPEAKFEE + nightu * RNIGHTFEE + totalu * RUNITFEE
    Sbill=(Stotalufee * (1+OECT) * (1+RFAVAT))/100
    Mbill=(Mtotalufee * (1+OECT) * (1+RFAVAT))/100
    if fam or SM == "S":
        ECT = Stotalufee * OECT / 100
        VAT = Stotalufee * RFAVAT / 100
        print("Daytime Usage", dayu)
        print("Peaktime Usage", peaku)
        print("Nighttime Usage", nightu)
        print("total usage kwh", totalu)
        print("total usage TL without tax", Stotalufee)
        print("ECT is", ECT, "VAT is", VAT)
        print("Bill is", Sbill)
        if SM == "S":
            if Sbill > Mbill:
                advantage = False
            else:
                advantage = True
            print("Change type diffrence is", Sbill - Mbill)
            return totalu, Sbill, totalu / daynum, ECT, VAT, advantage
        return totalu, Sbill, totalu / daynum, ECT, VAT
    else:
        ECT = Mtotalufee * OECT / 100
        VAT = Mtotalufee * RFAVAT / 100
        print("Daytime Usage", dayu)
        print("Peaktime Usage", peaku)
        print("Nighttime Usage", nightu)
        print("total usage kwh", totalu)
        print("total usage TL without tax", Mtotalufee)
        print("ECT is", ECT, "VAT is", VAT)
        print("Bill is", Mbill)
        print("Change type diffrence is", Sbill - Mbill)
        if Sbill > Mbill:
            advantage = True
        else:
            advantage = False
        return totalu, Mbill, totalu / daynum, ECT, VAT, advantage


def agricultural(dayu, peaku, nightu, daynum, SM):
    totalu = dayu + peaku + nightu
    Stotalufee = totalu * ASINGLEFEE + totalu * AUNITFEE
    Mtotalufee = dayu * ADAYFEE + peaku * APEAKFEE + nightu * ANIGHTFEE + totalu * AUNITFEE
    Sbill=(Stotalufee * (1+OECT) * (1+RFAVAT))/100
    Mbill=(Mtotalufee * (1+OECT) * (1+RFAVAT))/100
    if SM == 'S':
        ECT = Stotalufee * IECT / 100
        VAT = Stotalufee * RFAVAT / 100
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
        ECT = Mtotalufee * OECT / 100
        VAT = Mtotalufee * RFAVAT / 100
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


def lightning(dayu, peaku, nightu, daynum):
    totalu = dayu + peaku + nightu
    Stotalufee = totalu * LSINGLEFEE + totalu * LUNITFEE
    ECT = Stotalufee * OECT / 100
    VAT = Stotalufee * OVAT / 100
    Sbill = ((Stotalufee / 100) * (1 + ECT) * (1 + VAT))
    print("Daytime Usage", dayu)
    print("Peaktime Usage", peaku)
    print("Nighttime Usage", nightu)
    print("Total Usage kwh", totalu)
    print("Total usage TL without tax", Stotalufee)
    print("ECT is", ECT, "VAT is", VAT)
    print("Bill is", Sbill)
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
    curday = int(input("curday"))
    prepeak = int(input("prepeak"))
    curpeak = int(input("curpeak"))
    prenight = int(input("prenight"))
    curnight = int(input("curnight"))
    daynumber = int(input("daynumber"))
    totalamoyear = int(input("totalamo year"))
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
    maxrezusage,maxotherusage=0,0
    maxrezbill,maxotherbill=0,0
    maxrezave,maxotherave=0,0
    adv=0
    pubdays=0
    totalect,totalvat,totalbill=0,0,0
    while True:
        consno = int(input("Please enter the consumer no"))
        if consno == 0:
            totalcons = indcons + rezcons + agricons + lightcons + tpubcons
            totalkwh = indkwh + pubkwh + rezkwh + agrikwh + lightkwh
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
        dayu, peaku, nightu, daynum,freecons= reader()
        if constype == "I" or constype == "ı":
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
                maxotherusage=usage
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
                maxotherusage=usage
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
                maxrezusage=usage
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
                maxotherusage=usage
                maxotherconsno=consno
                maxotherave=average
            if nowadv:
                adv+=1
        elif constype == "L" or constype == "l":
            usage,bill,average,nowect,nowvat=lightning(dayu, peaku, nightu, daynum)
            lightcons+=1
            lightkwh+=usage
            totalect += nowect
            totalvat += nowvat
            totalbill+=bill
            if bill>maxotherbill:
                maxotherbill=bill
                maxotherusage=usage
                maxotherconsno=consno
                maxotherave=average
        if freecons==True:
            freenum+=1
            print("Consumer is Free")
main()
"""Kral SA benim ingilizce A0 o yüzden açıklamaları türkçe yazacağım sen çevir
sonra inputlardaki soruları formal dilde düzelt üstüne bir de test et tüm sistemi
istatistikler dahil sonra hocaya sorduğum soruya göre göndeririz kodu
türkçe biri
"""
"""
constant isimleri üç parça ilk parçası sektöre ait I industry P public(tam ismini yazarsın başkan)
R residential A agricultural activities L lightning ikinci parça zamana bağlı 
day peak single ya da night olarak ayrıldı üçüncü parça fee yada tarriff de ngelen tarr
vergiler 2 tip olduğu için I industry RFA Residential, Family veterans ve Agricultural kısaltmaları 
O ise ECT de industry hariç hepsi VAT da ise yukarıda belirtilen RFA hariç sektörler
vergilerde sektör yanında yazan A ise 1 added anlamına geliyor vergiyi hesaplarken tekrardan 1 eklememek için var
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
Printer fonksiyon her sektördeki tekrar tekrar basılan çıktıların okunulabilirliği arttırması için
tek fonksiyon altında toplanmasıdır
"""
def printer(dayu,peaku,nightu,totalu,totalufee,ECT,VAT,bill):
    print("Daytime Usage", dayu)
    print("Peaktime Usage", peaku)
    print("Nighttime Usage", nightu)
    print("Total Usage kwh", totalu)
    print("Total usage TL without tax", round(totalufee,2))
    print("ECT is", round(ECT,2), "VAT is", round(VAT,2))
    print("Bill is", round(bill,2))

"""
Alttaki beş fonksiyon her sektör için ayrı fatura hesabı yapılması için tasarlanmıştır.
hepsinde ortak değişken isimleri kullanılarak okunulabilirlik arttırılmıştır
kısaltmalar şu şekildedir sondaki u usage baştaki S single time M multi time temsil etmektedir
totalu total usage dır 
low limit ise düşük tarife sınırını belirtmektedir
"""
def industry(dayu, peaku, nightu, daynum, SM):
    totalu = dayu + peaku + nightu
    Stotalufee = totalu * ISINGLEFEE/100
    Mtotalufee = (dayu * IDAYFEE + peaku * IPEAKFEE + nightu * INIGHTFEE)/100
    SECT = (Stotalufee * IECT)
    MECT = (Mtotalufee * IECT)
    disturbfee=totalu*IUNITFEE/100
    Sbill = ((Stotalufee+SECT+disturbfee) * (OAVAT))
    Mbill = ((Mtotalufee+MECT+disturbfee) * (OAVAT))
    if SM == 'S':
        VAT = Sbill-(Stotalufee+SECT+disturbfee)
        printer(dayu,peaku,nightu,totalu,Stotalufee,SECT,VAT,Sbill)
        print("Change type diffrence is", round(Sbill - Mbill,2))
        if Sbill > Mbill:
            advantage = False
        else:
            advantage = True
        return totalu, Sbill, totalu / daynum, SECT, VAT, advantage
    else:
        VAT = Mbill-(Mtotalufee+SECT+disturbfee)
        printer(dayu,peaku,nightu,totalu,Mtotalufee,SECT,VAT,Mbill)
        print("Change type diffrence is", round(Sbill - Mbill,2))
        if Sbill > Mbill:
            advantage = True
        else:
            advantage = False
        return totalu, Mbill, totalu / daynum, MECT, VAT, advantage


def public(dayu, peaku, nightu, daynum, SM):
    totalu = dayu + peaku + nightu
    lowlimit = daynum * 30
    if totalu <= lowlimit:
        Stotalufee = (totalu * PLOWTAR)/100
    else:
        Stotalufee = (lowlimit * PLOWTAR + (totalu - lowlimit) * PHIGHTAR)/100
    Mtotalufee = (dayu * PDAYFEE + peaku * PPEAKFEE + nightu * PNIGHTFEE)/100
    SECT = (Stotalufee * OECT)
    MECT = (Mtotalufee * OECT)
    disturbfee=totalu*PUNITFEE/100
    Sbill = ((Stotalufee+SECT+disturbfee) * (OAVAT))
    Mbill = ((Mtotalufee+MECT+disturbfee) * (OAVAT))
    if SM == "S":
        VAT = Sbill-(Stotalufee+SECT+disturbfee)
        printer(dayu,peaku,nightu,totalu,Stotalufee,SECT,VAT,Sbill)
        print("Change type diffrence is", round(Sbill - Mbill,2))
        if Sbill > Mbill:
            advantage = False
        else:
            advantage = True
        return totalu, Sbill, totalu / daynum, SECT, VAT, advantage
    else:
        VAT = Mbill-(Mtotalufee+SECT+disturbfee)
        printer(dayu,peaku,nightu,totalu,Mtotalufee,MECT,VAT,Mbill)
        print("Change type diffrence is", round(Sbill - Mbill,2))
        if Sbill > Mbill:
            advantage = True
        else:
            advantage = False
        return totalu, Mbill, totalu / daynum, MECT, VAT, advantage

#fam değişkeni şehit gazi yakını olup olmadığını tutmaktadır
def residential(dayu, peaku, nightu, daynum, SM, fam):
    totalu = dayu + peaku + nightu
    lowlimit = daynum * 8
    if fam:
        Stotalufee = (totalu * FSINGLEFEE)/100
        disturbfee = totalu * FUNITFEE / 100
    else:
        if totalu <= lowlimit:
            Stotalufee = (totalu * RLOWTAR) / 100
        else:
            Stotalufee = (lowlimit * RLOWTAR + (totalu - lowlimit) * RHIGHTAR) / 100
        Mtotalufee = (dayu * RDAYFEE + peaku * RPEAKFEE + nightu * RNIGHTFEE) / 100
        disturbfee = totalu * RUNITFEE / 100
        MECT = (Mtotalufee * OECT)
        Mbill = ((Mtotalufee+MECT+disturbfee) * (RFAAVAT))
    SECT = (Stotalufee * OECT)
    Sbill = ((Stotalufee+SECT+disturbfee) * (RFAAVAT))
    if fam or SM == "S":
        VAT = Sbill-(Stotalufee+SECT+disturbfee)
        printer(dayu,peaku,nightu,totalu,Stotalufee,SECT,VAT,Sbill)
        if SM == "S":
            if Sbill > Mbill:
                advantage = False
            else:
                advantage = True
            print("Change type diffrence is", round(Sbill - Mbill,2))
            return totalu, Sbill, totalu / daynum, SECT, VAT, advantage
        return totalu, Sbill, totalu / daynum, SECT, VAT
    else:
        VAT = Mbill-(Mtotalufee+SECT+disturbfee)
        printer(dayu,peaku,nightu,totalu,Mtotalufee,MECT,VAT,Mbill)
        print("Change type diffrence is", round(Sbill - Mbill,2))
        if Sbill > Mbill:
            advantage = True
        else:
            advantage = False
        return totalu, Mbill, totalu / daynum, MECT, VAT, advantage


def agricultural(dayu, peaku, nightu, daynum, SM):
    totalu = dayu + peaku + nightu
    Stotalufee = (totalu * ASINGLEFEE)/100
    Mtotalufee = (dayu * ADAYFEE + peaku * APEAKFEE + nightu * ANIGHTFEE)/100
    SECT = (Stotalufee * OECT)
    MECT = (Mtotalufee * OECT)
    disturbfee=totalu*AUNITFEE/100
    Sbill = ((Stotalufee+SECT+disturbfee) * (RFAAVAT))
    Mbill = ((Mtotalufee+MECT+disturbfee) * (RFAAVAT))
    if SM == 'S':
        VAT = Sbill-(Stotalufee+SECT+disturbfee)
        printer(dayu,peaku,nightu,totalu,Stotalufee,SECT,VAT,Sbill)
        print("Change type diffrence is", round(Sbill - Mbill,2))
        if Sbill > Mbill:
            advantage = False
        else:
            advantage = True
        return totalu, Sbill, totalu / daynum, SECT, VAT, advantage
    else:
        VAT = Mbill-(Mtotalufee+SECT+disturbfee)
        printer(dayu,peaku,nightu,totalu,Mtotalufee,MECT,VAT,Mbill)
        print("Change type diffrence is", round(Sbill - Mbill,2))
        if Sbill > Mbill:
            advantage = True
        else:
            advantage = False
        return totalu, Mbill, totalu / daynum, MECT, VAT, advantage


def lightning(dayu, peaku, nightu, daynum):
    totalu = dayu + peaku + nightu
    Stotalufee = (totalu * LSINGLEFEE)/100
    ECT = Stotalufee * OECT
    disturbfee=totalu*LUNITFEE/100
    Sbill = ((Stotalufee+ECT+disturbfee) * (OAVAT))
    VAT = Sbill - (Stotalufee + ECT + disturbfee)
    printer(dayu, peaku, nightu, totalu, Stotalufee, ECT, VAT, Sbill)
    return totalu, Sbill, totalu / daynum, ECT, VAT

"""
Single veya multi time seçeneğini seçtirmek için yazılmıştır
"""
def singmulti():
    type = input("Single or Multi:")
    while type not in "SsMm":
        type = input("Single or Multi:")
    if type == "s" or type == "S":
        type = "S"
        return type
    elif type == "m" or type == "M":
        type = "M"
        return type

"""
Kullanıcıdan inputları almak için yazılmıştır
"""
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
    while totalamoyear<preday+prenight+prepeak:
        totalamoyear=int(input("total amount year"))
    if totalamoyear+curday - preday+ curpeak - prepeak+curnight - prenight > 1000:
        freecons = True
    else:
        freecons = False
    return curday - preday, curpeak - prepeak, curnight - prenight, daynumber, freecons,totalamoyear
"""
istatistk bölümündeki her sektör için olan istatistik kalabalığını azaltmak için yazılmıştır
"""
def consumerdata(ctype,cons,total,kwh):
    print(ctype,"number is",round(cons,2))
    print(ctype,"percentage of all consumers",round(cons/total*100,2))
    print(ctype,"total kwh usage is",round(kwh,2))
    print(ctype,"average kwh usage is",round(kwh/cons,2))
def main():
    indcons, rezcons, agricons, lightcons = 0, 0, 0, 0 #sektördeki consumer sayıları
    pubscons,pubmcons=0,0 #publicteki single ve multi seçenlerin sayısı
    frezcons=0 #Şehit gazi yakını sayısı
    indkwh, pubkwh, rezkwh, agrikwh, lightkwh = 0, 0, 0, 0, 0 #sektörlerin kullandı elektrik miktarı
    freenum = 0 #Free consumer sayısı
    maxrezconsno,maxotherconsno=0,0# Max istatistiği istenen rezidasn ve other kullanıcı verileri
    maxrezbill,maxotherbill=0,0
    maxrezave,maxotherave=0,0
    adv=0 #avantaj sağlayan kullanıcı sayısı
    pubdays=0 #Public kullanıcıların toplam kullandığı gün sayısı
    totalect,totalvat,totalbill=0,0,0 #toplam fatura bedeli, kdv ve ect verileri
    while True:
        consno = int(input("Please enter the consumer no")) #Consumer no inputu
        while consno<0:
            consno = int(input("Please enter the consumer no"))
        if consno == 0:
            tpubcons = pubscons + pubmcons #toplam public kullanıcı sayısı
            totalcons = indcons + rezcons + agricons + lightcons + tpubcons #toplam consumer sayısı
            totalkwh = indkwh + pubkwh + rezkwh + agrikwh + lightkwh #toplam harcanan kwh sayısı
            consumerdata("Industry",indcons,totalcons,indkwh)
            consumerdata("Public and Private Services Sector and Other", tpubcons, totalcons, pubkwh)
            consumerdata("Residential", rezcons, totalcons, rezkwh)
            consumerdata("Agricultural Activities", agricons, totalcons, agrikwh)
            consumerdata("Lightning", lightcons, totalcons, lightkwh)
            print("Bornova all electric consumption is ",totalkwh)
            print(pubscons,"of Public and Private Services Sector and Other consumers preferred single time")
            print(pubmcons, "of Public and Private Services Sector and Other consumers preferred multi time")
            print(round(pubscons/tpubcons*100,2), "% percent of Public and Private Services Sector and Other consumers preferred single time")
            print(round(pubmcons / tpubcons * 100,2),"% percent of Public and Private Services Sector and Other consumers preferred multi time")
            print("Public and Private Services Sector and Other consumers consumed an average",round(pubkwh/pubdays,2),"kWh per day")
            print("Freeconsumer number is",freenum,"free consumer percantage of industry%",round(freenum/indcons*100,2))
            print("Max rezidans average consumption consumer is",maxrezconsno,"consumed average of a day is",round(maxrezave,2),"bill is",round(maxrezbill,2))
            print("Max other bill consuemr no is",maxotherconsno,"bill is ",round(maxotherbill,2),"max average is",round(maxotherave,2))
            print("GDZ gained",round(totalbill-totalvat-totalect,2),"The municipality gained",round(totalect,2),"The state gained",round(totalvat,2))
            print("Advantage gainer is",round(adv/(totalcons-lightcons-frezcons)*100,2))
            break
        constype = input("Please enter the consumer type") #consumer type inputu
        while constype not in ["I","i","P","p","R","r","A","a","L","l"]:
            constype = input("Please enter the consumer type")
        """
        Consumer type'a göre veri girişi, çıktı basımı ve istatistik bölümü için veri tutma işlemleri
        """
        if constype == "I" or constype == "i":
            SMtype = singmulti()
            dayu, peaku, nightu, daynum, freecons,totalu = reader()
            print("Consumer no",consno)
            print("Consumer type is Industry")
            usage,bill,average,nowect,nowvat,nowadv=industry(dayu, peaku, nightu, daynum, SMtype)
            indcons+=1
            indkwh+=usage
            totalect+=nowect
            totalvat+=nowvat
            totalbill+=bill
            if usage>10000 or bill>100000 or totalu>1000:
                freenum+=1
            if bill>maxotherbill:
                maxotherbill=bill
                maxotherconsno=consno
                maxotherave=average
            if nowadv:
                adv+=1
        elif constype == "P" or constype == "p":
            SMtype = singmulti()
            dayu, peaku, nightu, daynum, freecons,totalu = reader()
            print("Consumer no",consno)
            print("Consumer type is Public and Private Services Sector and Other")
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
                dayu, peaku, nightu, daynum, freecons,totalu = reader()
                print("Consumer no", consno)
                print("Consumer type is Residential (family of martyrs and veterans)")
                usage,bill,average,nowect,nowvat=residential(dayu, peaku, nightu, daynum, "", True)
                frezcons+=1
            elif family == "N" or family == "n":
                SMtype = singmulti()
                dayu, peaku, nightu, daynum, freecons,totalu = reader()
                print("Consumer no", consno)
                print("Consumer type is Residential")
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
                maxrezconsno=consno
                maxrezave=average
        elif constype == "A" or constype == "a":
            SMtype = singmulti()
            dayu, peaku, nightu, daynum, freecons,totalu = reader()
            print("Consumer no", consno)
            print("Consumer type is Agricultural Activities")
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
            dayu, peaku, nightu, daynum, freecons,totalu = reader()
            print("Consumer no", consno)
            print("Consumer type is Lightning")
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
        if freecons:
            print("Total usage is ",totalu,"Consumer is Free")
        else:
            print("Total usage is ", totalu, "Consumer is not free")
main()
ISINGLEFEE,FSINGLEFEE,ASINGLEFEE,LSINGLEFEE=305.3828,6.1590,165.3096,259.5835
PLOWTAR,PHIGHTAR,RLOWTAR,RHIGHTAR=191.2220,282.8414,48.2187,113.2271
IDAYFEE,PDAYFEE,RDAYFEE,ADAYFEE=309.1833,285.8616,115.7700,170.4822
IPEAKFEE,PPEAKFEE,RPEAKFEE,APEAKFEE=490.9037,458.8843,208.3645,280.0325
INIGHTFEE,PNIGHTFEE,RNIGHTFEE,ANIGHTFEE=162.5171,148.1941,41.7225,77.1882
IUNITFEE,PUNITFEE,RUNITFEE,FUNITFEE,AUNITFEE,LUNITFEE=64.7998,87.8175,85.883,58.2521,72.1579,84.1099
IECT,OECT,RFAVAT,OVAT=1.01,1.05,1.1,1.2
def industry():
    print("Yavaş kardeş daha yazmadık")sadadsdsa
def public():
    print("Yavaş kardeş daha yazmadık")
def residential(fam):
    print("Yavaş kardeş daha yazmadık")
def agricultural():
    print("Yavaş kardeş daha yazmadık")
def lightning():
    print("Yavaş kardeş daha yazmadık")
def main():
    while True:
        consno=int(input("Please enter the consumer no"))
        if consno==0:
            break
        constype=input("Please enter the consumer type")
        if constype=="R" or constype=="r":
            family=input("Are you Family veterans")
            if family=="Y" or family=="y":
                residential(True)
            elif family=="N" or family=="n":
                residential(False)
        if constype=="I" or constype=="ı":
            industry()
        elif constype=="P" or constype=="p":
            public()
        elif constype=="A" or constype=="a":
            agricultural()
        elif constype=="L" or constype=="l":
            lightning()

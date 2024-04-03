

def loe_failist(fail:str)->list:
    """
    EESTI JA VENE SÕNASTIK
    """
    f=open(fail,'r',encoding="utf-8")
    est_sõn=[]
    for rida in f:
        est_sõn.append(rida.strip())
    f.close()
    return est_sõn
    f=open(fail,'r',encoding="utf-8")
    rus_sõn=[]
    for rida in f:
        rus_sõn.append(rida.strip())
    f.close()
    return rus_sõn

def sõna_lisamine(fail:str)->list:
    """
    SÕNA LISAMINE SÕNASTIKKU
    """
    estadd=input("Lisa sõna eesti keeles: ")
    if estadd in list_est:
        print(f"{estadd} on juba olemas")
    else:
        rusadd=input("Lisa sõna tõlge vene keeles: ")   
        list_est.append(estadd)
        list_rus.append(rusadd)
        print("Sõnad lisatud")
    return list_est, list_rus

def est_parandus(fail:str)->list:
    """
    SÕNA PARANDAMINE EESTI KEELES 
    """
    tofixest=input("Mis sõna soovid parandada: ")
    if tofixest not in list_est:
        print(f"{tofixest} puudub sõnade nimekirjas")
    else:
        fixedest=input("Lisa õige sõna: ")
        fixindexest=list_est.index(tofixest)
        list_est.insert(fixindexest, fixedest)
        list_est.remove(tofixest)
        print("Sõnad parandatud")
    return list_est, list_rus

def rus_parandus(fail:str)->list:
    """
    SÕNA PARANDAMINE VENE KEELES 
    """
    tofix=input("Mis sõna soovid parandada: ")
    if tofix not in list_rus:
        print(f"{tofix} puudub sõnade nimekirjas")
    else:
        fixed=input("Lisa õige sõna: ")
        fixindex=list_rus.index(tofix)
        list_rus.insert(fixindex, fixed)
        list_rus.remove(tofix)
        print("Sõnad parandatud")
    return list_est, list_rus

def tõlkimine_est(fail:str)->list:
    """
    EESTI SÕNA TÕLKIMINE
    """
    estword=input("Kirjuta sõna, mida tahad tõlkida eesti keelest vene keelde: ")
    if estword in list_est:
        print(f"{estword} vene keeles on:")
        translindexest=list_est.index(estword)
        print(list_rus[translindexest])
    else:
        print("Sõna puudub sõnade nimekirjas")
    return list_est, list_rus

def tõlkimine_rus(fail:str)->list:
    """
    VENE SÕNA TÕLKIMINE
    """
    rusword=input("Kirjuta sõna, mida tahad tõlkida vene keelest eesti keelde: ")
    if rusword in list_rus:
        print(f"{rusword} vene keeles on:")
        translindexrus=list_rus.index(rusword)
        print(list_est[translindexrus])
    else:
        print("Sõna puudub sõnade nimekirjas")
    return list_est, list_rus

list_est:list=loe_failist("est.txt")
list_rus:list=loe_failist("rus.txt")

while True:
    x=int(input("\n Tõlgi eesti keelest vene keelde - 1 \n Tõlgi vene keelest eesti keelde - 2 \n Lisa sõna sõnastikku - 3 \n Paranda viga eesti keeles - 4 \n Paranda viga vene keeles - 5 \n "))
    if x==1:
        tõlkimine_est(list_est)
    elif x==2:
        tõlkimine_rus(list_rus)
    elif x==3:
        print("Lisa sõna sõnastikku")
        sõna_lisamine(list_est)
    elif x==4:
        print("Paranda viga eesti keeles")
        est_parandus(list_est)
    elif x==5:
        print("Paranda viga vene keeles")
        rus_parandus(list_rus)
    else:
        print("-")


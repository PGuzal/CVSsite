import data as d
import numpy as np

#obliczenie procentow dla plci
def procent_plec(plec, dane_plec):
    procenty = 0
    #suma respondentow z ta odpowiedzia
    suma = int(dane_plec[0])+int(dane_plec[1])+int(dane_plec[2])
    #sprawdzenie odpowiedzi respondenta
    if plec == 'K':
        procenty = round(((int(dane_plec[1]))/suma)*100, 2)
    elif plec == 'M':
        procenty = round(((int(dane_plec[0]))/suma)*100, 2)
    else:
        procenty = round(((int(dane_plec[2]))/suma)*100, 2)
    return procenty

#obliczenie procentow dla wyksztalcenia
def procent_wyksztalcenie(wyksztalcenie, dane_wyksztalcenie):
    tekst = ""
    procenty = [0,0]
    suma = int(dane_wyksztalcenie[0])+int(dane_wyksztalcenie[1])
    if int(wyksztalcenie) == 1:
        procenty[0] = round(((int(dane_wyksztalcenie[0]))/suma)*100,2)
        procenty[1] = round(((int(dane_wyksztalcenie[1]))/suma)*100,2)
        #tekst do wyswietlenia na stronie
        tekst = 'wyższym wykształceniem'
    elif int(wyksztalcenie) == 2:
        procenty[0] =  round(((int(dane_wyksztalcenie[1]))/suma)*100,2)
        procenty[1] =  round(((int(dane_wyksztalcenie[0]))/suma)*100,2)
        tekst = 'niższym wykształceniem'
    return procenty, tekst

#obliczenie procentow dla wieku, urzadzen, wiedzy
def procent_liczby(odpowiedz,dane,mozliwe):
    suma = 0
    grupy = [0,0,0]
    procenty = [0,0,0]
    numer = 0
    for i in range(len(dane)):
        suma += int(dane[i])

    for i in mozliwe:
        #jesli odpowiedz jest wieksza niz dana mozliwa odpowiedz
        if i < int(odpowiedz):
           grupy[0] += dane[numer]
        elif i == int(odpowiedz):
           grupy[1] += dane[numer]
        #jesli odpowiedz jest mniejsza niz dana mozliwa odpowiedz
        elif i > int(odpowiedz):
           grupy[2] += dane[numer]
        numer +=1
    #obliczanie procentow w danej grupie(mniejsza, rowna, wieksza odpowiedz)
    procenty[0]= round(((grupy[0]/suma)*100),2)
    procenty[1]= round((((grupy[1])/suma)*100),2)
    procenty[2]= round(((grupy[2]/suma)*100),2)

    return procenty
#obliczanie procentow dla czasu pracy przy komputerze
def procent_czas(czas, dane_czas):
    suma = 0
    czas_mozliwy = [0,1,2,3,4]
    odpowiedz = 0
    grupy = [0,0,0]
    procenty = [0,0,0]
    numer = 0
    liczba = 0
    for i in range(len(dane_czas)):
        suma += int(dane_czas[i])
    for odp in d.zestaw_pytan[15]['wartosc']:
        if czas == odp:
           odpowiedz = liczba
        liczba +=1

    for i in czas_mozliwy:
        if i < odpowiedz:
           grupy[0] += dane_czas[numer]
        elif i == odpowiedz:
           grupy[1] += dane_czas[numer]
        elif i > odpowiedz:
           grupy[2] += dane_czas[numer]
        numer +=1

    procenty[0]= round(((grupy[0]/suma)*100),2)
    procenty[1]= round((((grupy[1])/suma)*100),2)
    procenty[2]= round(((grupy[2]/suma)*100),2)

    return procenty
#obliczanie procentow dla odpowiedzi typu tak nie
def procent_bool(dana, zestaw, numer):
    suma = 0
    procenty = 0
    tekst = [" "," "]
    for i in range(len(zestaw)):
        suma += int(zestaw[i])
    if int(dana) == 1:
         procenty= round(((zestaw[1])/suma)*100,2)
         if numer == 1:
            tekst[1] = "problemy"
    else:
         procenty= round(((zestaw[0])/suma)*100,2)
         #tekst do wyswietlania na stronie
         tekst[0] = "nie"
         if numer == 1:
            tekst[1] = "problemów"

    return procenty, tekst
#obliczanie procent dla pytan wielokrotnego wyboru
def procent_wielokrotnego(dane, dane_lista, ilosc):
    suma = len(ilosc)
    grupy = [0,0,0]
    procenty = [0,0,0]
    odpowiedzi = ""
    dane_liczba = 0
    for i in dane:
        if str(i) != "":
           dane_liczba +=1
           #dodanie przecinka do zbioru odpowiedzi
           odpowiedzi+=(str(i)+", ")

    for i in ilosc:
        if i < dane_liczba :
           grupy[0] += 1
        elif i == dane_liczba :
           grupy[1] += 1
        elif i > dane_liczba :
           grupy[2] += 1

    procenty[0]= round(((grupy[0]/suma)*100),2)
    procenty[1]= round((((grupy[1])/suma)*100),2)
    procenty[2]= round(((grupy[2]/suma)*100),2)

    return procenty, odpowiedzi

#zmiana kolejnosci danych do wykresow
def wykres_wiele(dane, odpowiedz, wartosci, legenda):
    legenda_zmiana = []
    dane_zmiana = []
    #przepisanie wartości z listy dostarczonej do funkcji
    for j in legenda:
        legenda_zmiana.append(j)

    for i in dane:
        dane_zmiana.append(int(i))

    #porownianie odpowiedzi na liscie do odpowiedzi respondenta
    if odpowiedz == wartosci[0]:
        dane_zmiana = dane
        legenda_zmiana = legenda
    elif odpowiedz == wartosci[1]:
        #zmiana kolejnosci elementow w listach
        dane_zmiana.insert(0,int(dane[1]))
        dane_zmiana.pop(2)
        legenda_zmiana.insert(0,legenda[1])
        legenda_zmiana.pop(2)
    elif odpowiedz == wartosci[2]:
        dane_zmiana.insert(0,int(dane[2]))
        dane_zmiana.pop(3)
        legenda_zmiana.insert(0,legenda[2])
        legenda_zmiana.pop(3)
    elif odpowiedz == wartosci[3]:
        dane_zmiana.insert(0,int(dane[3]))
        dane_zmiana.pop(4)
        dane_zmiana.insert(1,int(dane[4]))
        dane_zmiana.pop()
        legenda_zmiana.insert(0,legenda[3])
        legenda_zmiana.pop(4)
        legenda_zmiana.insert(1,legenda[4])
        legenda_zmiana.pop()
    elif odpowiedz == wartosci[4]:
        dane_zmiana.insert(0, int(dane[4]))
        dane_zmiana.pop()
        legenda_zmiana.insert(0,legenda[4])
        legenda_zmiana.pop()
    return dane_zmiana, legenda_zmiana
#zmiana kolejnosci danych do wykresow
def wykres_liczby(dane,odpowiedz, legenda):

    indeks = 0
    numer = 0
    dane_z = np.zeros(len(dane))
    legenda_z = np.zeros(len(dane))
    legenda_zmiana =[]
    dane_zmiana = []
    #przepisujemy tablice dostarczone do funkcji
    for i in range(len(dane)):
        legenda_zmiana.append(int(legenda_z[i]))
        dane_zmiana.append(int(dane_z[i]))
    #sprawdzanie indeksu odpowiedzi respondenta
    for i in legenda:
        if i == int(odpowiedz):
            indeks = legenda.index(int(odpowiedz))

    for i in dane:
        if numer < indeks:
            dane_zmiana[int(len(dane)-(indeks-numer))]=i
            legenda_zmiana[int(len(dane)-(indeks-numer))] = legenda[numer]
        elif numer > indeks:
            dane_zmiana[int(numer-indeks)]=i
            legenda_zmiana[int(numer-indeks)] = legenda[numer]
        elif numer == indeks:
            dane_zmiana[0]=i
            legenda_zmiana[0] = legenda[numer]
        numer +=1
    return dane_zmiana, legenda_zmiana
#zmiana kolejnosci danych do wykresow
def wykres_dwie(dane, odpowiedz, legenda):
    legenda_zmiana = []
    dane_zmiana = []
    for i in legenda:
        legenda_zmiana.append(i)

    for j in dane:
        dane_zmiana.append(int(j))

    if int(odpowiedz) == 1:
        dane_zmiana[0] = int(dane[1])
        dane_zmiana[1] = int(dane[0])
        legenda_zmiana[0] = "Tak"
        legenda_zmiana[1] = "Nie"
    return dane_zmiana, legenda_zmiana

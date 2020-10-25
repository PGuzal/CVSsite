from datetime import datetime
#lista pytan do ankiety
zestaw_pytan = [
    {
        'pytanie': u'1.1 E-mail:',
        'nazwa':u'email',
        'typ': u'E'
    },
    {
        'pytanie': u'1.2 Płeć:',
        'odpowiedzi': [u'Mężczyzna', u'Kobieta', u'Inna'],
        'wartosc': [u'M',u'K',u'I'],
        'nazwa':u'plec',
        'typ': u'C'
    },
        {
        'pytanie': u'1.3 Wiek: (zakres 16-35)',
        'nazwa':u'wiek',
        'typ': u'W'
    },
     {
        'pytanie': u'1.4 Wykształcenie:',
        'odpowiedzi': [u'studia pierwszego stopnia', u'studia drugiego stopnia', u'studia trzeciego stopnia'],
        'wartosc': [u'1',u'2',u'3'],
        'nazwa':u'wyksztalcenie',
        'typ': u'C'
    },
    {
        'pytanie': u'2.1 Jakie jest rozwinięcie skrótu CVS?',
        'odpowiedzi': [u'Common Visualisation Setback ', u'Computer Vision Syndrome', u'Current Vision Status'],
        'nazwa':u'CVS1',
        'typ': u'C'
    },
    {
        'pytanie': u'2.2 Wskaż poprawną definicję syndromu widzenia komputerowego.',
        'odpowiedzi': [u'zespół zmęczenia oka spowodowany nadmierną pracą przy monitorze objawiający się uczuciem suchości oczu',
                       u'zaburzenie w pracy narządu wzroku ujawniające się poprzez problemy z postrzeganiem zmian kolorów przy dłuższej pracy przy monitorze',
                       u'wada wzroku spowodowana długotrwałą pracą przy komputerze, która cechuje się zmniejszeniem siły mięśni oka i problemami ze skupieniem wzroku'],
        'nazwa':u'CVS2',
        'typ': u'C'
    },
          {
        'pytanie': u'2.3 Jakie są grupy objawów syndromu widzenia komputerowego?',
        'odpowiedzi': [u'zaburzenia konwergencji i akomodacji, dotyczące powierzchni oka, pozaoczne',
                       u'pozaoczne, psychiczne, immunologiczne',
                       u'zaburzenia konwergencji i akomodacji, pozaoczne, zaburzenia przyswajania składników odżywczych'],
        'nazwa':u'CVS3',
        'typ': u'C'
    },
     {
        'pytanie': u'2.4  Wskaż objawy syndromu widzenia komputerowego.',
        'odpowiedzi': [u'ból głowy, ból karku, pieczenie oczu',
                       u'zmęczenie, suchość oka, senność',
                       u'zmniejszenie intensywności barw, zamazany obraz, zaczerwienienie oczu'],
        'nazwa':u'CVS4',
        'typ': u'C'
    },
      {
        'pytanie': u'2.5 Wskaż przyczyny syndromu widzenia komputerowego.',
        'odpowiedzi': [u'praca przy odległości 40 cm od monitora pozbawiona przerw',
                       u'stosowanie soczewek kontaktowych i chorowanie na retinopatię',
                       u'brak mrugania i złe oświetlenie podczas pracy z monitorem'] ,
        'nazwa':u'CVS5',
        'typ': u'C'
    },
     {
        'pytanie': u'2.6 Czy przyjmowanie dużej ilości tabletek przeciwbólowych zwiększa prawdopodobieństwo zachorowania na syndrom widzenia komputerowego?',
        'nazwa':u'CVS6',
        'typ': u'B'
    },
     {
        'pytanie': u'2.7 Czy odległość od monitora ma wpływ na występowanie syndromu widzenia komputerowego?',
        'nazwa':u'CVS7',
        'typ': u'B'
    },
     {
        'pytanie': u'2.8 Czy zaniedbania w leczeniu trimetyloaminuria (TMAU) wywołują syndrom widzenia komputerowego?',
        'nazwa':u'CVS8',
        'typ': u'B'
    },
     {
        'pytanie': u'2.9 W jaki sposób można zapobiec syndromowi widzenia komputerowego?',
        'odpowiedzi': [u'częste mruganie, szczepienie, przyjmowanie odpowiedniej ilości witaminy C',
                       u'monitor w bezpiecznej odległości od oczu, uprawianie gimnastyki oczu, zdrowy styl życia, częste mruganie',
                       u'zdrowy styl życia, używanie okularów zamiast soczewek kontaktowych, aktywność fizyczna, unikanie długiego przebywania w słońcu',
                       u'odpowiedzi A i C są poprawne'],
        'nazwa':u'CVS9',
        'typ': u'C'
    },
      {
        'pytanie': u'2.10 W jaki sposób można leczyć syndrom widzenia komputerowego?',
        'odpowiedzi': [u'używanie przepisanych przez lekarza kropli/żeli/maści nawilżającej',
                       u'rezygnacja z korzystania z urządzeń emitujących intensywne światło lub całkowita rezygnacja z korzystania z urządzeń posiadających monitor na czas leczenia ',
                       u'sumienne stosowanie się do wytycznych prawidłowej pracy z urządzeniem posiadającym monitor',
                       u'wszystkie odpowiedzi są poprawne'],
        'nazwa':u'CVS10',
        'typ': u'C'
    },
    {
        'pytanie': u'3.1 Z jakiej ilości różnych urządzeń z monitorem korzystasz? (zakres 0-10)',
        'nazwa':u'warunki1',
        'typ': u'I'

    },
    {
        'pytanie': u'3.2 Jak dużo czasu spędzasz przed monitorem?',
        'odpowiedzi': [u'mniej niż 2 godziny',
                       u'2 godziny',
                       u'5 godzin',
                       u'8 godzin',
                       u'więcej niż 8 godzin'],
        'wartosc': [u'mniej niz 2 godziny',
                       u'2 godziny',
                       u'5 godzin',
                       u'8 godzin',
                       u'wiecej niz 8 godzin'],
        'nazwa':u'warunki2',
        'typ': u'C'
    },
     {
        'pytanie': u'3.3 Z jakiej odległości patrzysz na monitor?',
        'odpowiedzi': [u'mniejszej niż 40 cm',
                       u'40-55 cm',
                       u'55-70 cm',
                       u'70-85 cm',
                       u'85-100 cm',
                       u'większej niż 100 cm'],
        'wartosc': [u'mniejszej niz 40 cm',
                       u'40-55 cm',
                       u'55-70 cm',
                       u'70-85 cm',
                       u'85-100 cm',
                       u'wiekszej niz 100 cm'],
        'nazwa':u'warunki3',
        'typ': u'C'
    },
       {
        'pytanie': u'3.4 Czy dostosowujesz ustawienia ekranu do natężenia oświetlenia pomieszczenia?',
        'nazwa':u'warunki4',
        'typ': u'B'
    },
     {
        'pytanie': u'3.5 Czy stosujesz krople do oczu?',
        'nazwa':u'warunki5',
        'typ': u'B'
    },
    {
        'pytanie': u'3.6 Czy pamiętasz o regularnym mruganiu?',
        'nazwa':u'warunki6',
        'typ': u'B'
    },
       {
        'pytanie': u'3.7 Czy robisz sobie przerwy w pracy?',
        'typ': u'B',
        'nazwa':u'przerwa1',
        'podpytanie1': u'3.7.1 Jak często sobie robisz przerwy?',
        'odpowiedzi1': [u'częściej niż co pół godziny',
                       u'co pół godziny',
                       u'co godzinę',
                       u'co półtorej godziny',
                       u'rzadziej niż co półtorej godziny'],
        'wartosc1': [u'czesciej niz co pol godziny',
                       u'co pol godziny',
                       u'co godzine',
                       u'co poltorej godziny',
                       u'rzadziej niz co poltorej godziny'],
         'nazwa1':u'przerwa2',
         'podpytanie2': u'3.7.2 Jak długo trwa twoja przerwa?',
         'odpowiedzi2': [u'poniżej 5 minut',
                       u'5 minut',
                       u'10 minut',
                       u'15 minut',
                       u'powyżej 15 minut'],
         'wartosc2': [u'ponizej 5 minut',
                       u'5 minut',
                       u'10 minut',
                       u'15 minut',
                       u'powyzej 15 minut'],
         'nazwa2':u'przerwa3',
    },
    {
        'pytanie': u'4.1 Czy po pracy przed monitorem odczuwasz któryś z tych skutków? (pytanie wielokrotnego wyboru)',
        'odpowiedzi':[u'zmęczenie',
          u'zaczerwienienie oczu',
          u'zmniejszenie intensywności barw',
          u'suchość oczu',
          u'łzawienie',
          u'ból brzucha',
          u'ból głowy',
          u'bóle stawów',
          u'zamazany obraz',
          u'nadwrażliwość na ostre światło',
          u'senność',
          u'pieczenie oczu',
          u'ból karku', ],
        'wartosc':[u'zmeczenie',
          u'zaczerwienienie oczu',
          u'zmniejszenie intensywnosci barw',
          u'suchosc oczu',
          u'lzawienie',
          u'bol brzucha',
          u'bol glowy',
          u'bole stawow',
          u'zamazany obraz',
          u'nadwrazliwosc na ostre swiatlo',
          u'sennosc',
          u'pieczenie oczu',
          u'bol karku', ],
          'nazwa':u'samopoczucie',
          'typ': u'M'
    },
    {
        'pytanie': u'5.1 Czy masz problemy ze wzrokiem?',
        'typ': u'B',
        'nazwa':u'oczy1',
        'podpytanie1': u'5.1.1 Czy nosisz soczewki kontaktowe',
        'odpowiedzi1': [u'Tak',
                       u'Nie'],
        'nazwa1':u'oczy2',
        'podpytanie2': u'5.1.2 Wybierz choroby, którą posiadasz: (pytanie wielokrotnego wyboru)',
        'odpowiedzi2': [u'nadwzroczność',
                       u'anizometropia',
                       u'krótkowzroczność',
                       u'astygmatyzm',
                       u'jaskra',
                       u'katarakta',
                       u'presbiopia',
                       u'retinopatia',],
        'wartosc2': [u'nadwzrocznosc',
                       u'anizometropia',
                       u'krotkowzrocznosc',
                       u'astygmatyzm',
                       u'jaskra',
                       u'katarakta',
                       u'presbiopia',
                       u'retinopatia',],
        'nazwa2':u'choroba',
    },
    {
        'pytanie': u'6.1 Podaj datę swojej ostatniej wizyty u specjalisty: (rrrr-mm-dd)',
        'nazwa':u'kontrola1',
         'typ': u'D'
    },
     {
        'pytanie': u'6.2 Czy podczas tej wizyty zostało u Ciebie stwierdzone pogorszenie stanu oczu?',
        'nazwa':u'kontrola2',
        'typ': u'B'
    },
]
#lista kolorow do wykresow
colors = ["#ff6961", "#aee8e4", "#fdfd96", "#ffb7ce", "#bee7a5",
    "#b39eb5", "#ffc46b", "#aa9499", "#fe9e76", "#b9789f",
    "#e9d1bf", "#ff9899", "#99c5c4", "#dea5a4", "#98b884",
    "#fed876", "#c5468a", "#deece1", "#e5d9d3", "#bcbec0"]

#funkcja sprawdzajaca procentowy wynik z quizu
def quiz(odpowiedzi):
    dobre_odp = 0
    for nazwa,odp in odpowiedzi:
        #pytania w ktorych wartosc prawidlowej odpowiedzi to 0
        if(nazwa == 'CVS8' or nazwa == 'CVS6' or nazwa == 'CVS4'  or nazwa == 'CVS3' or nazwa == 'CVS2'):
           #sprawdzanie czy odpowiedz jest poprawna
           if(int(odp) == 0):
              dobre_odp +=1
        elif(nazwa == 'CVS9' or nazwa == 'CVS7' or nazwa == 'CVS1'):
           if(int(odp) == 1):
              dobre_odp +=1
        elif(nazwa == 'CVS5'):
           if(int(odp) == 2):
               dobre_odp +=1
        elif(nazwa == 'CVS10'):
            if(int(odp) == 3):
               dobre_odp +=1
    return (dobre_odp/10)*100

#funkcja dzielaca odpowiedzi na listy w celu latwiejszej pozniejszej pracy na nich
def podzial(odpowiedzi):
     respondent_odp = ['','','','']
     quiz_odp = []
     samopoczucie_odp = []
     choroba_odp = []
     przerwa_odp = ['','','']
     stan_oczu_odp = ['','']
     wizyta_odp = ['','']
     warunki_odp = ['','','','','','']
     blad = 0
     tekst = ['','','','','']
     #dla wszystkich odpowiedzi uzytkownika odczytujemy nazwe i wartosc odpowiedzi
     for nazwa, odp in odpowiedzi.items():
            #jezeli nazwa zaczyna sie  konkretnym czlonem
            if nazwa.startswith("email"):
                #jezeli nie jest zerowa
                if len(odp) != 0:
                    #sprawdzanie poprawnosci skladni odpowiedzi
                    if(odp.endswith(".pl") or odp.endswith(".com")) and odp.find("@") != -1 and len(odp)<255:
                        respondent_odp[0]= odp
                    else:
                        #jezeli jest blad dodawany jest komunikat i wartosc bool zmienia sie na true
                        tekst[0] = "Wpisana wartość email "+odp+" nie jest adresem e-mailem lub jest zbyt długie.  "
                        blad = 1
            elif nazwa.startswith("plec"):
                     respondent_odp[1] = odp
            elif nazwa.startswith("wiek"):
                    #sprawdzanie czy odpowiedz jest liczba i czy jest w dobrym zakresie
                     if odp.isdigit()== 1 and int(odp) > 15 and int(odp) <= 35:
                           respondent_odp[2] = odp
                     else:
                       tekst[1] = "Wpisana wartość wieku "+odp+" jest spoza zakresu 16-35.   "
                       blad = 1
            elif nazwa.startswith("wyksztalcenie"):
                respondent_odp[3] = odp
            elif nazwa.startswith("CVS"):
                quiz_odp.append([nazwa, odp])
            elif nazwa.startswith("samopoczucie"):
                samopoczucie_odp.append(odp)
            elif nazwa.startswith("choroba"):
                choroba_odp.append(odp)
            elif nazwa.startswith("przerwa"):
                if nazwa.endswith("1"):
                    przerwa_odp[0] = odp
                elif nazwa.endswith("2"):
                    przerwa_odp[1] = odp
                elif nazwa.endswith("3"):
                    przerwa_odp[2] = odp
            elif nazwa.startswith("oczy"):
                if nazwa.endswith("1"):
                    stan_oczu_odp[0] = odp
                elif nazwa.endswith("2"):
                    stan_oczu_odp[1] = odp
            elif nazwa.startswith("kontrola"):
                if nazwa.endswith("1"):
                    if len(odp) != 0:
                        #zmiana typu odpowiedzi na date
                        data_wizyty = datetime.strptime(odp, '%Y-%m-%d').date()
                        #obliczenie roznicy miedzy data obecna i data z odpowiedzi
                        roznica_dat = str(datetime.now().date()- data_wizyty)
                        #jezeli wartosc jest ujemna czyli data jest z przyszlosci
                        if roznica_dat[0]=='-':
                            tekst[2] = "Wpisana data "+odp+" jeszcze nie miała miejsca.   "
                            blad = 1
                        #jezeli wartosc roznicy lat jest wieksza niz wiek respondenta
                        elif respondent_odp[2] != '' and (datetime.now().date().year - data_wizyty.year) > int(respondent_odp[2]):
                            tekst[3] = "Wpisana data "+odp+" nie pokrywa się z zadeklarowanym wiekiem.   "
                            blad = 1
                        else:
                            wizyta_odp[0] = odp
                elif nazwa.endswith("2"):
                     wizyta_odp[1] = odp
            elif nazwa.startswith("warunki"):
                if nazwa.endswith("1"):
                    #sprawdzanie czy odpowiedz jest w dobrym zakresie
                    if odp.isdigit()== 1 and int(odp) >= 0 and int(odp) <= 10:
                        warunki_odp[0] = odp
                    else:
                        tekst[4] = "Wpisana wartość liczby urządzeń  "+odp+" jest spoza zakresu 0-10.   "
                        blad = 1
                elif nazwa.endswith("2"):
                    warunki_odp[1] = odp
                elif nazwa.endswith("3"):
                    warunki_odp[2] = odp
                elif nazwa.endswith("4"):
                    warunki_odp[3] = odp
                elif nazwa.endswith("5"):
                    warunki_odp[4] = odp
                elif nazwa.endswith("6"):
                    warunki_odp[5] = odp
     #wywolanie funkcji zwracajacej wynik z quizu
     procenty = quiz(quiz_odp)
     return respondent_odp, procenty, tekst, blad, choroba_odp, samopoczucie_odp, przerwa_odp, stan_oczu_odp, wizyta_odp, warunki_odp
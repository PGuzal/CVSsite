from flask_app import db
import data as d

#klasa bedacs odpowiednikiem tabeli w bazie
class Respondent(db.Model):

    __tablename__ = 'respondent'
    #odpowiedniki kolumn w bazie
    respondent_id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), nullable=True)
    wiek = db.Column(db.Integer)
    plec = db.Column(db.String(1), nullable=True)
    stopien_studiow = db.Column(db.Integer, nullable=True)
    wiedza = db.relationship("Wiedza", uselist=False, back_populates="respondent")
    warunki = db.relationship("Warunki", uselist=False, back_populates="respondent")
    samopoczucie = db.relationship("Samopoczucie", back_populates="respondent")
    stan_oczu = db.relationship("Stan_oczu", uselist=False, back_populates="respondent")
    choroba = db.relationship("Choroba", back_populates="respondent")
    wizyta = db.relationship("Wizyta", uselist=False, back_populates="respondent")

class Warunki(db.Model):

    __tablename__ = "warunki"

    warunki_id = db.Column(db.Integer, primary_key=True)
    ilosc = db.Column(db.Integer)
    czas = db.Column(db.String, nullable=True)
    przerwy = db.Column(db.Integer, nullable=True)
    odleglosc = db.Column(db.String, nullable=True)
    oswietlenie = db.Column(db.Integer, nullable=True)
    krople = db.Column(db.Integer, nullable=True)
    mruganie = db.Column(db.Integer, nullable=True)
    respondent_id = db.Column(db.Integer, db.ForeignKey('respondent.respondent_id'))
    respondent = db.relationship("Respondent", back_populates="warunki")
    przerwa = db.relationship("Przerwa", uselist=False, back_populates="warunki")


class Wiedza(db.Model):

    __tablename__ = 'wiedza'

    wiedza_id = db.Column(db.Integer, primary_key=True)
    wynik = db.Column(db.Integer)
    respondent_id = db.Column(db.Integer, db.ForeignKey('respondent.respondent_id'))
    respondent = db.relationship("Respondent", back_populates="wiedza")

class Wizyta(db.Model):

    __tablename__ = "wizyta"

    wizyta_id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.DateTime, nullable=True)
    pogorszenie = db.Column(db.Integer, nullable=True)
    respondent_id = db.Column(db.Integer, db.ForeignKey('respondent.respondent_id'))
    respondent = db.relationship("Respondent", back_populates="wizyta")

class Choroba(db.Model):

    __tablename__ = "choroba"

    choroba_id = db.Column(db.Integer, primary_key=True)
    nazwa = db.Column(db.String(24))
    respondent_id = db.Column(db.Integer, db.ForeignKey('respondent.respondent_id'))
    respondent = db.relationship("Respondent", back_populates="choroba")

class Samopoczucie(db.Model):

    __tablename__ = "samopoczucie"

    samopoczucie_id = db.Column(db.Integer, primary_key=True)
    nazwa = db.Column(db.String(32))
    respondent_id = db.Column(db.Integer, db.ForeignKey('respondent.respondent_id'))
    respondent = db.relationship("Respondent", back_populates="samopoczucie")

class Stan_oczu(db.Model):

    __tablename__ = "stan_oczu"

    stan_oczu_id = db.Column(db.Integer, primary_key=True)
    problemy = db.Column(db.Integer, nullable=True)
    soczewki = db.Column(db.Integer, nullable=True)
    respondent_id = db.Column(db.Integer, db.ForeignKey('respondent.respondent_id'))
    respondent = db.relationship("Respondent", back_populates="stan_oczu")

class Przerwa(db.Model):

    __tablename__ = "przerwa"

    przerwa_id = db.Column(db.Integer, primary_key=True)
    czestosc = db.Column(db.String(32), nullable=True)
    dlugosc = db.Column(db.String(16), nullable=True)
    warunki_id = db.Column(db.Integer, db.ForeignKey('warunki.warunki_id'))
    warunki = db.relationship("Warunki", back_populates="przerwa")

#odczyt odpowiedzi konkretnego respondenta
def odczyt_indywidualny(id,ilosc_respondentow):
    respondent_odp = ["","",""]
    respondent = " "
    warunki = " "
    warunki_odp = ["","","",""]
    wizyta = ""
    wizyta_odp = ""
    wiedza = ""
    wiedza_odp = ""
    stan_oczu = " "
    stan_oczu_odp = ""
    choroby = ""
    choroby_odp = ["","","",""]
    samopoczucie = ""
    samopoczucie_odp = ["","","","","","","","","","",""]
    ilosc_chorob = []
    ilosc_objawow = []

    #odczyt odpowiedzi z tabeli dla konkretnego id respondenta
    respondent= Respondent.query.filter_by(respondent_id=id).first()
    respondent_odp[1] = respondent.plec
    respondent_odp[2]  = respondent.stopien_studiow
    respondent_odp[0]  = respondent.wiek

    warunki = Warunki.query.filter_by(respondent_id=id).first()
    warunki_odp[0]= warunki.ilosc
    warunki_odp[1]= warunki.czas
    warunki_odp[2]= warunki.przerwy

    wizyta = Wizyta.query.filter_by(respondent_id=id).first()
    wizyta_odp = wizyta.pogorszenie

    wiedza = Wiedza.query.filter_by(respondent_id=id).first()
    wiedza_odp = wiedza.wynik

    stan_oczu = Stan_oczu.query.filter_by(respondent_id=id).first()
    stan_oczu_odp= stan_oczu.problemy

    for i in range(ilosc_respondentow):
        ilosc_chorob.append(Choroba.query.filter_by(respondent_id = i).count())

    choroby = Choroba.query.filter_by(respondent_id=id).all()
    liczba = Choroba.query.filter_by(respondent_id=id).count()
    for i in range(liczba):
        choroby_odp[i] =  choroby[i].nazwa

    for i in range(ilosc_respondentow):
        ilosc_objawow.append(Samopoczucie.query.filter_by(respondent_id = i).count())

    #odczyt wszystkich elementow tablicy samopoczucie dla danego respondenta
    samopoczucie = Samopoczucie.query.filter_by(respondent_id=id).all()
    #liczba odpowiedzi respondenta
    liczba1 = Samopoczucie.query.filter_by(respondent_id=id).count()
    #przepisanie do listy tylko kolumny nazwa z tabeli
    for i in range(liczba1):
        samopoczucie_odp[i] =  samopoczucie[i].nazwa

    return respondent_odp, warunki_odp, wiedza_odp, wizyta_odp, stan_oczu_odp, choroby_odp, samopoczucie_odp, ilosc_chorob, ilosc_objawow

#odczyt z bazy odpowiedzi wszystkich respondentow
def odczyt_bazy():
    odliczanie = 0
    plec_wykres = []
    wyksztalczenie_wykres = []
    problemy_wykres = []
    wiedza_wykres = []
    wiek_wykres = []
    pogorszenie_wykres = []
    przerwa_wykres = []
    czas_wykres = []
    choroby_wykres = []
    samopoczucie_wykres = []
    urzadzenia_wykres = []
    urzadzenia_ilosc = []
    ilosc_respondentow = 0

    #zliczeni ilosci respondentow ktorzy udzielili danej odpowiedzi
    for odp in range(0,11):
        urzadzenia_wykres.append(Warunki.query.filter_by(ilosc = odp).count())
        urzadzenia_ilosc.append(odp)
        ilosc_respondentow += int(urzadzenia_wykres[odp])

    for odp in d.zestaw_pytan[1]['wartosc']:
        plec_wykres.append(Respondent.query.filter_by(plec = odp).count())

    for odp in d.zestaw_pytan[22]['wartosc2']:
        choroby_wykres.append(Choroba.query.filter_by(nazwa = odp).count())

    for odp in d.zestaw_pytan[21]['wartosc']:
        samopoczucie_wykres.append(Samopoczucie.query.filter_by(nazwa = odp).count())

    for odp in d.zestaw_pytan[15]['wartosc']:
        czas_wykres.append(Warunki.query.filter_by(czas = odp).count())

    for liczba in range(17,36):
        wiek_wykres.append(Respondent.query.filter_by(wiek = liczba).count())

    for liczba in range(1,4):
        wyksztalczenie_wykres.insert(liczba, Respondent.query.filter_by(stopien_studiow = liczba).count())

    for liczba in range(11):
        wiedza_wykres.insert(liczba, Wiedza.query.filter_by(wynik = odliczanie).count())
        odliczanie += 10

    for liczba in range(2):
        problemy_wykres.append(Stan_oczu.query.filter_by(problemy = liczba).count())
        pogorszenie_wykres.append(Wizyta.query.filter_by(pogorszenie= liczba).count())
        przerwa_wykres.append(Warunki.query.filter_by(przerwy = liczba).count())


    return plec_wykres, wyksztalczenie_wykres, wiedza_wykres, problemy_wykres, wiek_wykres, pogorszenie_wykres, przerwa_wykres, czas_wykres, choroby_wykres, samopoczucie_wykres, urzadzenia_wykres, urzadzenia_ilosc, ilosc_respondentow

#zapis odpowiedzi respondenta do bazy
def zapis_bazy(respondent_odp, choroba_odp, samopoczucie_odp, przerwa_odp, stan_oczu_odp, wizyta_odp, warunki_odp, procenty):
    respondent_spr=[0,0,0,0]
    przerwa_spr = [0,0]
    wizyta_spr=[0,0]
    warunki_spr=[0,0,0,0,0,0]

    #sprawdzenie na ktore pytania respondent nie udzielil odpowiedzi
    for o in range(len(respondent_odp)):
                if respondent_odp[o]!='':
                    respondent_spr[o] = 1
                else:
                    respondent_spr[o] = 0
    #zapisanie do bazy wedlug danego schematu zaleznego od odpowiedzi lub ich braku
    if respondent_spr == [1, 1, 1, 1]:
        #wywołanie z odpowiedziami respondenta klasy będącej odpowiednikiem tabeli w bazie
        nowy_respondent = Respondent(email = respondent_odp[0], wiek = int(respondent_odp[2]), plec = str(respondent_odp[1]), stopien_studiow = int(respondent_odp[3]))
    elif respondent_spr == [1, 1, 1, 0]:
        nowy_respondent = Respondent(email = respondent_odp[0], wiek = int(respondent_odp[2]), plec = str(respondent_odp[1]))
    elif respondent_spr == [1, 0, 1, 1]:
        nowy_respondent = Respondent(email = respondent_odp[0], wiek = int(respondent_odp[2]), stopien_studiow = int(respondent_odp[3]))
    elif respondent_spr == [1, 0, 1, 0]:
        nowy_respondent = Respondent(email = respondent_odp[0], wiek = int(respondent_odp[2]))
    elif respondent_spr == [0, 1, 1, 1]:
        nowy_respondent = Respondent(wiek = int(respondent_odp[2]), plec = str(respondent_odp[1]), stopien_studiow = int(respondent_odp[3]))
    elif respondent_spr == [0, 1, 1, 0]:
        nowy_respondent = Respondent(wiek = int(respondent_odp[2]), plec = str(respondent_odp[1]))
    elif respondent_spr == [0, 0, 1, 1]:
        nowy_respondent = Respondent(wiek = int(respondent_odp[2]), stopien_studiow = int(respondent_odp[3]))
    else:
        nowy_respondent = Respondent(wiek = int(respondent_odp[2]))
    #wstawienie danych do bazy
    db.session.add(nowy_respondent)
    #zamknięcie sesji bazy
    db.session.commit()

    wiedza = Wiedza(wynik = procenty, respondent_id = nowy_respondent.respondent_id)
    db.session.add(wiedza)
    db.session.commit()

    for o in range(len(wizyta_odp)):
        if wizyta_odp[o]!='':
            wizyta_spr[o] = 1
        else:
            wizyta_spr[o] = 0
    if wizyta_spr == [1, 1]:
        nowa_wizyta = Wizyta(data = wizyta_odp[0], pogorszenie = wizyta_odp[1], respondent_id = nowy_respondent.respondent_id)
    elif wizyta_spr == [1, 0]:
        nowa_wizyta = Wizyta(data = wizyta_odp[0], respondent_id = nowy_respondent.respondent_id)
    elif wizyta_spr == [0, 1]:
        nowa_wizyta = Wizyta(pogorszenie = wizyta_odp[1], respondent_id = nowy_respondent.respondent_id)
    else:
        nowa_wizyta = Wizyta(respondent_id = nowy_respondent.respondent_id)
    db.session.add(nowa_wizyta)
    db.session.commit()

    for ch_odp in choroba_odp:
        nowa_choroba = Choroba(nazwa = ch_odp, respondent_id = nowy_respondent.respondent_id )
        db.session.add(nowa_choroba)
        db.session.commit()

    for sam_odp in samopoczucie_odp:
        nowe_samopoczucie = Samopoczucie(nazwa = sam_odp, respondent_id = nowy_respondent.respondent_id )
        db.session.add(nowe_samopoczucie)
        db.session.commit()

    for o in range(len(warunki_odp)):
        if warunki_odp[o]!='':
            warunki_spr[o] = 1
        else:
            warunki_spr[o] = 0
    if przerwa_odp[0]!='':
        warunki_spr.insert(2, 1)
    else:
        warunki_spr.insert(2, 0)
    if warunki_spr == [1, 1, 1, 1, 1, 1, 1]:
        nowe_warunki = Warunki(ilosc = warunki_odp[0], czas= warunki_odp[1], przerwy = przerwa_odp[0], odleglosc = warunki_odp[2], oswietlenie = warunki_odp[3], krople = warunki_odp[4], mruganie = warunki_odp[5], respondent_id = nowy_respondent.respondent_id)
    elif warunki_spr == [1, 1, 1, 1, 1, 1, 0]:
        nowe_warunki = Warunki(ilosc = warunki_odp[0], czas= warunki_odp[1], przerwy = przerwa_odp[0], odleglosc = warunki_odp[2], oswietlenie = warunki_odp[3], krople = warunki_odp[4], respondent_id = nowy_respondent.respondent_id)
    elif warunki_spr == [1, 1, 1, 1, 1, 0, 1]:
        nowe_warunki = Warunki(ilosc = warunki_odp[0], czas= warunki_odp[1], przerwy = przerwa_odp[0], odleglosc = warunki_odp[2], oswietlenie = warunki_odp[3], mruganie = warunki_odp[5], respondent_id = nowy_respondent.respondent_id)
    elif warunki_spr == [1, 1, 1, 1, 1, 0, 0]:
        nowe_warunki = Warunki(ilosc = warunki_odp[0], czas= warunki_odp[1], przerwy = przerwa_odp[0], odleglosc = warunki_odp[2], oswietlenie = warunki_odp[3], respondent_id = nowy_respondent.respondent_id)
    elif warunki_spr == [1, 1, 1, 1, 0, 1, 1]:
        nowe_warunki = Warunki(ilosc = warunki_odp[0], czas= warunki_odp[1], przerwy = przerwa_odp[0], odleglosc = warunki_odp[2], krople = warunki_odp[4], mruganie = warunki_odp[5], respondent_id = nowy_respondent.respondent_id)
    elif warunki_spr == [1, 1, 1, 1, 0, 1, 0]:
        nowe_warunki = Warunki(ilosc = warunki_odp[0], czas= warunki_odp[1], przerwy = przerwa_odp[0], odleglosc = warunki_odp[2], krople = warunki_odp[4], respondent_id = nowy_respondent.respondent_id)
    elif warunki_spr == [1, 1, 1, 1, 0, 0, 1]:
        nowe_warunki = Warunki(ilosc = warunki_odp[0], czas= warunki_odp[1], przerwy = przerwa_odp[0], odleglosc = warunki_odp[2], mruganie = warunki_odp[5], respondent_id = nowy_respondent.respondent_id)
    elif warunki_spr == [1, 1, 1, 1, 0, 0, 0]:
        nowe_warunki = Warunki(ilosc = warunki_odp[0], czas= warunki_odp[1], przerwy = przerwa_odp[0], odleglosc = warunki_odp[2], respondent_id = nowy_respondent.respondent_id)
    elif warunki_spr == [1, 1, 1, 0, 1, 1, 1]:
        nowe_warunki = Warunki(ilosc = warunki_odp[0], czas= warunki_odp[1], przerwy = przerwa_odp[0], oswietlenie = warunki_odp[3], krople = warunki_odp[4], mruganie = warunki_odp[5], respondent_id = nowy_respondent.respondent_id)
    elif warunki_spr == [1, 1, 1, 0, 1, 1, 0]:
        nowe_warunki = Warunki(ilosc = warunki_odp[0], czas= warunki_odp[1], przerwy = przerwa_odp[0], oswietlenie = warunki_odp[3], krople = warunki_odp[4], respondent_id = nowy_respondent.respondent_id)
    elif warunki_spr == [1, 1, 1, 0, 1, 0, 1]:
        nowe_warunki = Warunki(ilosc = warunki_odp[0], czas= warunki_odp[1], przerwy = przerwa_odp[0], oswietlenie = warunki_odp[3], mruganie = warunki_odp[5], respondent_id = nowy_respondent.respondent_id)
    elif warunki_spr == [1, 1, 1, 0, 1, 0, 0]:
        nowe_warunki = Warunki(ilosc = warunki_odp[0], czas= warunki_odp[1], przerwy = przerwa_odp[0], oswietlenie = warunki_odp[3], respondent_id = nowy_respondent.respondent_id)
    elif warunki_spr == [1, 1, 1, 0, 0, 1, 1]:
        nowe_warunki = Warunki(ilosc = warunki_odp[0], czas= warunki_odp[1], przerwy = przerwa_odp[0], krople = warunki_odp[4], mruganie = warunki_odp[5], respondent_id = nowy_respondent.respondent_id)
    elif warunki_spr == [1, 1, 1, 0, 0, 1, 0]:
        nowe_warunki = Warunki(ilosc = warunki_odp[0], czas= warunki_odp[1], przerwy = przerwa_odp[0], krople = warunki_odp[4], respondent_id = nowy_respondent.respondent_id)
    elif warunki_spr == [1, 1, 1, 0, 0, 0, 1]:
        nowe_warunki = Warunki(ilosc = warunki_odp[0], czas= warunki_odp[1], przerwy = przerwa_odp[0], mruganie = warunki_odp[5], respondent_id = nowy_respondent.respondent_id)
    elif warunki_spr == [1, 1, 1, 0, 0, 0, 0]:
        nowe_warunki = Warunki(ilosc = warunki_odp[0], czas= warunki_odp[1], przerwy = przerwa_odp[0], respondent_id = nowy_respondent.respondent_id)
    elif warunki_spr == [1, 1, 0, 1, 1, 1, 1]:
        nowe_warunki = Warunki(ilosc = warunki_odp[0], czas= warunki_odp[1], odleglosc = warunki_odp[2], oswietlenie = warunki_odp[3], krople = warunki_odp[4], mruganie = warunki_odp[5], respondent_id = nowy_respondent.respondent_id)
    elif warunki_spr == [1, 1, 0, 1, 1, 1, 0]:
        nowe_warunki = Warunki(ilosc = warunki_odp[0], czas= warunki_odp[1], odleglosc = warunki_odp[2], oswietlenie = warunki_odp[3], krople = warunki_odp[4], respondent_id = nowy_respondent.respondent_id)
    elif warunki_spr == [1, 1, 0, 1, 1, 0, 1]:
        nowe_warunki = Warunki(ilosc = warunki_odp[0], czas= warunki_odp[1], odleglosc = warunki_odp[2], oswietlenie = warunki_odp[3], mruganie = warunki_odp[5], respondent_id = nowy_respondent.respondent_id)
    elif warunki_spr == [1, 1, 0, 1, 1, 0, 0]:
        nowe_warunki = Warunki(ilosc = warunki_odp[0], czas= warunki_odp[1], odleglosc = warunki_odp[2], oswietlenie = warunki_odp[3], respondent_id = nowy_respondent.respondent_id)
    elif warunki_spr == [1, 1, 0, 1, 0, 1, 1]:
        nowe_warunki = Warunki(ilosc = warunki_odp[0], czas= warunki_odp[1], odleglosc = warunki_odp[2], krople = warunki_odp[4], mruganie = warunki_odp[5], respondent_id = nowy_respondent.respondent_id)
    elif warunki_spr == [1, 1, 0, 1, 0, 1, 0]:
        nowe_warunki = Warunki(ilosc = warunki_odp[0], czas= warunki_odp[1], odleglosc = warunki_odp[2], krople = warunki_odp[4], respondent_id = nowy_respondent.respondent_id)
    elif warunki_spr == [1, 1, 0, 1, 0, 0, 1]:
        nowe_warunki = Warunki(ilosc = warunki_odp[0], czas= warunki_odp[1], odleglosc = warunki_odp[2], mruganie = warunki_odp[5], respondent_id = nowy_respondent.respondent_id)
    elif warunki_spr == [1, 1, 0, 1, 0, 0, 0]:
        nowe_warunki = Warunki(ilosc = warunki_odp[0], czas= warunki_odp[1], odleglosc = warunki_odp[2], respondent_id = nowy_respondent.respondent_id)
    elif warunki_spr == [1, 1, 0, 0, 1, 1, 1]:
        nowe_warunki = Warunki(ilosc = warunki_odp[0], czas= warunki_odp[1], oswietlenie = warunki_odp[3], krople = warunki_odp[4], mruganie = warunki_odp[5], respondent_id = nowy_respondent.respondent_id)
    elif warunki_spr == [1, 1, 0, 0, 1, 1, 0]:
        nowe_warunki = Warunki(ilosc = warunki_odp[0], czas= warunki_odp[1], oswietlenie = warunki_odp[3], krople = warunki_odp[4], respondent_id = nowy_respondent.respondent_id)
    elif warunki_spr == [1, 1, 0, 0, 1, 0, 1]:
        nowe_warunki = Warunki(ilosc = warunki_odp[0], czas= warunki_odp[1], oswietlenie = warunki_odp[3], mruganie = warunki_odp[5], respondent_id = nowy_respondent.respondent_id)
    elif warunki_spr == [1, 1, 0, 0, 1, 0, 0]:
        nowe_warunki = Warunki(ilosc = warunki_odp[0], czas= warunki_odp[1], oswietlenie = warunki_odp[3], respondent_id = nowy_respondent.respondent_id)
    elif warunki_spr == [1, 1, 0, 0, 0, 1, 1]:
        nowe_warunki = Warunki(ilosc = warunki_odp[0], czas= warunki_odp[1], krople = warunki_odp[4], mruganie = warunki_odp[5], respondent_id = nowy_respondent.respondent_id)
    elif warunki_spr == [1, 1, 0, 0, 0, 1, 0]:
        nowe_warunki = Warunki(ilosc = warunki_odp[0], czas= warunki_odp[1], krople = warunki_odp[4], respondent_id = nowy_respondent.respondent_id)
    elif warunki_spr == [1, 1, 0, 0, 0, 0, 1]:
        nowe_warunki = Warunki(ilosc = warunki_odp[0], czas= warunki_odp[1], mruganie = warunki_odp[5], respondent_id = nowy_respondent.respondent_id)
    elif warunki_spr == [1, 1, 0, 0, 0, 0, 0]:
        nowe_warunki = Warunki(ilosc = warunki_odp[0], czas= warunki_odp[1], respondent_id = nowy_respondent.respondent_id)
    elif warunki_spr == [1, 0, 1, 1, 1, 1, 1]:
        nowe_warunki = Warunki(ilosc = warunki_odp[0], przerwy = przerwa_odp[0], odleglosc = warunki_odp[2], oswietlenie = warunki_odp[3], krople = warunki_odp[4], mruganie = warunki_odp[5], respondent_id = nowy_respondent.respondent_id)
    elif warunki_spr == [1, 0, 1, 1, 1, 1, 0]:
        nowe_warunki = Warunki(ilosc = warunki_odp[0], przerwy = przerwa_odp[0], odleglosc = warunki_odp[2], oswietlenie = warunki_odp[3], krople = warunki_odp[4], respondent_id = nowy_respondent.respondent_id)
    elif warunki_spr == [1, 0, 1, 1, 1, 0, 1]:
        nowe_warunki = Warunki(ilosc = warunki_odp[0], przerwy = przerwa_odp[0], odleglosc = warunki_odp[2], oswietlenie = warunki_odp[3], mruganie = warunki_odp[5], respondent_id = nowy_respondent.respondent_id)
    elif warunki_spr == [1, 0, 1, 1, 1, 0, 0]:
        nowe_warunki = Warunki(ilosc = warunki_odp[0], przerwy = przerwa_odp[0], odleglosc = warunki_odp[2], oswietlenie = warunki_odp[3], respondent_id = nowy_respondent.respondent_id)
    elif warunki_spr == [1, 0, 1, 1, 0, 1, 1]:
        nowe_warunki = Warunki(ilosc = warunki_odp[0], przerwy = przerwa_odp[0], odleglosc = warunki_odp[2], krople = warunki_odp[4], mruganie = warunki_odp[5], respondent_id = nowy_respondent.respondent_id)
    elif warunki_spr == [1, 0, 1, 1, 0, 1, 0]:
        nowe_warunki = Warunki(ilosc = warunki_odp[0], przerwy = przerwa_odp[0], odleglosc = warunki_odp[2], krople = warunki_odp[4], respondent_id = nowy_respondent.respondent_id)
    elif warunki_spr == [1, 0, 1, 1, 0, 0, 1]:
        nowe_warunki = Warunki(ilosc = warunki_odp[0], przerwy = przerwa_odp[0], odleglosc = warunki_odp[2], mruganie = warunki_odp[5], respondent_id = nowy_respondent.respondent_id)
    elif warunki_spr == [1, 0, 1, 1, 0, 0, 0]:
        nowe_warunki = Warunki(ilosc = warunki_odp[0], przerwy = przerwa_odp[0], odleglosc = warunki_odp[2], respondent_id = nowy_respondent.respondent_id)
    elif warunki_spr == [1, 0, 1, 0, 1, 1, 1]:
        nowe_warunki = Warunki(ilosc = warunki_odp[0], przerwy = przerwa_odp[0], oswietlenie = warunki_odp[3], krople = warunki_odp[4], mruganie = warunki_odp[5], respondent_id = nowy_respondent.respondent_id)
    elif warunki_spr == [1, 0, 1, 0, 1, 1, 0]:
        nowe_warunki = Warunki(ilosc = warunki_odp[0], przerwy = przerwa_odp[0], oswietlenie = warunki_odp[3], krople = warunki_odp[4], respondent_id = nowy_respondent.respondent_id)
    elif warunki_spr == [1, 0, 1, 0, 1, 0, 1]:
        nowe_warunki = Warunki(ilosc = warunki_odp[0], przerwy = przerwa_odp[0], oswietlenie = warunki_odp[3], mruganie = warunki_odp[5], respondent_id = nowy_respondent.respondent_id)
    elif warunki_spr == [1, 0, 1, 0, 1, 0, 0]:
        nowe_warunki = Warunki(ilosc = warunki_odp[0], przerwy = przerwa_odp[0], oswietlenie = warunki_odp[3], respondent_id = nowy_respondent.respondent_id)
    elif warunki_spr == [1, 0, 1, 0, 0, 1, 1]:
        nowe_warunki = Warunki(ilosc = warunki_odp[0], przerwy = przerwa_odp[0], krople = warunki_odp[4], mruganie = warunki_odp[5], respondent_id = nowy_respondent.respondent_id)
    elif warunki_spr == [1, 0, 1, 0, 0, 1, 0]:
        nowe_warunki = Warunki(ilosc = warunki_odp[0], przerwy = przerwa_odp[0], krople = warunki_odp[4], respondent_id = nowy_respondent.respondent_id)
    elif warunki_spr == [1, 0, 1, 0, 0, 0, 1]:
        nowe_warunki = Warunki(ilosc = warunki_odp[0], przerwy = przerwa_odp[0], mruganie = warunki_odp[5], respondent_id = nowy_respondent.respondent_id)
    elif warunki_spr == [1, 0, 1, 0, 0, 0, 0]:
        nowe_warunki = Warunki(ilosc = warunki_odp[0], przerwy = przerwa_odp[0], respondent_id = nowy_respondent.respondent_id)
    elif warunki_spr == [1, 0, 0, 1, 1, 1, 1]:
        nowe_warunki = Warunki(ilosc = warunki_odp[0], odleglosc = warunki_odp[2], oswietlenie = warunki_odp[3], krople = warunki_odp[4], mruganie = warunki_odp[5], respondent_id = nowy_respondent.respondent_id)
    elif warunki_spr == [1, 0, 0, 1, 1, 1, 0]:
        nowe_warunki = Warunki(ilosc = warunki_odp[0], odleglosc = warunki_odp[2], oswietlenie = warunki_odp[3], krople = warunki_odp[4], respondent_id = nowy_respondent.respondent_id)
    elif warunki_spr == [1, 0, 0, 1, 1, 0, 1]:
        nowe_warunki = Warunki(ilosc = warunki_odp[0], odleglosc = warunki_odp[2], oswietlenie = warunki_odp[3], mruganie = warunki_odp[5], respondent_id = nowy_respondent.respondent_id)
    elif warunki_spr == [1, 0, 0, 1, 1, 0, 0]:
        nowe_warunki = Warunki(ilosc = warunki_odp[0], odleglosc = warunki_odp[2], oswietlenie = warunki_odp[3], respondent_id = nowy_respondent.respondent_id)
    elif warunki_spr == [1, 0, 0, 1, 0, 1, 1]:
        nowe_warunki = Warunki(ilosc = warunki_odp[0], odleglosc = warunki_odp[2], krople = warunki_odp[4], mruganie = warunki_odp[5], respondent_id = nowy_respondent.respondent_id)
    elif warunki_spr == [1, 0, 0, 1, 0, 1, 0]:
        nowe_warunki = Warunki(ilosc = warunki_odp[0], odleglosc = warunki_odp[2], krople = warunki_odp[4], respondent_id = nowy_respondent.respondent_id)
    elif warunki_spr == [1, 0, 0, 1, 0, 0, 1]:
        nowe_warunki = Warunki(ilosc = warunki_odp[0], odleglosc = warunki_odp[2], mruganie = warunki_odp[5], respondent_id = nowy_respondent.respondent_id)
    elif warunki_spr == [1, 0, 0, 1, 0, 0, 0]:
        nowe_warunki = Warunki(ilosc = warunki_odp[0], odleglosc = warunki_odp[2], respondent_id = nowy_respondent.respondent_id)
    elif warunki_spr == [1, 0, 0, 0, 1, 1, 1]:
        nowe_warunki = Warunki(ilosc = warunki_odp[0], oswietlenie = warunki_odp[3], krople = warunki_odp[4], mruganie = warunki_odp[5], respondent_id = nowy_respondent.respondent_id)
    elif warunki_spr == [1, 0, 0, 0, 1, 1, 0]:
        nowe_warunki = Warunki(ilosc = warunki_odp[0], oswietlenie = warunki_odp[3], krople = warunki_odp[4], respondent_id = nowy_respondent.respondent_id)
    elif warunki_spr == [1, 0, 0, 0, 1, 0, 1]:
        nowe_warunki = Warunki(ilosc = warunki_odp[0], oswietlenie = warunki_odp[3], mruganie = warunki_odp[5], respondent_id = nowy_respondent.respondent_id)
    elif warunki_spr == [1, 0, 0, 0, 1, 0, 0]:
        nowe_warunki = Warunki(ilosc = warunki_odp[0], oswietlenie = warunki_odp[3], respondent_id = nowy_respondent.respondent_id)
    elif warunki_spr == [1, 0, 0, 0, 0, 1, 1]:
        nowe_warunki = Warunki(ilosc = warunki_odp[0], krople = warunki_odp[4], mruganie = warunki_odp[5], respondent_id = nowy_respondent.respondent_id)
    elif warunki_spr == [1, 0, 0, 0, 0, 1, 0]:
        nowe_warunki = Warunki(ilosc = warunki_odp[0], krople = warunki_odp[4], respondent_id = nowy_respondent.respondent_id)
    elif warunki_spr == [1, 0, 0, 0, 0, 0, 1]:
        nowe_warunki = Warunki(ilosc = warunki_odp[0], mruganie = warunki_odp[5], respondent_id = nowy_respondent.respondent_id)
    else:
        nowe_warunki = Warunki(ilosc = warunki_odp[0], respondent_id = nowy_respondent.respondent_id)

    db.session.add(nowe_warunki)
    db.session.commit()

    if stan_oczu_odp[0] == '1':
        nowy_stan_oczu = Stan_oczu(problemy = stan_oczu_odp[0], soczewki = stan_oczu_odp[1], respondent_id = nowy_respondent.respondent_id)
    else:
        nowy_stan_oczu = Stan_oczu(problemy = stan_oczu_odp[0], respondent_id = nowy_respondent.respondent_id)
    db.session.add(nowy_stan_oczu)
    db.session.commit()

    if przerwa_odp[0] == '1':
        for o in range(1, len(przerwa_odp)):
            if przerwa_odp[o]!='':
                przerwa_spr[o-1] = 1
            else:
                przerwa_spr[o-1] = 0
        if przerwa_spr == [1, 1]:
            nowa_przerwa = Przerwa(czestosc = przerwa_odp[1], dlugosc = przerwa_odp[2], warunki_id = nowe_warunki.warunki_id)
        elif przerwa_spr == [1, 0]:
            nowa_przerwa = Przerwa(czestosc = przerwa_odp[1], warunki_id = nowe_warunki.warunki_id)
        elif przerwa_spr == [0, 1]:
            nowa_przerwa = Przerwa(dlugosc = przerwa_odp[2], warunki_id = nowe_warunki.warunki_id)
        else:
            nowa_przerwa = Przerwa(warunki_id = nowe_warunki.warunki_id)
        db.session.add(nowa_przerwa)
        db.session.commit()

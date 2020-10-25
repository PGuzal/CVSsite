from flask import Flask # do aplikacji
from flask import render_template, request, redirect, url_for, flash # do aplikacji
from flask_sqlalchemy import SQLAlchemy # do bazy danych
import data as d
import statistic_data as sd

app = Flask(__name__)

# instancja bazy
SQLALCHEMY_DATABASE_URI = "mysql+mysqlconnector://PatrycjaRAIM:projektbaza@PatrycjaRAIM.mysql.pythonanywhere-services.com/PatrycjaRAIM$odpowiedziCVS".format(
    username="the username from the 'Databases' tab",
    password="the password you set on the 'Databases' tab",
    hostname="the database host address from the 'Databases' tab",
    databasename="the database name you chose, probably yourusername$odpowiedziCVS",
)
app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI
app.config["SQLALCHEMY_POOL_RECYCLE"] = 299
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

# konfiguracja aplikacji
app.config.update(dict(
    SECRET_KEY='bradzosekretnawartosc',
))

from models import odczyt_bazy, zapis_bazy, odczyt_indywidualny

@app.route('/end')
def end():
    #wywołanie formularza strony
    return render_template('end.html')

@app.route('/statistic', methods=['GET','POST'])
def statistic():
    dane_plec, dane_wyksztalcenie, dane_wiedza, dane_problemy, dane_wiek, dane_pogorszenie, dane_przerwa, dane_czas, dane_choroba, dane_samopoczucie, dane_urzadzenia, urzadzenia_ilosc, ilosc_respondentow = odczyt_bazy()
    #wartosci na wykres
    wartosc_wyksztalcenie = dane_wyksztalcenie
    wartosc_pogorszenie = dane_pogorszenie
    wartosc_przerwa = dane_przerwa
    wartosc_plec = dane_plec
    wartosc_wiek = dane_wiek
    wartosc_wiedza = dane_wiedza
    wartosc_problemy = dane_problemy
    wartosc_czas = dane_czas
    wartosc_choroba = dane_choroba
    wartosc_samopoczucie = dane_samopoczucie
    wartosc_urzadzenia = dane_urzadzenia
    #podpis do "legendy"
    legenda_bool =["Nie","Tak"]
    legenda_plec = d.zestaw_pytan[1]['wartosc']
    legenda_wiek = ["17","18","19","20","21","22","23","24","25","26","27","28","29","30","31","32","33","34","35"]
    legenda_wyksztalcenie = d.zestaw_pytan[3]['odpowiedzi']
    legenda_wiedza = ["0%","10%","20%","30%","40%","50%","60%","70%","80%","90%","100%"]
    legenda_czas = d.zestaw_pytan[15]['odpowiedzi']
    legenda_choroba = d.zestaw_pytan[22]['odpowiedzi2']
    legenda_samopoczucie = d.zestaw_pytan[21]['odpowiedzi']
    legenda_urzadzenia = urzadzenia_ilosc
    #jezeli ktos wpisał id i przechodzi na statystyki indywidualne
    if request.method == 'POST':
        dane = request.form
        id = 0
        for nazwa, wartosc in dane.items():
            if nazwa == 'id_respondent':
               id = wartosc
        return redirect(url_for('statistic_individual', dane = id))
    return render_template('statistic.html', max=100, plec=zip(wartosc_plec, legenda_plec, d.colors),
                           wiedza = zip(wartosc_wiedza, legenda_wiedza, d.colors),
                           wyksztalcenie = zip(wartosc_wyksztalcenie, legenda_wyksztalcenie, d.colors),
                           wiek = zip(wartosc_wiek, legenda_wiek, d.colors),
                           problemy = zip(wartosc_problemy, legenda_bool, d.colors),
                           pogorszenie = zip(wartosc_pogorszenie, legenda_bool, d.colors),
                           przerwa = zip(wartosc_przerwa, legenda_bool, d.colors),
                           czas = zip(wartosc_czas, legenda_czas, d.colors),
                           choroba = zip(wartosc_choroba, legenda_choroba, d.colors),
                           samopoczucie = zip(wartosc_samopoczucie, legenda_samopoczucie, d.colors),
                           urzadzenia = zip(wartosc_urzadzenia, legenda_urzadzenia, d.colors))

@app.route('/statistic_individual/<dane>')
def statistic_individual(dane):
    #pobranie danych do obliczeń procentowych i wykresów
    dane_plec, dane_wyksztalcenie, dane_wiedza, dane_problemy, dane_wiek, dane_pogorszenie, dane_przerwa, dane_czas, dane_choroba, dane_samopoczucie, dane_urzadzenia, urzadzenia_ilosc, ilosc_respondentow= odczyt_bazy()
    respondent_odp, warunki_odp, wiedza_odp, wizyta_odp, stan_oczu_odp, choroby_odp, samopoczucie_odp, ilosc_chorob, ilosc_objawow = odczyt_indywidualny(dane,ilosc_respondentow)
    legenda_bool =["Nie","Tak"]
    wiek_wartosci =  [17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35]
    wiedza_wartosci = [0,10,20,30,40,50,60,70,80,90,100]
    urzadzenia_wartosci  =[0,1,2,3,4,5,6,7,8,9,10]
    #procenty do wypisania
    plec_procenty = sd.procent_plec(respondent_odp[1], dane_plec)
    wyksztalcenie_procenty, tekst = sd.procent_wyksztalcenie(respondent_odp[2], dane_wyksztalcenie)
    wiek_procenty = sd.procent_liczby(respondent_odp[0], dane_wiek,wiek_wartosci)
    ilosc_procenty = sd.procent_liczby(warunki_odp[0], dane_urzadzenia,urzadzenia_wartosci)
    wiedza_procenty = sd.procent_liczby(wiedza_odp, dane_wiedza,wiedza_wartosci)
    czas_procenty = sd.procent_czas(warunki_odp[1], dane_czas)
    przerwy_procenty, odp_przerwa = sd.procent_bool(warunki_odp[2], dane_przerwa,0)
    pogorszenie_procenty, odp_pogorszenie = sd.procent_bool(wizyta_odp, dane_pogorszenie,0)
    stan_oczu_procenty, odp_problemy = sd.procent_bool(stan_oczu_odp, dane_problemy,1)
    objawy_procenty, odp_objawy = sd.procent_wielokrotnego(samopoczucie_odp,dane_samopoczucie, ilosc_objawow)
    choroby_procenty, odp_choroby = sd.procent_wielokrotnego(choroby_odp, dane_choroba, ilosc_chorob)
    #dane do wykresów
    wartosc_plec_id, legenda_plec_id= sd.wykres_wiele(dane_plec,respondent_odp[1],d.zestaw_pytan[1]['wartosc'],d.zestaw_pytan[1]['odpowiedzi'])
    wartosc_wiek_id, legenda_wiek_id = sd.wykres_liczby(dane_wiek,respondent_odp[0], wiek_wartosci)
    wartosc_wyksztalcenie_id, legenda_wyksztalcenie_id= sd.wykres_wiele(dane_wyksztalcenie,str(respondent_odp[2]),d.zestaw_pytan[3]['wartosc'],d.zestaw_pytan[3]['odpowiedzi'])
    wartosc_problemy_id, legenda_problemy_id = sd.wykres_dwie(dane_problemy,stan_oczu_odp,legenda_bool)
    wartosc_pogorszenie_id, legenda_pogorszenie_id= sd.wykres_dwie(dane_pogorszenie,wizyta_odp,legenda_bool)
    wartosc_przerwa_id, legenda_przerwa_id = sd.wykres_dwie(dane_przerwa,warunki_odp[2],legenda_bool)
    wartosc_wiedza_id, legenda_wiedza_id = sd.wykres_liczby(dane_wiedza,wiedza_odp,wiedza_wartosci)
    wartosc_urzadzenia_id, legenda_urzadzenia_id= sd.wykres_liczby(dane_urzadzenia,warunki_odp[0],urzadzenia_wartosci)
    wartosc_czas_id, legenda_czas_id= sd.wykres_wiele(dane_czas,warunki_odp[1],d.zestaw_pytan[15]['wartosc'],d.zestaw_pytan[15]['odpowiedzi'])
    #dodanie % do wartości wiedzy na wykresie
    for i in range(len(legenda_wiedza_id)):
        legenda_wiedza_id[i] = str(legenda_wiedza_id[i])+"%"

    return render_template('statistic_individual.html', max=100, plec_procent = plec_procenty,
                           wyksztalcenie_procent = wyksztalcenie_procenty , tekst = tekst, wiek_procent = wiek_procenty,
                           urzadzenia_procenty = ilosc_procenty, urzadzenie_resp = warunki_odp[0],
                           wiedza_procent = wiedza_procenty, wiedza_resp = wiedza_odp,
                           czas_procent = czas_procenty, czas_resp = warunki_odp[1],
                           przerwy_procent = przerwy_procenty, przerwy_resp = odp_przerwa,
                           pogorszenie_procent = pogorszenie_procenty, pogorszenie_resp = odp_pogorszenie,
                           stan_oczu_procent = stan_oczu_procenty, problemy_resp = odp_problemy,
                           objawy_procent = objawy_procenty, objawy_resp = odp_objawy,
                           choroby_procent = choroby_procenty, choroby_resp = odp_choroby,
                           problemy = zip(wartosc_problemy_id, legenda_problemy_id, d.colors),
                           pogorszenie = zip(wartosc_pogorszenie_id, legenda_pogorszenie_id, d.colors),
                           przerwa = zip(wartosc_przerwa_id, legenda_przerwa_id, d.colors),
                           wiek = zip(wartosc_wiek_id, legenda_wiek_id, d.colors),
                           plec=zip(wartosc_plec_id, legenda_plec_id, d.colors),
                           wiedza = zip(wartosc_wiedza_id, legenda_wiedza_id, d.colors),
                           wyksztalcenie = zip(wartosc_wyksztalcenie_id, legenda_wyksztalcenie_id, d.colors),
                           czas = zip(wartosc_czas_id, legenda_czas_id, d.colors),
                           urzadzenia = zip(wartosc_urzadzenia_id, legenda_urzadzenia_id, d.colors)
                           )


@app.route('/', methods=['GET', 'POST'])
def main():
    return render_template('main.html')

@app.route('/form', methods=[ 'GET','POST'])
def form():
    blad = 0
    #jezeli zostalo przeslane cos z formularza
    if request.method == 'POST':
        odpowiedzi = request.form
        #wywolanie funkcji podzialu na listy z odpowiedziami
        respondent_odp, procenty, tekst, blad, choroba_odp, samopoczucie_odp, przerwa_odp, stan_oczu_odp, wizyta_odp, warunki_odp  = d.podzial(odpowiedzi)
        #jezeli wszystko bylo wypelnione we wlasciwy sposob
        if blad == 0:
           zapis_bazy(respondent_odp, choroba_odp, samopoczucie_odp, przerwa_odp, stan_oczu_odp, wizyta_odp, warunki_odp, procenty)
           return redirect(url_for('end'))
        #jezeli nie wszystko bylo wypelnione we wlasciwy sposob
        else:
            #komunikat z bledem
            flash(u'{0}'.format(tekst[0]+tekst[1]+tekst[2]+tekst[3]+tekst[4]+"Niestety musisz wypełnić ankietę ponownie."))
            return redirect(url_for('form'))
    return render_template('form.html', pytania=d.zestaw_pytan)



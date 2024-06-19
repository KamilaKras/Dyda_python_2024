import datetime
import os
import traceback

import flask

from pogoda import *
from register import *

# Inicjalizacjia
app = flask.Flask(
    __name__,

    # Gdzie znajduja sie tempalty
    template_folder='templates',

    # Gdzie znajduja sie style
    static_folder='static',
)

app.secret_key = os.urandom(12)



@app.route('/')
def test2():
  return "hej hej hej razy "

# ładowanie template'u z html
@app.route('/strona_startowa')
def test3():
  return flask.render_template('home.html')

# możliwość zwracania tagów html
@app.route('/hej')
def test4():
  return "<h1> hej hej <h1> <br> <ul> <li> raz </li> <li> dwa </li> </ul> </br>"

# przekazywanie parametrow
@app.route('/powitanie/<name>')
def powitaj(name):
  return "Witaj" + " " + str(name)


# Zapisywanie do pliku
filename_powitanie = "powitania.txt"


#mnozenie\
@app.route('/mnozenie/<int:a>/<int:b>')
def mnozenie(a,b):
  wynik = str(a*b)
  return f"Wynik to {wynik}"


@app.route('/powitanie_zapis/<imie>')
def powitanie(imie):
  with open(filename_powitanie, "a") as writer:
    now = datetime.datetime.now()
    writer.writelines(imie + "," + str(now) + "\n")
  return "Witaj" + " " + str(imie)


# Proste przechwytywanie sesji
@app.route('/loguj_sesja')
def template_sesja():
  # session["logged_in"] = True
  flask.session['logged_in'] = False
  if flask.session.get("logged_in"):
    return flask.render_template("frontpage.html")
  else:
    return "Uzytkownik niezalogowany"

# Wylogowywanie
@app.route('/loguj_wyloguj')
def template_loguj_wyloguj():
    flask.session['logged_in'] = True
    if flask.session.get("logged_in"):
        return flask.render_template("frontpage2.html")
    else:
        return "Uzytkownik niezalogowany"

# Ścieżka taka sama jak w template po a href
@app.route('/wyloguj')
def wyloguj():
    flask.session['logged_in'] = False
    return "Wylogowano"

# Logowanie z formularzem, input - miejsce, gdzie uzytkownik coś wpisuje w formularzu
# w template w form action podajemy link, który mówi co się stanie jak kliknę przycisk submit

@app.route('/logowanie_z_formularzem')
def logowanie_z_folmularzem():
    return flask.render_template('logowanie.html')

# @app.route('/login', methods=["POST"])
# def login_user():
#   if request.form['password'] == "password" and request.form[
#       'username'] == "user":
#     session["logged_in"] = True
#     return render_template("frontpage.html")
#   else:
#     flash("wrong password")
#     return render_template("logowanie.html")

# Rejestracja użytkownika
@app.route('/signup', methods=["GET"])
def return_registrationpage():
  return flask.render_template('signup.html')



@app.route('/register', methods=["POST"])
def do_register():
  POST_USERNAME = str(flask.request.form['username'])
  POST_PASSWORD = str(flask.request.form['password'])

  sqlsession = return_sqlalchemysession()
  user = User(POST_USERNAME, POST_PASSWORD)

  sqlsession.add(user)
  sqlsession.commit()
  sqlsession.close()
  return test3()

#Interaktywne logowanie
@app.route('/home')
def home():
  if not flask.session.get('logged_in'):
    return flask.render_template('logowanie.html')
  else:
    return flask.render_template('frontpage2.html')


@app.route('/login', methods=["POST"])
def login_user_extended():
  POST_USERNAME = str(flask.request.form['username'])
  POST_PASSWORD = str(flask.request.form['password'])

  #Stworz obiekt sesji SQLalchemy (ORM)
  sqlsession = return_sqlalchemysession()

  # Zadaj zapytanie w sposob bezpieczny
  # od sqlinjection
  # query = sqlsession.query(User).filter(User.username.in_([POST_USERNAME]))
  query = sqlsession.query(User).filter(User.username == POST_USERNAME)

  #wez 1 uzytkownika z takim nickiem (zakladamy ze nie ma powtorek)
  user = query.first()
  try:
    #Ta linia musi być w try, bo jeżeli nie ma usera (user==None) to nie zadziała user.check_password

    if user.password == POST_PASSWORD:
      flask.session['logged_in'] = True
      # return render_template('frontpage.html')

    else:
      # Jak działa flash: https://flask.palletsprojects.com/en/1.1.x/patterns/flashing/
      flask.flash('No user or wrong password provided')
      return flask.render_template('logowanie.html')
  except AttributeError as e:
    flask.flash('No user or wrong password provided')
    #traceback trick to printout the error despite the except
    print(traceback.format_exc())

  return home()

@app.route("/pogoda")
def pokazpogode():
  temp, humid, weathertype, rain = pobierzpogode()
  return flask.render_template("pogoda.html",
                               temp=temp,
                               humid=humid,
                               weathertype=weathertype,
                               rain=rain)

if __name__ == "__main__":
  app.run()

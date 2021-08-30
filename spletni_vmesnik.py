import bottle
import shranjevalnik


shranjevalnik = shranjevalnik.Shranjevalnik()

@bottle.get("/stili/<filename>")
def stili(filename):
  return bottle.static_file(filename, "static")

@bottle.get("/")
def domov():
  name = bottle.request.get_cookie('Name')
  return bottle.template("templates/domov.html", name=name)

@bottle.get("/registracija")
def registracija():
  return bottle.template("templates/registracija.html")

@bottle.post("/registracija")
def nov_uporabnik():
  ime = bottle.request.forms.get("ime")
  priimek = bottle.request.forms.get("priimek")
  starost = bottle.request.forms.get("starost")
  opis = bottle.request.forms.get("opis")
  instagram = bottle.request.forms.get("instagram")
  
  podatki = {"ime":ime, "priimek":priimek, "opis":opis, "starost":starost, "instagram":instagram}
  
  napaka = shranjevalnik.preveri_podatke(podatki)

  if napaka:
    return bottle.template("templates/napaka.html", sporocilo=napaka)
  
  shranjevalnik.dodaj_uporabnika(podatki)
  return bottle.redirect("/osebe")

@bottle.get("/osebe")
def osebe():
  return bottle.template("templates/osebe.html", podatki=shranjevalnik.podatki)


bottle.run(host="0.0.0.0", port=8080, debug=True)

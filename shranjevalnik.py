import json

class Shranjevalnik():
  def __init__(self):
    datoteka = open("podatki.json", "r")
    self.podatki = json.load(datoteka)
    datoteka.close()
    
  def preveri_podatke(self, uporabnik):
    if not uporabnik["ime"].isalpha() or uporabnik["ime"] == "":
      return "Napaka pri vnosu imena"
    if not uporabnik["priimek"].isalpha() or uporabnik["priimek"] == "" :
      return "Napaka pri vnosu priimka"
    if uporabnik["starost"] == "" or not uporabnik["starost"].isnumeric() or int(uporabnik["starost"]) < 12:
      return "Napaka pri vnosu starosti, starost mora biti številka, stari morate biti vsaj 12 let"
    if uporabnik["opis"] == "":
      return "Napaka pri vnosu opisa"
    if uporabnik["instagram"] == "" or uporabnik["instagram"][0] != "@":
      return "Napaka pri vnosu instagram imena - ime se mora zaceti z znakom @"
    
    return None

  def dodaj_uporabnika(self, uporabnik):
    self.podatki.append(uporabnik)
    self.shrani_podatke()

  def shrani_podatke(self):
    print(self.podatki)
    datoteka = open("podatki.json", "w")
    json.dump(self.podatki, datoteka)
    datoteka.close()
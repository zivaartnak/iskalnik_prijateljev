from shranjevalnik import Shranjevalnik

shranjevalnik = Shranjevalnik()

print("Dobrodosli v tekstovnem vmesniku, kjer lahko sami sebe dodate med uporabnike aplikacije za spoznavanje")

while True:
  ime = input("Vpišite vaše ime: ")
  priimek = input("Vpišite vas priimek: ")
  starost = input("Vpišite vašo starost: ")
  opis = input("Povejte nekaj o sebi: ")
  instagram = input("Vnesite svoje instagram uporabniško ime, začnite z '@': ")


  podatki = {"ime":ime, "priimek":priimek, "opis":opis, "starost":starost, "instagram":instagram}

  napaka = shranjevalnik.preveri_podatke(podatki)
  if napaka:
    print(napaka)
  else:
    break

print("Uspešno ste dodani med uporabnike!")

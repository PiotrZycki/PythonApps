import math
import random

wartosc = 100
dodawanie = wartosc + 123.15
potega = dodawanie**12
tekst = str(potega)
wartosc_pi = math.pi
losowa = random.choice([1,2,3,4,5])

tekst = f"Wartosc: {tekst}"
print("Dlugosc zmiennej tekst: " + str(len(tekst)))
print("Wykorzystanie wycinkow: " + tekst[1:4])
print(dir(tekst))
tekst = tekst.upper()
#tekst[2] = "p"


lista = list(tekst)
lista = lista[0:8]
print(lista)
print(dir(list))

lista.append([1,2,3,4,5])
print(lista)
lista.remove(":")
print(lista)


lista2 = [1,2,3,"banan",100]
lista3 = []
for a in lista2:
    if a != "banan":
        lista3.append(a**2)
print(lista3)

lista4 = [*range(2,17,2)]
print(lista4)

ja = {
    'imie': 'Piotr',
    'nazwisko': 'Zycki',
    'wiek': 22,
    'rodzice': [ {'imie': 'Danuta', 'nazwisko': 'Pedziwiatr'}, {'imie': 'Andrzej', 'nazwisko': 'Zycki'}]
}

print(ja['rodzice'])
print(ja['rodzice'][0]['imie'])
print(ja.keys())
if "rodzenstwo" in ja:
    print(True)
else:
    print(False)


krotka1 = (1, 2, "3", 4.2, 5)
print(len(krotka1))
print(krotka1[0])
print(dir(tuple))
print(krotka1.count(2))
#krotka1[0] = 2
lista5 = list(krotka1)
lista5[0] = 2
krotka1 = tuple(lista5)
print(krotka1)


X = set("kalarepa")
Y = set("lepy")
print(X & Y)


#import this
#6
dane = (2024, 'Python', 3.8)
rok, jezyk, wersja = dane
print(rok, jezyk, wersja)

#7
oceny = [4,3,5,2,5,4]
pierwsza, *srodek, ostatnia = oceny
print(pierwsza, srodek, ostatnia)

#8
info = ('Jan', 'Kowalski', 30, 'Polska', 'programista')
imie, nazwisko, zawod, *_ = info
print(imie, nazwisko, zawod)

#9
dane = (2024, ['Python', 3.8, ('Stabilna', 'Wersja')])
rok = dane[0]
jezyk = dane[1][0]
wersja = dane[1][1]
opis = dane[1][2]
print(rok, jezyk, wersja, opis)

#10
a = b = [1,2,3]
b[0] = 'zmieniono'
print(a, b)

#11
c = a[:]
c[0] = 'nowa wartosc'
print(a,b,c)

#12
x = y = 10
y += 1
print(x, y)

#13
K = [1,2]
L = K
K = K + [3,4]
M = [1,2]
N = M
M += [3,4]
print(K,L,M,N)

#14
imiona = ['Anna', 'Jan', 'Ewa']
oceny = [5,4,3,6]
aaa = zip(imiona, oceny)
for i in aaa:
    print(i)

#15
liczby = [1,2,3,4,5]
def kwadrat(x):
    return x**2

bbb = map(kwadrat, liczby)
for i in bbb:
    print(i)

#16
def zmien_wartosc(arg):
    if(isinstance(arg, list)):
        arg[0] = 'kalafior'
    elif(isinstance(arg, int)):
        arg = 65482652

aa = 1
bb = [1,2,3]
zmien_wartosc(aa)
zmien_wartosc(bb)
print(aa,bb)

#17
def zamowienie_produktu(nazwa_produktu, cena = 0, ilosc = 0):
    return 'Zamowienie: ' + nazwa_produktu + ', ' + str(round(cena*ilosc,2)) + ' zl, ' + str(ilosc) +' szt'

suma = 0
ddd = []
for d in ['cukier', 'chleb', 'sol']:
    ddd.append(zamowienie_produktu(d, (1.3*len(d)+0.99), len(d)))
    

print(ddd[0].split(',')[1].strip().split(' ')[0])
#print(ddd)

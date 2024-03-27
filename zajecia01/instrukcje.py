#1
imiona = ["Alicja", "Miłosz", "Piotr", "Oskar", "Jan", "Tadeusz", "Karol"]

for a, b in enumerate(imiona):
    print(str(a) + ". " + b)

#2a
liczba1 = float(input("Wprowadź liczbę: "))
if (liczba1>0) & (liczba1%2==0):
    print("Liczba jest dodatnia i parzysta")
else:
    print("nie.")

#2b
liczba2 = float(input("Wprowadź liczbę: "))
if liczba2!=0:
    print("Liczba jest rozna od zera")
else:
    print("nie!")

#2c
owoc = input("Wprowadź nazwę owoca: ")
if owoc in ["banan", "cytryna", "kiwi"]:
    print("Owoc jest dostępny")
else:
    print("nie e")

#3
suma = 0
while suma<=100:
    liczba3 = float(input("Wprowadź liczbę: "))
    suma = suma + liczba3

print(f"Suma wprowadzonych liczb: {suma}")



#praca z plikami
with open('example.txt', 'r') as file: 
    content = file.read() 
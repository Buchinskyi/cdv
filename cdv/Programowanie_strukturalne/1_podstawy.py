print("cdv")
print(2)
#NSJDKIW
potega = 2 ** 10
print (potega)
tekst = "CDV"
print(tekst * 2)


#pobieranie dannyck z klawiatury
imie = input()
print("Twoje imię podane z klawiatury: " + imie)
nazwisko = input()
print("Twoje imię podane z klawiatury: " + imie + ", twoje nazwisko: " + nazwisko)


dlugosc = len(nazwisko)
print(type(nazwisko)) #string
print(type(dlugosc)) #integer
print("Długość nazwiska: " , dlugosc)
dlugosc = str(dlugosc)
print("Długość nazwiska: " + dlugosc)


#użytkownik wpisuje z klawiatury swój wiek, wyświetl dane w formacie: Twój wiek:....lat
print("\nPodaj swój wiek: ", end="")
wiek = input()
print("Twoj wiek: " + wiek + " lat")


nazwisko = "Buchynskyi"
pierwszyZnak = nazwisko[0]
print(pierwszyZnak)
ostatniZnak = nazwisko[len(nazwisko) - 1]
print(ostatniZnak)
ostatniZnak = nazwisko[-1]
print(ostatniZnak)


#konwersja
x = "5"
print(type(x)) #str
x = int(x)
print(type(x)) #int


y = 4
print(type(y)) #int
y = y / 2
print(type(y)) #float
print(y) #2.0


wiek = 21
print("Twój wiek: " , wiek)


nazwisko = "Buchinskiy"
print(nazwisko[0]) #B
print(nazwisko[0:3]) #Buc
print(nazwisko[-2]) #i druga od końca
print(nazwisko[-2:]) #iy
print(nazwisko[0:-2]) #Bez dwóch ostatnich
print(nazwisko[0:-2:2]) #Bcisi






print()

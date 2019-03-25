tekst = "Anna, Paweł, Tomek"

tab = tekst.split(", ")
print(tekst)
print(tab)


imie1 = tab[0]
print(imie1) #Anna


imieDuze = imie1.upper()
print(imieDuze)

imieMale = imie1.lower()
print(imieMale)


#sprawdzanie zawartośći
nazwisko = input()
zawartosc = nazwisko.isalpha()
print(zawartosc)


imie = "Julia"
print("\nDane użytkownika \n Masz na imię: ", imie)


text1 = "Vlad\n"
text2 = "Buchinskiy\n"
print(text1 + text2)

text = text1.rstrip()
print(text1 + text2)
print(text1 + " " + text2)

#Wyświetlenie łańcuchów znaków

#Wszystkie wersje Pythona
text = "%s, Java i %s" % ("PHP", "PHYTON")
print(text)

#nowsze wersje Pythona >2.6
text = "{0}, Java i {1}".format("PHP", "PHYTON")
print(text)


#help(text.replace)

newText = text.replace("PHP", "C#")
print(newText)


#wypisanie danych
rok = 2019
miesiac = "marzec"
dzien = 25

print("Data: ", end="")
print(dzien, miesiac, rok, sep="-")










print()

import random
import string
from itertools import count
from operator import index

# # kintamieji
# # uzduotis 1
# vardas = 'Jenna'
# pavard = 'Ortega'
# result = vardas + ' ' + pavard
# print(result)

# uzduotis 2

# vardas = 'Jenna'
# vardas = vardas.upper()
# pavard = 'Ortega'
# pavard = pavard.lower()
# result = vardas + ' ' + pavard
# print(result)
#
# # uzduotis 3
# vardas = 'Jenna'
# pavard = 'Ortega'
# three = vardas[:3] + pavard[:3]
# print(three)

# # uzduotis 4

# vardas = 'Jenna'
# pavard = 'Ortega'
# three = vardas[-3:] + pavard[-3:]
# print(three)

# # uzduotis 5

# filmas = 'An American in Paris'
# naujas = filmas.replace('A', '*')
# naujas2 = naujas.replace('a', '*')
# print(naujas2)

# # uzduotis 6

# filmas = 'An American in Paris'
# print(filmas.translate({ord(i): None for i in 'AaEeIiOoUuYy'}))
# filmas2 = "Breakfast at Tiffany's"
# print(filmas2.translate({ord(i): None for i in 'AaEeIiOoUuYy'}))
# filmas3 = "2001: A Space Odyssey"
# print(filmas3.translate({ord(i): None for i in 'AaEeIiOoUuYy'}))
# filmas4 = "It's a Wonderful Life"
# print(filmas4.translate({ord(i): None for i in 'AaEeIiOoUuYy'}))
#

# uzduotis 7

# starWars = "Star Wars: Episode " + ("" * random.randint(1, 9)) + str(random.randint(1, 7)) + " - A New Hope"
# print(starWars)
# print(starWars[19])
#
#
# uzduotis 8

# filmas = "Don't Be a Menace to South Central While Drinking Your Juice in the Hood"
# raides = list(map(len, filmas.split()))
# print(raides)
# print(raides.count(5) + raides.count(4) + raides.count(3) + raides.count(2) + raides.count(1))
# filmas2 = "Tik nereikia gąsdinti Pietų Centro, geriant sultis pas save kvartale"
# raides2 = list(map(len, filmas2.split()))
# print(raides2)
# print(raides2.count(5) + raides2.count(4) + raides2.count(3) + raides2.count(2) + raides2.count(1))

# uzduotis 9

# pirmas = random.choice(string.ascii_lowercase)
# antras = random.choice(string.ascii_lowercase)
# trecias = random.choice(string.ascii_lowercase)
# print(pirmas + antras + trecias)

# uzduotis 10

# filmas = ["Don't", "Be", "a", "Menace", "to", "South", "Central", "While", "Drinking", "Your", "Juice", "in", "the", "Hood"]
# filmas2 = ["Tik", "nereikia", "gąsdinti", "Pietų Centro,", "geriant", "sultis", "pas", "save", "kvartale"]
# vienas = random.sample(filmas, 5)
# antras = random.sample(filmas2, 5)
# eilute = vienas + antras
# print(' '.join(eilute))
#

# sarasai
# uzduotis 1
#
# vardai = ['Monika', 'Naglis', 'Miksas', 'Pupa']
# print(' '.join(vardai))
# print('vardu kiekis:', len(vardai))
# print('pirmas vardas:', vardai[0])
# print('paskutinis vardas:', vardai[len(vardai) - 1])

# uzduotis 2

# ugiai = ['200 cm', '187 cm', '165 cm', '150 cm', '190 cm', '155 cm', '172 cm']
# print(' '.join(ugiai))
# print('ugiu kiekis:', len(ugiai))

# uzduotis 3

# pazymiai = [8, 7, 9, 9, 8]
# print(pazymiai)
# while True:
#     user_input = input("Ar norite ivesti daugiau pazymiu? (taip/ne): ")
#     if user_input.lower() in ["taip", "t"]:
#         print("Iveskite pazymi:")
#         naujas = int(input())
#         pazymiai.append(naujas)
#     elif user_input.lower() in ["ne", "n"]:
#         average = round(sum(pazymiai) / len(pazymiai), 2)
#         print("Visi pazymiai:", pazymiai)
#         print('Pazymiu vidurkis:', average)
#         break
#     else:
#         print("Neteisingas pasirinkimas, irasykite TAIP arba NE")

# uzduotis 4

# miestai = ['Vilnius', 'Kaunas', 'Klaipeda']
# miestai.append('Marijampole')
# miestai.extend(['Sakiai', 'Jurbarkas'])
# print(miestai)
# print("Iveskite miesta:")
# naujas = input()
# miestai.append(naujas)
# print(miestai)
# print("Iveskite miesta:")
# naujas2 = input()
# print('Iveskite pozicijos numeri kur prideti irasyta miesta i sarasa:')
# pozicija = int(input())
# miestai.insert(pozicija - 1, naujas2)
# print(miestai)

# uzduotis 5

# salys = []
# salys.extend(['Lietuva', 'Latvija', 'Estija', 'USA', 'Peru'])
# salys.append('Norvegija')
# print(salys)
# salys.pop()
# salys.pop()
# print(salys)
# print('Irasykite skaiciu kiek dar pasalinti duomenu:')
# skaicius = int(input())
# del salys[0:skaicius]
# print(salys)

# uzduotis 6

# salys = ['Lietuva', 'Latvija', 'Estija', 'USA', 'Peru', 'Norvegija']
# print(salys)
# if len(salys) > 5:
#     salys.clear()
#     print(salys)
# else:
#     print(salys)
#
# uzduotis 7

# zodziai = ['Lietuva', 'Latvija', 'Estija', 'USA', 'Peru', 'Norvegija', 'Geles', 'Vartai', 'Mokykla']
# print("Iveskite zodi paieskai:")
# naujas = input()
# try:
#     print('Zodis sarase uzima', zodziai.index(naujas) + 1, 'vieta')
# except ValueError:
#     print("That item does not exist")

# uzduotis 8

# pazymiai = [8, 7, 9, 9, 8, 10, 8, 10]
# print(pazymiai)
# while True:
#     user_input = input("Ar norite ivesti daugiau pazymiu? (taip/ne): ")
#     if user_input.lower() in ["taip", "t"]:
#         print("Iveskite pazymi:")
#         naujas = int(input())
#         pazymiai.append(naujas)
#     elif user_input.lower() in ["ne", "n"]:
#         kiekis = pazymiai.count(10)
#         print("Visi pazymiai:", pazymiai)
#         print('Desimtuku kiekis:', kiekis)
#         break
#     else:
#         print("Neteisingas pasirinkimas, irasykite TAIP arba NE")

# uzduotis 9
#
# auto = ['Audi', 'BMW', 'Subaru', 'Wolksvagen', 'Kia', 'Citroen', 'Nissan']
# print(auto)
# auto.sort()
# print(auto)
# auto.reverse()
# print(auto)

# uzduotis 10
# pazymiai = []
# pazymiai.extend([8, 7, 9, 9, 8, 10, 8, 10])
# print(pazymiai)
# pazymiai.sort(reverse=True)
# print('Trys didziausi pazymiai:', pazymiai[0], pazymiai[1], pazymiai[2])

# uzuotis 11

pazymiai = []
pazymiai.extend([8, 7, 9, 9, 8, 10, 8, 10, 4, 3, 10, 2, 1])
print(pazymiai)
if 1 or 2 or 3 or 4 in pazymiai:
    print('Mokinys turi', pazymiai.count(1) + pazymiai.count(2) + pazymiai.count(3) + pazymiai.count(4), 'neigiamus pazymius')
else:
    print("Neigiamu pazymiu nera")

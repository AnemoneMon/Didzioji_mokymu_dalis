import math
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

# pazymiai = []
# pazymiai.extend([8, 7, 9, 9, 8, 10, 8, 10, 4, 3, 10, 2, 1])
# print(pazymiai)
# if 1 or 2 or 3 or 4 in pazymiai:
#     print('Mokinys turi', pazymiai.count(1) + pazymiai.count(2) + pazymiai.count(3) + pazymiai.count(4), 'neigiamus pazymius')
# else:
#     print("Neigiamu pazymiu nera")

# uzduotis 12

# pazymiai = [8, 7, 9, 9, 8, 10, 8, 10, 4, 3, 10, 2, 1]
# print(pazymiai)
# print(pazymiai[0:3])
# print(pazymiai[3:5])
# print(pazymiai[-4:])
# print(pazymiai[2:14:2])
# pazymiai.sort(reverse=True)
# print(pazymiai)

# uzduotis 13

# vidurkiai = ['8.5', '9', '8.3', '7.5', '8', '9.1', '6.6', '7.2']
# print(vidurkiai)
# vidurkiai.sort(reverse=True)
# print(vidurkiai)
# maxtrys = [vidurkiai[0], vidurkiai[1], vidurkiai[2]]
# print(maxtrys)

# uzduotis 14

# zodynas = ['lape', 'katinas', 'medis']
# zodynas.sort()
# print(zodynas)
# while True:
#     user_input = input("Ar norite ivesti daugiau duomenu? (taip/ne): ")
#     if user_input.lower() in ["taip", "t"]:
#         print('Iveskite nauja zodi:')
#         naujas = input()
#         zodynas.append(naujas)
#         zodynas.sort()
#         print(zodynas)
#     elif user_input.lower() in ["ne", "n"]:
#         zodynas.sort()
#         print(zodynas)
#         break
#     else:
#         print(zodynas)

# uzduotis 15

# likuciai = []
# likuciai.append(['Dviraciai', 20])
# likuciai.append(['Batai', 30])
# likuciai.append(['Kojines', 10])
# print(likuciai)

# uzduotis 16

# listas = []
# listas.extend(['Lietuva', 'Latvija', 'Estija', 'USA', 'Peru', 'Norvegija', 'Geles', 'Vartai', 'Mokykla'])
# print(', '.join(listas))
# print('|'.join(listas))
# print(' '.join(listas))

# uzduotis 17

# a, b, *other = ['Python', 'Desktop', 'Project1', 'Project2', 'Project3']
# print('Naudojama programavimo kalba:', a)
# print('Dirbama su:', b)
# print('Projektu pavadinimai:', other)

# ciklai
# uzduotis 1
#
# for var in range(5):
#     print('Monika')

# Uzduotis 2

# kiekis = 11
# for i in range(kiekis):
#     print(i)

# uzduotis 3

# kiekis = 16
# for i in range(kiekis):
#     if i % 2 == 0:
#         continue
#     print(i)

# uzduotis 4

# for i in range(0, 21, 3):
#     print(f'[{i}]')

# uzduotis 5

# kiekis = 21
# for i in range(kiekis):
#     if i % 4 == 0:
#         print(i)

# uzduotis 6

# for i in range(1, 16):
#     if i % 2 == 0:
#         print(i, 'yra lyginis')
#     else:
#         print(i, 'yra nelyginis')

# uzduotis 7

# pradzia, pabaiga = 5, 30
# if pradzia < pabaiga:
#     for i in range(pradzia, pabaiga + 1):
#         print(i, i*i)

# uzduotis 8
#
# pradzia, pabaiga = 5, 30
# if pradzia < pabaiga:
#     for i in range(pradzia, pabaiga + 1):
#         if i % 2 == 1 or i % 8 == 0:
#             print(i, 'yra nelyginis arba dalinasi is 8')

# uzduotis 9

# print('Iveskite savo varda')
# naujas = input()
# for i in range(len(naujas)):
#     print('Labas', naujas)

# uzduotis 10

# for i in [88, 65, 21, 26, 47]:
#     if i % 2 == 0:
#         print(i)

# uzduotis 11
#
# print('Iveskite reziu pradzia:')
# pradzia = int(input())
# print('Iveskite reziu pabaiga:')
# pabaiga = int(input())
# print('Iveskite norima zingsni (skaiciais)')
# zingsnis = int(input())
# print('Irasykite norite matyti lyginius ar nelyginius skaicius (rasyti l arba n)')
# arlyg = input()
# print(pradzia, pabaiga, zingsnis)
# if pradzia < pabaiga:
#     for i in range(pradzia, pabaiga, zingsnis):
#             if arlyg in 'l':
#                  if i % 2 == 0:
#                     print(i)
#             else:
#                 if i % 2 == 1:
#                     print(i)

# uzduotis 12
#
# simb = '*'
# print("iveskite eiluciu kieki:")
# skaicius = int(input())
# for i in range(0, skaicius + 1):
#     print(simb * i)
#

# uzduotis 13

# print("Iveskite zodi:")
# zodis = input()

# uzduotis 14

# print("iveskite pirma skaiciu:")
# skaicius = int(input())
# print("iveskite antra skaiciu:")
# skaicius2 = int(input())
#
# def multiply(x, y):
#     if y < 0:
#         return -multiply(x, -y)
#     elif y == 0:
#         return 0
#     elif y == 1:
#         return x
#     else:
#         return x + multiply(x, y - 1)
#
# print('Ivestu skaiciu sandauga:')
# print(multiply(skaicius, skaicius2))

# uzduotis 15

# suma = 0
# for i in range(100):
#     suma += i
# print(f'gauta suma: {suma}')


# uzduotis 16
#
# suma = 0
# for i in range(20,50):
#     if i % 2 == 0:
#         suma += i
# print(f'lyginiu nuo 20 iki 50 suma: {suma}')

# uzduotis 17

# suma = 0
# for i in range(30,60):
#     if i % 2 == 1:
#         suma += i
# print(f'nelyginiu nuo 30 iki 60 suma: {suma}')

# uzduotis 18

# suma = 0
# sarasas = []
# for i in range(1000):
#     if i % 3 == 0 or i % 5 == 0:
#         sarasas.append(i)
#         suma += i
# print(f'Visi skaičiai mažesni už 1000 ir kurie dalinasi iš 3 arba 5 yra: {sarasas}')
# print(f'skaiciu suma yra: {suma}')


# --------------------------------------
# ciklai 2
# 3 uzduotis
#
# augalai = ['roze', 'tulpe', 'azuolas', 'pluke', 'lelija', 'berzas', 'uosis', 'egle', 'dilgele', 'liepa']
# print(', '.join(augalai))

# 4 uzduotis
#
# index = 0
#
# while index < len(augalai):
#     print(augalai[index])
#     index += 1
#
# # 5 uzduotis
#
# index = 9
#
# while index < len(augalai) + 1:
#     print(augalai[index])
#     index -= 1
#     if index == 0:
#         break

# -------------------------------------------------------------------
# ciklas while

# Uzduotis 1

# skaicius = 1
# while skaicius < 21:
#     print(skaicius)
#     skaicius += 1

# Uzduotis 2

# skaicius = 1
# while skaicius < 51:
#     if skaicius % 2 == 0:
#         print(skaicius, 'lyginis')
#         skaicius += 1
#     else:
#         print(skaicius, 'nelyginis')
#         skaicius += 1

# Uzduotis 3

# skaicius = 25
# while skaicius < 51:
#     if skaicius % 3 == 0:
#         print('dalinasi is 3')
#         skaicius += 1
#     else:
#         print(skaicius)
#         skaicius += 1

# Uzduotis 4

# skaicius = 1
# while skaicius < 100:
#     print(skaicius)
#     skaicius += 1
#     if skaicius == 7:
#         break

# Uzduotis 5

# skaicius = 1
# while skaicius < 1000:
#     print(skaicius)
#     skaicius += 1
#     if skaicius % 3 == 0 and skaicius % 5 == 0:
#         break

# Uzduotis 6

# print('Iveskite reziu pradzia:')
# pradzia = int(input())
# print('Iveskite reziu pabaiga:')
# pabaiga = int(input())
# if pradzia > pabaiga:
#     print('Klaida, neteisingi reziai, pradzia turi buti mazesne uz pabaiga! Iveskite is naujo.')
#     print('Iveskite reziu pradzia:')
#     pradzia = int(input())
#     print('Iveskite reziu pabaiga:')
#     pabaiga = int(input())
#     while pradzia < pabaiga:
#         continue
# for i in range(pradzia, pabaiga + 1):
#     if i % 2 == 0:
#         lyg = 'Lyginis'
#     else:
#         lyg = 'Nelyginis'
#     print(f'{i} {lyg}, skaiciaus kvadratas: {i * i}')

# uzduotis 7

# primes = []
# for possiblePrime in range(1, 30):
#     # Assume number is prime until shown it is not.
#     isPrime = True
#     for num in range(2, possiblePrime):
#         if possiblePrime % num == 0:
#             isPrime = False
#     if isPrime:
#         primes.append(possiblePrime)
#         if possiblePrime > 20:
#             break
# print(primes)

# uzduotis 8

# skaiciai = []
# while True:
#     print('Iveskite betkoki skaiciu:')
#     sk = int(input())
#     skaiciai.append(sk)
#     if sk == 0:
#         break
# print('Ivestu skaiciu suma:', sum(skaiciai))

# uzduotis 9

# while True:
#     print('Iveskite pirma skaiciu:')
#     sk = int(input())
#     print('Iveskite antra skaiciu:')
#     sk2 = int(input())
#     print('Irasykite norima veiksma - sudetis, atimtis, daugyba ar dalyba:')
#     veiksmas = input()
#     if veiksmas == 'sudetis':
#         print(sk, '+', sk2, '=', sk + sk2)
#     if veiksmas == 'atimtis':
#         print(sk, '-', sk2, '=', sk - sk2)
#     if veiksmas == 'daugyba':
#         print(sk, '*', sk2, '=', sk * sk2)
#     if veiksmas == 'dalyba':
#         print(sk, '/', sk2, '=', sk / sk2)
#     user_input = input('Ar norite pakartoti is naujo? (taip/ne): ')
#     if user_input.lower() in ["taip", "t"]:
#         continue
#     elif user_input.lower() in ["ne", "n"]:
#         break

# uzduotis 10

# while True:
#     print('Iveskite skaiciu:')
#     sk = int(input())
#     for i in range(1, 10):
#         print(sk, '*', i, '=', i * sk)
#     user_input = input('Ar norite pakartoti is naujo? (taip/ne): ')
#     if user_input.lower() in ["taip", "t"]:
#         continue
#     elif user_input.lower() in ["ne", "n"]:
#         break

# uzduotis 11

# skaiciai = []
# while True:
#     print('Iveskite betkoki skaiciu:')
#     sk = int(input())
#     skaiciai.append(sk)
#     if sk == 0 or sk == -1:
#         break
# print('Ivestu skaiciu suma:', sum(skaiciai))
# print('Ivestu skaiciu vidurkis:', sum(skaiciai)/len(skaiciai))

# uzduotis 12

# pazymiai = []
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
# while True:
#     user_input2 = input("Ar norite ivesti pazymius kitam mokiniui? (taip/ne): ")
#     if user_input2.lower() in ["taip", "t"]:
#         pazymiai.clear()
#         print("Iveskite pazymi:")
#         naujas = int(input())
#         pazymiai.append(naujas)
#         while True:
#             user_input = input("Ar norite ivesti daugiau pazymiu? (taip/ne): ")
#             if user_input.lower() in ["taip", "t"]:
#                 print("Iveskite pazymi:")
#                 naujas = int(input())
#                 pazymiai.append(naujas)
#             else:
#                 average = round(sum(pazymiai) / len(pazymiai), 2)
#                 print("Visi pazymiai:", pazymiai)
#                 print('Pazymiu vidurkis:', average)
#                 break
#     elif user_input2.lower() in ["ne", "n"]:
#         break

# 11 tema lists

# 18 uzduotis

# sarasas = [['Monika', 'Skinkaityte'], ['Ruta', 'Viskantaite']]
# sarasas.append(['Saulius', 'Dziugelis'])
# print('Prie projekto dirba sie komandos nariai:')
# i = 0
# while i < len(sarasas):
#     print(' '.join(sarasas[i]))
#     i += 1

# 20 uzduotis

# sarasas = ['Psichologija', 'Matematika', 'Medicina', 'Inzinerija']
# print('Studiju programu sarasas:')
# i = 0
# while i < len(sarasas):
#     print(''.join(sarasas[i]))
#     i += 1

# 21 uzduotis

# sarasas = []
# sarasas.extend(['Lietuva', 'Latvija', 'Estija'])
# i = 0
# while i < len(sarasas):
#     print('Salis:',''.join(sarasas[i]))
#     i += 1

# 22 uzduotis

# sarasas = []
# sarasas.extend(['Sampunas', 'Bulves', 'Miltai'])
# i = 0
# while i < len(sarasas):
#     print('Preke nr', i + 1, ''.join(sarasas[i]))
#     i += 1

# 24 uzduotis

# print('Iveskite skaiciu kieki:')
# sk = int(input())
# saras = random.sample(range(0, 1000), sk)
# print(saras)
# i = 0
# while i < len(saras):
#     print(saras[i], 'kvadratas:', saras[i] * saras[i])
#     i += 1

# 25 uzduotis

# saras = ['Psichologija', 'Matematika', 'Medicina', 'Inzinerija', 'Fizika', 'Filosofija']
# print(' '.join(saras))
# saras[0] = 'Pakeistas'
# saras[2] = 'Pakeistas2'
# saras[4] = 'Pakeistas3'
# print(' '.join(saras))
#
# listai continued

# uzduotis 26

# skaiciai = [1,2,3,4,5,6,7,8,9,10]
# print('Lyginiai skaiciai:')
# for a in skaiciai:
#     if a % 2 == 0:
#         print(a)
# print('Neyginiai skaiciai:')
# for b in skaiciai:
#     if b % 2 == 1:
#         print(b)
# print('Dalinasi is 3:')
# for c in skaiciai:
#     if c % 3 == 0:
#         print(c)

# uzduotis 27

# skaiciai = []
# for a in range(10):
#     skaiciai.append(random.randint(1, 100))
# print(skaiciai)
# print('Vidurkis:', sum(skaiciai)/len(skaiciai))
# print('Skaiciai didesni uz vidurki:')
# for b in skaiciai:
#     if b > sum(skaiciai)/len(skaiciai):
#         print(b)

# uzduotis 28

# skaiciai = []
# for a in range(5):
#     skaiciai.append(random.randint(1, 100))
# print(skaiciai)
#
# for n in skaiciai:
#     print(n, 'ir jo dalikliai:')
#     for i in range(1,n+1):
#         if n % i==0:
#             print(i)

# uzduotis 29

# print('Kiek zodziu noresite ivesti?')
# zodziai = []
# n = int(input())
# for a in range(n):
#     print('Iveskite zodi')
#     a = input()
#     zodziai.append(a)
# print(' '.join(zodziai))

# uzduotis 30

# listas = ['pirmas', 'antras', 'keturiolika', 'nebegalima']
# print(', '.join(listas))
# for zodis in listas:
#     print(zodis, 'ir jo raidziu kiekis:', len(zodis))

# uzduotis 31

# print('Kiek pazymiu noresite ivesti?')
# pazymiai = []
# n = int(input())
# for a in range(n):
#     print('Iveskite pazymi')
#     a = int(input())
#     pazymiai.append(a)
# print(pazymiai)
# print('pazymiu vidurkis:', round(sum(pazymiai)/len(pazymiai)))
# neigiami = []
# for b in pazymiai:
#     if b < 5:
#         neigiami.append(b)
# if len(neigiami) > 0:
#     print('Studentas turi', len(neigiami), 'neigiamus pazymius:', neigiami)

# # uzduotis 32
#
# listas = ['pirmasis', 'antras', 'keturiolika', 'nebegalima', 'rozes', 'menesis', 'mama']
# print(', '.join(listas))
# ilgiausias = ''
# for zodis in listas:
#     if len(zodis) > len(ilgiausias):
#         ilgiausias = zodis
# print('Ilgiausias zodis yra', ilgiausias, 'ir turi', len(ilgiausias), 'raides(-iu)')
# listas.sort(key=len)
# print('Trumpiausias zodis yra', listas[0], 'ir turi', len(listas[0]), 'raides(-iu)')

# # uzduotis 33
#
# skaiciai = []
# for a in range(100):
#     skaiciai.append(random.randint(1, 10000))
# print(skaiciai)
# print('Vidurkis:', sum(skaiciai)/len(skaiciai))
# print('Didziausias skaicius:', max(skaiciai))
# print('Maziausias skaicius:', min(skaiciai))
# mazesni = []
# for sk in skaiciai:
#     if sk < sum(skaiciai)/len(skaiciai):
#         mazesni.append(sk)
# mazesni.sort(reverse=True)
# print('Mazesni skaiciai uz vidurki:', mazesni)
# print('Bei ju vidurkis:', round(sum(mazesni)/len(mazesni), 2))
# didesni = []
# for sk2 in skaiciai:
#     if sk2 > sum(skaiciai)/len(skaiciai):
#         didesni.append(sk2)
# didesni.sort()
# print('Didesni skaiciai uz vidurki:', didesni)
# print('Bei ju vidurkis:', round(sum(didesni)/len(didesni), 2))

# # uzduotis 34

# listas = ['pirmasis', 'antras', 'keturiolika', 'nebegalima', 'rozes', 'menesis', 'mama']
# print(', '.join(listas))
# ilgiausias = ''
# for zodis in listas:
#     if len(zodis) > len(ilgiausias):
#         ilgiausias = zodis
# print('Ilgiausias zodis yra', ilgiausias, 'ir turi', len(ilgiausias), 'raides(-iu)')
# listas.sort(key=len)
# print('Trumpiausias zodis yra', listas[0], 'ir turi', len(listas[0]), 'raides(-iu)')
# print('Raidziu skirtumas tarp ilgiausio ir trumpiausio:', len(ilgiausias) - len(listas[0]))

# # uzduotis 35
#
# print('Kiek pazymiu noresite ivesti pirmam studentui?')
# pazymiai = []
# n = int(input())
# for a in range(n):
#     print('Iveskite pazymi')
#     a = int(input())
#     pazymiai.append(a)
# print(pazymiai)
# print('pazymiu vidurkis:', round(sum(pazymiai)/len(pazymiai)))
# neigiami = []
# for b in pazymiai:
#     if b < 5:
#         neigiami.append(b)
# if len(neigiami) > 0:
#     print('Studentas turi', len(neigiami), 'neigiamus pazymius:', neigiami)
#
# print('Kiek pazymiu noresite ivesti antram studentui?')
# pazymiai2 = []
# n2 = int(input())
# for a2 in range(n2):
#     print('Iveskite pazymi')
#     a2 = int(input())
#     pazymiai2.append(a2)
# print(pazymiai2)
# print('pazymiu vidurkis:', round(sum(pazymiai2)/len(pazymiai2)))
# neigiami2 = []
# for b2 in pazymiai2:
#     if b2 < 5:
#         neigiami2.append(b2)
# if len(neigiami2) > 0:
#     print('Studentas turi', len(neigiami2), 'neigiamus pazymius:', neigiami2)
#
# if sum(pazymiai2)/len(pazymiai2) > sum(pazymiai)/len(pazymiai):
#     print('Antrojo stundeto pazymiu vidurkis yra didesnis')
# elif sum(pazymiai2)/len(pazymiai2) < sum(pazymiai)/len(pazymiai):
#     print('Pirmojo stundeto pazymiu vidurkis yra didesnis')
# else:
#     print('Abieju studentu pazymiu vidurkiai yra lygus')

# # uzduotis 36

# skaiciai = []
# for a in range(30):
#     skaiciai.append(random.randint(1, 1000))
# print(skaiciai)
# dalinasi = []
# for b in skaiciai:
#     if b % 4 == 0:
#         dalinasi.append(b)
# print(dalinasi)
# print('Skaiciu kurie dalinasi is 4 suma:', sum(dalinasi))

# # uzduotis 37

# skaiciai = []
# for a in range(20):
#     skaiciai.append(random.randint(1, 100))
# print(skaiciai)
# for b in skaiciai:
#     if b % 2 == 0:
#         print(b, 'yra lyginis, jo kvadratas:', b * b)
#     else:
#         print(b)

# # uzduotis 38

# pazymiai = []
# for a in range(10):
#     pazymiai.append(random.randint(1, 10))
# for d in pazymiai:
#     if d < 5:
#         print(d, 'Neigiamas, pritruko', 5 - d, 'balu iki teigiamo pazymio')
#     else:
#         print(d, 'Teigiamas')
#
# # uzduotis 39

# listas = ['pirmasis', 'antras', 'keturiolika', 'nebegalima', 'rozese', 'menesis', 'brolis']
# for zodis in listas:
#     print(zodis, 'zodzio ilgis:', len(zodis))
# suma = 0
# for zod in listas:
#     suma = len(zod) + suma
# print('Visu raidziu kiekis:', suma)

# # uzduotis 40

# skaiciai = []
# for a in range(10):
#     skaiciai.append(random.randint(1, 100))
# print(skaiciai)
# dalinasi = []
# print('Skaiciai, kurie dalinasi is 3:')
# for b in skaiciai:
#     if b % 3 == 0:
#         dalinasi.append(b)
#         print(b)
# print('Siu skaiciu suma:', sum(dalinasi))
# print('Siu skaiciu vidurkis:', sum(dalinasi)/len(dalinasi))

# # uzduotis 42

# klaidos = ['ui87','sys12', 'ui90', 'abc11']
# print('Iveskite klaidos koda:')
# kodas = input()
# if kodas == 'ui87':
#     print('Grafinės sąsajos klaida navigacijoje')
# elif kodas == 'sys12':
#     print('Trūksta operatyviosios atminties sistemoje')
# elif kodas == 'ui90':
#     print('Trūksta antivirusines sistemos')
# elif kodas == 'abc11':
#     print('Pasenusi operatyvioji sistema')
# else:
#     print('Klaidos kodas nerastas')

# # uzduotis 43

# likuciai = [25,30,40,55,41,36,12,50]
# for lik in likuciai:
#     print(lik, 'likuciai, prekes uzteks dar', lik // 5, 'dienoms(-u)')
# maziau = []
# for maz in likuciai:
#     if maz < 35:
#         maziau.append(maz)
# print('Likuciai kuriu uzteks savaitei ar maziau:')
# print(maziau)

# # uzduotis 44

# listas = ['pirmasis', 'antras', 'keturiolika', 'nebegalima', 'roze', 'menesis', 'brolis', 'mama', 'oi']
# print(listas)
# trumpi = []
# for zodis in listas:
#     if len(zodis) < 5:
#         trumpi.append(zodis)
# print(trumpi)

# ciklas for continued

# uzduotis 19

# skaiciai = []
# for i in range(1,101):
#     skaiciai.append(i)
# print(skaiciai)
# for sk in skaiciai:
#     if sk % 3 == 0 and sk % 5 == 0:
#         print('FizzBuzz')
#     elif sk % 3 == 0:
#         print('Fizz')
#     elif sk % 5 == 0:
#         print('Buzz')
#     else:
#         print(sk)

# uzduotis 20

# print('Irasykite kiek norite matyti fibonačiaus skaičių (seka prasides nuo 1):')
# n = int(input())
# a = 1
# b = 2
# print(a)
# print(b)
# for i in range(2,n - 2):
#     c = a + b
#     print(c)
#     a = b + c
#     print(a)
#     b = a + c
#     print(b)

# cikla visi  continued

# uzduotis 6

# skaiciai = []
# for i in range(10,51):
#     if i % 2 == 0:
#         skaiciai.append(i)
#         print(i)

# uzduotis 7

# for i in range(10,51):
#     if i % 2 == 0:
#         if i % 10 == 0:
#             continue
#         else:
#             print(i)


# uzduotis 8
#
# skaiciai = []
# for i in range(0,21):
#     if i % 2 == 0:
#         skaiciai.append(i)
# print('Porine reiksme turejo', len(skaiciai), 'kartu')

# uzduotis 9

# augalai = ['roze', 'tulpe', 'azuoliukas', 'pluke', 'lelija', 'berzas', 'uosis', 'egle', 'dilgeles', 'liepa', 'rasa']
# penki = []
# septyni = []
#
# for zod in augalai:
#     if len(zod) < 5:
#         penki.append(zod)
# print('Trumpesniu negu 5 raides zodziu buvo', len(penki))
#
# for zodis in augalai:
#     if len(zodis) > 7:
#         septyni.append(zodis)
# print('Ilgesniu negu 7 raides zodziu buvo', len(septyni))

# uzduotis 10

# augalai = ['roze', 'tulpe', 'azuoliuko', 'pluke', 'lelija', 'berzas', 'uosis', 'egle', 'dilgeles', 'liepa', 'rasa']
# ieskom = []
# for zod in augalai:
#     if 5 < len(zod) < 10:
#         ieskom.append(zod)
# print('Ilgesniu negu 5 raides, bet trumpesniu negu 10 raidziu zodziu buvo', len(ieskom))

#  sunkesni

# uzduotis 1

# skaiciai = []
# for a in range(300):
#     skaiciai.append(random.randint(1, 300))
# print(' '.join(str(b) for b in skaiciai))

# funkcijos

# ---------------------------------------------------------------------------------------

# uzduotis 1

# def vardasIRpriez ():
#     print('As esu Monika ir programuoju, nes idomu')
# vardasIRpriez()
# vardasIRpriez()
# vardasIRpriez()

# uzduotis 2

# def eilerastis ():
#     print('Su aušra saulutė atsikėlė\n'
#           'Ir į darbą kibo iš pat ryto.\n'
#           'O pavargus saulė motinėlė\n'
#           'Pailsėt už miško nusirito.\n'
#           )
# eilerastis()
# eilerastis()
# eilerastis()
# eilerastis()
# eilerastis()

# # uzduotis 3

# def vardas ():
#     print('Mano vardas Monika')
# def metai ():
#     print('Man 32 metai')
# def kates ():
#     print('Turiu 2 katinus')
# vardas()
# metai()
# kates()

# # uzduotis 4

# def vardas ():
#     print('Mano vardas Monika')
# def metai ():
#     print('Man 32 metai')
# def trecia ():
#     vardas()
#     metai()
# trecia()

# # uzduotis 5

# def skaiciai ():
#     a = random.randint(1,100)
#     b = random.randint(1,100)
#     print(a, '+', b, '=', a + b)
# skaiciai()
# skaiciai()
# skaiciai()
# skaiciai()
# skaiciai()

# # uzduotis 6

# def policija ():
#     vardas = 'Marius'
#     pavarde = 'Pavardenis'
#     amzius = 40
#     alga = 1000
#     etatas = 0.75
#     specia = 'Kriminologas'
#     print(specia, vardas, pavarde, amzius, 'metu', 'dirbantis', etatas, 'etatu ir uzdirba', alga, 'EUR')
# policija()

# # uzduotis 7

# def skaiciukai ():
#     for i in range(10):
#         print(random.randint(1,1000))
#     print()
#     print('Tuscia eilute virs cia')
# skaiciukai()

# # uzduotis 8
#
# def skaic():
#     print(random.randint(1,100))
#
# for i in range(10):
#     skaic()
#
# # uzduotis 9
#
# def sveiki (vardas):
#     print('Labas', vardas)
#
# def viso (vardas):
#     print('Viso gero', vardas)
#
# vardas2 = 'Miksas'
#
# sveiki(vardas2)
# viso(vardas2)

# # uzduotis 10

# def arlygus (a,b):
#     if a == b:
#         print('Skaiciai lygus')
#     elif a > b:
#         print(a, 'didesnis uz', b)
#     else:
#         print(b, 'didesnis uz', a)
#
# arlygus(4,5)
# arlygus(4,4)
# arlygus(7,5)
# arlygus(1,-1)

# # uzduotis 11

# def automob (marke, modelis, metai, turis):
#     print('Automobilis', marke, modelis, 'pagamintas', metai, 'metais', 'turintis', turis, 'darbinio turio')
#
# automob('Audi', 'A50', 2012, 50)
# automob('Tesla', 'Zaibas', 2020, 500)

# # uzduotis 12
#
# def suma(a,b):
#     print(a, '+', b, '=', a + b)
# def atimtis(a,b):
#     print(a, '-', b, '=', a - b)
# def daugyba(a,b):
#     print(a, '*', b, '=', a * b)
# def dalyba(a,b):
#     print(a, '/', b, '=', a / b)
#
# def viskas ():
#     a = random.randint(1,100)
#     print(a)
#     b = random.randint(1,100)
#     print(b)
#     suma(a,b)
#     atimtis(a,b)
#     daugyba(a,b)
#     dalyba(a,b)
#
# viskas()
# viskas()
# viskas()
# viskas()
# viskas()

# # uzduotis 13

# def saras (listas):
#     for a in listas:
#         print(a, len(a))
#
# geles = ['Roze', 'Tulpe', 'Kadagys', 'Pluke', 'Aguona']
#
# saras(geles)

# # uzduotis 14

# def skai (masiv):
#     for a in masiv:
#         print(a, 'kvadratas:', a * a, 'padalinta is 2:', a/2)
#     print()
#
# pirmas = [1, 5, 6, 4, 8, 9]
# antras = [2, 5, 4, 10, 500, 23, 84, 25]
#
# skai(pirmas)
# skai(antras)

# # uzduotis 15

# def mokiniai (vardas, pavard, pazym):
#     print(vardas, pavard)
#     print(pazym)
#     print(sum(pazym)/len(pazym))
#
# mokiniai('Monika', 'Skinkaityte', [5, 6, 10, 7])
# mokiniai('Vardenis', 'Pavardenis', [6, 8, 9, 4])

# # uzduotis 16

# def didz(listas):
#     maxi = listas[0]
#     for sk in listas:
#         if sk > maxi:
#             maxi = sk
#     print('didziausias rastas skaicius:', maxi)
#
# def skaic(listukas):
#         listukas.append(random.randint(1,100))
#         listukas.append(random.randint(1, 100))
#         listukas.append(random.randint(1, 100))
#         listukas.append(random.randint(1, 100))
#         listukas.append(random.randint(1, 100))
#         print(listukas)
#
# pirmas = []
# antras = []
# trecias = []
#
# skaic(pirmas)
# skaic(antras)
# skaic(trecias)
#
# didz(pirmas)
# didz(antras)
# didz(trecias)

# # uzduotis 17
#
# def tekstas ():
#     return 'Random sakinys'
#
# print(tekstas())

# # uzduotis 18

# def atsitiktinis ():
#     a = random.randint(1,100)
#     return a
#
# print(atsitiktinis())
# print(atsitiktinis())
# print(atsitiktinis())
# print(atsitiktinis())
# print(atsitiktinis())

# # uzduotis 19
#
# def studentai (vardas, vidurkis):
#     return 'Studentas ' + vardas + ' turi vidurki ' + str(vidurkis)
#
# print(studentai('Monika', 9))
# print(studentai('Naglis', 8))
# print(studentai('Pupa', 10))
# print(studentai('Miksas', 10))

# # uzduotis 20

# def naujaskai (n):
#     a=[]
#     for i in range(2,n+1):
#         if n%i==0:
#             a.append(i)
#     a.sort()
#     print(n, "ir maziausias jo daliklis:",a[0])
#
# for i in range(10,30):
#     naujaskai(i)

# # uzduotis 21

# def arpirmin (a):
#     if a > 1:
#         for i in range(2, (a // 2) + 1):
#             if (a % i) == 0:
#                 print(a, "False") # nepirminis
#                 break
#         else:
#             print(a, "True") #pirminis
#     else:
#         print(a, "False") # nepirminis
#
# for i in range(2,15):
#     arpirmin(i)

# # uzduotis 22

# def suma(a,b):
#     print(a, '+', b, '=', a + b)
# def sumatriju(a,b,c):
#     print(a, '+', b, '+', c, '=', a + b + c)
# def daugyba(a,b):
#     print(a, '*', b, '=', a * b)
#
# def viskas ():
#     a = 100
#     print(a)
#     b = random.randint(1,100)
#     print(b)
#     c = random.randint(1, 100)
#     print(c)
#     suma(a,b)
#     sumatriju(a,b,c)
#     daugyba(a,b)
#     print()
#
# viskas()
# viskas()

# # uzduotis 23

# def sumele (listas):
#     return sum(listas)
#
# vienas = [1,2,5,6,7,5,8,100]
# antras = [2,5,6,40,5,2,10,63]
#
# print(sumele(vienas))
# print(sumele(antras))
#
# if sumele(vienas) > sumele(antras):
#     print('Pirma suma didesne')
# elif sumele(vienas) < sumele(antras):
#     print('Antra suma didesne')
# else:
#     print('Abi sumos lygios')

# # uzduotis 24

# def zodis(kazkas):
#     res = max(kazkas, key=len)
#     print('Ilgiausias zodis:', res)
#     print('Zodzio ilgis:',max(len(a) for a in kazkas))
#
# listas = ['geles', 'morkyteeees', 'agurkai', 'arbuzai', 'makaronai']
#
# zodis(listas)

# # uzduotis 25

# def pazymiai(listas):
#     t = 'True'
#     f = 'False'
#     for a in listas:
#         if a < 4:
#             return False
#     return True
#
# pirmi = [5,6,7,3,9]
# antri = [5,8,6,5,7]
# treti = [5,3,10,4]
#
# def sakinys(eilute):
#     if bool(eilute) == False:
#         print('studentas turi bent vieną neigiamą pažymį')
#     if bool(eilute) == True:
#         print('visi studento pažymiai teigiami')
#
# sakinys(pazymiai(pirmi))
# sakinys(pazymiai(antri))
# sakinys(pazymiai(treti))

# # uzduotis 26

# def dalyba (skaicius, daliklis=2):
#     return skaicius / daliklis
#
#
# print(dalyba(6))
# print(dalyba(6,3))
# print(dalyba(10))
# print(dalyba(100,5))

# ----------------------------------------------------------------------------------------
# FUnkcijos wordas

# uzduotis 1

# def suma(a,b):
#     print(a, '+', b, '=', a + b)
#
# a = random.randint(1,100)
# print(a)
# b = random.randint(1,100)
# print(b)
#
# suma(a,b)

# uzduotis 2

# def PISq():
#     print('Atsakymas yra:', math.pi * math.pi)
#
# PISq()

# uzduotis 3

# def daugyba(a,b):
#     print(a, '*', b, '=', a * b)
#
# a = random.randint(1,100)
# print(a)
# b = random.randint(1,100)
# print(b)
# daugyba(a,b)

# uzduotis 4

# def sarasas(listas):
#     b = random.randint(1, 100)
#     print(b)
#     for a in listas:
#         if a == 0:
#             break
#         else:
#             a = a + b
#     print(listas)
#
# listukas = [2, 4, 5, 8, 6, 4, 7]
#
# sarasas(listukas)

# uzduotis 5

# def funkcija(a,b):
#     c = random.randint(a,b)
#     print(c)
#
#
# funkcija(1,100)

# uzduotis 6

# listas = []

# def funkcija(a,b,c):
#     for i in range(1,c+1):
#         listas.append(random.randint(a,b))
#     print(listas)

# funkcija(1,10,5)

# uzduotis 7

# def funkcija2(listukas):
#     suma = 0
#     for narys in listas:
#         suma = suma + narys
#     print(suma)
#
# funkcija2(funkcija(1,10,5))

# def funkcija3(listukas):
#     print(sum(listas))
#
# funkcija3(funkcija(1,10,5))

# uzduotis 8

# def vidurkis(listukas):
#     print(sum(listas)/len(listas))
#
# vidurkis(funkcija(1,10,5))

# uzduotis 9

# def simbolis(a,b):
#     for i in range(a):
#         print("*  " * b)
#
# simbolis(5,7)

# uzduotis 10

# def raides(betkas):
#     print('sakinyje yra', len(betkas), 'simboliai')
#     listas = []
#     for i in betkas:
#         if i == ' ':
#             continue
#         else:
#             listas.append(i)
#     print('sakinyje yra', len(listas), 'simboliai, neskaitant tarpu')
#
# raides('laba diena, labas vakaras, viso gero ir taip toliau. ')

# uzduotis 10

def apversta(betkas):
    listas = []
    for raide in reversed(betkas):
        listas.append(raide)
    print(''.join(listas))

apversta('laba diena')

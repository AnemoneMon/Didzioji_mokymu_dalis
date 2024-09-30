import random
import string

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

filmas = ["Don't", "Be", "a", "Menace", "to", "South", "Central", "While", "Drinking", "Your", "Juice", "in", "the", "Hood"]
filmas2 = ["Tik", "nereikia", "gąsdinti", "Pietų Centro,", "geriant", "sultis", "pas", "save", "kvartale"]
vienas = random.sample(filmas, 5)
antras = random.sample(filmas2, 5)
eilute = vienas + antras
print(' '.join(eilute))


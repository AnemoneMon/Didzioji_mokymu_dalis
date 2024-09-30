# # kintamieji
# # uzduotis 1
# vardas = 'Jenna'
# pavard = 'Ortega'
# result = vardas + ' ' + pavard
# print(result)
from dataclasses import replace

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

filmas = 'An American in Paris'
print(filmas.translate({ord(i): None for i in 'AaEeIiOoUuYy'}))
filmas2 = "Breakfast at Tiffany's"
print(filmas2.translate({ord(i): None for i in 'AaEeIiOoUuYy'}))
filmas3 = "2001: A Space Odyssey"
print(filmas3.translate({ord(i): None for i in 'AaEeIiOoUuYy'}))
filmas4 = "It's a Wonderful Life"
print(filmas4.translate({ord(i): None for i in 'AaEeIiOoUuYy'}))


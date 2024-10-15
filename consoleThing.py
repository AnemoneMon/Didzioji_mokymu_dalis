kaciukai = [
    ['Meino meskenas','oranzine', '6', '200'],
    ['Sfinksas','smelio', '5', '300'],
    ['Britu trumpaplaukis','pilka', '7', '350'],
    ['Burmos','ruda/smelio', '4', '300'],
    ['Bombejaus','juoda', '5', '400']
]

def pradinis():
    print('1. Rodyti visas turimas kates')
    print('2. Ivesti nauja kate')
    print('3. Pakeisti turimos kates duomenis')
    print('4. Pasalinti turimos kates duomenis')
    print('5. Iseiti is programos')

def rodytikate(kat, nr = 1):
    print(f'{nr}. Kates veisle - {kat[0]}, kailio spalva - {kat[1]}, amzius - {kat[2]} menesiai, kaina - {kat[3]} eurai')

def rodytivisas():
    nr = 1
    for kat in kaciukai:
        rodytikate(kat, nr)
        nr += 1
    print('************')

def pridetikate():
    print('Irasykite kates veisle:')
    veisle = input()
    print('Irasykite kates kailio spalva:')
    spalva = input()
    print('Irasykite kates amziu (menesiais):')
    amzius = input()
    print('Irasykite kates kaina:')
    kaina = input()
    kaciukai.append([veisle, spalva, amzius, kaina])

def pakeistikate():
    print('Iveskite kates iraso numeri, kuri norite pakeisti')
    nr2 = int(input())
    rodytikate(kaciukai[nr2 - 1])
    print('Irasykite kates veisle:')
    veisle2 = input()
    print('Irasykite kates kailio spalva:')
    spalva2 = input()
    print('Irasykite kates amziu (menesiais):')
    amzius2 = input()
    print('Irasykite kates kaina:')
    kaina2 = input()
    kaciukai[nr2 - 1] = [veisle2, spalva2, amzius2, kaina2]

def istrintikate():
    print('Iveskite kates iraso numeri, kuri norite istrinti')
    nr3 = int(input())
    kaciukai.pop(nr3 -1)

print('*** Kaciuku parduotuves sistema ***')
print('Funkciju pasirinkimai:')

while True:
    pradinis()
    print('Irasykite funkcijos numeri, kuri norite atlikti:')
    pasirink = int(input())
    match pasirink:
        case 1:
            rodytivisas()
        case 2:
            pridetikate()
            rodytivisas()
        case 3:
            pakeistikate()
            rodytivisas()
        case 4:
            istrintikate()
            rodytivisas()
        case 5:
            exit(1)




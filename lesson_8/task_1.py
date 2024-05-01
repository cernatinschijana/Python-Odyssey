# Aceasta este tema pentru lecția 8 legată de loops

# Creați o listă de numere de la 1 la 10 folosind un for loop și funcția range().

# CODUL TĂU VINE MAI JOS:
lista = []
for num in range(1,11):
    lista.append(num)
# CODUL TĂU VINE MAI SUS:

# Folosind un for loop, parcurgeți lista creată și afișați numai numerele pare.

# CODUL TĂU VINE MAI JOS:
for num in lista:
    if (num % 2 == 0):
        print(num)
# CODUL TĂU VINE MAI SUS:

# Folosind un while loop, creați o variabilă 'i' inițializată cu 1 și incrementați-o până când ajunge la 5. Afișați valoarea 'i' la fiecare pas.

# CODUL TĂU VINE MAI JOS:
i = 1
while i <= 5:
    print(i)
    i = i + 1
# CODUL TĂU VINE MAI SUS:

# Creați un dicționar person cu cheile 'name', 'age' și 'city' și iterați prin dicționar afișând perechile de cheie-valoare.

# CODUL TĂU VINE MAI JOS:
person = {'name':'Alice',
          'age' :'22',
          'city':'Chisinau'}

for key, value in person.items():
    print(key, value)
# CODUL TĂU VINE MAI SUS:

# Utilizați un for loop pentru a itera printr-o listă de liste (matrice) și afișați fiecare element.

# CODUL TĂU VINE MAI JOS:
matrix = [[0, 1, 3], [9, 4, 2], [1, 5, 3]]

for row in matrix:
    for i in row:
        print(i) 
# CODUL TĂU VINE MAI SUS:

# Creați o secvență de numere folosind funcția range() și apoi iterați prin această secvență folosind un for loop pentru a afișa numerele.

# CODUL TĂU VINE MAI JOS:
secventa = list(range(1, 23, 3))

for n in secventa:
    print(n)
# CODUL TĂU VINE MAI SUS:

# Folosiți funcția enumerate() pentru a itera printr-o listă și a afișa indexul fiecărui element alături de valoarea sa.

# CODUL TĂU VINE MAI JOS:
for i, num in enumerate(secventa):
    print(i, num)
# CODUL TĂU VINE MAI SUS:

# Folosiți funcția zip() pentru a itera simultan prin două liste și a afișa elementele corespunzătoare.

# CODUL TĂU VINE MAI JOS:
legume = ['cartofi', 'broccoli', 'ceapa']
pret = [4.2, 11.0, 3.1]

for leguma , pretul in zip(legume, pret):
    print(leguma, pretul)
# CODUL TĂU VINE MAI SUS:

# Creați o listă de numere de la 1 la 10 folosind un for loop și funcția range().

# CODUL TĂU VINE MAI JOS:
lista2 = list()
for num in range(1,11):
    lista2.append(num)
# CODUL TĂU VINE MAI SUS:

# Folosind un buclă while, dublează valorile listei până când primul element va deveni mai mare decât 50.

# CODUL TĂU VINE MAI JOS:
index = 0
while lista2[0] <= 50:
    lista2[index] = lista2[index] * 2
    index = index + 1
    if index == len(lista2):
        index = 0
print(lista2)
# CODUL TĂU VINE MAI SUS:

# Generează și printează o listă cu toate numerele pătrat perfect din intervalul [1, 100].

# CODUL TĂU VINE MAI JOS:
lista3 = []
for i in range(1,101):
    if i * i <= 100:
        lista3.append(i * i)

print(lista3)
# CODUL TĂU VINE MAI SUS:

# Folosind un buclă for , printează tabla înmulțirii pentru numărul 7.

# CODUL TĂU VINE MAI JOS:
for i in range(11):
    inmultirea = i * 7
    print('7 * ' + str(i) + ' = ' + str(inmultirea))
# CODUL TĂU VINE MAI SUS:

# Creează o listă de liste, unde fiecare sub-listă conține perechi (i, j) pentru i și j de la 1 la 5. Printează această listă de perechi.

# CODUL TĂU VINE MAI JOS:
lista4 = []
for j in range(1,6):
    for i in range(1,6):
        lista4.append([i , j])

print(lista4)
# CODUL TĂU VINE MAI SUS:

# Parcurge lista de la punctul anterior și printează doar perechile unde i < j .

# CODUL TĂU VINE MAI JOS:
for row in lista4:
    if(row[0] < row[1]):
        print(row)
# CODUL TĂU VINE MAI SUS:

# Folosind un buclă while , caută și printează prima valoare care este mai mare decât 10 dintr-o listă cu numere random creată de tine. Dacă nu există, printează "Nu există valori mai mari decât 10".

# CODUL TĂU VINE MAI JOS:
index = 0
isMoreThan10 = False
lista5 = [2, 5, 7, 58, 45, 89, 34]
while index < len(lista5):
    if lista5[index] > 10:
        print(lista5[index])
        isMoreThan10 = True
        break 
    index = index + 1
if (not isMoreThan10):
    print('Nu exista valori mai mari decit 10')
# CODUL TĂU VINE MAI SUS:

# Folosind loop-uri Creează un pătrat de stele ( * ) folosind bucle încadrate. Dimensiunea pătratului va fi citită de la utilizator.
# Exemplu pentru un pătrat de dimensiune 5:
# *****
# *****
# *****
# *****
# *****

# CODUL TĂU VINE MAI JOS:
lungimea = int(input('Introduce lungimea patratului: '))
for i in range(lungimea):
    print('*' * lungimea)
# CODUL TĂU VINE MAI SUS:

# Folosind for sau while loops realizați afișările de mai jos

# Afișarea 1:
# 1
# 12
# 123
# 1234
# 12345
# 123456

# CODUL TĂU VINE MAI JOS:
num =''
for i in range(1, 7):
    num = num + str(i)
    print(int(num)) 
# CODUL TĂU VINE MAI SUS:

# Afișarea 2:

# 54321
# 5432
# 543
# 54
# 5

# CODUL TĂU VINE MAI JOS:
num2 = []
for i in range(1, 6):
    num2.append(str(i))
num2.reverse()
while len(num2) > 0:
    print(''.join(num2))
    num2.pop()
# CODUL TĂU VINE MAI SUS:

# Afișarea 3:

# abcdefg
# bcdefg
# cdefg
# defg
# efg
# fg
# g

# CODUL TĂU VINE MAI JOS:
alfabet = list('abcdefg')
while len(alfabet) > 0:
    print(''.join(alfabet))
    alfabet.pop(0)
# CODUL TĂU VINE MAI SUS:

# Afișarea 4:

# +-+-+-+-+-+-+-+-
# -+-+-+-+-+-+-+-+
# +-+-+-+-+-+-+-+-
# -+-+-+-+-+-+-+-+
# +-+-+-+-+-+-+-+-
# -+-+-+-+-+-+-+-+
# +-+-+-+-+-+-+-+-
# -+-+-+-+-+-+-+-+

# CODUL TĂU VINE MAI JOS:
pattern = ''
for i in range(8):
    for j in range(8):
        if i % 2 == 0:
            pattern = pattern + '+' + '-'
        else:
            pattern = pattern + '-' + '+'    
    print(pattern)
    pattern = ''
# CODUL TĂU VINE MAI SUS:

# Afișarea 5:

# 3
# 3 9
# 3 9 27
# 3 9 27 81
# 3 9 27 81 243
# 9 27 81 243
# 27 81 243
# 81 243
# 243

# CODUL TĂU VINE MAI JOS:
numere = []
for i in range(1,6):
    numere.append(str(3 ** i))
    print(' '.join(numere))
while len(numere) > 1:
    numere.pop(0)
    print(' '.join(numere))
# CODUL TĂU VINE MAI SUS:

# Completați sarcinile de mai sus pentru a exersa lucrul cu buclele în Python.

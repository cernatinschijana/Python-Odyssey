# Aceasta este a doua ta sarcină legată de seturi

# Creați un set gol numit `numbers_set`

number_set = set()

# Acum adăugați numerele de la 1 la 5 în setul `numbers_set`

number_set = {1, 2, 3, 4, 5}

# Acum afișați setul `numbers_set`

print(number_set)

# Acum adăugați numărul 6 la setul `numbers_set`

number_set.add(6)

# Acum adaugă numerele de la 1 la 5 în setul `numbers_set` folosind metoda update()

number_set.update({1, 2, 3, 4, 5})

# Extrageți numărul 3 din setul `numbers_set`

number_set.remove(3)

# Ștergeți un număr inexistent din setul `numbers_set` fără a genera o eroare

number_set.discard(10)

# Verificați dacă numărul 3 există în setul `numbers_set`

print(3 in number_set)

# Verificați elementele comune din setul `numbers_set` și setul {4, 5, 6, 7}

print(number_set.intersection({4, 5, 6, 7}))

# Verificați elementele diferite din setul `numbers_set` și setul {4, 5, 6, 7}

print(number_set.difference({4, 5, 6, 7}))

# Verificați dacă setul `numbers_set` este un subset al setului {1, 2, 3, 4, 5, 6, 7}

print(number_set.issubset({1, 2, 3, 4, 5, 6, 7}))

# Verificați dacă setul {1, 2, 3, 4, 5, 6, 7} este un subset al setului `numbers_set`

print({1, 2, 3, 4, 5, 6, 7}.issubset(number_set))

# Verificați dacă setul `numbers_set` este un superset al setului {1, 2, 3, 4, 5, 6, 7}

print(number_set.issuperset({1, 2, 3, 4, 5, 6, 7}))

# Verificați dacă setul {1, 2, 3, 4, 5, 6, 7} este un superset al setului `numbers_set`

print({1, 2, 3, 4, 5, 6, 7}.issuperset(number_set))

# Afișați lungimea setului `numbers_set`

print(len(number_set))

# Ștergeți toate elementele din setul `numbers_set`

number_set.clear()

# Afișați setul `numbers_set` pentru a verifica dacă a fost șters

print(number_set)

# Asta a fost tot pentru a doua ta sarcină legată de seturi
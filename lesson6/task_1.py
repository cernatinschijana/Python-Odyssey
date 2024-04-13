# Aceeasta este prima sarcină a aceestei lecții și este legată de dicționare.

# Creați un dicțioar gol

person = {}

# Acum adăugați o pereche de cheie-valoare în dicționar, cheia fiind "name" și valoarea fiind "John"

person = {
    "name" : "John"
}

# Acum adăugați o pereche de cheie-valoare în dicționar, cheia fiind "age" și valoarea fiind 30

person["age"] = 30

# Acum afișați dicționarul

print(person)

# Acum ștergeți cheia "name" din dicționar

del person["name"]

# Acum afișați dicționarul

print(person)

# Acum adăugați o pereche de cheie-valoare în dicționar, cheia fiind "city" și valoarea fiind "New York" folosind metoda setdefault()

person.setdefault("city" , "New York")

# Afișați toate cheile din dicționar 

print(person.keys())

# Afișați toate valorile din dicționar

print(person.values())

# Afișați toate perechile de cheie-valoare din dicționar folosind metoda items()

print(person.items())

# Afișați numărul de perechi de cheie-valoare din dicționar

print(len(person))

# Extrageți valoarea unei chei inexistente fără a genera o eroare

person.get("height")

# Acum actualizați dicționarul cu un alt dicționar, folosind metoda update()

dictionary = {
    "gender": "male"
}

person.update(dictionary)

# Setați valoarea cheii "pizza" la 10 folosind metoda setdefault()

person.setdefault("pizza", 10)

# Afișați dicționarul

print(person)

# Ștergeți cheia "pizza" din dicționar folosind metoda pop()

person.pop("pizza")

# Afișați dicționarul

print(person)

# Ștergeți toate perechile de cheie-valoare din dicționar

person.clear()

# Afișați dicționarul

print(person)

# Asta a fost tot, ai terminat prima ta sarcină legată de dicționare
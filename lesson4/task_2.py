# Aceasta este a doua ta sarcină legată a leciei legate de stringuri în python

# Creează o variabilă numită `name` și seteaz-o la numele tău

name = "Jana"

# Acum afișează valoarea variabilei `name` folosind funcția `print`

print(name)

# Acum creează o nouă variabilă numită `name2` și seteaz-o la valoarea variabilei `name` și afișează valoarea variabilei `name2` folosind funcția `print`

name2 = name
print(name2)

# Acum printează ultimul caracter al variabilei `name` folosind indexarea

print(name[-1])

# Acum printează primele 3 caractere ale variabilei `name` folosind slicing

print(name[:3])

# Acum printează valoarea variabilei `name` în majuscule folosind metoda `upper`

print(name.upper())

# Acum printează valoarea variabilei `name` în minuscule folosind metoda `lower`

print(name.lower())

# Acum printează concatenarea variabilelor `name` și `name2`

print(name + name2)

# Creează o variabilă `text` și setează-i un text la alegere, cu restricția ca acesta să conțină mai multe rânduri

text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."

# Verifică dacă variabila `text` conține cuvântul `python`

print('python' in text)

# Folosește metoda replace pentru a înlocui litera `a` din variabila `text` cu litera `e`

print(text.replace('a','e'))

# Folosește metoda split pentru a transforma variabila `text` într-o listă de cuvinte

print(text.split())

# Creează un f-string care să conțină variabilele `name` și `name2`

f_string = f'Ma numesc {name}. {name2} este un nume destul de comun'

# Verifică dacă string-ul creat se termină cu `!`

print(f_string.endswith('!'))

# Verifică dacă string-ul creat începe cu `Hello`

print(f_string.startswith('Hello'))

# Identifică indexul unde se află `!` în string-ul creat

print(f_string.find('!'))

# Identifică indexul unde se află `o` în string-ul creat folosind altă metodă

print(f_string.index('o'))

# Utilizând format string-uri, creează un string care să conțină variabilele `name` și `name2`

format_string = '{0} si {1} sunt prietene bune.'.format(name, name2)

# Concatenează string-ul creat cu string-ul `text`

new_text = format_string + text
print(new_text)

# Afișează lungimea string-ului creat

print(len(new_text))

# Aceasta a fost tot pentru această sarcină


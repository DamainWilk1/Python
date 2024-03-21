# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 19:37:30 2024

@author: Damian
"""

# %%
#ZAdanie 1
figures = ['prostokat' , 'trojkat' , 'kolo']

input_figure = input('Podaj figure: ')

if input_figure not in figures:
    exit('nie ma takiej figury')
    
if input_figure == 'prostokat':
    parameters = input('Podaj bok A i B po spacji: ').split(' ')
    if len(parameters)==2 and int(parameters[1])>0 and int(parameters[0])>0:
        print(int(parameters[0]) * int(parameters[1]))
elif input_figure == 'trojkat':
    parameters = input('Podaj bok A i h po spacji: ').split(' ')
    if len(parameters)==2 and int(parameters[1])>0 and int(parameters[0])>0:
        print(int(parameters[0]) * int(parameters[1])/2)
elif input_figure == 'kolo':
    parameters = input('Podaj srednica: ')
    if len(parameters)==1 and int(parameters[0])>0:
        print(f'{(int(parameters[0])/2)**2 * 3.14}')
        
# %%

#[2pkt] Zdefiniuj słownik, którego wartościami będą wydatki na życie w ostatnich kilku miesiącach, a kluczami nazwy miesięcy. Wyznacz i wyświetl wartość minimalną, maksymalną, sumę i wartość średnią (wykonaj odpowiednie operacje na
#liście wartości). Sprawdź czy kwota za ostatni miesiąc (nie istnieje prosty sposób na “automatyczne” wybranie ostatniego miesiąca ze słownika, odwołaj się po prostu do nazwy) przekracza wartość średnią - jeśli tak, to wyświetl tekst
#ostrzeżenia “zacznij oszczędzać”, a jeśli nie, informację “jesteś bezpieczny”.

slownik = {'Styczen' : 1000,'Luty' : 2000,'Marzec' : 3000,'Kwiecien' : 4000,'Maj' : 5000,'Czerwiec' :3000}
Minimalna = min(slownik.values())
Maksymalna = max(slownik.values())
Suma = sum(slownik.values())
Average = Suma/len(slownik)
print(f' Minimalna: {Minimalna}\n Maksymalna: {Maksymalna}\n Srednia: {Average}\n Suma: {Suma}')

#for keys,values in slownik.items():
#    print(f'{keys}: {values}')
print(f'To twoja srednia z ostatnich miesięcy: {Average}')

print(f'Ostatni miesiac: {list(slownik)[-1]}')

if  list(slownik.values())[-1] < Average:
    print('Zacznij oszczędzać')
else:
    print('Jesteś bezpieczny')
    
# %%
#Zadanie 3
def validate_date(date_str):
    try:
        day, month, year = map(int, date_str.split('-'))
        if 1 <= month <= 12 and 1 <= day <= 31:
            return True
    except ValueError:
        pass
    return False

def validate_email(email):
    if '@' in email and '.' in email.split('@')[1] and not email[0].isdigit():
        return True
    return False

def encrypt_name(name):
    return ' '.join([part[0].upper() + '*' * (len(part) - 1) for part in name.split()])

def encrypt_email(email):
    local_part, domain_part = email.split('@')
    return local_part[0].upper() + '*' * (len(local_part) - 1) + '@' + domain_part

def calculate_age(year_of_birth):
    return 2024 - year_of_birth

first_name = input("Podaj imię: ")
last_name = input("Podaj nazwisko: ")
date_of_birth = input("Podaj datę urodzenia w formacie dd-mm-rrrr: ")
email = input("Podaj adres e-mail: ")

if not validate_date(date_of_birth):
    print("Błędny format daty urodzenia!")
    exit()

if not validate_email(email):
    print("Błędny format adresu e-mail!")
    exit()

encrypted_name = encrypt_name(first_name + ' ' + last_name)
age = calculate_age(int(date_of_birth.split('-')[2]))
encrypted_email = encrypt_email(email)

user_data = {
    "imię i nazwisko": encrypted_name,
    "wiek": age,
    "mail": encrypted_email
}

print(user_data)

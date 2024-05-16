# -*- coding: utf-8 -*-
"""
Created on Thu Apr 18 21:54:12 2024

@author: Damian
"""

# %% Samochody - dziedziczenie i wielodziedziczenie: DAmianWilk1
class Samochod:
    def __init__(self, marka, model):
        self.marka = marka
        self.model = model

class Elektryczny(Samochod):
    def __init__(self, marka, model, zasieg_na_ladowaniu):
        super().__init__(marka, model)
        self.zasieg_na_ladowaniu = zasieg_na_ladowaniu

class Sportowy(Samochod):
    def __init__(self, marka, model, maksymalna_predkosc):
        super().__init__(marka, model)
        self.maksymalna_predkosc = maksymalna_predkosc

class ElektrycznySportowy(Elektryczny, Sportowy):
    def __init__(self, marka, model, zasieg_na_ladowaniu, maksymalna_predkosc):
        Elektryczny.__init__(self, marka, model, zasieg_na_ladowaniu)
        Sportowy.__init__(self, marka, model, maksymalna_predkosc)

elektro_sportowy = ElektrycznySportowy("Tesla", "Model S", 500, 250)
print("Marka:", elektro_sportowy.marka)
print("Model:", elektro_sportowy.model)
print("Zasięg na jednym ładowaniu:", elektro_sportowy.zasieg_na_ladowaniu)
print("Maksymalna prędkość:", elektro_sportowy.maksymalna_predkosc)

# %% Konto bankowe - enkapsulacja i magic methods: DamianWilk2
class BankAccount:
    def __init__(self, numer, waluta, saldo, wlasciciel):
        self.numer = numer
        self.waluta = waluta
        self.__saldo = saldo
        self.__wlasciciel = wlasciciel

    def get_saldo(self):
        return self.__saldo

    def set_saldo(self, value):
        self.__saldo = value

    def get_wlasciciel(self):
        return self.__wlasciciel

    def set_wlasciciel(self, value):
        self.__wlasciciel = value

    def __str__(self):
        return f"Konto {self.numer} należy do {self.__wlasciciel} i ma saldo {self.__saldo} {self.waluta}"

    def __len__(self):
        return self.__saldo

    def __add__(self, other):
        if (self.numer == other.numer) and (self.waluta == other.waluta) and (self.__wlasciciel == other.__wlasciciel):
            new_balance = self.__saldo + other.get_saldo()
            return new_balance
        else:
            raise ValueError("Nie można dodać konta - różne numery, waluty lub właściciele")

konto1 = BankAccount(123456, "PLN", 1000, "Jan Kowalski")
konto2 = BankAccount(654321, "PLN", 2000, "Anna Nowak")

print(konto1)
print(konto2)
print("Długość konta 1:", len(konto1))
print("Długość konta 2:", len(konto2))

try:
    konto3 = konto1 + konto2
    print("Nowe saldo po dodaniu:", konto3)
except ValueError as e:
    print(e)
# %% Konto bankowe c.d - settery, gettery, metoda statyczna: DamianWilk3
class BankAccount:
    def __init__(self, numer, waluta, saldo, wlasciciel):
        self.numer = numer
        self.waluta = waluta
        self.__saldo = saldo
        self.__wlasciciel = wlasciciel

    @property
    def saldo(self):
        return self.__saldo

    @saldo.setter
    def saldo(self, value):
        self.__saldo = value

    @property
    def wlasciciel(self):
        return self.__wlasciciel

    @wlasciciel.setter
    def wlasciciel(self, value):
        self.__wlasciciel = value

    @staticmethod
    def convert_currency(amount, exchange_rate):
        return amount * exchange_rate

kwota_euro = BankAccount.convert_currency(1000, 4.5)
print("Kwota w euro:", kwota_euro)

# %% Generator haseł - yield: DamainWilk4
import random
import string

def generate_password(length=8, min_letters=4, min_digits=2):
    while True:
        password = ''.join(random.choices(string.ascii_letters + string.digits, k=length))
        if sum(c.isdigit() for c in password) >= min_digits and sum(c.isalpha() for c in password) >= min_letters:
            yield password

generator_haseł = generate_password(length=10, min_letters=5, min_digits=3)
for _ in range(5):
    print(next(generator_haseł))

# %% Czas wywołania funkcji - dekoratory: DamainWilk5
import time

def measure_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Czas wykonania funkcji {func.__name__}: {end_time - start_time} sekund")
        return result
    return wrapper

@measure_time
def factorial_recursive(n):
    if n == 0:
        return 1
    else:
        return n * factorial_recursive(n-1)

@measure_time
def factorial_iterative(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

print(factorial_recursive(5))
print(factorial_iterative(5))

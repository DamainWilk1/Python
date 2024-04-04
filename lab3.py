# -*- coding: utf-8 -*-
"""
Created on Thu Apr  4 21:53:46 2024

@author: Damian
"""
# %%  DamianWilk1: Kasa fiskalna
def kasa_fiskalna():
    product = input("Wpisz produkty oddzielone przecinkiem: ")
    
    list_of_products = set(product.split(","))
    price_product = {}
    
    for product in list_of_products:
        price = input(f"Wpisz cenę dla produktu '{product}': ")
        price_product[product] = price
    
    print("Kasa fiskalna:")
    for products, price in price_product.items():
        print(f"{product}: {price}")

kasa_fiskalna()
# %% DamianWilk2: Obliczanie pola figur geometrycznych
import math
def square_area(side):
    return side * side

def rectangle_area(side_a, side_b):
    return side_a * side_b

def circle_area(radius):
    return math.pi * radius ** 2

def triangle_area(base, height):
    return 0.5 * base * height

def calculate_area_of_figure():
    while True:
        figure = input("Wybierz figurę (square, rectangle, circle, triangle): ").lower()
        
        if figure == "stop":
            print("Koniec programu.")
            break
        
        if figure not in ["square", "rectangle", "circle", "triangle"]:
            print("Nieznana figura. Spróbuj ponownie.")
            continue
        
        if figure == "square":
            side = float(input("Podaj długość boku: "))
            print(f"Pole kwadratu wynosi: {square_area(side)}")
        elif figure == "rectangle":
            side_a = float(input("Podaj długość boku a: "))
            side_b = float(input("Podaj długość boku b: "))
            print(f"Pole prostokąta wynosi: {rectangle_area(side_a, side_b)}")
        elif figure == "circle":
            radius = float(input("Podaj promień koła: "))
            print(f"Pole koła wynosi: {circle_area(radius)}")
        elif figure == "triangle":
            base = float(input("Podaj długość podstawy: "))
            height = float(input("Podaj wysokość: "))
            print(f"Pole trójkąta wynosi:{triangle_area(base, height)}")

calculate_area_of_figure()
# %%  DamianWilk3: Kalkulator

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if b < 0.00000001: #ewentualnie po prostu dać b != 0
        return a / b
    else:
        return "Nie można dzielić przez zero."

def kalkulator():
    while True:
        operacja = input("Wybierz operację (+, -, *, /) lub wpisz 'stop' aby zakończyć: ")
        
        if operacja == "stop":
            print("Koniec programu.")
            break
        
        if operacja not in ["+", "-", "*", "/"]:
            print("Nieprawidłowa operacja. Spróbuj ponownie.")
            continue
        
        a = float(input("Podaj pierwszą liczbę: "))
        b = float(input("Podaj drugą liczbę: "))
        
        if operacja == "+":
            print(f"Wynik dodawania: {add(a, b)}")
        elif operacja == "-":
            print(f"Wynik odejmowania: {sub(a, b)}")
        elif operacja == "*":
            print(f"Wynik mnożenia: {mul(a, b)}")
        elif operacja == "/":
            print(f"Wynik dzielenia: {div(a, b)}")

kalkulator()
# %%  DamianWilk4: Obliczanie pola trójkąta 
import math
def triangle_area_heron(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        p = (a + b + c) / 2
        return math.sqrt(p * (p - a) * (p - b) * (p - c))
    else:
        print("Podany trójkąt nie istnieje")
        return None

a = float(input('Podaj a: '))
b = float(input('Podaj b: '))
c = float(input('Podaj c: '))


print(triangle_area_heron(a, b, c))

# %%  DamianWilk4: Obliczanie pierwiastków równania kwadratowego

import math
def equation(a, b, c):
    if a == 0:
        print("Rownanie nie ma rozwiązań")
    else:
        delta = b**2 - 4 * a * c
        if delta > 0:
             x1 = (-b - math.sqrt(delta)) / (2 * a)
             x2 = (-b + math.sqrt(delta)) / (2 * a)
             return x1, x2
        elif delta == 0:
              x0 = -(b / 2 * a)
              return x0
        elif delta < 0:
               print("Brak pierwiastków rzeczywistych")

a = int(input('Podaj a: '))
b = int(input('Podaj b: '))
c = int(input('Podaj c: '))

print(equation(a, b, c))
# %%  DamianWilk5: Trójkąt z gwiazdek

def triangle_iterative(level):
    for i in range(1, level + 1):
        print("*" * i)

triangle_iterative(4)
# %%  DamianWilk5: Rekurencja

def triangle_recursive(level):
    if level > 0:
        triangle_recursive(level - 1)
        print("*" * level)

triangle_recursive(4)
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 18 21:21:31 2024

@author: Damian
"""

# %% Zadanie 1: Pola figur
import math

class Shape:
    def __init__(self, name):
        self.name = name

    def calculate_area(self):
        pass

    def calculate_perimeter(self):
        pass

    def display_name(self):
        print(f"Shape: {self.name}")


class Triangle(Shape):
    def __init__(self, side_length):
        super().__init__("Triangle")
        self.side_length = side_length

    def calculate_area(self):
        return (math.sqrt(3) / 4) * self.side_length ** 2

    def calculate_perimeter(self):
        return 3 * self.side_length


class Rectangle(Shape):
    def __init__(self, length, width):
        super().__init__("Rectangle")
        self.length = length
        self.width = width

    def calculate_area(self):
        return self.length * self.width

    def calculate_perimeter(self):
        return 2 * (self.length + self.width)


class Circle(Shape):
    def __init__(self, radius):
        super().__init__("Circle")
        self.radius = radius

    def calculate_area(self):
        return math.pi * self.radius ** 2

    def calculate_perimeter(self):
        return 2 * math.pi * self.radius


def main():
    triangle = Triangle(5)
    rectangle = Rectangle(4, 6)
    circle = Circle(3)

    triangle.display_name()
    rectangle.display_name()
    circle.display_name()

    print(f"Pole trójkąta: {triangle.calculate_area()}, obwód: {triangle.calculate_perimeter()}")
    print(f"Pole prostokąta: {rectangle.calculate_area()}, Obwód: {rectangle.calculate_perimeter()}")
    print(f"Pole kola: {circle.calculate_area()}, Obwód: {circle.calculate_perimeter()}")


if __name__ == "__main__":
    main()
    
# %% Zadanie 2: Tworzymy żółwia DAmianWilk2

class Turtle:
    def __init__(self, name, speed):
        self.name = name
        self.speed = speed
        self.__x = 0  # Prywatne pole

    def say_name(self):
        print(f"Nazywam się {self.name} i moja prędkość to {self.speed}")

    def move(self, distance):
        self.__x += distance

    def get_position(self):
        return self.__x


def main():
    turtle = Turtle("Tadek", 5)
    turtle.say_name()
    turtle.move(10)
    print(f"Bieżąca pozycja: {turtle.get_position()}")


if __name__ == "__main__":
    main()
# %% Zadanie 3: Projektowanie klas DamainWilk3
#a
class Pracownik:
    def __init__(self, imie, stanowisko, pensja):
        self.imie = imie
        self.stanowisko = stanowisko
        self.pensja = pensja

    def awansuj(self, nowe_stanowisko, nowa_pensja):
        self.stanowisko = nowe_stanowisko
        self.pensja = nowa_pensja

    def wyswietl_informacje(self):
        print(f"\nImię: {self.imie}, Stanowisko: {self.stanowisko}, Pensja: {self.pensja}")

#b
class Potwor:
    def __init__(self, nazwa, zdrowie, obrazenia):
        self.nazwa = nazwa
        self.zdrowie = zdrowie
        self.obrazenia = obrazenia

    def atak(self, cel):
        print(f"{self.nazwa} atakuje {cel.nazwa} z obrażeniami {self.obrazenia}")
        cel.otrzymaj_obrazenia(self.obrazenia)

    def otrzymaj_obrazenia(self, ilosc):
        self.zdrowie -= ilosc
        if self.zdrowie <= 0:
            print(f"{self.nazwa} został pokonany!")
        else:
            print(f"{self.nazwa} ma jeszcze {self.zdrowie} punktów życia")

#c
class Lodowka:
    def __init__(self, marka, pojemnosc):
        self.marka = marka
        self.pojemnosc = pojemnosc
        self.przedmioty = []

    def dodaj_przedmiot(self, przedmiot):
        self.przedmioty.append(przedmiot)

    def usun_przedmiot(self, przedmiot):
        if przedmiot in self.przedmioty:
            self.przedmioty.remove(przedmiot)
            print(f"\n{przedmiot} został usunięty z lodówki")
        else:
            print(f"\n{przedmiot} nie znaleziono w lodówce")

    def wyswietl_zawartosc(self):
        print(f"\nMarka lodówki: {self.marka}, Pojemność: {self.pojemnosc}")
        print("Przedmioty w lodówce:")
        for przedmiot in self.przedmioty:
            print(przedmiot)


def main():
    # Przykładowe obiekty
    pracownik = Pracownik("Jan Kowalski", "Programista", 5000)
    pracownik.wyswietl_informacje()

    potwor1 = Potwor("\nSmok", 100, 20)
    potwor2 = Potwor("\nGoblin", 80, 15)

    while potwor1.zdrowie > 0 and potwor2.zdrowie > 0:
        potwor1.atak(potwor2)
        if potwor2.zdrowie > 0:
            potwor2.atak(potwor1)

    if potwor1.zdrowie <= 0:
        print(f"\n{potwor2.nazwa} wygrał walkę!")
    else:
        print(f"\n{potwor1.nazwa} wygrał walkę!")

    lodowka = Lodowka("Samsung", 300)
    lodowka.dodaj_przedmiot("Mleko")
    lodowka.dodaj_przedmiot("Jajka")
    lodowka.wyswietl_zawartosc()


if __name__ == "__main__":
    main()
# %% Zadanie 4: Schematy dziedziczenia DamianWilk4
#a
class Zwierze:
    def __init__(self, gatunek):
        self.gatunek = gatunek

    def wydaj_dzwiek(self):
        pass


class Ptak(Zwierze):
    def __init__(self, gatunek, rozpietosc_skrzydel):
        super().__init__(gatunek)
        self.rozpietosc_skrzydel = rozpietosc_skrzydel

    def latanie(self):
        print(f"{self.gatunek} leci")

    def wydaj_dzwiek(self):
        print("Ptak wydaje dźwięk")


class Wrobel(Ptak):
    def __init__(self, rozpietosc_skrzydel):
        super().__init__("Wrobel", rozpietosc_skrzydel)

    def wydaj_dzwiek(self):
        print("Cwir cwir")

#b
class Wojownik:
    def __init__(self, nazwa, zdrowie):
        self.nazwa = nazwa
        self.zdrowie = zdrowie

    def atak(self):
        pass


class Rycerz(Wojownik):
    def __init__(self, nazwa, zdrowie, sila):
        super().__init__(nazwa, zdrowie)
        self.sila = sila

    def atak(self):
        print(f"{self.nazwa} uderza mieczem z siłą {self.sila}")


class Lucznik(Wojownik):
    def __init__(self, nazwa, zdrowie, zrecznosc):
        super().__init__(nazwa, zdrowie)
        self.zrecznosc = zrecznosc

    def atak(self):
        print(f"{self.nazwa} strzela z łuku z zręcznością {self.zrecznosc}")


def main():
    ptak = Ptak("Orzeł", 2)
    ptak.latanie()
    ptak.wydaj_dzwiek()

    wrobel = Wrobel(1)
    wrobel.latanie()
    wrobel.wydaj_dzwiek()

    rycerz = Rycerz("Artur", 100, 10)
    rycerz.atak()

    lucznik = Lucznik("Robin", 80, 8)
    lucznik.atak()


if __name__ == "__main__":
    main()

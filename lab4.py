# -*- coding: utf-8 -*-
"""
Created on Thu Apr 16 20:08:39 2024

@author: Damian
"""

# %% Zadanie 1: Porządkowanie plików DamianWilk1

import os
import shutil

base_directory = "ścieżka/do/katalogu/bazowego"

copy_path = os.path.join(base_directory, "kopie")
if not os.path.exists(copy_path):
    os.makedirs(copy_path)

def copy_images(folder_path, folder_name):
    image_files = [file for file in os.listdir(folder_path)
                   if file.lower().endswith(('.jpg', '.png'))]
    for index, file in enumerate(image_files):
        new_name = f"{folder_name}_{index}.{file.split('.')[-1].lower()}"
        shutil.copy2(os.path.join(folder_path, file),
                     os.path.join(copy_path, new_name))

report = ""

for folder, _, files in os.walk(base_directory):
    if folder != copy_path:
        report += f"\n\n{folder}:\n"
        copy_images(folder, os.path.basename(folder))
        for file in files:
            report += f"{file}\n"

with open(os.path.join(base_directory, "report.txt"), "w") as file:
    file.write(report)

print("Operacja zakończona. Sprawdź plik raportu.")

# %% Zadanie 2: Wysyłka maila DamianWilk2
import smtplib
from email.mime.text import MIMEText

def send_email(sender_email, sender_password, recipient_email, subject, message):
    msg = MIMEText(message)
    msg['Subject'] = subject
    msg['From'] = sender_email
    msg['To'] = recipient_email

    with smtplib.SMTP_SSL('smtp.example.com', 465) as smtp_server:
        smtp_server.login(sender_email, sender_password)
        smtp_server.send_message(msg)

def read_file_content(file_name):
    with open(file_name, 'r') as file:
        return file.read()

sender_email = "twoj_email@example.com"
sender_password = input("Podaj hasło do Twojego emaila: ")
recipient_email = "adres_odbiorcy@example.com"
subject = "Treść pliku"
file_name = "przyklad.txt"  

message = read_file_content(file_name)

send_email(sender_email, sender_password, recipient_email, subject, message)

print("Email został pomyślnie wysłany!!")

# %% Zadanie 3: Kalendarz wypłat DamianWilk3

import calendar
import datetime
from datetime import timedelta
import holidays

def last_working_day_of_month(year, month):
    while True:
        last_day = calendar.monthrange(year, month)[1]
        last_day_of_month = datetime.date(year, month, last_day)
        if last_day_of_month.weekday() < 5 and last_day_of_month not in holidays.Poland():
            return last_day_of_month
        else:
            last_day_of_month -= timedelta(days=1)

year = int(input("Podaj rok: "))

for month in range(1, 13):
    month_name = calendar.month_name[month]
    payday = last_working_day_of_month(year, month)
    print(f"{month_name}: {payday.strftime('%d %B %Y')}")

# %% Zadanie 4: Baza danych LEGO

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 23 17:56:24 2025

@author: Sussu
"""


# Del a - Les inn filen og lagre data i arrays

import pandas as pd
import matplotlib.pyplot as plt

# Leser inn Excel-filen
data = pd.read_excel("/Users/Sussu/Desktop/Prosjektoppgave/support_uke_24.xlsx")

# Hver kolonne leses inn og lagres i en egen array for videre analyse
u_dag = data['Ukedag'].values
kl_slett = data['Klokkeslett'].values
varighet = data['Varighet'].values
score = data['Tilfredshet'].values



# Del b - Antall henvendelser per ukedag og visualisering

# Definer riktig rekkefølge for ukedager
ukedager_riktig_rekkefolge = ['Mandag', 'Tirsdag', 'Onsdag', 'Torsdag', 'Fredag']  

# Tell antall henvendelser per ukedag
antall_henvendelser = data['Ukedag'].value_counts()

# Sorter antall henvendelser etter riktig rekkefølge (mandag til fredag)
antall_henvendelser = antall_henvendelser.reindex(ukedager_riktig_rekkefolge)

# Visualiser resultatet
plt.figure(figsize=(8, 5))  # Gjør diagrammet større
ax = antall_henvendelser.plot(kind='bar', color="skyblue", width=0.8)

for i, v in enumerate(antall_henvendelser.values):
    ax.text(i, v + 0.5, str(v), ha='center', va='bottom')  # Legger til verdier over søylene
    
# Legg til etiketter, tittel og rutenett
plt.xlabel('Ukedag') 
plt.ylabel('Antall henvendelser')  
plt.title('Antall henvendelser per ukedag')
plt.xticks(rotation=45)  # Roterer teksten på x-aksen
plt.grid(axis="y", linestyle="--", alpha=0.7)
plt.show()



# Del c - Minste og lengste samtaletid (i minutter)

# Funksjon for å konvertere tidsstreng til minutter
def tid_til_minutter(tid):
    timer, minutter, sekunder = map(int, tid.split(':'))
    return timer * 60 + minutter + sekunder / 60

# Konverter alle tider til minutter
varighet_minutter = [tid_til_minutter(tid) for tid in varighet]

# Finn minste og lengste samtaletid i minutter
min_varighet_minutter = min(varighet_minutter)
max_varighet_minutter = max(varighet_minutter)

print(f"Minste samtaletid: {min_varighet_minutter:.2f} minutter")
print(f"Lengste samtaletid: {max_varighet_minutter:.2f} minutter")


# Del d - Gjennomsnittlig samtaletid (i minutter)

# Beregn gjennomsnittlig samtaletid i minutter
gjennomsnitt_varighet_minutter = sum(varighet_minutter) / len(varighet_minutter)

print(f"Gjennomsnittlig samtaletid: {gjennomsnitt_varighet_minutter:.2f} minutter")


# Del e - Antall henvendelser per tidsrom og visualisering (sektordiagram)

# Konverter kl_slett til datetime og hent ut timene som heltall
kl_slett_timer = pd.to_datetime(data['Klokkeslett'], format='%H:%M:%S').dt.hour

# Definer tidsrommene
tidsrom = ['08-10', '10-12', '12-14', '14-16']
antall_henvendelser_tidsrom = []

# Grupper henvendelser etter tidsrom
for t in tidsrom:
    start, slutt = map(int, t.split('-'))
    antall = ((kl_slett_timer >= start) & (kl_slett_timer < slutt)).sum()
    antall_henvendelser_tidsrom.append(antall)

# Visualiser resultatet i et sektordiagram (kakediagram)
plt.figure(figsize=(6, 6))  # Gjør diagrammet kvadratisk
plt.pie(
    antall_henvendelser_tidsrom, 
    labels=tidsrom, 
    autopct='%1.1f%%', 
    startangle=260, 
    colors=['lightsalmon', 'bisque', 'paleturquoise', 'lavenderblush'],
    counterclock=False  # Tegn sektorene med klokken
)
#plt.pie(antall_henvendelser_tidsrom, labels=tidsrom, autopct='%1.1f%%', startangle=90, colors=['skyblue', 'lightgreen', 'lightcoral', 'gold'])
plt.title('Antall henvendelser per tidsrom')
plt.show()


# Del f - Beregn NPS (Net Promoter Score)

# Filtrer bort kunder som ikke har gitt tilbakemelding på tilfredshet
score_filtrert = score[~pd.isna(score)]

# Kategoriser tilbakemeldingene
negative = ((score_filtrert >= 1) & (score_filtrert <= 6)).sum()
noytrale = ((score_filtrert >= 7) & (score_filtrert <= 8)).sum()
positive = ((score_filtrert >= 9) & (score_filtrert <= 10)).sum()

# Beregn NPS
total_kunder = len(score_filtrert)
nps = ((positive - negative) / total_kunder) * 100

print(f"Net Promoter Score (NPS): {nps:.0f}")











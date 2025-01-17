"""
Created on Thu Jan 16 20:36:50 2025

PY1010_Arbeidskrav_2_oppgave_2

Programmet regner ut hvor mange pizzaer som må handles inn til en klassefest når elevene spiser 1/4 pizza hver.

@author: s.honkanen
"""

import math

# Tar inn antall elever fra konsollen
antall_elever = int(input('Skriv inn antall elever: '))

# Beregner hvor mange pizzaer som trengs
pizza_per_elev = 1/4
antall_pizzaer = math.ceil(antall_elever * pizza_per_elev) ## math.ceil runder opp til nærmeste heltall

# Skriver ut resultatet som et heltall
print(f'Det må handles inn {antall_pizzaer} pizzaer til festen.')

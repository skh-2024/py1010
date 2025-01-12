#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 12 16:41:51 2025

PY1010_Arbeidskrav_2_oppgave_2

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
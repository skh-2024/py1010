#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 16 20:34:00 2025

PY1010_Arbeidskrav_2_oppgave_1

Programmet tar inn årstallet fra brukeren og regner ut alder i 2024.

@author: s.honkanen
"""

# Spør om fødselsår
alder = int(input('Hvilket år er du født? '))

# Regner ut alderen i 2024
alder = 2024 - alder

# Skriver ut resultatet
print(f"Du blir {alder} år gammel i løpet av året 2024.")
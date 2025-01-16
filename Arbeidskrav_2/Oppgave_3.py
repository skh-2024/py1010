#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 16 20:38:18 2025

PY1010_Arbeidskrav_2_oppgave_3

Programmet regner om fra grader til radianer. 

@author: s.honkanen
"""

import numpy as np
# Ber brukeren om å skrive inn gradtallet
v_grad = float(input('Skriv inn gradtallet: '))

# Regner ut radiantallet fra grader
v_rad = v_grad * np.pi / 180

# Skriver ut resultatet
print(f'{v_grad} grader tilsvarer {v_rad:.2f} radianer.')
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 16 20:52:27 2025

PY101_Oppgave_6

Programmet plotter funksjonen f(x) = -x**2 - 5 for x i intervallet [-10, 10]

@author: s.honkanen
"""

import numpy as np
import matplotlib.pyplot as plt

# Lager 200 jevnt fordelte punkter mellom -10 og 10
x = np.linspace(-10, 10, 200)

# Beregner funksjonsverdier
y = -x**2 - 5

# Plotter funksjonen og legger til tittel og aksebeskrivelser
plt.plot (x, y)
plt.title("Plot av funksjonen f(x) = −x^2 − 5")
plt.xlabel("x")
plt.ylabel("f(x)")
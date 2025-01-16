#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 16 20:47:26 2025

PY1010_Arbeidskrav_2_oppgave_5
Programmet inneholder to funksjoner, bregn_areal og beregn_omkrets, som hver for seg beregner henholdsvis arealet og den ytre omkretsen av en figur bestående av en rettvinklet trekant og en halvsirkel.

@author: s.honkanen
"""

import math

def beregn_areal (a, b):
    """
    Beregner arealet av en figur som består av en rettvinklet trekant og en halvsirkel.
    
    Parametere:
        a (float): Grunnlinjen til trekanten og diameteren til halvsirkelen.
        b (float): Høyden til trekanten.
        
    Returnerer:
        float: Det totale arealet av figuren.

    """

    # Regner ut arealer
    areal_trekant = (a * b)/2
    areal_halvsirkel = (math.pi * (a/2)**2 / 2)
    return areal_trekant + areal_halvsirkel

def beregn_omkrets (a, b):
    """
    Beregner den ytre omkretsen av en figur som består av en rettvinklet trekant og en halvsirkel.
    
    Parametere:
        a (float): Grunnlinjen til trekanten og diameteren til halvsirkelen.
        b (float): Høyden til trekanten.
        
    Returnerer:
        float: Den ytre omkretsen av figuren.

    """
    
    # Regner ut hypotenusen
    hypotenuse = math.sqrt(a**2 + b**2)

    # Regner ut ytre omkrets
    omkrets_halvsirkel = math.pi *(a/2) # Omkretsen av halvsirkelen, ekslusive diamenteren.
    omkrets_trekant_uten_grunnlinje = hypotenuse + b
    return omkrets_halvsirkel + omkrets_trekant_uten_grunnlinje

# Tar inn lengden på grunnlinjen (a) og høyden (b) fra brukeren
a = float(input('Skriv inn lengden på grunnlinjen (a): '))
b = float(input('Skriv inn høyden til trekanten (b): '))

# Beregning av areal og omkrets
areal = beregn_areal(a, b)
omkrets = beregn_omkrets(a, b)

# Skriver ut resultatet
print(f"Den ytre omkretsen av figuren er: {omkrets:.1f}.")
print(f"Arealet av figuren er: {areal:.1f}.")
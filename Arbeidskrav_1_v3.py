
"""
Created on Thu Oct 24 16:52:59 2024
PY1010_Arbeidskrav_1

@author: susannahonkanen
"""

# Antall kjørte km per år
km_per_aar = 20000

#Årlige kostnader i kroner for både elbil og bensinbil 
trafikkforsikring = 8.38 * 365  # 8.38 kr/dag

# Årlige kostnader i kroner - Elbil
forsikring_elbil = 5000
drivstoff_elbil = 0.2 * km_per_aar * 2.00  # Drivstoffkostnad per km og strømpris
bomavgift_elbil = 0.1 * km_per_aar  # Bomavgift: 0.1 kr/km

# Årlige kostnader i kroner - Bensinbil
forsikring_bensinbil = 7500
drivstoff_bensinbil = 1.0 * km_per_aar  # Drivstoffkostnad per km
bomavgift_bensinbil = 0.3 * km_per_aar  # Bomavgift: 0.3 kr/km

# Årlig totalkostnad for bensinbil
totalkostnad_bensinbil = trafikkforsikring + forsikring_bensinbil + drivstoff_bensinbil + bomavgift_bensinbil

# Årlig totalkostnad for elbil
totalkostnad_elbil = trafikkforsikring + forsikring_elbil + drivstoff_elbil + bomavgift_elbil

# Årlig kostnadsdifferanse mellom elbil og bensinbil
aarlig_kostnadsdifferanse = totalkostnad_bensinbil - totalkostnad_elbil

print(f"Årlig totalkostnad for elbil: {totalkostnad_elbil} kr")
print(f"Årlig totalkostnad for bensinbil: {totalkostnad_bensinbil} kr")
print(f"Årlig kostnadsdifferanse mellom bensinbil og elbil: {aarlig_kostnadsdifferanse} kr")
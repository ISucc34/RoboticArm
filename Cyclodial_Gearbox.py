# Written by Alan Bonilla Santos

# --- Libraries ---
import math

# --- Cyclodial Gearbox Rotor Shape ---

# Constraint: 
theta = 

if 0 <= theta <= 360:
  print(f"{theta} is within the constraint")

psi = -math.atan(math.sin((1-N)theta)/((R/E*N) - math.cos(1-N)*theta)

X = R*math.cos(theta) - Rr*math.cos(theta - psi) - E*math.cos(N*theta)
Y = -R*math.sin(theta) + Rr*math.sin(theta - psi) + E*math.sin(N*theta)

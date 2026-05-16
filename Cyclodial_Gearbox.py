# Written by Alan Bonilla Santos

# --- Libraries ---
import math

# --- Determining the parameters ---

# The gearbox ratio
N = 16                # Number of rollers
Ratio = N - 1         # Ratio Number
print(f"Your ratio is {Ratio}:1 reduction ratio for this gearbox.")

# Constraints from parts
Dr = 13       # diamater of the 686-2RS bearings (mm)
Rr = 13/2     # Radius of bearings (mm)
R = 90/2      # Radius of the bearings (mm)
E = 1.5       # Eccentricity (mm)

# Constraint for when making the cyclodial drive disks
if E < Rr:
  print(f"{E} is within the constraint.") 
  
# --- Cyclodial Gearbox Rotor Shape ---

# Constraint: 
theta = 

if 0 <= theta <= 360:
  print(f"{theta} is within the constraint")

psi = -math.atan(math.sin((1-N)theta)/((R/E*N) - math.cos(1-N)*theta)

X = R*math.cos(theta) - Rr*math.cos(theta - psi) - E*math.cos(N*theta)
Y = -R*math.sin(theta) + Rr*math.sin(theta - psi) + E*math.sin(N*theta)

print("Hello, Welcome to DensityCalc!")
mass = int(input("What is the mass?: "))
volume = int(input("What is the volume?: "))

if mass == 0 or volume == 0:
    print("Invalid Number either by mass or volume!")
    exit(0)


def calc_density(mass, volume):
    dens = mass / volume
    return dens

def properties(dens):
  if dens == 1:
    return "hover"
  elif dens > 1:
    return "sink"
  else:
    return "float"

    
dens = calc_density(mass, volume)

ans = properties(dens)
print("The Item will",ans, "!")

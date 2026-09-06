print("Hello, Welcome to DensityCalc!")
mass = int(input("What is the mass?: "))
volume = int(input("What is the volume?: "))

if mass or volume == 0:
    print("Invalid Number either by mass or volume!")
    exit(0)


def calc_density(mass, volume):
    dens = mass / volume
    print("Density is: ", dens)




calc_density(mass, volume)
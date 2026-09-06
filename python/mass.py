print("Hello, Welcome to MassCalc!")
dens = int(input("What is the density?: "))
volume = int(input("What is the volume?: "))

# if dens or volume == 0:
#     print("Invalid Number either by mass or volume!")
#     exit(0)


def calc_mass(dens, volume):
    mass = dens * volume
    print("Mass is: ", mass)




calc_mass(dens, volume)
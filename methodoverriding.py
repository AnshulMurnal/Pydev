class Energy:
    def rule(self):
        print("any energy cannot be created or destroyed")
    def transferred(self):
        print("The energy is transferred")

class Kinetic_energy(Energy):
    def rule(self):
        print("energy based on movement")
class Potential_energy(Energy):
    def rule(self):
        print("energy based on position or height")
class Thermal_energy(Energy):
    def rule(self):
        print("energy based on temperature")
class Sound_energy(Energy):
    def rule(self):
        print("energy based on vibration or noise")
class Light_energy(Energy):
    def rule(self):
        print("energy based on light")
class Electrical_energy(Energy):
    def rule(self):
        print("energy based on electricity")

Kinetic_energy = Kinetic_energy
Potential_energy = Potential_energy
Thermal_energy = Thermal_energy
Sound_energy = Sound_energy
Light_energy = Light_energy
Electrical_energy = Electrical_energy
Kinetic_energy.transferred(Energy)
Light_energy.rule(Energy)
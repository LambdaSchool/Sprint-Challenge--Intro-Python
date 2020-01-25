def __init__(self, name, groundvehicles, flightvehicles):
        self.name = name
        self.groundvehicles = groundvehicles
        self.flightvehicles = flightvehicles
    
    def __str__(self):
        vehicle_string = self.name
        i = 1
        for b in self.vehicles:
            vehicle_string += f"\n{i}. {b.get_name()}"
            i+=1
        return vehicle_string
    
    def get_name(self):
        return self.name
    
    def set_name(self, new_name):
        self.name = new_name
    
    def get_groundvehicles(self):
        return self.groundvehicles
    
    def set_groundvehicles(self, new_groundvehicles):
        self.groundvehicles = new_groundvehicles
    
    def get_flightvehicles(self):
        return self.flightvehicles
    
    def set_flightvehicles(self, new_flightvehicles):
        self.flightvehicles = new_flightvehicles

class GroundVehicle:
    def __init__(self, name, model, price):
        self.name = name
        self.model = model
        self.price = price
    
    def __str__(self):
        output = f"{self.name}: {self.model}, {self.price}"
        for 

    
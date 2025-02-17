from swap_meet.item import Item

class Clothing(Item):
    
    # constructor
    def __init__(self, id = None, condition = 0.0, fabric = "Unknown"):
        super().__init__(id = id, condition = condition)
        self.fabric = fabric
    
    def __str__(self): 
        return f"{super().__str__()} It is made from {self.fabric} fabric."
    
    
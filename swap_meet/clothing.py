class Clothing:
    
    def __init__(self, condition=0):
        self.category = "Clothing"
        self.condition = condition

    def __str__(self):
        return "The finest clothing you could wear."        
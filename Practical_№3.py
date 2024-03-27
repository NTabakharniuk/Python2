class Citrus:
    def get_name(self):
        return "Grapefruit, Mandarin, Orange, Lime"


class Grapefruit(Citrus):
    def get_name(self):
        return "Grapefruit"
    
class Mandarin(Citrus):
    def get_name(self):
        return "Mandarin"
    
class Orange(Citrus):
    def get_name(self):
        return "Orange"     
    
class Lime(Citrus):
    def get_name(self):
        return "Lime"
    
class Rangpur(Lime, Mandarin):
    pass

class Clementine(Orange, Mandarin):
    pass

class Penterin(Mandarin, Grapefruit):
    pass

class Orlando(Penterin, Grapefruit):
    pass

orlando = Orlando()
rangpur = Rangpur()

print(orlando.get_name())        
print(rangpur.get_name())
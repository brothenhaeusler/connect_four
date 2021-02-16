
class MyClass:
    """A simple example class"""
    i = 12345

    def f(self):
        return 'hello world'


class Flower:
    def __init__(self):
        self.name = "sunflower"
        self.color = "yellow"
        # element {1, .. , 10}
        self.objective_attraction_level = 6
        # element {1, .. , 10}
        self.obvious_dating_ingenuity_level = 5
        self.estimated_gift_pathos_level= self.calculate_gift_pathos_level()

    # name = "sunflower"
    # color = "yellow"
    # # element {1, .. , 10}
    # objective_attraction_level = 6
    # # element {1, .. , 10}
    # obvious_dating_ingenuity_level = 5
    # estimated_gift_pathos_level= self.calculate_gift_pathos_level()
    # #estimated_gift_pathos_level= 10

    def calculate_gift_pathos_level(self):
        return int( (self.objective_attraction_level + self.obvious_dating_ingenuity_level) / 2)
    
    def __str__(self):
        return "Flower=>" + "[" + self.name + ","+ self.color + ", obvious_dating_ingenuity_level: "  + str(self.obvious_dating_ingenuity_level) + ", objective_attraction_level: " + str(self.objective_attraction_level) + ", estimated_gift_pathos_level: " + str(self.estimated_gift_pathos_level) + "]"

    def set_name(self, _name):
        self.name = _name
        return self

    def set_color(self, _color):
        self.color = _color
        return self

    def set_attraction_index(self, _objective_attraction_level):
        self.objective_attraction_level = _objective_attraction_level
        self.estimated_gift_pathos_level=self.calculate_gift_pathos_level()
        return self

    def set_ingenuity_index(self, _obvious_dating_ingenuity_level):
        self.obvious_dating_ingenuity_level = _obvious_dating_ingenuity_level
        self.estimated_gift_pathos_level=self.calculate_gift_pathos_level()
        return self

flower_1 = Flower()
flower_2 = Flower()
flower_3=Flower()

flower_1.set_name("lily").set_color("violet").set_attraction_index(7).set_ingenuity_index(9)
flower_2.set_name("tulip").set_color("red").set_attraction_index(8).set_ingenuity_index(3)
flower_3.set_name("hyacinth").set_color("blue").set_attraction_index(5).set_ingenuity_index(8)

print("Print Flowers...")
print(flower_1)
print(flower_2)
print(flower_3)
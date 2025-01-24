import math
class cylinder:

    def __init__(self,radius,height):
        self.radius=radius
        self.height=height


def cylinder_volume(radius, height):

    

height = float(input("Enter the height of the cylinder: "))
radius = float(input("Enter the radius of the cylinder: "))
a = cylinder(4,3)
print("The radius of the cylinder is ",a.radius)

    return math.pi * radius**2 * height


        



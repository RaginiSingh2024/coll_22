class cylinder:
    def __init__(self,radius,height):
        self.radius=radius
        self.height=height
    

height = float(input("Enter the height of the cylinder: "))
radius = float(input("Enter the radius of the cylinder: "))
a = cylinder(3,4)
print("The radius of the cylinder is ",a.radius)
print("height of the cylinder is ",a.height)
        



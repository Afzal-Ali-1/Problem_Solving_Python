class Vector():
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def __repr__(self):
        string=f"vector({self.x},{self.y})"
        return string
    def __add__(self,other):
        x=self.x+other.x
        y=self.y+other.y
        return Vector(x,y)
    def __sub__(self,other):
        x=self.x-other.x
        y=self.y-other.y
        return Vector(x,y)
    def random_walk(self):
        try:
            self.bewda_position=self
            random_round=int(input("\nEnter The rounds which bewda going to take : "))
            for var in range(random_round):
                print("\ne.g If you want to go North press '1' ")
                print("\nIf you want to know the current postion of bewda press '5'")
                direction=int(input("input your direction\n1.North\n2.East\n3.South\n4.West : "))
                if direction==1:
                    steps=int(input("\nEnter the steps that much bewda want to move :"))
                    next_positon=Vector(0,steps)
                    self.bewda_position=self.bewda_position.__add__(next_positon)
                elif direction==2:
                    steps=int(input("\nEnter the steps :"))
                    next_positon=Vector(steps,0)
                    self.bewda_position=self.bewda_position.__add__(next_positon)
                elif direction==3:
                    steps=int(input("\nEnter the steps :"))
                    next_positon=Vector(0,steps)
                    self.bewda_position=self.bewda_position.__sub__(next_positon)
                elif direction==4:
                    steps=int(input("\nEnter the steps :"))
                    next_positon=Vector(steps,0)
                    self.bewda_position=self.bewda_position.__sub__(next_positon)
                elif direction==5:
                    print(self.bewda_position)
                else:
                    print("Sahi input de tu bhi piya hua hai kya .")
            return print(f"Current position of bewda is {self.bewda_position}")
        except ValueError as arg:
            print("Error ! integer de be ",arg)
bewda_position= Vector(0,0)
bewda_position.random_walk()
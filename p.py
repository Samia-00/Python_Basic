class Robot:
    def introduce_self(self):
        print("My name is " + self.name)
        print("My color is " + self.color)
        print (self.weight)
        
r1=Robot()
r1.name = "tom"
r1.color = "red"
r1.weight = 30

r2=Robot()
r2.name="jerry"
r2.color="blue"
r2.weight = 40

r1.introduce_self()
r2.introduce_self()

class Vec():
    def __init__(self,x,y):
        self.x=x
        self.y=y
    
    
    def print(self):
        print(self.x,self.y)
      

    def add(self,v):
        self.x = self.x + v.x
        self.y = self.y + v.y

    def sub(self,c):
        self.x = self.x - c.x
        self.y = self.y - c.y


a=Vec(1,2)
a.print()
b=Vec(3,4)
a.add(b)
a.print()
d=Vec(4,4)
a.sub(d)
a.print()


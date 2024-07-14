class PlumState:
        
    def __init__(self, plum, pointer, mulfac=1, addfac=0):
        self.pointer = pointer
        self.mulfac  = mulfac
        self.addfac  = addfac
        self.plum = plum
        
    def __add__(self, other):
        if isinstance(other, (int, float)):
            return PlumState(plum=self.plum, pointer=self.pointer, mulfac=self.mulfac, addfac= self.addfac + other)
    def __radd__(self, other):
        if isinstance(other, (int, float)):
            return PlumState(plum=self.plum, pointer=self.pointer, mulfac=self.mulfac, addfac= self.addfac + other)
    def __sub__(self, other):
        if isinstance(other, (int, float)):
            return PlumState(plum=self.plum, pointer=self.pointer, mulfac=self.mulfac, addfac= self.addfac - other)
    def __rsub__(self, other):
        if isinstance(other, (int, float)):
            return PlumState(plum=self.plum, pointer=self.pointer, mulfac=self.mulfac, addfac= self.addfac - other)
    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return PlumState(plum=self.plum, pointer=self.pointer, mulfac=self.mulfac*other, addfac= self.addfac * other)
    def __rmul__(self, other):
        if isinstance(other, (int, float)):
            return PlumState(plum=self.plum, pointer=self.pointer, mulfac=self.mulfac*other, addfac= self.addfac * other)
    def __div__(self, other):
        if isinstance(other, (int, float)):
            return PlumState(plum=self.plum, pointer=self.pointer, mulfac=self.mulfac/other, addfac= self.addfac/other)
    def __rdiv__(self, other):
        if isinstance(other, (int, float)):
            return PlumState(plum=self.plum, pointer=self.pointer, mulfac=self.mulfac/other, addfac= self.addfac/other)
    
    def value(self):
        return self.mulfac * self.plum.memory[self.pointer] + self.addfac
    
class Plum:
    def __init__(self):
        self.memory = {}

    def create(self, name, value):
        if name in self.memory:
            raise ValueError("Variable already exists")
        self.memory[name] = value
        return PlumState(plum=self, pointer=name)
        
    def update(self, name, value):
        if name not in self.memory:
            raise ValueError("Variable does not exist")
        self.memory[name] = value
        
    def getVar(self, name):
        if name not in self.memory:
            raise ValueError("Variable does not exist")
        return PlumState(plum=self, pointer=name)
    
        
if __name__ == "__main__":
    # you initialize a plum
    plum = Plum()
    
    # you create a variable a with value 10
    a = plum.create(name='a', value= 10)
    
    # you create a variable b with dependent on a
    b =  3*a + 4
    
    # you print the value of b
    print(b.value())
    
    # you update the value of a
    plum.update('a', 20)
    
    # and you notice that the value of b also changes
    print(b.value())
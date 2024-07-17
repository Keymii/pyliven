from exceptions import IllegalOperationError
class LiveNum():
    
    size = 0
    memory = {}
    
    def __init__(self, core, pow = 1, ncoeff = 1, dcoeff=1, add =0, ) -> None:
        if not isinstance(core, (int, float, LiveNum)):
            raise TypeError("Core must be a number or another LiveNum object")
        if not isinstance(pow, (int, float, LiveNum)):
            raise TypeError("Pow must be a number or another LiveNum object")
        if not isinstance(add, (int, float, LiveNum)):
            raise TypeError("Add must be a number or another LiveNum object")
        if not isinstance(ncoeff, (int, float, LiveNum)):
            raise TypeError("nCoeff must be a number or another LiveNum object")
        if not isinstance(dcoeff, (int, float, LiveNum)):
            raise TypeError("dCoeff must be a number or another LiveNum object")
    
        
        self._core = core 
        self._pow = pow 
        self._ncoeff = ncoeff 
        self._dcoeff = dcoeff 
        self._add = add
        self._id = LiveNum.size
        LiveNum.size+=1
        LiveNum.memory[self._id] = {
            'pointer':self,
            'dependants':[],
            'cache':None
            }
        self.value()
        
        params = [core, pow, ncoeff, dcoeff, add]        
        self._depends_on = []
        for i in params:
            if isinstance(i, LiveNum):
                self._depends_on.append(i)
                LiveNum.memory[i._id]['dependants'].append(self)
        
    def value(self, force=False):
        if force or (LiveNum.memory[self._id]['cache'] is None):
            core = self._core if isinstance(self._core, (int, float)) else self._core.value()
            power = self._pow if isinstance(self._pow, (int, float)) else self._pow.value()
            ncoeff = self._ncoeff if isinstance(self._ncoeff, (int, float)) else self._ncoeff.value()
            dcoeff = self._dcoeff if isinstance(self._dcoeff, (int, float)) else self._dcoeff.value()
            add = self._add if isinstance(self._add, (int, float)) else self._add.value()
            val = (core**power)*ncoeff/dcoeff+add
            LiveNum.memory[self._id]['cache'] = val
            return val
        else:
            return LiveNum.memory[self._id]['cache']
    
    def __add__(self, other):
        if not isinstance(other, (int, float, LiveNum)):
            raise IllegalOperationError
        return LiveNum(core=self, add=other)
    def __radd__(self, other):
        if not isinstance(other, (int, float, LiveNum)):
            raise IllegalOperationError
        return LiveNum(core=other, add=self)
    def __neg__(self):
        return LiveNum(core=self, ncoeff=-1)
    def __sub__(self, other):
        if not isinstance(other, (int, float, LiveNum)):
            raise IllegalOperationError
        return LiveNum(core=self, add=-other)
    def __rsub__(self, other):
        if not isinstance(other, (int, float, LiveNum)):
            raise IllegalOperationError
        return LiveNum(core=other, add=-self)
    def __mul__(self, other):
        if not isinstance(other, (int, float, LiveNum)):
            raise IllegalOperationError
        return LiveNum(core=self, ncoeff=other)
    def __rmul__(self, other):
        if not isinstance(other, (int, float, LiveNum)):
            raise IllegalOperationError
        return LiveNum(core=other, ncoeff=self)
    def __truediv__(self, other):
        if not isinstance(other, (int, float, LiveNum)):
            raise IllegalOperationError
        return LiveNum(core=self, dcoeff=other)
    def __rtruediv__(self, other):
        if not isinstance(other, (int, float, LiveNum)):
            raise IllegalOperationError
        return LiveNum(core=other, dcoeff=self)
    def __pow__(self, other):
        if not isinstance(other, (int, float, LiveNum)):
            raise IllegalOperationError
        return LiveNum(core=self, pow=other)
    def __rpow__(self, other):
        if not isinstance(other, (int, float, LiveNum)):
            raise IllegalOperationError
        return LiveNum(core=other, pow=self)
    
    def __repr__(self) -> str:
        return str(self.value())
    def __str__(self) -> str:
        return str(self.value())
    
    def __int__(self):
        return int(self.value())
    def __float__(self):
        return float(self.value())
    
    def update(self, value):
        self._core = value
        self._add = 0
        self._pow = 1
        self._ncoeff = 1
        self._dcoeff = 1
        for i in self._depends_on:
            LiveNum.memory[i._id]['dependants'].remove(self)
        self._depends_on = []
        if isinstance(value, LiveNum):
            self._depends_on.append(value)
            LiveNum.memory[value._id]['dependants'].append(self)
        
        self.value(force=True)
        for i in LiveNum.memory[self._id]['dependants']:
            LiveNum.memory[self._id]['dependants'].extend( LiveNum.memory[i._id]['dependants'] )
            i.value(force=True)
    
k = 9e9
q1 = (2e-3)
q2 = (3e-3)

r = LiveNum(1)

f = k*q1*q2/r**2
for i in range(1,11):
    r.update(i)
    print(f)
from pyliven.exceptions import *
from typing import Optional, Union, Any


class LiveNum():    
    """LiveNum is a stateful class that allows you to create a number whose updation will update past calculations."""
    size : int = 0
    memory : dict[int, dict[str, Any]]= {}
    
    # User API functions
    def __init__(self, core: Union[int,float,'LiveNum'], side : Optional[Union[int,float,'LiveNum']] = None , operator : Optional[int] = None) -> None:
        
        """LiveNum is a stateful class that allows you to create a number whose updation will update past calculations.        
        
        Operator Table:
            0: Addition
            1: Subtraction
            2: Multiplication
            3: Division
            4: Floor Division 
            5. Modulo
            6. Power"""
        
        if not isinstance(core, (int, float, LiveNum)):
            raise ImproperCoreValueError
        if not isinstance(side, (int, float, LiveNum, type(None))):
            raise ImproperSideValueError
        
        if (operator or side) is not None and (operator and side) is None:
            raise MissingOperatorOrSideError
        
        self._core = core 
        self._side = side
        self._operator = operator
        
        self._id = LiveNum.size
        LiveNum.size+=1
        LiveNum.memory[self._id] = {
            'pointer':self,
            'dependants':[],
            'cache':None
            }
        self.value()
        
        params = [core, side]        
        self._depends_on = []
        for i in params:
            if isinstance(i, LiveNum):
                self._depends_on.append(i)
                LiveNum.memory[i._id]['dependants'].append(self)
                    
    def value(self, force=False):
        """Returns the value of the LiveNum object. If force is set to True, it will recalculate the value of the object."""
        
        if force or (LiveNum.memory[self._id]['cache'] is None):
            core = self._core if isinstance(self._core, (int, float)) else self._core.value()
            if self._side is None:
                val = core
                LiveNum.memory[self._id]['cache'] = val
                return val
            side = self._side if isinstance(self._side, (int, float)) else self._side.value()
            val = None
            if self._operator == 0:
                val = core + side
            elif self._operator == 1:
                val = core - side
            elif self._operator == 2: 
                val = core * side
            elif self._operator == 3:
                val = core / side
            elif self._operator == 4:
                val = core // side
            elif self._operator == 5:
                val = core % side
            elif self._operator == 6:
                val = core ** side
            LiveNum.memory[self._id]['cache'] = val
            return val
        else:
            return LiveNum.memory[self._id]['cache']
        
    def update(self, value):
        """Updates the value of the LiveNum object."""
        if not isinstance(value, (int, float)):
            raise ImproperUpdateValueError
        
        self._core = value
        self._side = None
        self._operator = None
        
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

    # Arithmetic Operations
    def __add__(self, other):
        self._checkIllegalOperation(other)
        return LiveNum(core=self, side=other, operator=0)
    def __radd__(self, other):
        self._checkIllegalOperation(other)
        return LiveNum(core=other, side=self, operator=0)
    def __neg__(self):
        return LiveNum(core=self, ncoeff=-1)
    def __sub__(self, other):
        self._checkIllegalOperation(other)
        return LiveNum(core=self, side=other, operator=1)
    def __rsub__(self, other):
        self._checkIllegalOperation(other)
        return LiveNum(core=other, side=self, operator=1)
    def __mul__(self, other):
        self._checkIllegalOperation(other)
        return LiveNum(core=self, side=other, operator=2)
    def __rmul__(self, other):
        self._checkIllegalOperation(other)
        return LiveNum(core=other, side=self, operator=2)
    def __truediv__(self, other):
        self._checkIllegalOperation(other)
        return LiveNum(core=self, side=other, operator=3)
    def __rtruediv__(self, other):
        self._checkIllegalOperation(other)
        return LiveNum(core=other, side=self, operator=3)
    def __floordiv__(self, other):
        self._checkIllegalOperation(other)
        return LiveNum(core=self, side=other, operator=4)
    def __rfloordiv__(self, other):
        self._checkIllegalOperation(other)
        return LiveNum(core=other, side=self, operator=4)
    def __mod__(self, other):
        self._checkIllegalOperation(other)
        return LiveNum(core=self, side=other, operator=5)
    def __rmod__(self, other):
        self._checkIllegalOperation(other)
        return LiveNum(core=other, side=self, operator=5)
    def __pow__(self, other):
        self._checkIllegalOperation(other)
        return LiveNum(core=self, side=other, operator=6)
    def __rpow__(self, other):
        self._checkIllegalOperation(other)
        return LiveNum(core=other, side=self, operator=6)
    
    # Private Helper Functions
    def _checkIllegalOperation(self, other):
        if not isinstance(other, (int, float, LiveNum)):
            raise IllegalOperationError
    
    # Representation and Type Conversions
    def __repr__(self) -> str:
        return str(self.value())
    def __str__(self) -> str:
        return str(self.value())
    def __int__(self):
        return int(self.value())
    def __float__(self):
        return float(self.value())

if __name__ == "__main__":
    k = 9e9
    q1 = LiveNum(2e-3)
    q2 = (3e-3)

    r = LiveNum(1)

    f = k*q1*q2/r**2
    for i in range(1,11):
        r.update(i)
        q1.update(q1.value()-i*1e-5)
        print(f)
class IllegalOperationError(Exception):
    """Raised when an illegal operation is performed on LiveNum"""
    def __init__(self):
        super().__init__("Arithmetic operation on LiveNum only permitted with int, float and LiveNum objects")

class ImproperCoreValueError(Exception):
    """Raised when an improper core value is passed to LiveNum"""
    def __init__(self):
        super().__init__("Core value must be a number or another LiveNum object")
        
class ImproperSideValueError(Exception):
    """Raised when an improper side value is passed to LiveNum"""
    def __init__(self):
        super().__init__("Side must be a number, another LiveNum object, or None")
        
class MissingOperatorOrSideError(Exception):
    """Raised when operator or side is not provided together"""
    def __init__(self):
        super().__init__("Operator and Side must be provided together")
    
class ImproperUpdateValueError(Exception):
    """Raised when an improper value is passed to update method"""
    def __init__(self):
        super().__init__("Update value must be a number (int or float)")
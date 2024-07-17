class IllegalOperationError(Exception):
    """Raised when an illegal operation is performed on LiveNum"""
    def __init__(self):
        super().__init__("Arithmetic operation on LiveNum only permitted with int, float and LiveNum objects")

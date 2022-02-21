
def Plus(a, b):
    return a + b

def Minus(a, b):
    return a - b

def Multiply(a, b):
    return a * b

def Division(a, b):
    if not b:
        raise ZeroDivisionError
    
    return a // b

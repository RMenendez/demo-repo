# This is a comment to test the merging when destination branch has changes from when the source branch was created.
#


# Change name adition to suma from main branch
def suma(a, b):
    """
    Returns the adition of a and b. 
    """
    return a + b

# Change x,y to a,b from conf/test3 branch
# Change resta to substraction from main branch
def substraction(a, b):
    """
    Returns the difference of a and b.
    Devuelve la resta de a y b.
    """
    return a - b

def multiplicacion(x, y):
    """
    Returns the product of x and y.
    """
    return x * y

def division(x, y):
    """
    Returns the quotient of x and y.
    """
    if y == 0:
        raise ValueError("Cannot divide by zero")
    return x / y
# ADD COMMENT FROM feature/test2 branch

# ADD COMMENT IN LOCAL feature/test1732


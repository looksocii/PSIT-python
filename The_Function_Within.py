"""Quiz"""
def main(num_a, num_b, num_c, num_d):
    """Docstring"""
    print(fun01(fun01(num_a)))
    print(fun02(fun01(num_a-num_b)))
    print(fun03(fun01(num_a+num_b), fun01(num_a+num_c), fun02(fun01(num_d**2))))
    print(fun04(fun03(fun01(num_a+num_b), fun01(num_a-num_c), fun02(fun01(num_d**2))), \
        fun02(fun01(num_a-num_b)), fun01(fun01(fun01(fun01(fun01(num_c))))), num_d**8))
def fun01(num_x):
    """Docstring"""
    total = 2*num_x
    return total
def fun02(num_x):
    """Docstring"""
    total = (3*(num_x**4))-(num_x**3)+(2*(num_x**2))+10
    return total
def fun03(num_x, num_y, num_z):
    """Docstring"""
    total = ((num_z+num_x)**2)-(num_x*num_y)+(num_y**2)
    return total
def fun04(num_a, num_b, num_c, num_d):
    """Docstring"""
    total = ((num_a**2)+(num_b**2)-(num_c**2))/((num_d**2)-(2*num_a*num_d)+(2*num_a))
    return total
main(float(input()), float(input()), float(input()), float(input()))

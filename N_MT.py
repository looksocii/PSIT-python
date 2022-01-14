"""M_T"""
def main(num_a, num_b, num_i):
    """Docstring"""
    if abs(num_i-num_a) == abs(num_i-num_b):
        print("Sundaes %d" %abs(num_i-num_a))
    elif abs(num_i-num_a) < abs(num_i-num_b):
        print("Alice %d" %abs(num_i-num_a))
    else:
        print("Bob %d" %abs(num_i-num_b))
main(int(input()), int(input()), int(input()))

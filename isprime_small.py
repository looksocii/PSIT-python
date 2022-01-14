"""isprime_small"""
def main(num, cou):
    """Docstring"""
    if num == 1:
        print("No")
    else:
        for i in range(2, num):
            if num%i == 0:
                cou += 1
        if cou == 0:
            print("Yes")
        else:
            print("No")
main(int(input()), 0)

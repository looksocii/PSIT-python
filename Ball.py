"""Ball"""
def main(num, cou):
    """Docstring"""
    while 1:
        if num < 0.01:
            break
        num = num*(3/5)
        cou += 1
    print(cou-1)
main(float(input()), 0)

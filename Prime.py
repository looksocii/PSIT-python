"""isprime_small"""
def main(num):
    """Docstring"""
    if num == 1:
        print("No")
    else:
        for i in range(2, num-1):
            if num%i == 0:
                print("No")
                break
        else:
            print("Yes")
main(int(input()))

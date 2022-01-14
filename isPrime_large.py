"""isPrime_lerge"""
def main(cou):
    """Docstring"""
    num = int(input())
    state = "YES"
    for i in range(2, (int((num**0.5)//2))):
        if num % i == 0:
            cou += 1
            break
    if cou == 0 and num != 1 and num != 0:
        print("Yes")
    else:
        print("No")
main(0)

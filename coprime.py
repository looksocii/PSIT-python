"""coprime"""
def main(num1, num2, ans):
    """Docstring"""
    lst = []
    for i in range(num1, num2+1):
        if is_(i) == 1:
            lst.append(i)
            ans += is_(i)
    print("Is Prime :", lst)
    print(ans)
def is_(num):
    cou = 0
    if num == 1:
        cou = 0
    else:
        for i in range(2, num):
            if num%i == 0:
                cou += 1
    if cou != 0:
        return 0
    else:
        if num != 1:
            return 1
main(int(input()), int(input()), 0)

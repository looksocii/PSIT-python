"""Refrigerator"""
def main(num, day, num2):
    """Docstring"""
    lst = input().split()
    lst = [int(i) for i in lst]
    while 1:
        if min(lst) == 0:
            break
        for i in range(num):
            lst[i] -= 1
        for j in lst:
            if j == min(lst):
                lst[num2] += 1
                num2 = 0
                break
            num2 += 1
        day += 1
    print(day)
main(int(input()), 0, 0)

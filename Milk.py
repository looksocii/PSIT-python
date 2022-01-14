"""Milk"""
def main(price, pro, free, money):
    """Docstring"""
    kud = money//price
    fhar = kud
    while fhar >= pro and pro > 0:
        diy_1 = (fhar//pro)*free
        diy_2 = fhar%pro
        kud += diy_1
        fhar = diy_1 + diy_2
    print(kud)
main(int(input()), int(input()), int(input()), int(input()))

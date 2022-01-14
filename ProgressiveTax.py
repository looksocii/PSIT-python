"""ProgressiveTax"""
def main(money, num, ans):
    """Docsrting"""
    if money > 4000000:
        num = 7
        ans += (money-4000000)*((num*5)/100)
        money = money-(money-4000000)
    if money > 2000000:
        num = 6
        ans += (money-2000000)*((num*5)/100)
        money = money-(money-2000000)
    if money > 1000000:
        num = 5
        ans += (money-1000000)*((num*5)/100)
        money = money-(money-1000000)
    if money > 750000:
        num = 4
        ans += (money-750000)*((num*5)/100)
        money = money-(money-750000)
    if money > 500000:
        num = 3
        ans += (money-500000)*((num*5)/100)
        money = money-(money-500000)
    if money > 300000:
        num = 2
        ans += (money-300000)*((num*5)/100)
        money = money-(money-300000)
    if money > 150000:
        num = 1
        ans += (money-150000)*((num*5)/100)
        money = money-(money-150000)
    if num == 0:
        print(0)
    else:
        print(int(ans))
main(int(input()), 0, 0)

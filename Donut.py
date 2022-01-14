"""Donut"""
def main():
    """what is the donut"""
    price = int(input())
    donut = int(input())
    free = int(input())
    want = int(input())
    pack = donut+free
    packs = want//pack
    remains = want%pack
    donuts = 0
    cost = 0
    if remains >= donut:
        packs += 1
    else:
        donuts += remains
        cost += (remains*price)
    donuts += (pack*packs)
    cost += (packs*donut*price)
    print("%d %d" %(cost, donuts))
main()

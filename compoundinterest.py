"""compoundinterest"""
def main(money, bri, year):
    """Docsrting"""
    for _ in range(year):
        money += (money*(bri/100))
    print("%.2f" %money)
main(int(input()), float(input()), int(input()))

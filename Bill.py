"""Bill"""
def main(price):
    """Docstring"""
    ser = price*0.1
    if ser <= 50:
        ser = 50
    elif ser >= 1000:
        ser = 1000
    vat = (price+ser)*0.07
    total = price+ser+vat
    print("%.2f" %total)
main(int(input()))

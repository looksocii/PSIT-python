"""M_T"""
def main(price, but, lod, add):
    """Docstring"""
    pro = (price+add)*(lod/100)
    jay = ((price+add)-pro)
    if price == but:
        if add > 0:
            print("No %.3f" %abs(price-jay))
        else:
            print("Yes")
    elif add == 0 or (jay-pro) <= price:
        print("Yes")
    elif jay > price:
        print("No %.3f" %(jay-price))
    else:
        print("Yes %.3f" %(price-jay))
main(float(input()), float(input()), float(input()), float(input()))

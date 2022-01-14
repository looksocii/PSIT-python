"""S_P_R"""
def main(spr, tam_a, tam_b):
    """Docstring"""
    while len(spr) != 0:
        ans = spr[:2]
        spr = spr[2:]
        if ans == "SP" or ans == "PR" or ans == "RS":
            tam_a += 1
        if ans == "SR" or ans == "PS" or ans == "RP":
            tam_b += 1
    if tam_a > tam_b:
        print("A win %d-%d" %(tam_a, tam_b))
    elif tam_a < tam_b:
        print("B win %d-%d" %(tam_b, tam_a))
    else:
        print("DRAW %d" %tam_a)
main(input(), 0, 0)

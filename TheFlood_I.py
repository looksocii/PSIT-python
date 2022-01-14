"""TheFlood_I"""
def main(txt, cou):
    """Docstring"""
    txt = txt.split()
    txt = [int(i) for i in txt]
    while 1:
        if min(txt) == 0:
            break
        else:
            for i in range(len(txt)):
                txt[i] = txt[i]-1
            for k in range(len(txt)):
                if txt[k] == min(txt):
                    txt[k] = txt[k]+1
                    break
        cou += 1
    print(cou)
main(input(), 0)

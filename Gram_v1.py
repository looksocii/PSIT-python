"""Gram_v1"""
def main(txt, lst, string, last, num):
    """Docstring"""
    for i in range(len(txt)):
        if (i+1) > len(txt)-1:
            pass
        else:
            string += txt[i]+txt[i+1]
        if string != "":
            lst.append(string)
            string = ""
    lst.sort()
    dic1 = {}
    dic2 = {}
    for i in lst:
        if i != last:
            num += 1
            if num > 0:
                if last != "":
                    num -= 1
                    dic1 = {num:last}
                    dic2.update(dic1)
                    num = 1
        else:
            num += 1
        last = i
    dic1 = {num:last}
    dic2.update(dic1)
    maxim = max(dic2.keys())
    print(dic2[maxim])
    print(maxim)
main(input(), [], "", "", 0)

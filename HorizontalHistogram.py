"""Horizontal_Histogram"""
def main(txt, lst2, lst3, total, num):
    """Docstring"""
    lst = list(txt)
    for i in lst:
        if ord(i) >= 65 and ord(i) <= 90:
            lst3.append(i)
        else:
            lst2.append(i)
    lst2.sort()
    lst3.sort()
    lst2 = fun(lst2, "", [], "")
    lst3 = fun(lst3, "", [], "")
    for i in lst2:
        total.append(i)
    for i in lst3:
        total.append(i)
    vul = ""
    total.remove("")
    print(total)
    for i in total:
        for _ in i:
            if len(vul) == num:
                num += 6
                vul += "|"
                vul += "-"
            else:
                vul += "-"
        if len(vul) > 0:
            print("%s : %s" %(i[-1:], vul))
            vul = ""
            num = 5
def fun(lst, string, lst4, last):
    """Docstring"""
    for i in lst:
        if i != last and string != "":
            lst4.append(string)
            string = ""
            string += i
        else:
            string += i
        last = i
    lst4.append(string)
    return lst4
main(input(), [], [], [], 5)

"""Vertical_Histogram"""
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
    if "" in total:
        total.remove("")
    lst_num = []
    for i in total:
        lst_num.append(len(i))
    dic = {}
    for i in range(len(lst_num)):
        dic[total[i][0]] = lst_num[i]
    print(dic)
    print(total)
    print(lst_num)
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

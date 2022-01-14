"""Classify"""
def main(lst, last, lst2, lst3, last2):
    """Docstring"""
    while 1:
        txt = input()
        if txt == "END":
            break
        else:
            lst.append(txt)
    lst.sort()
    for i in lst:
        if i[0:4] != last[0:4]:
            lst3.append(lst2)
            lst2 = []
            lst2.append(i)
        else:
            lst2.append(i)
        last = i
    lst3.append(lst2)
    lst3.remove([])
    for i in lst3:
        if len(i) > 1:
            if i[0][0:2] == last2:
                print("--", int(i[0][2:4]), len(i))
            else:
                print(i[0][0:2], int(i[0][2:4]), len(i))
                last2 = i[0][0:2]
        else:
            if i[0][0:2] == last2:
                print("--", int(i[0][2:4]), 1)
            else:
                print(i[0][0:2], int(i[0][2:4]), 1)
                last2 = i[0][0:2]
main([], "", [], [], "")

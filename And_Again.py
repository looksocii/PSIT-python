"""And_Again"""
def main(txt, var, lst, lst2):
    """Docstring"""
    for i in txt:
        if i == " " or i == ".":
            lst.append(var)
            var = ""
        else:
            var += i
    for i in lst:
        if (i.count("a")+i.count("e")+i.count("i")+\
            i.count("o")+i.count("u")) >= 2:
            lst2.append(i)
    lst2.sort()
    if lst2 == []:
        print("Nope")
    else:
        for i in lst2:
            print(i)
main(input(), "", [], [])

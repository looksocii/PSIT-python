"""Olympic"""
def main(num, scor, lst1, lst2,num2):
    """Docstring"""
    for _ in range(num):
        txt = input()
        for i in txt:
            if i.isdigit() == 1:
                scor += int(i)
        lst1.append(txt)
        lst2.append(scor)
        scor = 0
    lst2.sort()
    for i in lst2:
        while i in lst2:
            for j in lst1:
                if j.isdigit() == 1:
                    scor += int(j)
            if i == scor:
                print(num2, j, lst2.pop(i))
                num2 += 1
main(int(input()), 0, [], [], 1)

"""BusStop_I"""
def main(num1, num2, ans, lst_ans, cou):
    """Docstring"""
    for b in range(1, num2+1):
        lst = input().split()
        lst.remove(lst[0])
        if len(lst_ans) != num1:
            for i in lst:
                if len(lst_ans) < num1:
                    if int(i) > b:
                        lst_ans.append(i)
                else:
                    break
        for n in lst_ans:
            if int(n) == b+1:
                lst_ans.remove(n)
                cou += 1
        if str(b+1) in lst_ans:
            lst_ans.remove(str(b+1))
            cou += 1
    for m in lst_ans:
        if int(m) == num2:
                lst_ans.remove(m)
                cou += 1
    print(cou)
main(int(input()), int(input()), 0, [], 0)

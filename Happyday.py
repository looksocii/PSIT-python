"""Happyday"""
def main(num, lst, string, ans):
    """Docstring"""
    for i in num:
        if i == ",":
            lst.append(int(string))
            string = ""
        else:
            string += i
    lst.append(int(string))
    last = lst[0]
    for i in lst:
        if i >= 80:
            ans += 1
        elif i >= 20 and (i-last) >= 10:
            ans += 1
        last = i
    print(ans)
main(input(), [], "", 0)

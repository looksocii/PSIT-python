"""Flatten"""
def main(txt, lst, string, ans):
    """Docstring"""
    for i in txt:
        if i == "-":
            string += i
        if i.isdigit() == 0:
            if string != "" and string != "-":
                lst.append(string)
                string = ""
        else:
            string += i
    for i in lst:
        i = int(i)
        ans.append(i)
    ans.sort()
    print(ans[::-1])
main(input(), [], "", [])

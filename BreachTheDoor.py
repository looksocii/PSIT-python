"""BreachTheDoor"""
def main(paragraph, txt, lst, ans):
    """Docstring"""
    for i in paragraph:
        if i.isalpha() == False:
            lst.append(txt)
            txt = ""
        else:
            txt += i
    lst.append(txt)
    for i in lst:
        if i == lst[(len(lst)-1)] and len(i) > 6:
            ans += i
        elif len(i) > 6:
            ans += i+" "
    print(ans)
main(input(), "", [], "")

"""Run_Length_Decoding"""
def main(key, num, lst, ans):
    """Docstring"""
    for i in key:
        if i.isalpha() == False:
            num += i
        else:
            num += i
            lst.append(num)
            num = ""
    for i in lst:
        ans += i[-1:]*int(i[:-1])
    print(ans)
main(input(), "", [], "")

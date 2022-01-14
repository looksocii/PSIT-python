"""Run_Length_Encoding"""
def main(txt, last, string, lst, ans):
    """Docstring"""
    for i in txt:
        if i != last and string != "":
            lst.append(string)
            string = ""
            string += i
        else:
            string += i
        last = i
    lst.append(string)
    for i in lst:
        ans += str(len(i))+i[:1]
    print(ans)
main(input(), "", "", [], "")

"""Remove_Tag"""
def main(txt, last, string, str_ans):
    """Docstring"""
    for i in txt:
        if i == "<" and len(string) != 0:
            str_ans += string+" "
            string = ""
            last = ""
        if last == ">":
            string += i
            if string == "<br />" or string == "<p>":
                string = ""
        if i == ">":
            last = ">"
    if string == ".":
        str_ans += string
    str_ans = str_ans.split()
    print(str_ans)
main(input(), "", "", "")

"""Seeker"""
def main(txt, total, string):
    """Docstring"""
    for i in txt:
        if i.isdigit() == 1:
            string += i
        else:
            if len(string) > 0:
                total += int(string)
                string = ""
    if string.isdigit() == 1:
        total += int(string)
    print(total)
main(input(), 0, "")

"""Inverter"""
def main(txt, string):
    """Docstring"""
    for i in txt:
        if i == "0":
            string += "1"
        else:
            string += "0"
    if int(string) == 0:
        pass
    else:
        print(string)
main(input(), "")

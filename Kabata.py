"""Kabata"""
def main(num, lst, lst2):
    """Docsrting"""
    for _ in range(num):
        txt = input()
        while len(txt) != 0:
            if txt[:5] == "bakka":
                lst.append(txt[:5])
                txt = txt[5:]
            elif txt[:4] == "baka":
                lst.append(txt[:4])
                txt = txt[4:]
            else:
                lst.append(txt[:2])
                txt = txt[2:]
        for i in lst:
            if i == "ka" or i == "ba" or i == "ta" or i == "bakka":
                lst2.append("1")
            else:
                lst2.append("0")
        if "0" not in lst2:
            print("yes")
        else:
            print("no")
        lst = []
        lst2 = []
main(int(input()), [], [])

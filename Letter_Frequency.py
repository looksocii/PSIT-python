"""Letter_Frequency"""
def main(txt, dic):
    """Docstring"""
    for i in txt:
        if i.isalpha():
            if i in dic:
                dic[i] += 1
            else:
                dic[i] = 1
    maxx = max(dic.values())
    for i in dic:
        if dic[i] == maxx:
            print(i)
main(input().lower(), {})

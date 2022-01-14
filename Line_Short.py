"""Line_Short"""
def main(num, dic):
    """Docstring"""
    for _ in range(num):
        txt = input()
        dic[len(txt)] = txt
    lst = sorted(dic)
    for i in lst:
        print(dic[i])
main(int(input()), {})

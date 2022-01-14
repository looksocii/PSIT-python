"""Parallelogram"""
def main(txt):
    """Docstring"""
    num = len(txt)
    for i in range(1, num+1):
        num -= 1
        print(" "*num+txt[:i])
    for j in range(1, len(txt)+1):
        print(txt[j:])
main(input())

"""Missing_Numbers"""
def main():
    """Docstring"""
    lst = []
    num = int(input())
    for i in range(num):
        number = int(input())
        if number == 0:
            break
        lst.append(number)
    for i in range(1, num+1):
        if i not in lst:
            print(i)
main()

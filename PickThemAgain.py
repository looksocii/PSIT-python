"""PickThemAgain"""
def main(lst, lst2):
    """Docstring"""
    lst = lst[len(lst)::-1]
    for i in lst:
        if int(i)%3 == 0 or int(i)%5 == 0:
            lst2.append(i)
    if len(lst2) > 0:
        for i in lst2:
            print(int(i))
    else:
        print("Nope")
main(input().split(" "), [])

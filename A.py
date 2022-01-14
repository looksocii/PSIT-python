"""Quiz"""
def main():
    """Docstring"""
    data1 = int(input())
    data2 = input()
    data3 = input()
    if data2 == "left":
        print(data3)
    elif data2 == "right":
        print("%s" %data3.rjust(data1))
    elif data2 == "center":
        if len(data3)%2 == 0:
            print("%s" %data3.center(data1))
        else:
            print(" %s" %data3.center(data1))
main()

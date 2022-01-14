"""Quiz"""
def main():
    """Docstring"""
    num = int(input())
    if num%4 != 0:
        print("No")
    elif num%4 == 0 and num%100 == 0 and num%400 != 0:
        print("No")
    elif num%4 == 0 and num%100 != 0:
        print("Yes")
    elif num%4 == 0 and num%100 == 0:
        print("Yes")
main()

"""Quiz"""
def main():
    """Docstring"""
    num = input()
    total = 0
    for i in num:
        total += int(i)
    total += ((int(num)%1000)*10)
    if total < 1000:
        total += 1000
        print("%04d" %(total%10000))
    else:
        print("%04d" %(total%10000))
main()

"""Duplicate_I"""
def main(num1, num2, set1, set2):
    """Docstring"""
    for _ in range(num1):
        data = int(input())
        set1.add(data)
    for _ in range(num2):
        data = int(input())
        set2.add(data)
    total = set1&set2
    total = list(total)
    total.sort()
    total.reverse()
    if total != []:
        for i in total:
            print(i)
    else:
        print("Nope")
main(int(input()), int(input()), set({}), set({}))

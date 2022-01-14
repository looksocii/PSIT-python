"""Difference"""
def main(set1, set2, lst1, lst2):
    """Docstring"""
    for i in range(set1):
        lst1.append(int(input()))
    for i in range(set2):
        lst2.append(int(input()))
    print(*sorted(set(lst1)-set(lst2)))
main(int(input()), int(input()), [], [])

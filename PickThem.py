"""PickThem"""
import json
def main(lst, lst2):
    """Docstring"""
    for i in lst:
        if i%2 == 0:
            lst2.append(i)
    if len(lst2) == 0:
        print("Nope")
    else:
        for i in lst2:
            print(i)
main(json.loads(input()), [])

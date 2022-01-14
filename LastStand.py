"""Pick"""
import json
def main(lst, lst2):
    """Docstring"""
    for i in lst:
        lst2.append(str(i)[-1:])
    for i in lst2:
        print(i)
main(json.loads(input()), [])

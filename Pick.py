"""Pick"""
import json
def main(dic, key):
    """Docstring"""
    if key in dic.keys():
        print("Yes")
        print(dic[key])
    else:
        print("No")
main(json.loads(input()), input())

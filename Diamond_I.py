"""Diamond_I"""
def main(num1, num2, lst):
    """Docstring"""
    for i in range(num2):
        lst.append(0)
    for i in range(num1):
        txt = input()
        txt = txt.split()
        txt = [int(i) for i in txt]
        for i in range(num2):
            lst[i] = lst[i] + txt[i]
    print(max(lst))
main(int(input()), int(input()), [])

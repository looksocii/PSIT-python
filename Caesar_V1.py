"""Caesar_V1"""
def main(num, txt, string):
    """Docstring"""
    lst1 = [i for i in range(65, 91)]
    lst2 = [i for i in range(97, 123)]
    for i in txt:
        if ord(i) in lst1:
            if ord(i)+num < 65:
                string += chr(91-(65-(ord(i)+num)))
            elif ord(i)+num > 90:
                string += chr(((ord(i)+num)-90)+64)
            else:
                string += chr(ord(i)+num)
        elif ord(i) in lst2:
            if ord(i)+num < 97:
                string += chr(123-(97-(ord(i)+num)))
            elif ord(i)+num > 122:
                string += chr(((ord(i)+num)-122)+96)
            else:
                string += chr(ord(i)+num)
        else:
            string += i
    print(string)
main(int(input()), input(), "")

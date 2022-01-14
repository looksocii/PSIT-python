"""Triangle"""
def main(num):
    """Docstring"""
    for j in range(num, 0, -1):
        print((" "*((j*2)-2))+("%02d" %j)+(" "*\
            (((num-j)*4)-2))+(("%02d" %j) if j != num else ""))
main(int(input()))

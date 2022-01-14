"""MacaronBoxSML"""
def main(num):
    """Docsrting"""
    low = 0 #6
    medium = 0 #12
    high = 0 #24
    if num%24 == 0:
        high += num/24
    else:
        high += num//24
        num = num%24
        if num%12 == 0:
            medium += num/12
        else:
            if num%6 == 0:
                low += num/6
            else:
                medium += num//12
                low += num%12
    print("%d\n%d\n%d" %(low, medium, high))
main(int(input()))

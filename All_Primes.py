"""All_Primes"""
def main(loop, num):
    """Docstring"""
    for i in range(2, loop+1):
        if i == 1:
            pass
        else:
            for j in range(2, num-1):
                if num%j == 0:
                    break
            else:
                num += 1
    print(num)
main(int(input()), 0)

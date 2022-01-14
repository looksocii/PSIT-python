"""CoinChangev1"""
def main(num):
    """Docstring"""
    con1 = num//25
    con2 = (num%25)//10
    con3 = ((num%25)%10)//5
    con4 = ((num%25)%10)%5
    print(con1+con2+con3+con4)
main(int(input()))

"""Quiz"""
def main():
    """Docstring"""
    avg = float(input())
    num1 = float(input())
    num2 = float(input())
    num3 = float(input())
    num4 = (avg*4)-(num1+num2+num3)
    if num1+num2+num3+num4 > 15000:
        print("Overweight")
    elif (avg/2) > num1 or num1 > avg+(avg/2):
        print("Unbalance")
    elif (avg/2) > num2 or num2 > avg+(avg/2):
        print("Unbalance")
    elif (avg/2) > num3 or num3 > avg+(avg/2):
        print("Unbalance")
    elif (avg/2) > num4 or num4 > avg+(avg/2):
        print("Unbalance")
    else:
        print("Pass %.2f" %num4)
main()

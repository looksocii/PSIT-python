"""Diginity_Midterm2014"""
def main():
    """Docstring"""
    ans = 0
    while 1:
        num = int(input())
        if num == 0:
            break
        else:
            while 1:
                for i in str(num):
                    ans += int(i)
                if ans > 0 and ans < 10:
                    print(ans)
                    ans = 0
                    break
                else:
                    num = ans
                    ans = 0
main()

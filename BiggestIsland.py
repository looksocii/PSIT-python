"""BiggestIsland"""
def main(num, lst, maping, ans, total):
    """Docstring"""
    num1, num2 = int(num.split()[0]), int(num.split()[1])
    for _ in range(num2):
        maping.append(0)
    for _ in range(num1):
        lst.append(input().split())
    for m in lst:
        for n in range(len(m)):
            maping[n] += int(m[n])
    last = ""
    for i in maping:
        if i == 0 and ans != 0:
            total.append(ans)
            ans = 0
        else:
            ans += i
    print(max(total))
main(input(), [], [], 0, [])

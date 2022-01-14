"""Island"""
def main(num, lst, maping, totalmap):
    """Docstring"""
    num1, num2 = int(num.split()[0]), int(num.split()[1])
    for _ in range(num2):
        maping.append("0")
    for _ in range(num1):
        lst.append(input().split())
    for m in lst:
        if "1" not in m:
            if "1" in maping:
                totalmap.append(maping)
                maping = ["0" for _ in range(num2)]
        else:
            for n in range(len(m)):
                if m[n] == "1":
                    maping[n] = "1"
    if "1" in maping:
        totalmap.append(maping)
    kok = 0
    for i in totalmap:
        last = ""
        for j in i:
            if last == "1" and j == "0":
                kok += 1
            last = j
        if last == "1":
            kok += 1
    print(kok)
main(input(), [], [], [])

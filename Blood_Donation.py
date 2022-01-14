"""Blood_Donation"""
def main(cou, ans):
    """Docstring"""
    age = int(input())
    wigth = int(input())
    num = int(input())
    if wigth >= 45:
        cou += 1
    if num == 0:
        if age <= 55:
            cou += 1
    else:
        cou += 1
    if age >= 17 and age <= 70:
        cou += 1
        if age == 17 or age >= 60:
            ans = 1
            if input() == "True":
                cou += 1
    if ans == 1 and cou == 4:
        print("Yes")
    elif cou == 3 and ans == 0:
        print("Yes")
    else:
        print("No")
main(0, 0)

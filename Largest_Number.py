"""Largest_Number"""
def main(num1, num2, num3, num_ans):
    """Docstring"""
    one = int(str(num1)+str(num2)+str(num3))
    two = int(str(num1)+str(num3)+str(num2))
    thr = int(str(num2)+str(num1)+str(num3))
    fou = int(str(num2)+str(num3)+str(num1))
    fiv = int(str(num3)+str(num1)+str(num2))
    six = int(str(num3)+str(num2)+str(num1))
    if one > num_ans:
        num_ans = one
    if two > num_ans:
        num_ans = two
    if thr > num_ans:
        num_ans = thr
    if fou > num_ans:
        num_ans = fou
    if fiv > num_ans:
        num_ans = fiv
    if six > num_ans:
        num_ans = six
    print(num_ans)
main(int(input()), int(input()), int(input()), 0)

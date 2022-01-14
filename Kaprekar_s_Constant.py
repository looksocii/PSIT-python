"""Kaprekar's_Constant"""
def main(num_in, cout):
    """Docstring"""
    ans = num_in
    while ans = 6174:
        ans =  number(ans)[0] - number(ans)[1]
def number(num_out):
    one, two, thr, fou = 0, 0, 0, 0
    for i in num:
        i = int(i)
        if i >= one:
            fou = thr
            thr = two
            two = one
            one = i
        elif one > i >= two:
            fou = thr
            thr = two
            two = i
        elif two > i >= thr:
            fou = thr
            thr = i
        elif thr > i >= fou:
            fou = i
    return str(one)+str(two)+str(thr)+str(fou), str(fou)+str(thr)+str(two)+str(one)
main(input(), 0)

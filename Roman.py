"""Roman"""
def main(txt, ans):
    """Docstring"""
    rom = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
    for i in txt:
    	ans += rom[i]
    print(ans)
main(input(), 0)

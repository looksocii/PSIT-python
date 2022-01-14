"""FOR!F-Ball"""
def main(txt, loc):
    """Docstring"""
    for i in txt:
        if i == "A" or i == "B":
            if loc == 1 and i == "A":
                loc += 1
            elif loc == 2 and i == "A":
                loc -= 1
            elif loc == 2 and i == "B":
                loc += 1
            elif loc == 3 and i == "B":
                loc -= 1
            else:
                pass
        elif i == "C":
            if loc == 3:
                loc -= 2
            elif loc == 1:
                loc += 2
            else:
                pass
    print(loc)
main(input(), 1)

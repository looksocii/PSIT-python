"""Four_Directions"""
def main():
    """Docstring"""
    txt = input()
    r01, r02, r03, r04, r05 = "", "", "", "", ""
    for i in txt:
        if i == "U":
            r01 += "  *   "
            r02 += " ***  "
            r03 += "* * * "
            r04 += "  *   "
            r05 += "  *   "
        elif i == "D":
            r01 += "  *   "
            r02 += "  *   "
            r03 += "* * * "
            r04 += " ***  "
            r05 += "  *   "
        elif i == "L":
            r01 += "  *   "
            r02 += " *    "
            r03 += "***** "
            r04 += " *    "
            r05 += "  *   "
        elif i == "R":
            r01 += "  *   "
            r02 += "   *  "
            r03 += "***** "
            r04 += "   *  "
            r05 += "  *   "
    print("%s\n%s\n%s\n%s\n%s" %(r01, r02, r03, r04, r05))
main()

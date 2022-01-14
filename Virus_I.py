"""Virus_I"""
def main():
    """Docstring"""
    txt = input()
    virus = 0
    for i in txt:
        if i == "o":
            virus += 1
        else:
            pass
    print(virus)
main()

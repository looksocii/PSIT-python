"""Turnstile"""
def main():
    """Docstring"""
    total = ""
    while True:
        cmmand = input()
        if cmmand == "END":
            break
        else:
            total += cmmand
    print(total.count("CP"))
main()

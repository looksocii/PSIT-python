"""Gift_III"""
def main():
    """Docstring"""
    sub = 0
    most = 0
    gift = int(input())
    for _ in range(gift):
        weight = int(input())
        if weight > most:
            sub = most
            most = weight
        if weight > sub and weight < most:
            sub = weight
    if gift == 0 or gift == 1 or most == 0 or sub == 0:
        print("Exit")
    else:
        print(sub)
main()

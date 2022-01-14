"""Dart"""
def main(num, ans):
    """Docstring"""
    for _ in range(num):
        loc = input()
        num_x2, num_y2 = int(loc.split()[0]), int(loc.split()[1])
        total = (((0-num_x2)**2)+((0-num_y2)**2))**0.5
        if total > 8 and total <= 10:
            ans += 1
        elif total > 6 and total <= 8:
            ans += 2
        elif total > 4 and total <= 6:
            ans += 3
        elif total > 2 and total <= 4:
            ans += 4
        elif total <= 2:
            ans += 5
    print(ans)
main(int(input()), 0)

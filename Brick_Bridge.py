"""Brick_Bridge"""
def main(low, high, want):
    """Docsrting"""
    if low+(high*5) < want:
        print(-1)
    else:
        if abs(((want//5)*5)-want) <= low:
            print(abs(((want//5)*5)-want))
        else:
            print(-1)
main(int(input()), int(input()), int(input()))

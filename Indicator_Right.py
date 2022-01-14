"""Quiz"""
def main():
    """Docstring"""
    num_1 = int(input())
    num_2 = int(input())
    for i in range(num_2//2):
        print((" "*i)+("*"*num_1), end="")
        print()
    for j in range((num_2//2), -1, -1):
        print((" "*j)+("*"*num_1), end="")
        print()
main()

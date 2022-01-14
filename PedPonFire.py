"""PedPonFire"""
def main(num, lst, number, lst2):
    """Docstring"""
    for _ in range(num):
        lst.append(int(input()))
    num_k = int(input())
    for i in lst:
        for k in range(len(lst)):
            if k != number:
                if i+lst[k] == num_k:
                    if [i, lst[k]] not in lst2:
                        lst2.append([i, lst[k]])
        number += 1
    print(len(lst2))
main(int(input()), [], 0, [])

"""Sequence_IX"""
def main(num):
    """main"""
    for i in range(1, num+1):
        #print(i)
        for _ in range(num-i, 0, -1):
            print('  ', end=' ')
        for k in range(1, i+1):
            print('%02d'%k, end=' ')
        if i > 1:
            for j in range(i-1, 0, -1):
                print('%02d'%j, end=' ')
        print(end='\n')
main(int(input()))

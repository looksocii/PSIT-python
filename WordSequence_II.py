"""WordSequence_II"""
def main(lock, key):
    """Docsrting"""
    if len(lock) == len(key):
        print(lock)
        for i in range(len(lock)):
            txt = key[i]+lock[i:]
            print(txt)
main(input(), input())

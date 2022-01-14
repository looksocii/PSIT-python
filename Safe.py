"""Safe"""
def main(key, lock, ans):
    """Docsrting"""
    for i in range(len(lock)):
        if abs(ord(lock[i])-ord(key[i])) > abs(26-abs(ord(lock[i])-ord(key[i]))):
            ans += (26-abs(ord(lock[i])-ord(key[i])))
        else:
            ans += abs(ord(lock[i])-ord(key[i]))
    print(ans)
main(input(), input(), 0)

"""Black_Jack"""
def main():
    """Docstring"""
    num = int(input())
    score = 0
    for _ in range(num):
        card = input()
        if card == "J" or card == "Q" or card == "K":
            card = 10
            score += card
        elif card == "A":
            if num == 2:
                if score <= 10:
                    score += 11
                elif score == 20:
                    score += 1
                else:
                    score += 1
            if num == 3:
                if score == 0:
                    score += 11
                elif score == 11:
                    score += 1
                elif score == 12:
                    score += 1
                elif score == 20:
                    score += 1
                elif score <= 10:
                    score += 11
                else:
                    score += 1
        else:
            score += int(card)
    print(score)
main()

"""  Circular I """
def main(count, var):
    """ main """
    for _ in range(count):
        num = float(input())
        if num >= 95 and num <= 100:
            var += 4.0
        elif num >= 90 and num <= 94:
            var += 3.5
        elif num >= 85 and num <= 89:
            var += 3.0
        elif num >= 80 and num <= 84:
            var += 2.5
        elif num >= 75 and num <= 79:
            var += 2.0
        elif num >= 70 and num <= 74:
            var += 1.5
        elif num >= 65 and num <= 69:
            var += 1.0
        elif num >= 60 and num <= 64:
            var += 0.5
        elif num >= 0 and num < 60:
            var += 0.0
    var /= count
    print('%.2f'%(int(var*100)/100))
main(int(input()), 0)

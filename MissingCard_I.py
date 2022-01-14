"""MissingCard_I"""
def main(card_me):
    """Docstring"""
    card = ['AS', 'AH', 'AD', 'AC', 'KS', 'KH', 'KD', 'KC', \
    'QS', 'QH', 'QD', 'QC', 'JS', 'JH', 'JD', 'JS', '10S', \
    '10H', '10D', '10C', '9S', '9H', '9D', '9C', '8S', '8H', \
    '8D', '8C', '7S', '7H', '7D', '7C', '6S', '6H', '6D', '6C', \
    '5S', '5H', '5D', '5C', '4S', '4H', '4D', '4C', '3S', '3H', \
    '3D', '3C', '2S', '2H', '2D', '2C']
    for _ in range(51):
        card_input = input()
        card_me.append(card_input)
    print(card_me)
    for i in card_me:
        if i not in card:
            print(i)
main([])

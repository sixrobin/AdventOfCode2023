import functools

symbols_order = '23456789TJQKA'
pattern_to_type = ['11111', '1112', '122', '113', '23', '14', '5']


def hand_type(h):
    cards = {}
    for c in h:
        if c in cards:
            cards[c] += 1
        else:
            cards[c] = 1

    counts = list(cards.values())
    counts.sort()
    pattern = ''.join([str(count) for count in counts])
    return pattern_to_type.index(pattern)


def compare_hands(ha, hb):
    ha = ha[0]
    hb = hb[0]

    type_diff = hand_type(ha) - hand_type(hb)
    if type_diff != 0:
        return type_diff

    # Both hands are the same type, compare using the first different card.
    for i in range(5):
        if ha[i] != hb[i]:
            return symbols_order.index(ha[i]) - symbols_order.index(hb[i])

    print(f'Hands comparison error: could not compare {ha} and {hb}.')
    return 0


if __name__ == '__main__':
    with open('input_day7.txt') as file:
        lines = file.read().splitlines()
        hands = []
        for line in lines:
            line_split = line.split()
            hand = list(line_split[0].strip())
            bid = int(line_split[1])
            hands.append((hand, bid))

        hands = sorted(hands, key=functools.cmp_to_key(compare_hands))

        total_winnings = 0
        for i in range(len(hands)):
            hand = hands[i]
            total_winnings += hand[1] * (i + 1)

        print(f'Total winnings: {total_winnings}')

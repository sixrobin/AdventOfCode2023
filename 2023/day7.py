import functools
from collections import Counter

symbols_order = 'J23456789TQKA'
pattern_to_type = ['11111', '1112', '122', '113', '23', '14', '5']


def hand_type(h):
    counts = list(Counter(h).values())
    counts.sort()
    pattern = ''.join([str(count) for count in counts])
    return pattern_to_type.index(pattern)


def compare_hands(ha, hb):
    # Tuple second element.
    type_diff = hand_type(ha[1]) - hand_type(hb[1])
    if type_diff != 0:
        return type_diff

    # Both hands are the same type, compare using the first different card.
    for x in range(5):
        if ha[0][x] != hb[0][x]:
            return symbols_order.index(ha[0][x]) - symbols_order.index(hb[0][x])

    return 0


def replace_jokers_with_card(h, c):
    for ic in range(len(h)):
        if h[ic] == 'J':
            h[ic] = c


def replace_jokers(h):
    nh = h.copy()
    counter = Counter(nh)
    jokers_count = counter['J']
    if jokers_count == 0:
        return nh

    counter.pop('J')

    # Find the card with the most occurrences, to replace jokers with it.
    # If two cards have the same occurrences count, use the best of the two.
    card = 'J'
    for c, o in counter.items():
        if o > counter[card] or (o == counter[card] and symbols_order.index(c) > symbols_order.index(card)):
            card = c

    if card == 'J':
        card = symbols_order[-1]

    replace_jokers_with_card(nh, card)
    return nh


if __name__ == '__main__':
    with open('input_day7.txt') as file:
        lines = file.read().splitlines()

        hands = []
        for line in lines:
            line_split = line.split()
            hand = list(line_split[0].strip())
            bid = int(line_split[1])
            hand_replaced_jokers = replace_jokers(hand)
            hands.append((hand, hand_replaced_jokers, bid))

        hands = sorted(hands, key=functools.cmp_to_key(compare_hands))

        total_winnings = 0
        for i in range(len(hands)):
            total_winnings += hands[i][2] * (i + 1)

        print(f'Total winnings: {total_winnings}')

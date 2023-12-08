import functools

symbols_order = 'J23456789TQKA'
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
    jokers_count = nh.count('J')
    if jokers_count == 0:
        return nh

    t = hand_type(nh)

    # For one joker only, it's okay to try out every hand and keep the best one.
    if jokers_count == 1:
        joker_index = nh.index('J')
        best_card = symbols_order[0]
        nh[joker_index] = best_card
        best_type = hand_type(nh)
        for c in range(len(symbols_order)):
            if symbols_order[c] == 'J':
                continue
            nh[joker_index] = symbols_order[c]
            t = hand_type(nh)
            if t > best_type:
                best_card = symbols_order[c]
                best_type = t
            elif t == best_type:
                best_card = symbols_order[c]
        nh[joker_index] = best_card
        return nh

    elif jokers_count == 2 and t != 1:
        if t == 4:  # Full house with 2 jokers, replace them to get five of a kind.
            replace_jokers_with_card(nh, next(other_card for other_card in nh if other_card != 'J'))
        elif t == 2:  # Two pairs, replace them the get four of a kind.
            other_cards = [c for ic, c in enumerate(nh) if c != 'J']
            replacement_card = other_cards[0]
            if other_cards.count(other_cards[1]) >= 2:
                replacement_card = other_cards[1]
            replace_jokers_with_card(nh, replacement_card)
        return nh

    # In every other cases, replace jokers with best card in hand, or by aces for a full jokers hand.
    else:
        best_card = symbols_order[0]
        for c in nh:
            if c != 'J' and symbols_order.index(c) > symbols_order.index(best_card):
                best_card = c
        if best_card == 'J':
            best_card = symbols_order[-1]
        replace_jokers_with_card(nh, best_card)
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

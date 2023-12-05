from numpy import sign

if __name__ == '__main__':
    with open('input_day4.txt') as file:
        lines = file.read().splitlines()
        range_contained_pairs = 0
        overlapping_pairs = 0

        for line in lines:
            pairs = line.split(',')
            pair_a = [int(x) for x in pairs[0].split('-')]
            pair_b = [int(x) for x in pairs[1].split('-')]
            if pair_a[0] < pair_b[0]:
                pair_a, pair_b = pair_b, pair_a

            if pair_b[1] >= pair_a[0]:
                overlapping_pairs += 1
            if pair_a == pair_b or sign(pair_a[0] - pair_b[0]) != sign(pair_a[1] - pair_b[1]):
                range_contained_pairs += 1

        print(f'Range contained pairs: {range_contained_pairs}')
        print(f'Overlapping pairs: {overlapping_pairs}')

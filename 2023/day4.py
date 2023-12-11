if __name__ == '__main__':
    with open('input_day4.txt') as file:
        lines = file.readlines()
        points_sum = 0
        cards_counts = [1] * len(lines)

        for i in range(len(lines)):
            numbers_split = lines[i].split(':')[1].split('|')
            winning_numbers_count = sum(map(lambda x: x in numbers_split[0].split(), numbers_split[1].split()))

            if winning_numbers_count > 0:
                points_sum += 2 ** (winning_numbers_count - 1)
                for j in range(i + 1, i + winning_numbers_count + 1):
                    cards_counts[j] += cards_counts[i]

        cards_count = sum(cards_counts)

        print(f'Cards count: {cards_count}')
        print(f'Points sums: {points_sum}')

if __name__ == '__main__':
    with open('input_day1.txt') as file:
        lines = file.readlines()

        ordered_calories = []
        current_calories = 0

        for line in lines:
            if line != '\n':
                current_calories += int(line)
            else:
                ordered_calories.append(current_calories)
                current_calories = 0

        ordered_calories.sort()

        top_three_sum = 0
        for i in reversed(range(3)):
            top_three_sum += ordered_calories[len(ordered_calories) - (i + 1)]

        print(f'Top 1: {ordered_calories[len(ordered_calories) - 1]}')
        print(f'Top 3 sum: {top_three_sum}')

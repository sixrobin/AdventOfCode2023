if __name__ == '__main__':
    with open('input_day1.txt') as file:
        lines = file.readlines()
        count = 0
        three_measurement_count = 0
        three_measurement_sum = 0

        for i in range(len(lines)):
            line = int(lines[i])
            if i > 0 and line > int(lines[i - 1]):
                count += 1

            previous_three_measurement_sum = three_measurement_sum
            three_measurement_sum -= int(lines[i - 3])

            if i > 2 and three_measurement_sum + line > previous_three_measurement_sum:
                three_measurement_count += 1

            three_measurement_sum += line

        print(f'Increases count: {count}')
        print(f'Three measurement increases count: {three_measurement_count}')

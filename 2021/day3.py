def compute_rate_array(values):
    result = [0] * len(values[0])

    for value_index in range(len(values)):
        value = values[value_index]
        for bit in range(len(result)):
            result[bit] += int(value[bit]) * 2 - 1

    return result


if __name__ == '__main__':
    with open('input_day3.txt') as file:
        lines = file.readlines()
        for i in range(len(lines)):
            lines[i] = lines[i].replace('\n', '')

        rate_array = compute_rate_array(lines)

        for i in range(len(rate_array)):
            rate_array[i] = -1 if rate_array[i] < 0 else 1 if rate_array[i] > 0 else 0

        gamma_rate = ''
        epsilon_rate = ''
        for r in rate_array:
            r = 0 if r < 0 else 1
            gamma_rate += str(r)
            epsilon_rate += str(1 - r)

        oxygen_gen_rating = lines.copy()
        for i in range(len(rate_array)):
            r = 0 if rate_array[i] < 0 else 1
            oxygen_gen_rating = list(filter(lambda o: int(o[i]) == r, oxygen_gen_rating))
            rate_array = compute_rate_array(oxygen_gen_rating)
            if len(oxygen_gen_rating) == 1:
                break

        co2_scrubber_rating = lines.copy()
        for i in range(len(rate_array)):
            r = 0 if rate_array[i] < 0 else 1
            co2_scrubber_rating = list(filter(lambda o: int(o[i]) != r, co2_scrubber_rating))
            rate_array = compute_rate_array(co2_scrubber_rating)
            if len(co2_scrubber_rating) == 1:
                break

        print(f'Oxygen gen rating * CO2 scrubber rating: {int(oxygen_gen_rating[0], 2) * int(co2_scrubber_rating[0], 2)}')
        print(f'Gamma rate * Epsilon rate: {int(gamma_rate, 2) * int(epsilon_rate, 2)}')

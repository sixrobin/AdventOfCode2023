if __name__ == '__main__':
    with open('input_day3.txt') as file:
        lines = file.readlines()

        rate_array = [0] * (len(lines[0]) - 1)

        for i in range(len(lines)):
            line = lines[i]
            for j in range(len(rate_array)):
                rate_array[j] += int(line[j]) * 2 - 1

        for i in range(len(rate_array)):
            rate_array[i] = 0 if rate_array[i] < 0 else 1

        gamma_rate = ''
        epsilon_rate = ''
        for r in rate_array:
            gamma_rate += str(r)
            epsilon_rate += str(1 - r)

        print(int(gamma_rate, 2) * int(epsilon_rate, 2))

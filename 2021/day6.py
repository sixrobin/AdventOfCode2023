if __name__ == '__main__':
    with open('input_day6.txt') as file:
        init_state = file.readlines()[0]
        state = [0 for _ in range(9)]

        for fish in init_state.split(','):
            state[int(fish)] += 1

        for _ in range(80):
            prev_zeros = state[0]

            for i in range(8):
                state[i] = state[i + 1]

            state[8] = prev_zeros
            state[6] += prev_zeros

        print(f'Fishes after 80 days: {sum(state)}')

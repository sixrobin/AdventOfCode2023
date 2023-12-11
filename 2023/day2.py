import re

max_cubes = {'red': 12, 'green': 13, 'blue': 14}

if __name__ == '__main__':
    with open('input_day2.txt') as file:
        lines = file.readlines()
        valid_games_sum = 0
        set_powers_sum = 0

        for line in lines:
            line_split = line.replace(' ', '').split(':')
            reveal_sets = line_split[1].split(';')
            fewer_needed_cubes = {'red': 0, 'green': 0, 'blue': 0}
            invalid_game = False

            for reveal_set in reveal_sets:
                reveals = reveal_set.split(',')
                for reveal in reveals:
                    color = re.sub('[^a-z]', '', reveal)
                    count = re.sub('[^0-9]', '', reveal)
                    fewer_needed_cubes[color] = max(fewer_needed_cubes[color], int(count))

                if not invalid_game:  # If game is already invalid, no need to check for it again.
                    for k, v in max_cubes.items():
                        invalid_game |= fewer_needed_cubes[k] > v
                        if invalid_game:
                            break

            set_power = 1
            for k, v in fewer_needed_cubes.items():
                set_power *= v
            set_powers_sum += set_power

            if not invalid_game:
                valid_games_sum += int(re.sub('[^0-9]', '', line_split[0]))  # Game ID.

        print(f'Valid games IDs sum: {valid_games_sum}')
        print(f'Set powers sum: {set_powers_sum}')

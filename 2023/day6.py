import re

if __name__ == '__main__':
    with open('input_day6.txt') as file:
        lines = file.read().splitlines()

        # Part 1.
        # times = [int(i) for i in lines[0].split() if i.isdigit()]
        # distances = [int(i) for i in lines[1].split() if i.isdigit()]
        # Part 2.
        times = [int(re.sub('[^0-9]', '', lines[0]))]
        distances = [int(re.sub('[^0-9]', '', lines[1]))]

        win_options_product = 1

        for i in range(len(times)):
            race_time = times[i]
            record_dist = distances[i]
            win_options = 0

            hold_duration = 1
            while hold_duration < times[i]:
                dist = hold_duration * (race_time - hold_duration)
                if dist > record_dist:
                    win_options += 1
                elif win_options > 0:
                    break
                hold_duration += 1

            if win_options > 0:
                win_options_product *= win_options

        print(win_options_product)

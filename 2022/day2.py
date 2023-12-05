shape_lookup = {'A': 'X', 'B': 'Y', 'C': 'Z'}
outcomes = {'AX': 0, 'AY': 1, 'AZ': -1, 'BX': -1, 'BY': 0, 'BZ': 1, 'CX': 1, 'CY': -1, 'CZ': 0}
outcome_instructions = {'X': -1, 'Y': 0, 'Z': 1}
shape_points = {'X': 1, 'Y': 2, 'Z': 3}
outcome_points = {-1: 0, 0: 3, 1: 6}


def part_one():
    with open('input_day2.txt') as file:
        lines = file.readlines()
        points = 0

        for line in lines:
            line = line.replace(' ', '')
            line = line.replace('\n', '')
            points += outcome_points[outcomes[line]]
            points += shape_points[line[1]]

        print(points)


def part_two():
    with open('input_day2.txt') as file:
        lines = file.readlines()
        points = 0

        for line in lines:
            line = line.replace(' ', '')
            line = line.replace('\n', '')
            shape = line[1]
            instruction = outcome_instructions[shape]

            for k, v in outcomes.items():
                if k[0] == line[0] and v == instruction:
                    points += shape_points[k[1]] + outcome_points[instruction]

        print(points)


if __name__ == '__main__':
    part_one()
    part_two()

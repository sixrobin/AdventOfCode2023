import sys


def item_priority(item_type):
    priority = ord(str.lower(item_type)) - 96  # ord('a') is 97 -> subtract 96 to get a == 1.
    if str.isupper(item_type):
        priority += 26
    return priority


if __name__ == '__main__':
    with open('input_day3.txt') as file:
        lines = file.readlines()
        priorities_sum = 0
        group_counter = 0
        current_group_badge = ''
        group_badges_sum = 0

        for line in lines:
            line = line.replace('\n', '')
            line_length = len(line)

            first_compartment = set(line[0:line_length//2])
            second_compartment = set(line[line_length//2:])
            common_item_type = first_compartment.intersection(second_compartment)
            priorities_sum += item_priority(common_item_type.pop())

            if current_group_badge == '':
                current_group_badge = set(line)
            else:
                current_group_badge = current_group_badge.intersection(set(line))

            group_counter += 1
            if group_counter == 3:
                group_badges_sum += item_priority(current_group_badge.pop())
                current_group_badge = ''
                group_counter = 0

        print(f'Priorities sum: {priorities_sum}')
        print(f'Group badges sum: {group_badges_sum}')

def any_duplicated_char(s):
    return len(set(filter(lambda c: s.count(c) >= 2, s))) > 0


if __name__ == '__main__':
    with open('input_day6.txt') as file:
        signal = file.readlines()[0]
        packet = signal[0:4]
        message = signal[0:14]
        start_of_packet = -1
        for i in range(4, len(signal)):
            packet = packet[1:] + signal[i]
            message = message[1:] + signal[i]
            if not any_duplicated_char(packet):
                if start_of_packet == -1:
                    start_of_packet = i + 1
                    print(f'Start of packet: {start_of_packet}')
                if not any_duplicated_char(message):
                    print(f'Start of message: {i + 1}')
                    break

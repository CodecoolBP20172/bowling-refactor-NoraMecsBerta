


def get_value(char):
    possible_num_characters = '123456789'
    if char in possible_num_characters:
        for character in possible_num_characters:
            if char == character:
                return int(char)
    elif char == 'X' or char == 'x' or char == '/': #str format?
        return 10
    elif char == '-':
        return 0
    else:
        raise ValueError()


def ten_is_the_value(actual_char, next_char, second_next_char):
    result = 0
    if actual_char == '/':
        result += get_value(next_char)
    elif actual_char == 'X' or actual_char == 'x':
        if second_next_char == '/':
            result += 10 # get_value(game[character+1]) + 10 - get_value(game[character+1])
        else:
            result += get_value(next_char) + get_value(second_next_char)
    return result

def change_half_count_frame(frame, in_first_half, actual_char):
    if not in_first_half:
        frame += 1
    in_first_half = not in_first_half # saját
    if actual_char == 'X' or actual_char == 'x':
        in_first_half = True
        frame += 1
    return frame, in_first_half


def score(game):
    result = 0
    frame = 1
    in_first_half = True
    for character in range(len(game)):
        actual_char = game[character]
        previous_char = game[character-1]
        value_of_the_previous = get_value(previous_char)
        if actual_char == '/':
            result += 10 - value_of_the_previous
        else:
            result += get_value(actual_char)
        if frame < 10: # and get_value(actual_char) == 10: - saját rövidítés LEHET, H KELL
            try:
                result += ten_is_the_value(actual_char, game[character+1], game[character+2])
            except IndexError:
                continue
        frame, in_first_half = change_half_count_frame(frame, in_first_half, actual_char)
    return result
print(score('3/4x12'))



def get_score(char):
    possible_num_characters = '123456789'
    if char in possible_num_characters:
        for character in possible_num_characters:
            if char == character:
                return int(char)
    elif char == 'X' or char == 'x' or char == '/':
        return 10
    elif char == '-':
        return 0
    else:
        raise ValueError()


def extra_score_for_strike(second_next_knockdown, score_of_the_next, score_of_the_second_next, score_of_the_previous):
    plus_score_for_strike = 0
    spare = '/'
    if second_next_knockdown == spare:
        plus_score_for_strike += score_of_the_second_next
    else:
        plus_score_for_strike += score_of_the_next + score_of_the_second_next
    return plus_score_for_strike


def next_try_count_turns(turn, first_try_in_two_tries, actual_knockdown):
    strike = 'x', 'X'
    if not first_try_in_two_tries:
        turn += 1
    first_try_in_two_tries = not first_try_in_two_tries
    if actual_knockdown in strike:
        first_try_in_two_tries = True
        turn += 1
    return turn, first_try_in_two_tries


def score(game):
    total_score = 0
    turn = 1
    turns_of_the_game = 10
    first_try_in_two_tries = True
    series_of_knockdowns = range(len(game))
    spare = '/'
    strike = 'x', 'X'
    for index_of_knockdown in series_of_knockdowns:
        actual_knockdown = game[index_of_knockdown]
        previous_knockdown = game[index_of_knockdown-1]
        score_of_the_actual = get_score(actual_knockdown)
        score_of_the_previous = get_score(previous_knockdown)

        total_score += score_of_the_actual
        if actual_knockdown == spare:
            total_score -= score_of_the_previous
        if turn < turns_of_the_game:
            try:
                if actual_knockdown == spare:
                    extra_score_for_spare = get_score(game[index_of_knockdown+1])
                    total_score += extra_score_for_spare
                if actual_knockdown in strike:
                    total_score += extra_score_for_strike(game[index_of_knockdown+2], get_score(game[index_of_knockdown+1]), get_score(game[index_of_knockdown+2]), score_of_the_previous)
            except IndexError:
                continue
        turn, first_try_in_two_tries = next_try_count_turns(turn, first_try_in_two_tries, actual_knockdown)
    return total_score

#print(score('3/4x12'))
#print(score('xxxxxxxxxxxx'))
#print(score('11111111112222222222'))
print(score('X34-----------'))

def score(game):
    result = 0
    frame = 1
    in_first_half = True
    for record in range(len(game)):
        if game[record] == '/':
            result += 10 - last
        else:
            result += get_value(game[record])
        if frame < 10 and get_value(game[record]) == 10:
            if game[record] == '/':
                result += get_value(game[record+1])
            elif game[record] == 'X' or game[record] == 'x':
                result += get_value(game[record+1])
                if game[record+2] == '/':
                    result += 10 - get_value(game[record+1])
                else:
                    result += get_value(game[record+2])
        last = get_value(game[record])
        if not in_first_half:
            frame += 1
        if in_first_half:
            in_first_half = False
        else:
            in_first_half = True
        if game[record] == 'X' or game[record] == 'x':
            in_first_half = True
            frame += 1
    return result


def get_value(char):
    if char == '1' or char == '2' or char == '3' or \
       char == '4' or char == '5' or char == '6' or \
       char == '7' or char == '8' or char == '9':
        return int(char)
    elif char == 'X' or char == 'x' or char == '/':
        return 10
    elif char == '-':
        return 0
    else:
        raise ValueError()

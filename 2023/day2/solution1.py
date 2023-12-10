import re

MAX_DICE = {
    'red': 12,
    'green': 13,
    'blue': 14
}

def parse_line(line):
    game_info = {}
    parsed_line = re.match(r"Game (\d+):(.*)", line)
    game_info['id'] = int(parsed_line.group(1))

    parsed_rounds = []
    rounds = parsed_line.group(2).split(';')
    # print(rounds)
    for round in rounds:
        colors = round.split(',')
        parsed_colors = {}
        for color in colors:
            parsed_color = re.match(r"(\d+) (red|green|blue)", color.strip())
            parsed_colors[parsed_color.group(2)] = int(parsed_color.group(1))
        parsed_rounds.append(parsed_colors)

    game_info['rounds'] = parsed_rounds

    return game_info

def is_valid_round(round):
    for key, value in round.items():
        if MAX_DICE[key] < value:
            return False
    return True
    
def solve():
    id_total = 0
    with open("input.txt", "r") as f:
        for line in f:
            game_info = parse_line(line)
            valid_game = True
            for round in game_info['rounds']:
                if not is_valid_round(round):
                    valid_game = False
                    break
            if valid_game:
                id_total += game_info['id']

    return id_total

if __name__ == "__main__":
    answer = solve()
    print(answer)

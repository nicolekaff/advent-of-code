from solution1 import parse_line

def solve():
    total_power = 0
    with open("input.txt", "r") as f:
        for line in f:
            game_info = parse_line(line)

            power = 1
            min_dice = {'red': 0, 'green': 0, 'blue': 0}

            for round in game_info['rounds']:
                for key, value in round.items():
                    if min_dice[key] < value:
                        min_dice[key] = value
            
            for value in min_dice.values():
                power *= value
            
            total_power += power

    return total_power

if __name__ == "__main__":
    answer = solve()
    print(answer)

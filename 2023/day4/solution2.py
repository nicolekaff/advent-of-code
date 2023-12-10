import re

lookup = {}

def parse_line(line):
    parsed_line = re.match(r"Card\s+\d+:\s+(.*)\s+\|\s+(.*)", line)  # not perfect
    
    winning = set(parsed_line.group(1).split(" "))
    numbers = parsed_line.group(2).split(" ")

    # jank workaround until i fix my regex
    if '' in winning:
        winning.remove('')

    num_winning = 0
    for num in numbers:
        if num in winning:
            num_winning += 1

    return num_winning

def compute_cards(all_cards, index):
    if index in lookup:
        num_winning = lookup[index]
    else:
        num_winning = parse_line(all_cards[index])
        lookup[index] = num_winning
    
    if num_winning == 0:
        return 0
    else:
        sub_total = 0
        for i in range(index + 1, index + num_winning + 1):
            sub_total += compute_cards(all_cards, i)
        return num_winning + sub_total

    
def solve():
    with open("input.txt", "r") as f:
        all_cards = f.readlines()
    
    total_cards = 0
    for i in range(0, len(all_cards)):
        total_cards += compute_cards(all_cards, i)

    return total_cards + len(all_cards)

if __name__ == "__main__":
    answer = solve()
    print(answer)

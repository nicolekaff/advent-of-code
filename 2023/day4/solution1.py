import re

def parse_line(line):
    card_info = {}
    parsed_line = re.match(r"Card\s+\d+:\s+(.*)\s+\|\s+(.*)", line)  # not perfect
    # print(parsed_line)
    
    card_info['winning'] = set(parsed_line.group(1).split(" "))
    card_info['numbers'] = parsed_line.group(2).split(" ")

    # jank workaround until i fix my regex
    if '' in card_info['winning']:
        card_info['winning'].remove('')

    return card_info
    
def solve():
    total_points = 0
    with open("input.txt", "r") as f:
        for line in f:
            card_info = parse_line(line)
            
            num_winning = 0
            for num in card_info['numbers']:
                if num in card_info['winning']:
                    num_winning += 1

            if num_winning > 0:
                total_points += 2 ** (num_winning - 1)
                        
    return total_points

if __name__ == "__main__":
    answer = solve()
    print(answer)

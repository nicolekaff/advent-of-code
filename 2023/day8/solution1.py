import re
from collections import namedtuple

def solve():
    Node = namedtuple('Node', ['left', 'right'])
    node_map = {}

    # parse input
    with open("input.txt", "r") as f:
        instructions = list(f.readline().rstrip())
        _ = f.readline().rstrip()  # throw away blank line
        line = f.readline().rstrip()
        while line:
            parsed_line = re.match(r"([A-Z]{3}) = \(([A-Z]{3}), ([A-Z]{3})\)", line)
            node_map[parsed_line.group(1)] = Node(parsed_line.group(2), parsed_line.group(3))
            line = f.readline().rstrip()

    # traverse
    steps = 0
    element = 'AAA'
    while element != 'ZZZ':
        node = node_map[element]
        move = instructions[steps % len(instructions)]  # wrap around
        element = node.left if move == 'L' else node.right
        steps += 1

    return steps

if __name__ == "__main__":
    answer = solve()
    print(answer)

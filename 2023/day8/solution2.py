# yoinks

import re
import math
from collections import namedtuple

def solve():
    Node = namedtuple('Node', ['left', 'right'])
    node_map = {}
    starting_nodes = set()

    # parse input
    with open("input.txt", "r") as f:
        instructions = list(f.readline().rstrip())
        _ = f.readline().rstrip()  # throw away blank line
        line = f.readline().rstrip()
        while line:
            parsed_line = re.match(r"([A-Z]{3}) = \(([A-Z]{3}), ([A-Z]{3})\)", line)
            node_id = parsed_line.group(1)
            node_map[node_id] = Node(parsed_line.group(2), parsed_line.group(3))
            if node_id[2] == 'A':
                starting_nodes.add(node_id)
            line = f.readline().rstrip()

    # traverse
    all_steps = []
    steps = 0
    for start_node in starting_nodes:
        element = start_node
        while element[2] != 'Z':
            node = node_map[element]
            move = instructions[steps % len(instructions)]  # wrap around
            element = node.left if move == 'L' else node.right
            steps += 1
        all_steps.append(steps)
        steps = 0

    print(f'All steps: {all_steps}')

    return math.lcm(*all_steps)  # bless python >=3.9

if __name__ == "__main__":
    answer = solve()
    print(answer)

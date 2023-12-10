# I'M NOT PROUD OF THIS ONE EITHER I'M JUST TRYNA GET CAUGHT UP
from solution1 import is_valid_part

def solve():
    
    # Process the file once, looking for part numbers
    f = open("input.txt", "r")
    curr = list(f.readline().rstrip())
    next = list(f.readline().rstrip())
    prev = []
    part_map = []
    
    while curr:
        start = None
        end = None
        i = 0
        map_row = [ None for j in range(0, len(curr)) ]
        while i < len(curr):
            if curr[i].isdigit():
                if start is None:
                    start = i
                if end is None:
                    end = i
                else:
                    end += 1
                # Check if we are at the end of the line
                if i == len(curr) - 1:
                    if is_valid_part(prev, curr, next, start, end):
                        part_number = int(''.join([curr[x] for x in range(start, end+1)]))
                        for j in range(start, end+1):
                            map_row[j] = part_number
            elif start is not None and end is not None:
                if is_valid_part(prev, curr, next, start, end):
                    part_number = int(''.join([curr[x] for x in range(start, end+1)]))
                    for j in range(start, end+1):
                        map_row[j] = part_number
                start = None
                end = None
            i += 1
        
        part_map.append(map_row)

        # Read in the next line
        prev = curr
        curr = next
        next = list(f.readline().rstrip())

    # print(part_map)

    # Go through the file again, this time looking for gears
    f.seek(0)
    gear_ratio_sum = 0
    line_index = 0
    for line in f:
        line = list(line.rstrip())
        pos = 0
        for char in line:
            if char == "*":
                surrounding_parts = get_surrounding_part_nums(pos, line_index, part_map)
                gear_ratio_sum += validate_part_nums(surrounding_parts)
            pos += 1
        line_index += 1

    f.close()
    return gear_ratio_sum

def validate_part_nums(part_nums):
    # Account for 3 digit numbers above or below
    if part_nums['top'] is not None:
        if part_nums['top_left'] == part_nums['top']:
            part_nums['top_left'] = None
        if part_nums['top_right'] == part_nums['top']:
            part_nums['top_right'] = None

    if part_nums['bottom'] is not None:
        if part_nums['bottom_left'] == part_nums['bottom']:
            part_nums['bottom_left'] = None
        if part_nums['bottom_right'] == part_nums['bottom']:
            part_nums['bottom_right'] = None


    # Verify there is exactly two part numbers
    num_found = 0
    num1 = None
    num2 = None
    for num in part_nums.values():
        if num is not None:
            num_found += 1
            if num1 is None:
                num1 = num
            else:
                num2 = num
    
    if num_found == 2:
        return num1 * num2
    else:
        return 0


def get_surrounding_part_nums(x, y, mapping):
    # Isolate the 3 rows
    curr = mapping[y]
    prev = mapping[y-1] if y != 0 else []
    next = mapping[y+1] if y != len(mapping) - 1 else []
    
    # Get x bounds
    if x != 0:
        min_x = x - 1
    else:
        min_x = None

    if x != len(curr) - 1:
        max_x = x + 1
    else:
        max_x = None

    part_nums = {
        'left': None,
        'right': None,
        'top_left': None,
        'top': None,
        'top_right': None,
        'bottom_left': None,
        'bottom': None,
        'bottom_right': None
    }
    if min_x is not None:
        # left
        test = curr[min_x]
        if test is not None:
            part_nums['left'] = test
        # top left
        if prev:
            test = prev[min_x]
            if test is not None:
                part_nums['top_left'] = test
        # bottom left
        if next:
            test = next[min_x]
            if test is not None:
                part_nums['bottom_left'] = test
    
    if max_x is not None:
        # right
        test = curr[max_x]
        if test is not None:
            part_nums['right'] = test
        # top right
        if prev:
            test = prev[max_x]
            if test is not None:
                part_nums['top_right'] = test
        # bottom right
        if next:
            test = next[max_x]
            if test is not None:
                part_nums['bottom_right'] = test

    # top
    if prev:
        test = prev[x]
        if test is not None:
            part_nums['top'] = test
    
    # bottom
    if next:
        test = next[x]
        if test is not None:
            part_nums['bottom'] = test

    return part_nums


if __name__ == "__main__":
    answer = solve()
    print(answer)

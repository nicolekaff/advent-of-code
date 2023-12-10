# THIS IS NOT ELEGANT AT ALL I KNOW!!!

def is_valid_part(prev, curr, next, start, end):
    # Adjust the bounds
    if start != 0:
        start -= 1
    if end != len(curr) - 1:
        end += 1
    
    if curr:
        if curr[start] != '.' and not curr[start].isdigit():
            return True
        if curr[end] != '.' and not curr[end].isdigit():
            return True

    if prev:
        prev_slice = prev[start:end+1]
        for char in prev_slice:
            if char != '.' and not char.isdigit():
                return True

    if next:
        next_slice = next[start:end+1]
        for char in next_slice:
            if char != '.' and not char.isdigit():
                return True

    return False

def solve():
    
    f = open("input.txt", "r")
    curr = list(f.readline().rstrip())
    next = list(f.readline().rstrip())
    prev = []
    
    parts_sum = 0
    while curr:
        start = None
        end = None
        i = 0
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
                        parts_sum += part_number
            elif start is not None and end is not None:
                if is_valid_part(prev, curr, next, start, end):
                    part_number = int(''.join([curr[x] for x in range(start, end+1)]))
                    parts_sum += part_number
                start = None
                end = None
            i += 1
        
        # Read in the next line
        prev = curr
        curr = next
        next = list(f.readline().rstrip())

    f.close()
    return parts_sum

if __name__ == "__main__":
    answer = solve()
    print(answer)

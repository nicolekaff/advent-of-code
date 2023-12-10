import re

number_map = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9"
}

def solve():
    total = 0
    pattern = r"(?=(\d|one|two|three|four|five|six|seven|eight|nine))"  # allows overlapping matches
    with open("input.txt", "r") as f:
        for line in f:
            digits = re.findall(pattern, line)
            first = digits[0]
            last = digits [-1]

            # Correct the digits
            first = first if first not in number_map else number_map[first]
            last = last if last not in number_map else number_map[last]

            result = first + last
            total += int(result)

    return total

if __name__ == "__main__":
    answer = solve()
    print(answer)

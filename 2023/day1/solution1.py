import re

def solve():
    total = 0
    with open("input.txt", "r") as f:
        for line in f:
            digits = re.findall(r"\d", line)
            result = digits[0] + digits[-1]
            total += int(result)
    return total

if __name__ == "__main__":
    answer = solve()
    print(answer)

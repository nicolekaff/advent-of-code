# Unacceptably slow I know

def solve():
    time = 46828479
    distance = 347152214061471

    total = 0
    for i in range(1, time):
        remaining_time = time - i
        distance_traveled = remaining_time * i
        if distance_traveled > distance:
            total += 1

    return total


if __name__ == "__main__":
    answer = solve()
    print(answer)

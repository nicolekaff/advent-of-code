
def solve():
    # parse input
    with open("input.txt", "r") as f:
        line = f.readline().rstrip().split(':')[1].split()
        time = [int(t) for t in line]

        line = f.readline().rstrip().split(':')[1].split()
        distance = [int(d) for d in line]  

    product = 1
    for t, d in zip(time, distance):
        total = 0
        for i in range(1, t):  # exclude 0 and t because these always lose
            remaining_time = t - i
            distance_traveled = remaining_time * i
            if distance_traveled > d:
                total += 1
        print(total)
        product *= total

    return product

if __name__ == "__main__":
    answer = solve()
    print(answer)

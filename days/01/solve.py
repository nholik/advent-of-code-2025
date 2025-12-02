from advent_of_code_2025.utils import read

def walk(start,direction, steps):
    delta = 1 if direction == "R" else -1
    pos = start
    for _ in range(steps):
        pos = (pos+delta) % 100
        yield pos

def solve(data:str, count_intermediate=False):
    curr_pos = 50
    hits = 0
    for line in data.splitlines():
        direction = line[0]
        steps = int(line[1:])

        for p in walk(curr_pos,direction,steps):
            curr_pos = p
            if curr_pos == 0 and count_intermediate:
                hits += 1
        if curr_pos == 0 and not count_intermediate:
            hits += 1

    return hits

def part1(data: str):
    return solve(data,False)

def part2(data: str):
    return solve(data,True)

if __name__ == "__main__":
    data = read(1)
    print("Part 1:", part1(data))
    print("Part 2:", part2(data))

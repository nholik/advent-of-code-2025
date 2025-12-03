import math
from advent_of_code_2025.utils import read

def is_repeat_any(num):
    num_str = str(num)
    num_len = len(num_str)
    for i in range(0,num_len//2):
        if num_len % (i+1) == 0:
            check = num_str[0:(i+1)]
            chunk_size = num_len // len(check)
            if chunk_size*check == num_str:
                return True
    return False

def is_repeat(n: int) -> bool:
    tmp = n
    digits = 0
    while tmp > 0:
        tmp //= 10
        digits += 1

    if digits % 2 != 0:
        return False

    k = digits // 2
    base = 10 ** k

    left = n // base
    right = n % base

    return left == right

def solve(data:list[str], check):
    result = 0
    for line in data:
        start,end = line.split('-')
        for num in range(int(start),int(end)+1):
            if check(num):
                result += num
    return result

def part1(data: str):
    return solve(data,is_repeat)

def part2(data: str):
    return solve(data,is_repeat_any)

if __name__ == "__main__":
    data = read(2).split(',')
    print("Part 1:", part1(data))
    print("Part 2:", part2(data))

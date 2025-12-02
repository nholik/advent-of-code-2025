def read(day: int, filename: str = "input.txt") -> str:
    path = f"days/{day:02d}/{filename}"
    with open(path) as f:
        return f.read().rstrip("\n")

def ints(s: str):
    return list(map(int, s.strip().split()))

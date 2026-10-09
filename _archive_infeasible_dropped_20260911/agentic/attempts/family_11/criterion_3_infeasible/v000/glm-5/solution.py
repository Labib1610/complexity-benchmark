import sys

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    u = int(next(it))
    s = int(next(it))
    
    covered = [False] * (u + 1)
    
    for _ in range(s):
        c = int(next(it))
        for _ in range(c):
            skill = int(next(it))
            covered[skill] = True
    
    for skill in range(1, u + 1):
        if not covered[skill]:
            print(skill)
            return

if __name__ == "__main__":
    solve()
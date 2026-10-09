import sys

def solve():
    input = sys.stdin.readline
    k, t = map(int, input().split())
    triples = []
    for _ in range(t):
        x, y, z = map(int, input().split())
        triples.append((x-1, y-1, z-1))
    
    # Group triples by operator for faster lookup
    by_operator = [[] for _ in range(k)]
    for idx, (x, y, z) in enumerate(triples):
        by_operator[x].append((y, z, idx))
    
    used_op = 0
    used_app = 0
    used_shift = 0
    chosen = []
    
    # Backtracking
    def dfs(op):
        nonlocal used_op, used_app, used_shift
        if op == k:
            return True
        for y, z, idx in by_operator[op]:
            if not (used_app & (1 << y)) and not (used_shift & (1 << z)):
                used_app |= (1 << y)
                used_shift |= (1 << z)
                chosen.append(triples[idx])
                if dfs(op + 1):
                    return True
                chosen.pop()
                used_app &= ~(1 << y)
                used_shift &= ~(1 << z)
        return False
    
    if dfs(0):
        print("YES")
        for x, y, z in chosen:
            print(x+1, y+1, z+1)
    else:
        print("NO")

if __name__ == "__main__":
    solve()
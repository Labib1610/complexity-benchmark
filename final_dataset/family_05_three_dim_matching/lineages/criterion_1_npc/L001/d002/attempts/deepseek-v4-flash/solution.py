import sys

def solve():
    input = sys.stdin.readline
    k, t = map(int, input().split())
    triples = []
    for _ in range(t):
        x, y, z = map(int, input().split())
        triples.append((x-1, y-1, z-1))
    
    # Group by operator
    by_operator = [[] for _ in range(k)]
    for x, y, z in triples:
        by_operator[x].append((y, z))
    
    used_hardware = [False] * k
    used_phase = [False] * k
    assignment = [None] * k

    # Sort each list to try deterministic order
    for i in range(k):
        by_operator[i].sort()

    def dfs(op_idx):
        if op_idx == k:
            return True
        for y, z in by_operator[op_idx]:
            if not used_hardware[y] and not used_phase[z]:
                used_hardware[y] = True
                used_phase[z] = True
                assignment[op_idx] = (op_idx, y, z)
                if dfs(op_idx + 1):
                    return True
                used_hardware[y] = False
                used_phase[z] = False
        return False

    if dfs(0):
        print("YES")
        for op, y, z in assignment:
            print(op+1, y+1, z+1)
    else:
        print("NO")

if __name__ == "__main__":
    solve()
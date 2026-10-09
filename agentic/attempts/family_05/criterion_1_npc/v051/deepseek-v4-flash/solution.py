import sys

def solve():
    input = sys.stdin.readline
    k, t = map(int, input().split())
    trios = []
    for _ in range(t):
        x, y, z = map(int, input().split())
        trios.append((x-1, y-1, z-1))
    
    # Group trios by linguist
    by_linguist = [[] for _ in range(k)]
    for x, y, z in trios:
        by_linguist[x].append((y, z))
    
    # Sort each list for deterministic order
    for i in range(k):
        by_linguist[i].sort()
    
    # We'll try to assign each linguist a manuscript and algorithm
    used_man = [False]*k
    used_alg = [False]*k
    assignment = [None]*k
    
    # Backtracking
    def dfs(idx):
        if idx == k:
            return True
        for y, z in by_linguist[idx]:
            if not used_man[y] and not used_alg[z]:
                used_man[y] = True
                used_alg[z] = True
                assignment[idx] = (idx, y, z)
                if dfs(idx+1):
                    return True
                used_man[y] = False
                used_alg[z] = False
        return False
    
    if dfs(0):
        print("YES")
        for x, y, z in assignment:
            print(x+1, y+1, z+1)
    else:
        print("NO")

if __name__ == "__main__":
    solve()
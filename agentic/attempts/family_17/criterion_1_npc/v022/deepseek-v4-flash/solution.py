import sys

def solve():
    input = sys.stdin.readline
    q, t = map(int, input().split())
    n = 3 * q
    triplets_by_start = [[] for _ in range(n + 1)]
    triplets = []
    for _ in range(t):
        a, b, c = map(int, input().split())
        triplets_by_start[a].append((a, b, c))
        triplets.append((a, b, c))
    
    # Sort each group by c (third element) to try earliest end first
    for i in range(1, n + 1):
        triplets_by_start[i].sort(key=lambda x: x[2])
    
    used = [False] * (n + 1)
    selected = []
    
    # Find the smallest unused page from start
    def find_next(start):
        for i in range(start, n + 1):
            if not used[i]:
                return i
        return n + 1
    
    def dfs(pos):
        # pos is the current smallest unused page
        if pos > n:
            return True
        if used[pos]:
            return dfs(find_next(pos + 1))
        
        for a, b, c in triplets_by_start[pos]:
            if not used[b] and not used[c]:
                used[a] = used[b] = used[c] = True
                selected.append((a, b, c))
                nxt = find_next(pos + 1)
                if dfs(nxt):
                    return True
                selected.pop()
                used[a] = used[b] = used[c] = False
        return False
    
    if dfs(1):
        print("YES")
        for a, b, c in selected:
            print(a, b, c)
    else:
        print("NO")

if __name__ == "__main__":
    solve()
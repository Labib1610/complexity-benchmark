import sys

def solve():
    input = sys.stdin.readline
    k, t = map(int, input().split())
    trios = []
    for _ in range(t):
        s, c, f = map(int, input().split())
        trios.append((s-1, c-1, f-1))
    
    # adjacency list for each starter
    by_starter = [[] for _ in range(k)]
    for idx, (s, c, f) in enumerate(trios):
        by_starter[s].append(idx)
    
    used_s = [False]*k
    used_c = [False]*k
    used_f = [False]*k
    chosen = []
    
    def dfs(count):
        if count == k:
            return True
        # find first unused starter
        s = -1
        for i in range(k):
            if not used_s[i]:
                s = i
                break
        if s == -1:
            return False
        for idx in by_starter[s]:
            sc, cc, ff = trios[idx]
            if not used_c[cc] and not used_f[ff]:
                used_s[s] = True
                used_c[cc] = True
                used_f[ff] = True
                chosen.append(idx)
                if dfs(count+1):
                    return True
                chosen.pop()
                used_s[s] = False
                used_c[cc] = False
                used_f[ff] = False
        return False
    
    if dfs(0):
        print("YES")
        for idx in chosen:
            s, c, f = trios[idx]
            print(s+1, c+1, f+1)
    else:
        print("NO")

if __name__ == "__main__":
    solve()
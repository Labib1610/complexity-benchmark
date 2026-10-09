import sys

def solve():
    input = sys.stdin.readline
    k, t = map(int, input().split())
    by_m = [[] for _ in range(k)]
    for _ in range(t):
        m, c, f = map(int, input().split())
        by_m[m-1].append((c-1, f-1))
    
    used_c = [False]*k
    used_f = [False]*k
    chosen = [None]*k
    
    def dfs(m_idx):
        if m_idx == k:
            return True
        for c, f in by_m[m_idx]:
            if not used_c[c] and not used_f[f]:
                used_c[c] = True
                used_f[f] = True
                chosen[m_idx] = (m_idx+1, c+1, f+1)
                if dfs(m_idx+1):
                    return True
                used_c[c] = False
                used_f[f] = False
        return False
    
    if dfs(0):
        print("YES")
        for triple in chosen:
            print(*triple)
    else:
        print("NO")

if __name__ == "__main__":
    solve()
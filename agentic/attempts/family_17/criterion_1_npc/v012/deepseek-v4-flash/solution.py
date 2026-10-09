import sys

def solve():
    input = sys.stdin.readline
    q, t = map(int, input().split())
    n = 3 * q
    triples = []
    adj = [[] for _ in range(n + 1)]
    for _ in range(t):
        a, b, c = map(int, input().split())
        triples.append((a, b, c))
        adj[a].append(len(triples) - 1)
        adj[b].append(len(triples) - 1)
        adj[c].append(len(triples) - 1)

    used = [False] * (n + 1)
    chosen = []

    def dfs(count):
        if count == q:
            return True
        # find first unused vertex
        start = 1
        while start <= n and used[start]:
            start += 1
        if start > n:
            return False
        # try all triples containing start
        for idx in adj[start]:
            a, b, c = triples[idx]
            if used[a] or used[b] or used[c]:
                continue
            used[a] = used[b] = used[c] = True
            chosen.append((a, b, c))
            if dfs(count + 1):
                return True
            chosen.pop()
            used[a] = used[b] = used[c] = False
        return False

    if dfs(0):
        print("YES")
        for a, b, c in chosen:
            print(a, b, c)
    else:
        print("NO")

if __name__ == "__main__":
    solve()
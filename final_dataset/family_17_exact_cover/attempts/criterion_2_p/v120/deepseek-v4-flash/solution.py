import sys

def main():
    input = sys.stdin.readline
    q, t = map(int, input().split())
    adj = [[] for _ in range(q)]
    for _ in range(t):
        a, b = map(int, input().split())
        adj[a-1].append(b - q - 1)  # store right index 0..q-1

    matchR = [-1] * q  # which left node is matched to right node

    def dfs(u, seen):
        for v in adj[u]:
            if seen[v]:
                continue
            seen[v] = True
            if matchR[v] == -1 or dfs(matchR[v], seen):
                matchR[v] = u
                return True
        return False

    matchL = [-1] * q
    for u in range(q):
        seen = [False] * q
        if dfs(u, seen):
            matchL[u] = True

    if all(m != -1 for m in matchR):
        print("YES")
        for v, u in enumerate(matchR):
            print(u+1, v+q+1)
    else:
        print("NO")

if __name__ == "__main__":
    main()
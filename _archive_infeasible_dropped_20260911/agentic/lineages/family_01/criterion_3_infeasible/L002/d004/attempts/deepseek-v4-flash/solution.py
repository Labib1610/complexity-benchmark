import sys

def main():
    input = sys.stdin.readline
    n, m = map(int, input().split())
    adj = [set() for _ in range(n+1)]
    for _ in range(m):
        u, v = map(int, input().split())
        adj[u].add(v)
        adj[v].add(u)
    
    for i in range(1, n+1):
        for j in range(i+1, n+1):
            if j in adj[i]:
                # find smallest k > j connected to both
                common = adj[i] & adj[j]
                for k in sorted(common):
                    if k > j:
                        print(i, j, k)
                        return

if __name__ == "__main__":
    main()
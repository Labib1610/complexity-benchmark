import sys

def main():
    input = sys.stdin.readline
    n, m = map(int, input().split())
    adj = [set() for _ in range(n + 1)]
    for _ in range(m):
        u, v = map(int, input().split())
        adj[u].add(v)
        adj[v].add(u)
    
    for x in range(1, n + 1):
        for y in range(x + 1, n + 1):
            if y in adj[x]:
                # find smallest z > y connected to both x and y
                common = adj[x] & adj[y]
                for z in sorted(common):
                    if z > y:
                        print(x, y, z)
                        return

if __name__ == "__main__":
    main()
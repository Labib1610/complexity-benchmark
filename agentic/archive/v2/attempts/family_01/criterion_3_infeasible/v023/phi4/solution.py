import sys

def find_mutual_connection():
    n, m = map(int, input().split())
    adj_list = [set() for _ in range(n + 1)]
    
    for _ in range(m):
        u, v = map(int, input().split())
        if u < v:
            adj_list[u].add(v)
            adj_list[v].add(u)
        else:
            adj_list[v].add(u)
            adj_list[u].add(v)

    # We will try to find the lexicographically smallest triplet
    for a in range(1, n + 1):
        for b in adj_list[a]:
            if b > a:  # Ensure a < b
                for c in adj_list[b]:
                    if c > b and c in adj_list[a]:  # Check mutual connection a-b-c
                        print(a, b, c)
                        return

find_mutual_connection()
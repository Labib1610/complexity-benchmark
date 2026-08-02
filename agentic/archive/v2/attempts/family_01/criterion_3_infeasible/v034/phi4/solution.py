import sys

def find_mutually_reactive_triple():
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    m = int(data[1])
    
    # Adjacency list to store reactive pairs
    adj_list = {i: set() for i in range(1, n+1)}
    
    index = 2
    for _ in range(m):
        u = int(data[index])
        v = int(data[index + 1])
        adj_list[u].add(v)
        adj_list[v].add(u)
        index += 2
    
    # Find the lexicographically smallest triple (a, b, c) such that all pairs are reactive
    for a in range(1, n+1):
        for b in sorted(adj_list[a]):
            if b > a:
                for c in sorted(adj_list[a]):
                    if c > b and c in adj_list[b]:
                        print(a, b, c)
                        return

if __name__ == "__main__":
    find_mutually_reactive_triple()
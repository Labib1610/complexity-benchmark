from sys import stdin, stdout
from collections import defaultdict

def find_mutual_couplings(n, m, edges):
    graph = defaultdict(set)
    
    for u, v in edges:
        graph[u].add(v)
        graph[v].add(u)
    
    for a in range(1, n + 1):
        for b in graph[a]:
            if b > a:  # Ensure a < b
                for c in graph[b]:
                    if c > b and c in graph[a]:  # Ensure b < c and a, b, c form a triangle
                        return (a, b, c)

input = stdin.read
data = input().splitlines()
n, m = map(int, data[0].split())
edges = [tuple(map(int, line.split())) for line in data[1:m+1]]

result = find_mutual_couplings(n, m, edges)
stdout.write(f"{result[0]} {result[1]} {result[2]}\n")
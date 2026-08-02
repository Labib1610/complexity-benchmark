n, m = map(int, input().split())
adjacency_list = [[] for _ in range(n)]

for _ in range(m):
    u, v = map(lambda x: int(x) - 1, input().split())
    adjacency_list[u].append(v)
    adjacency_list[v].append(u)

# Sort neighbors to facilitate lexicographical comparison
for neighbors in adjacency_list:
    neighbors.sort()

answer = None

for i in range(n):
    for j in adjacency_list[i]:
        # Ensure a < b
        if i >= j:
            continue
        
        for k in adjacency_list[j]:
            # Ensure b < c and check if (i, c) is an unstable pair
            if j > k and k in adjacency_list[i]:
                current_triple = [i + 1, j + 1, k + 1]
                
                if answer is None or current_triple < answer:
                    answer = current_triple

print(*answer)
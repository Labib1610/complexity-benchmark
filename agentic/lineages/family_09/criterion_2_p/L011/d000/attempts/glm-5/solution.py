import sys
from collections import deque

def solve():
    input_data = sys.stdin.buffer.read().split()
    idx = 0
    n = int(input_data[idx]); idx += 1
    m = int(input_data[idx]); idx += 1
    k = int(input_data[idx]); idx += 1

    if m == 0:
        if k <= n:
            sys.stdout.write("YES\n")
            sys.stdout.write(" ".join(str(i) for i in range(1, k + 1)) + "\n")
        else:
            sys.stdout.write("NO\n")
        return

    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        u = int(input_data[idx]); idx += 1
        v = int(input_data[idx]); idx += 1
        adj[u].append(v)
        adj[v].append(u)

    color = [0] * (n + 1)
    comp = [0] * (n + 1)
    comp_id = 0
    comp_sizes = []
    comp_nodes = []

    for start in range(1, n + 1):
        if color[start] == 0:
            comp_id += 1
            color[start] = 1
            comp[start] = comp_id
            queue = deque([start])
            comp_list = [start]
            while queue:
                u = queue.popleft()
                for v in adj[u]:
                    if color[v] == 0:
                        color[v] = 3 - color[u]
                        comp[v] = comp_id
                        queue.append(v)
                        comp_list.append(v)
            comp_nodes.append(comp_list)
            comp_sizes.append(len(comp_list))

    total = sum(comp_sizes)
    if k > total:
        sys.stdout.write("NO\n")
        return

    dp = [False] * (k + 1)
    dp[0] = True
    prev = [0] * (k + 1)

    for i in range(comp_id):
        s = comp_sizes[i]
        for j in range(k, s - 1, -1):
            if not dp[j] and dp[j - s]:
                dp[j] = True
                prev[j] = i
        if dp[k]:
            break

    if not dp[k]:
        sys.stdout.write("NO\n")
        return

    chosen_comps = set()
    j = k
    while j > 0:
        i = prev[j]
        chosen_comps.add(i)
        j -= comp_sizes[i]

    result = []
    for i in chosen_comps:
        cnt0 = 0
        cnt1 = 0
        for node in comp_nodes[i]:
            if color[node] == 1:
                cnt0 += 1
            else:
                cnt1 += 1
        if cnt0 >= cnt1:
            target_color = 1
        else:
            target_color = 2
        for node in comp_nodes[i]:
            if color[node] == target_color:
                result.append(node)

    sys.stdout.write("YES\n")
    sys.stdout.write(" ".join(map(str, result[:k])) + "\n")

solve()
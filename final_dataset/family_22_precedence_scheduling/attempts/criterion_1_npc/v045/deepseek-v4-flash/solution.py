from collections import deque, defaultdict
import sys

def solve():
    input = sys.stdin.readline
    n, M, T, m = map(int, input().split())
    adj = [[] for _ in range(n)]
    indeg = [0] * n
    for _ in range(m):
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        adj[a].append(b)
        indeg[b] += 1

    # Kahn's algorithm with round assignment
    q = deque([i for i in range(n) if indeg[i] == 0])
    round_assign = [0] * n
    current_round = 1
    count_in_round = 0
    processed = 0

    while q:
        # We can process up to M nodes in the current round
        # But we must be careful: if we take a node, all its successors
        # must be in later rounds, so we can take any available nodes.
        # We'll take up to M nodes for this round.
        next_q = deque()
        for _ in range(min(M, len(q))):
            u = q.popleft()
            round_assign[u] = current_round
            processed += 1
            for v in adj[u]:
                indeg[v] -= 1
                if indeg[v] == 0:
                    next_q.append(v)
        current_round += 1
        if current_round > T:
            # If we still have nodes left, impossible
            if processed < n:
                print("NO")
                return
        q = next_q

    if processed != n:
        print("NO")
        return

    # Check if any round exceeds T
    if max(round_assign) > T:
        print("NO")
        return

    print("YES")
    print(" ".join(str(x) for x in round_assign))

if __name__ == "__main__":
    solve()
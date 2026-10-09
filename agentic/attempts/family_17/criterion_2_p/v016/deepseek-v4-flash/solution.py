import sys
import heapq

def main():
    input = sys.stdin.readline
    q, t = map(int, input().split())
    adj = [[] for _ in range(q + 1)]
    for _ in range(t):
        a, b = map(int, input().split())
        adj[a].append(b)
    
    # Sort each controller's platform list
    for i in range(1, q + 1):
        adj[i].sort()
    
    # Greedy matching: process controllers in order, assign smallest available platform
    # that is >= q+1 and <= 3q - controller_id
    # We'll use a min-heap of available platforms.
    # Since platforms are unique, we can just iterate.
    
    # We'll use a pointer approach: for each controller, pick the smallest platform
    # that hasn't been used and is in its list.
    
    used = [False] * (2 * q + 1)
    result = []
    ptr = [0] * (q + 1)
    
    # We'll process controllers from 1 to q
    # For each controller, we need the smallest platform in its list that is unused.
    # Since lists are sorted, we can advance pointer until we find unused.
    
    for c in range(1, q + 1):
        found = False
        while ptr[c] < len(adj[c]):
            p = adj[c][ptr[c]]
            ptr[c] += 1
            if not used[p]:
                used[p] = True
                result.append((c, p))
                found = True
                break
        if not found:
            print("NO")
            return
    
    print("YES")
    for c, p in result:
        print(c, p)

if __name__ == "__main__":
    main()
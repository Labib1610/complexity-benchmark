import sys
from collections import defaultdict, deque

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    idx = 0
    n = int(data[idx])
    idx += 1
    m = int(data[idx])
    idx += 1
    k = int(data[idx])
    idx += 1
    
    # Build adjacency list
    adj = defaultdict(set)
    edges = []
    for _ in range(m):
        u = int(data[idx])
        idx += 1
        v = int(data[idx])
        idx += 1
        adj[u].add(v)
        adj[v].add(u)
        edges.append((u, v))
    
    # If no edges, any k nodes work
    if m == 0:
        print("YES")
        print(' '.join(map(str, range(1, min(k+1, n+1)))))
        return
    
    # Bipartite check and get the two camps
    color = {}
    camps = [[], []]
    
    visited = [False] * (n + 1)
    
    for start in range(1, n + 1):
        if visited[start]:
            continue
        queue = deque()
        queue.append(start)
        color[start] = 0
        visited[start] = True
        camps[0].append(start)
        
        while queue:
            u = queue.popleft()
            c = color[u]
            for v in adj[u]:
                if not visited[v]:
                    visited[v] = True
                    color[v] = 1 - c
                    camps[1 - c].append(v)
                    queue.append(v)
                elif color[v] == c:
                    # Should not happen as per problem statement
                    print("NO")
                    return
    
    # Now we have two camps: camps[0] and camps[1]
    camp0 = camps[0]
    camp1 = camps[1]
    
    # Check if we can take k nodes from one camp
    if k <= len(camp0):
        print("YES")
        print(' '.join(map(str, camp0[:k])))
        return
    elif k <= len(camp1):
        print("YES")
        print(' '.join(map(str, camp1[:k])))
        return
    else:
        # We need to take some from camp0 and some from camp1
        # But since there are no edges within a camp, we can take any subset from each
        # However, we can only take up to len(camp0) + len(camp1) = n
        # But we are only allowed to take k, and k > max(len(camp0), len(camp1))
        # So we can take min(k, len(camp0)) from camp0 and min(k - min(k, len(camp0)), len(camp1)) from camp1
        # But since k <= n, and we can take at most len(camp0) + len(camp1) = n
        # If k > len(camp0) and k > len(camp1), then we can take all of camp0 and some of camp1 or vice versa
        # Actually, we can take any combination as long as total is k and no two are friends
        # Since camps are independent, we can take any subset from each
        # So total possible is len(camp0) + len(camp1) = n
        # We want exactly k
        # If k <= len(camp0) + len(camp1), and k > max(len(camp0), len(camp1)), then we can take i from camp0 and (k-i) from camp1
        # for some i in [max(0, k - len(camp1)), min(len(camp0), k)]
        # Since there are no edges within camps, any such selection is valid
        
        if k > len(camp0) + len(camp1):
            print("NO")
            return
        else:
            # We can take some from each
            # Let's take min(k, len(camp0)) from camp0 and k - that from camp1
            take0 = min(k, len(camp0))
            take1 = k - take0
            if take1 > len(camp1):
                # Adjust
                take1 = len(camp1)
                take0 = k - take1
            if take0 <= len(camp0) and take1 <= len(camp1):
                result = camp0[:take0] + camp1[:take1]
                print("YES")
                print(' '.join(map(str, result)))
                return
            else:
                print("NO")
                return

if __name__ == "__main__":
    main()
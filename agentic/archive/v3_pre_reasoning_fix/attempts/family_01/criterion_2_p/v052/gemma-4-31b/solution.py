import sys

# Increase recursion depth for deep DFS trees
sys.setrecursionlimit(300000)

def solve():
    # Read n and m
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    m = int(input_data[1])
    
    adj = [[] for _ in range(n + 1)]
    idx = 2
    for _ in range(m):
        u = int(input_data[idx])
        v = int(input_data[idx+1])
        adj[u].append(v)
        adj[v].append(u)
        idx += 2
        
    # s[i] will store the channel (1 or 2). 0 means unassigned.
    s = [0] * (n + 1)
    
    # To get the lexicographically smallest assignment:
    # For each connected component, we want to assign 1 to the smallest 
    # index in that component if possible.
    # However, the lexicographical smallest sequence is determined 
    # by the value of s[1], then s[2], and so on.
    # Thus, we iterate through nodes 1 to n. If a node is not visited,
    # it's the smallest node in its component. To minimize the sequence,
    # we MUST try setting s[i] = 1 first.
    
    for i in range(1, n + 1):
        if s[i] == 0:
            # Start a BFS/DFS from node i.
            # To minimize lexicographically, we set s[i] = 1.
            stack = [i]
            s[i] = 1
            
            # Use a manual stack for DFS to avoid recursion limits and for efficiency
            visited_in_comp = [i]
            ptr = 0
            while ptr < len(visited_in_comp):
                u = visited_in_comp[ptr]
                ptr += 1
                for v in adj[u]:
                    if s[v] == 0:
                        s[v] = 3 - s[u] # Flip 1 to 2 or 2 to 1
                        visited_in_comp.append(v)
                    elif s[v] == s[u]:
                        print("NO")
                        return
    
    # Since we process components in increasing order of their smallest element
    # and always assign the smallest element of a new component to 1,
    # this naturally produces the lexicographically smallest valid sequence.
    # Because if we assigned the smallest element to 2, the sequence would be
    # lexicographically larger.
    
    print("YES")
    print(*(s[i] for i in range(1, n + 1)))

if __name__ == "__main__":
    solve()
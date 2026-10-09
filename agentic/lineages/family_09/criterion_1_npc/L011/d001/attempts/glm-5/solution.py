import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    m = int(input_data[1])
    k = int(input_data[2])
    
    adj = [0] * (n + 1)
    for i in range(m):
        u = int(input_data[3 + 2*i])
        v = int(input_data[3 + 2*i + 1])
        adj[u] |= 1 << (v - 1)
        adj[v] |= 1 << (u - 1)
        
    if k == 0:
        print("YES")
        print()
        return
        
    if n <= 23:
        dp = [-1] * (1 << n)
        dp[0] = 0
        for mask in range(1 << n):
            if dp[mask] == -1:
                continue
            for i in range(n):
                if not (mask & (1 << i)):
                    if (mask & adj[i+1]) == 0:
                        nxt = mask | (1 << i)
                        if dp[nxt] == -1:
                            dp[nxt] = i + 1
                            
        target = -1
        for mask in range(1 << n):
            if bin(mask).count('1') == k and dp[mask] != -1:
                target = mask
                break
                
        if target != -1:
            print("YES")
            res = []
            curr = target
            while curr > 0:
                v = dp[curr]
                res.append(v)
                curr ^= (1 << (v - 1))
            print(' '.join(map(str, res)))
        else:
            print("NO")
            
    else:
        half = n // 2
        L = half
        R = n - half
        
        adj_L = [0] * (n + 1)
        adj_R = [0] * (n + 1)
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if adj[i] & (1 << (j - 1)):
                    if j <= half:
                        adj_L[i] |= 1 << (j - 1)
                    else:
                        adj_R[i] |= 1 << (j - half - 1)
                        
        dp_L = [-1] * (1 << L)
        dp_L[0] = 0
        for mask in range(1 << L):
            if dp_L[mask] == -1:
                continue
            for i in range(L):
                if not (mask & (1 << i)):
                    if (mask & adj_L[i+1]) == 0:
                        nxt = mask | (1 << i)
                        if dp_L[nxt] == -1:
                            dp_L[nxt] = i + 1
                            
        dp_R = [-1] * (1 << R)
        dp_R[0] = 0
        for mask in range(1 << R):
            if dp_R[mask] == -1:
                continue
            for i in range(R):
                if not (mask & (1 << i)):
                    if (mask & adj_R[half+1+i]) == 0:
                        nxt = mask | (1 << i)
                        if dp_R[nxt] == -1:
                            dp_R[nxt] = half + 1 + i
                            
        valid_L = {}
        for mask in range(1 << L):
            if dp_L[mask] != -1:
                cnt = bin(mask).count('1')
                if cnt not in valid_L:
                    valid_L[cnt] = mask
                    
        valid_R = {}
        for mask in range(1 << R):
            if dp_R[mask] != -1:
                cnt = bin(mask).count('1')
                if cnt not in valid_R:
                    valid_R[cnt] = mask
                    
        found = False
        for c1 in valid_L:
            c2 = k - c1
            if c2 in valid_R:
                mask_L = valid_L[c1]
                mask_R = valid_R[c2]
                
                ok = True
                for i in range(L):
                    if mask_L & (1 << i):
                        if adj[i+1] & (mask_R << half):
                            ok = False
                            break
                            
                if ok:
                    print("YES")
                    res = []
                    curr = mask_L
                    while curr > 0:
                        v = dp_L[curr]
                        res.append(v)
                        curr ^= (1 << (v - 1))
                    curr = mask_R
                    while curr > 0:
                        v = dp_R[curr]
                        res.append(v)
                        curr ^= (1 << (v - half - 1))
                    print(' '.join(map(str, res)))
                    found = True
                    break
                    
        if not found:
            print("NO")

if __name__ == '__main__':
    solve()
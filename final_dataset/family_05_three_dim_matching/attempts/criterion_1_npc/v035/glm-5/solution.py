import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    it = iter(input_data)
    k = int(next(it))
    t = int(next(it))
    
    adj = [[] for _ in range(k)]
    for _ in range(t):
        x = int(next(it)) - 1
        y = int(next(it)) - 1
        z = int(next(it)) - 1
        adj[x].append((y, z))
        
    match_y = [-1] * k
    match_z = [-1] * k
    ans = [-1] * k
    
    def dfs(u, visited):
        for v, w in adj[u]:
            if visited[v][w]:
                continue
            visited[v][w] = True
            if match_y[v] == -1 and match_z[w] == -1:
                match_y[v] = u
                match_z[w] = u
                ans[u] = (v, w)
                return True
            u_prime = match_y[v]
            if match_z[w] != u_prime:
                visited_v = [False] * k
                visited_w = [False] * k
                visited_v[v] = True
                visited_w[w] = True
                
                queue = [(v, w)]
                head = 0
                found = -1
                
                while head < len(queue) and found == -1:
                    curr_v, curr_w = queue[head]
                    head += 1
                    for next_v, next_w in adj[u_prime]:
                        if visited_v[next_v] or visited_w[next_w]:
                            continue
                        visited_v[next_v] = True
                        visited_w[next_w] = True
                        queue.append((next_v, next_w))
                        if match_y[next_v] == -1 and match_z[next_w] == -1:
                            found = (next_v, next_w)
                            break
                            
                if found != -1:
                    fv, fw = found
                    match_y[fv] = u_prime
                    match_z[fw] = u_prime
                    ans[u_prime] = (fv, fw)
                    
                    curr_v, curr_w = fv, fw
                    for i in range(len(queue) - 1, -1, -1):
                        pv, pw = queue[i]
                        if pv == curr_v or pw == curr_w:
                            match_y[pv] = match_z[pw] = -1
                            for alt_v, alt_w in adj[u_prime]:
                                if alt_v == pv and alt_w == pw:
                                    continue
                                if match_y[alt_v] == -1 and match_z[alt_w] == -1:
                                    match_y[alt_v] = u_prime
                                    match_z[alt_w] = u_prime
                                    ans[u_prime] = (alt_v, alt_w)
                                    curr_v, curr_w = alt_v, alt_w
                                    break
                            else:
                                break
                    else:
                        continue
                        
                    match_y[v] = u
                    match_z[w] = u
                    ans[u] = (v, w)
                    return True
                    
            u_prime2 = match_z[w]
            if match_y[v] != u_prime2:
                visited_v = [False] * k
                visited_w = [False] * k
                visited_v[v] = True
                visited_w[w] = True
                
                queue = [(v, w)]
                head = 0
                found = -1
                
                while head < len(queue) and found == -1:
                    curr_v, curr_w = queue[head]
                    head += 1
                    for next_v, next_w in adj[u_prime2]:
                        if visited_v[next_v] or visited_w[next_w]:
                            continue
                        visited_v[next_v] = True
                        visited_w[next_w] = True
                        queue.append((next_v, next_w))
                        if match_y[next_v] == -1 and match_z[next_w] == -1:
                            found = (next_v, next_w)
                            break
                            
                if found != -1:
                    fv, fw = found
                    match_y[fv] = u_prime2
                    match_z[fw] = u_prime2
                    ans[u_prime2] = (fv, fw)
                    
                    curr_v, curr_w = fv, fw
                    for i in range(len(queue) - 1, -1, -1):
                        pv, pw = queue[i]
                        if pv == curr_v or pw == curr_w:
                            match_y[pv] = match_z[pw] = -1
                            for alt_v, alt_w in adj[u_prime2]:
                                if alt_v == pv and alt_w == pw:
                                    continue
                                if match_y[alt_v] == -1 and match_z[alt_w] == -1:
                                    match_y[alt_v] = u_prime2
                                    match_z[alt_w] = u_prime2
                                    ans[u_prime2] = (alt_v, alt_w)
                                    curr_v, curr_w = alt_v, alt_w
                                    break
                            else:
                                break
                    else:
                        continue
                        
                    match_y[v] = u
                    match_z[w] = u
                    ans[u] = (v, w)
                    return True
        return False

    for u in range(k):
        visited = [[False] * k for _ in range(k)]
        if not dfs(u, visited):
            print("NO")
            return
            
    print("YES")
    for u in range(k):
        v, w = ans[u]
        print(u + 1, v + 1, w + 1)

if __name__ == '__main__':
    solve()
import sys

def solve():
    input = sys.stdin.readline
    n, m = map(int, input().split())
    must0 = [False] * (n + 1)
    must1 = [False] * (n + 1)
    
    for _ in range(m):
        l1, l2 = map(int, input().split())
        for l in (l1, l2):
            if l > 0:
                must0[l] = True
            else:
                must1[-l] = True
    
    for i in range(1, n + 1):
        if must0[i] and must1[i]:
            print("NO")
            return
    
    res = []
    for i in range(1, n + 1):
        if must0[i]:
            res.append('0')
        elif must1[i]:
            res.append('1')
        else:
            res.append('0')
    
    print("YES")
    print(' '.join(res))

if __name__ == "__main__":
    solve()
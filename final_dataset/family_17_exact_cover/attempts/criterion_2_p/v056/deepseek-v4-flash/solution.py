import sys
from bisect import bisect_right

def solve():
    input = sys.stdin.readline
    q, t = map(int, input().split())
    adj = [[] for _ in range(q + 1)]
    for _ in range(t):
        a, b = map(int, input().split())
        adj[a].append(b)
    
    # Sort each adjacency list
    for i in range(1, q + 1):
        adj[i].sort()
    
    # We'll use a balanced structure: a sorted list of available Betas
    # Since q up to 100k, we can use a Fenwick tree or just a sorted list with bisect.
    # But we need to remove used ones efficiently. Use a Fenwick tree for availability.
    
    # Fenwick tree for available Betas (q+1 .. 2q)
    size = 2 * q + 2
    bit = [0] * (size + 1)
    
    def update(idx, delta):
        while idx <= size:
            bit[idx] += delta
            idx += idx & -idx
    
    def query(idx):
        s = 0
        while idx > 0:
            s += bit[idx]
            idx -= idx & -idx
        return s
    
    def find_kth(k):
        # smallest idx such that prefix sum >= k
        idx = 0
        bitmask = 1 << (size.bit_length())
        while bitmask:
            nxt = idx + bitmask
            if nxt <= size and bit[nxt] < k:
                idx = nxt
                k -= bit[nxt]
            bitmask >>= 1
        return idx + 1
    
    # Initially all Betas q+1..2q available
    for b in range(q + 1, 2 * q + 1):
        update(b, 1)
    
    result = []
    for a in range(1, q + 1):
        # Find smallest available Beta > a
        # Count available Betas <= a
        cnt_le = query(a)
        total_avail = query(2 * q)
        if cnt_le == total_avail:
            print("NO")
            return
        # The next available Beta after a is the (cnt_le+1)-th available
        b = find_kth(cnt_le + 1)
        # Check if b > a (should be, since we picked next after a)
        if b <= a:
            print("NO")
            return
        # Use it
        update(b, -1)
        result.append((a, b))
    
    print("YES")
    for a, b in result:
        print(a, b)

if __name__ == "__main__":
    solve()
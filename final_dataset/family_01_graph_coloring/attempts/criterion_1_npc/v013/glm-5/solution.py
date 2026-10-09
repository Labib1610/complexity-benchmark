import sys
from sys import setrecursionlimit

def main():
    input_data = sys.stdin.buffer.read().split()
    n = int(input_data[0]); m = int(input_data[1])
    adj = [0]*n
    idx = 2
    for _ in range(m):
        u = int(input_data[idx])-1; v = int(input_data[idx+1])-1; idx += 2
        if u != v:
            adj[u] |= 1 << v
            adj[v] |= 1 << u
    # note: u != v guaranteed? "pairs" - assume u != v; but handle just in case: self-loop → impossible? A task incompatible with itself → NO. Edge case; m ≤ n(n-1)/2 implies u≠v. But just in case, if u==v, answer NO.
    
    color = [-1]*n  # 0-based colors 0,1,2
    
    # Peel degree ≤ 2 vertices per component? Actually peeling works globally.
    # But careful: peeling + component decomposition interplay: peel first, then components of the core.
    ...
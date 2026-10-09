import sys
from sys import setrecursionlimit

def main():
    input_data = sys.stdin.buffer.read().split()
    n = int(...); m = int(...)
    edges: list of (u, v) 0-indexed vertices.
    adj[v] = list of (eid, u)
    
    # 1. Bridge detection via iterative DFS (edge-based).
    #    If any bridge: print("NO"); return.
    
    # 2. For each connected component: run search.
    #    Actually the search can run globally: buckets are global; 
    #    components are independent but the search handles them 
    #    sequentially anyway (frontier exhausts one component before 
    #    starting another — since buckets pick min uncolored count, 
    #    and a fresh component's vertices are in bucket 3 while 
    #    active component has bucket ≤2 vertices... hmm, not exactly:
    #    a component could have all vertices in bucket ≥... let me think:
    #    while a component is partially colored, it has bucket-1/2 vertices 
    #    (frontier). Only when it's fully colored do we move on. 
    #    But wait: could a component have NO bucket-1/2 vertices while 
    #    not fully colored? If partially colored, the colored region's 
    #    boundary vertices have colored edges → bucket ≤ 2. Yes, so 
    #    frontier always exists in bucket ≤ 2 until component done. ✓
    #    So global search naturally processes components one at a time.
    #    But the symmetry-fixing (first vertex of each component → 1 branch)
    #    needs care: when picking a bucket-3 vertex (fresh component), 
    #    fix the assignment (only 1 permutation) — valid by color symmetry 
    #    ONLY for the first vertex of that component. Since components are 
    #    independent, per-component symmetry fixing is valid. ✓
    
    # 3. Search: recursive or iterative with explicit stack.
    #    State: color[eid], used_mask[v], uncolored_count[v] (= 3 - popcount... 
    #    maintain explicitly), buckets: bucket[k] = list/set of vertices, 
    #    bucket_pos for O(1) removal (or just use lists + lazy deletion 
    #    with a "in_bucket" check... hmm).
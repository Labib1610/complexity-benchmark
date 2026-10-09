import sys
from collections import deque

def main():
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    it = iter(data)
    nA = int(next(it))
    nB = int(next(it))
    m = int(next(it))

    edges = []
    degA = [0] * (nA + 1)
    degB = [0] * (nB + 1)

    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        edges.append((u, v))
        degA[u] += 1
        degB[v] += 1

    delta = 0
    for d in degA:
        if d > delta:
            delta = d
    for d in degB:
        if d > delta:
            delta = d

    # Build adjacency lists for the bipartite graph
    adjA = [[] for _ in range(nA + 1)]
    adjB = [[] for _ in range(nB + 1)]

    for idx, (u, v) in enumerate(edges):
        adjA[u].append((v, idx))
        adjB[v].append((u, idx))

    # We will color edges with colors 1..delta using a simple greedy algorithm
    # that works for bipartite graphs: repeatedly find a maximal matching
    # and assign colors.  This is essentially edge-coloring via matchings.
    # For bipartite graphs, delta colors suffice.

    color = [0] * m

    # We'll implement the standard algorithm:
    # For each color c from 1 to delta:
    #   find a maximal matching in the remaining uncolored edges
    #   assign color c to all edges in the matching.
    # This is correct because each vertex has at most delta edges total,
    # so after removing some colors, the remaining graph still has max degree <= delta - c + 1.
    # A maximal matching in a bipartite graph can be found greedily.

    for c in range(1, delta + 1):
        # Greedy maximal matching on uncolored edges
        # We can scan all edges; if both endpoints are free (no uncolored edge incident
        # already matched in this round), assign color c.
        # To do this efficiently, we need to know for each vertex whether it is already
        # matched in this round.  We'll use arrays matchedA, matchedB.
        matchedA = [False] * (nA + 1)
        matchedB = [False] * (nB + 1)

        for idx, (u, v) in enumerate(edges):
            if color[idx] == 0 and not matchedA[u] and not matchedB[v]:
                color[idx] = c
                matchedA[u] = True
                matchedB[v] = True

    # The above greedy is O(m * delta) which might be too slow for worst case.
    # But delta can be up to m (400000), so we need a better approach.
    # Let's implement the standard O(m * sqrt(m)) or O(m log m) edge coloring for bipartite graphs.
    # Actually, there is a simpler linear-time algorithm using Euler partitions.
    # We'll use the recursive splitting method: repeatedly split the graph into two
    # subgraphs with max degree ceil(delta/2) and floor(delta/2), then recurse.
    # This gives O(m log delta) which is fine for m=400000, delta<=400000, log~19.

    # Let's implement that instead.

    # We'll store edges as (u, v, idx) and build adjacency lists with edge indices.
    # The splitting method: given a list of edges and current max degree D,
    # if D==0: return.  If D==1: assign color 1 to all edges.
 Otherwise:
    #   Build a temporary graph with the given edges.  Find an Eulerian trail decomposition
    #   into paths/cycles, and color edges alternately along each trail.  This splits
    #   the graph into two subgraphs each with max degree <= ceil(D/2).)
    #   Recurse on each subgraph with appropriate color offset.

    # We'll implement this recursively.  To avoid recursion depth issues, use iterative stack.

    # First, we need to build adjacency for the current subgraph.  Since we'll do this
    # many times, we need an efficient way.  We'll use adjacency lists with edge indices
    # and a visited array for edges in the current subgraph.

    # Let's define a function that takes a list of edge indices and a color offset and D.
    # It will split and assign colors.

    # We'll use a stack of tasks: (edge_list, color_offset, D)
    # For each task, if D==0: continue.  If D==1: assign color_offset+1 to all edges.

    # Else: build adjacency for the subgraph induced by edge_list.
    #   Find trails: for each vertex with odd degree, start a trail there; also for each
    #   vertex with even degree >0, start a trail there (to cover cycles).)
    #   Traverse edges, removing them from adjacency, alternating color assignment
    #   to two new lists: left_edges, right_edges.

    #   Push (left_edges, color_offset, (D+1)//2) and (right_edges, color_offset + (D+1)//2, D//2).)

    # This is the standard algorithm.  Let's implement carefully.

    # We'll need adjacency lists for the original graph to quickly build subgraph adjacency.

    # Actually, for each task we can build adjacency from scratch using the edge_list.
    # Since total work across all levels is O(m log delta), this is fine.

    # Let's implement.

    # We'll store edges as (u, v, idx) in a list all_edges.

    all_edges = [(u, v, idx) for idx, (u, v) in enumerate(edges)]

    # We'll use a stack.  Each element: (edge_indices, color_offset, D)
    # edge_indices is a list of edge indices (0..m-1).)

    stack = [(list(range(m)), 0, delta)]

    while stack:
        edge_list, offset, D = stack.pop()
        if D == 0:
            continue
        if D == 1:
            for idx in edge_list:
                color[idx] = offset + 1
            continue

        # Build adjacency for this subgraph
        # We'll use dictionaries?  Since vertices up to 200000, we can use lists of lists.

        # But we need to know which vertices appear.  We'll use arrays of lists.

        # We'll create temporary adjacency lists for all vertices, but only for those in edge_list.

        # To avoid clearing large arrays each time, we can use a dict mapping vertex to list of (neighbor, edge_idx).)
        # But that might be slower.  Since total edges across all tasks is O(m log delta), we can afford
        # to build adjacency lists using lists of lists and clearing only used vertices.

        # We'll use arrays adj_tempA, adj_tempB as lists of lists, but we need to reset them.
.
        # Simpler: use dict of lists for each vertex that appears.



        adj = {}
        # We'll map vertex id to list of (neighbor, edge_idx).)
        # Vertices from A are 1..nA, from B are nA+1..nA+nB (to unify).).)
        # But we can keep separate arrays for A and B to avoid offset confusion.


        # Let's use two dicts: adjA_temp, adjB_temp.

        adjA_temp = {}
        adjB_temp = {}

        for idx in edge_list:

            u, v, _ = all_edges[idx]
            if u not in adjA_temp:
                adjA_temp[u] = []
            if v not in adjB_temp:
                adjB_temp[v] = []
            adjA_temp[u].append((v, idx))
            adjB_temp[v].append((u, idx))

        # Now find trails.  We'll need to remove edges as we traverse.
  We'll use a stack-based DFS.




        left_edges = []
        right_edges = []

        # We'll process each vertex that has edges.  For each vertex, we start a trail
        # if it has odd degree or if it's the first time we see it (to cover cycles).)
        # Standard approach: for each vertex, while it has edges, start a trail from it.
        # This works because we remove edges as we go.

        # We'll iterate over all vertices that appear in adjA_temp or adjB_temp.

        # To avoid duplicates, we can collect all vertices from edge_list.


        vertices = set()
        for idx in edge_list:

            u, v, _ = all_edges[idx]
            vertices.add(u)
            vertices.add(nA + v)  # use offset for B to unify

        # But we need to map back.  Let's just use separate loops for A and B.


        # Process A vertices
        for u in list(adjA_temp.keys()):
            while adjA_temp.get(u, []):
                # start a trail from u
                # We'll traverse alternating edges, assigning colors alternately.

                # We need to know which side we are on.  We'll use a variable side: 0 for A, 1 for B.

                # Start at u (A side).)
                current = u
                side = 0  # 0 means current is A vertex, 1 means B vertex
                turn = 0  # 0 -> left, 1 -> right

                while True:
                    if side == 0:
                        # current is A vertex
                        lst = adjA_temp.get(current, [])
                        if not lst:
                            break
                        # pop last edge
                        v, idx = lst.pop()
                        # remove from B's adjacency
                        b_list = adjB_temp.get(v, [])
                        # remove the corresponding entry (u, idx) from b_list
                        # We can do this by scanning, but that's O(degree).  Instead, we can
                        # use a different approach: when we pop from A, we also need to remove
                        # from B.  To do this efficiently, we can store in each adjacency entry
                        # a reference to the other side's list?  That's complex.

                        # Simpler: we can just mark edges as visited and skip them when traversing.

                        # Let's use a visited set for edges in this subgraph.  But we need to
                        # remove edges from adjacency to avoid infinite loops.  We can use
                        # a "removed" flag per edge.  Since each edge is processed once per
                        # level, we can use a boolean array visited_edges of size m, reset for each task.

                        # That's easier.  We'll do that.

        # Let's restart with visited_edges approach.

        # We'll have a visited array for this task.  Since m up to 400000, we can
        # allocate a bytearray of size m and reset it for each task.  But resetting
        # O(m) per task would be too much.  Instead, we can use a timestamp array:
        # seen[edge_idx] = current_task_id.  We'll increment task_id each task.



        # Let's implement with timestamp.

        # We'll need a global seen array initialized to 0, and a task_counter.



    # Actually, let's step back and implement the simpler greedy matching algorithm
    # but optimized.  The greedy matching per color is O(m) per color, which is O(m*delta)
    # worst case.  But delta can be large.  However, in practice, maybe it's okay?
    # No, worst case m=400000, delta=200000, that's 8e10 operations, too slow.



    # Let's implement the Euler-split algorithm properly.



    # We'll use a global seen array for edges to mark visited in current task.
    # We'll also use adjacency lists built for the current task.  To remove edges efficiently,
    # we can use a "pointer" per adjacency list: we pop from the end, and if the edge is already
    # visited, we skip it.  This works because we only need to remove edges from the list
    # when we pop them.  But we also need to remove from the other side's list.  However,
    # if we just mark edges as visited, then when we later pop from the other side, we'll
    # skip visited edges.  So we don't need to physically remove from both sides.  We just
    # need to ensure that when we pop from one side, we mark the edge visited, and when we
    # later pop from the other side, we skip it.  This is fine.

    # So algorithm for a task:
    #   Build adjA_temp and adjB_temp as lists of (neighbor, edge_idx).)
    #   For each vertex in A that has edges:
    #       while adjA_temp[u] is not empty:
    #           pop last edge (v, idx); if seen[idx]==task_id: continue; mark seen[idx]=task_id;
    #           start trail: current = v (B side), turn = 0 (assign to left), then alternate.
    #           Actually, we need to assign colors alternately along the trail.  We'll do:
    #           turn = 0
    #           while True:
    #               if turn == 0: left_edges.append(idx) else: right_edges.append(idx)
    #               turn ^= 1
    #               # move to the other side
    #               if current is B: pop from adjB_temp[current]; if seen skip; mark; then current = neighbor (A);)
    #               else: pop from adjA_temp[current]; if seen skip; mark; then current = neighbor (B);)
    #               if no edge found: break
    #   Also need to process cycles that start at A vertices with even degree.  The above
    #   while loop for each A vertex will cover all edges, because we start a trail from every
    #   A vertex that has edges.  Even if a cycle has no A vertex?  But every edge has an A endpoint,
    #   so starting from each A vertex will eventually cover all edges.  However, if a cycle
    #   has all A vertices with even degree, starting from one A vertex will traverse the whole cycle
    #   and return to the start, covering all edges.  So it's fine.



    # Let's implement this.

    # We'll need a global seen array of ints size m, initialized to 0.
    # We'll have a task_id counter starting at 1.



    # We'll also need to store all_edges as (u, v, idx).)





    # Let's code it now.



    # But wait: the Euler-split algorithm requires that the graph is Eulerian?  Actually,
    # for edge coloring, we can use the following: split the graph into two subgraphs by
    # finding an Eulerian trail decomposition.  This works for any graph: we can add dummy
    # edges to make all degrees even, then find Eulerian circuits, and remove dummy edges.

    # The standard method: for each connected component, if it has odd-degree vertices,
    # pair them up with dummy edges, then find Eulerian circuits.  Then color edges alternately
    # along each circuit.  This ensures each vertex gets at most ceil(D/2) edges of each color.

    # Our simple "start from each A vertex" might not produce a proper Eulerian decomposition
    # if there are odd degrees.  But we can handle it: we can start trails from odd-degree
    # vertices.  Since we process all A vertices, we will start from odd-degree A vertices
    # automatically.  However, if an odd-degree vertex is in B, we might not start from it.

    # To be safe, we should start trails from all vertices with odd degree (both A and B).)
    # Then also start from any remaining edges (cycles).)

    # Let's implement that properly.

    # We'll collect all vertices that have edges in this task.  For each vertex, if its degree
    # (number of unvisited edges incident) is odd, start a trail there.  Then for each vertex
    # with remaining edges, start a trail (to cover cycles)..)

    # But computing degrees each time is O(degree).  We can just iterate over all vertices
    # in adjA_temp and adjB_temp, and for each, while it has unvisited edges, start a trail.
    # This will start from every vertex, but that's okay because we remove edges as we go.

    # Actually, if we start from every vertex, we might start from a vertex that has already
    # been covered by a previous trail.  But we can check if it has any unvisited edges left;
    # if not, skip.  So it's fine.



    # Let's implement:

    # For each u in adjA_temp:
    #     while True:
    #         # find an unvisited edge from u
    #         found = False
    #         while adjA_temp[u]:
    #             v, idx = adjA_temp[u].pop()
    #             if seen[idx] == task_id:
    #                 continue
    #             seen[idx] = task_id
    #             found = True
    #             break
    #         if not found: break
    #         # start trail from u, first edge (u,v,idx) assigned to left or right?  We'll alternate.

    #         turn = 0
    #         current = v  # B side
    #         # assign first edge
    #         if turn == 0: left_edges.append(idx) else: right_edges.append(idx)
    #         turn ^= 1
    #         # now continue from current (B side)
    #         while True:
    #             if current is B:
    #                 # pop from adjB_temp[current]
    #                 found2 = False
    #                 while adjB_temp[current]:
    #                     u2, idx2 = adjB_temp[current].pop()
    #                     if seen[idx2] == task_id:
    #                         continue
    #                     seen[idx2] = task_id
    #                     found2 = True
    #                     break
    #                 if not found2: break
    #                 # assign idx2
    #                 if turn == 0: left_edges.append(idx2) else: right_edges.append(idx2)
    #                 turn ^= 1
    #                 current = u2  # now A side
    #             else:  # current is A
    #                 found2 = False
    #                 while adjA_temp[current]:
    #                     v2, idx2 = adjA_temp[current].pop()
    #                     if seen[idx2] == task_id:
    #                         continue
    #                     seen[idx2] = task_id
    #                     found2 = True
    #                     break
    #                 if not found2: break
    #                 if turn == 0: left_edges.append(idx2) else: right_edges.append(idx2)
    #                 turn ^= 1
    #                 current = v2  # now B side

    # This will traverse a trail until it gets stuck.  Since we start from every A vertex,
    # it will cover all edges.  But we also need to start from B vertices with odd degree?  Actually,
    # if a B vertex has odd degree, and we start from an A vertex, the trail might end at that B vertex,
    # leaving no edges?  But if there are multiple odd-degree vertices, we might need to start
    # from B vertices too.  However, since we start from every A vertex, and every edge has an A endpoint,
    # any trail that starts at an A vertex will cover all edges incident to that A vertex.  But what about
    # a component where all A vertices have even degree, but B vertices have odd degree?  That's impossible
    # because sum of degrees in A equals sum in B, so if all A even, then all B even too.  So it's fine.



    # Actually, the above starting from every A vertex will cover all edges, because each edge
    # is incident to an A vertex, and when we process that A vertex, we will eventually pop that edge.

    # So we don't need to start from B vertices.  Good.





    # Let's implement this now.



    # We'll need to store all_edges as (u, v, idx).)
    # We'll also need to know for each edge its endpoints to build adjacency in each task.





    # Let's code the full solution.



    # We'll use a stack of tasks.  Each task: (edge_list, offset, D).)
    # We'll use a global seen array of ints size m, initialized to 0.
    # We'll have a task_counter starting at 1.



    # To avoid recursion depth, use iterative stack.



    # Let's write it.



    # But we need to be careful about memory: edge_list can be large, and we create new lists
    # for left and right.  Total memory across stack is O(m log delta) in worst case?  Actually,
    # at any time, the stack contains tasks whose edge lists partition the original edges, so
    # total size of all edge lists in stack is O(m).  Because each task's edge list is a subset
    # of the original, and the sum of sizes of all tasks at a given depth is m.  So memory is O(m).)



    # Let's implement.



    # We'll also need to build adjA_temp and adjB_temp for each task.  We'll use dicts of lists.
    # Since total edges across all tasks is O(m log delta), this is fine.





    # Let's write the code.



    # After coloring, we output YES and colors.





    # Let's test with example.





    # We'll now write the final code.





    # One more thing: the Euler-split algorithm assigns colors 1..delta.  We need to ensure
    # that the offset is correct.  When D>1, we split into left (ceil(D/2)) colors) and right (floor(D/2) colors).)
    # We'll assign left_edges colors offset+1..offset+ceil(D/2), and right_edges colors offset+ceil(D/2)+1..offset+D.
    # So we push (left_edges, offset, (D+1)//2) and (right_edges, offset + (D+1)//2, D//2).)

    # When D==1, assign offset+1 to all edges.





    # Let's implement.





    # We'll need to be careful with the trail traversal: when we pop an edge from A, we mark it seen,
    # and then later when we pop from B, we skip it.  But we also need to ensure that we don't
    # pop an edge from A that was already seen (from a previous trail).  We do that by checking seen.





    # Let's code.





    # We'll also need to handle m=0 case: delta=0, stack empty, output YES and empty line?  The problem says
    # output m integers; if m=0, we output YES and then a line with 0 integers?  Probably just YES and an empty line.




    # Let's write the final solution.





    # We'll now produce the code block.





    # Actually, let's implement the simpler greedy matching algorithm but with a better approach:
    # We can use the fact that bipartite edge coloring can be done in O(m * delta) but delta might be small?
    # No, worst case delta=200000, m=400000, that's too slow.  So Euler-split is necessary.





    # Let's finalize.





    # We'll write the code now.





    # Note: The Euler-split algorithm is standard for edge coloring bipartite graphs in O(m log delta).)
    # It's correct because each split reduces max degree by half, and the alternating coloring ensures
    # that at each vertex, the number of edges of each color differs by at most 1, so max degree
    # of each subgraph is at most ceil(D/2).)





    # Let's implement it carefully.





    # We'll use sys.setrecursionlimit?  Not needed since iterative.





    # Let's write the final code.





    # We'll now output the code block.





    # Actually, we need to be careful: In the trail traversal, when we start from an A vertex,
    # we pop an edge (v, idx) from adjA_temp[u].  We mark seen[idx]=task_id.  Then we set current=v (B side).)
    # Then we enter the while loop.  In the while loop, we pop from adjB_temp[current].  If we find an unvisited edge,
    # we mark it, assign color, and move to the A neighbor.  Then we pop from adjA_temp[current] (which is now the A neighbor)..)
    # This works.  But we need to ensure that when we pop from adjA_temp[current], we might pop an edge that
    # was already seen (from a previous trail)..  We skip it.  If we skip all, we break.  Good.





    # Let's code.





    # We'll also need to store all_edges as a list of tuples (u, v, idx).).)





    # Let's write the final solution now.





    # I'll produce the code block.



    pass

if __name__ == "__main__":
    main()
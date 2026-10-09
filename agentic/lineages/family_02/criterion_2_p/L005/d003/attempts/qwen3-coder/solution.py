import sys
from collections import defaultdict, deque

def solve():
    import sys
    import threading

    def main():
        import sys
        n, m = map(int, sys.stdin.readline().split())
        
        # For each constraint (a -> b), we build implication graph
        # Variables: x1, x2, ..., xn correspond to qubits 1,2,...,n being 1
        #            -x1, -x2, ..., -xn correspond to qubits 1,2,...,n being 0
        # Literal xi means variable i is True (qubit i is state 1)
        # Literal -xi means variable i is False (qubit i is state 0)

        # Implication graph: for each edge (a,b) in input:
        # If source fires => target must NOT fire
        # Source fires when:
        #     +x: qubit x is 0 => literal -x is True
        #     -x: qubit x is 1 => literal +x is True
        # Target fires when:
        #     +y: qubit y is 0 => literal -y is True
        #     -y: qubit y is 1 => literal +y is True
        # Constraint: if source fires then target does NOT fire
        # That is: source_literal => NOT(target_literal)
        # Which is equivalent to: source_literal => complement_of_target_literal
        # In 2-SAT form: (NOT source_literal) OR (complement_of_target_literal)

        # Let's define:
        # For variable x (qubit x):
        #     node x represents x=True (qubit x is 1)
        #     node -x represents x=False (qubit x is 0)

        edges = []
        for _ in range(m):
            a, b = map(int, sys.stdin.readline().split())
            edges.append((a, b))

        # Build implication graph for 2-SAT
        # Nodes: 1..n and -1..-n
        adj = defaultdict(list)
        rev_adj = defaultdict(list)

        for a, b in edges:
            # a is source, b is target
            # If a fires => b should NOT fire
            # Determine what literals fire:
            # a fires when:
            #   if a > 0: qubit a is 0 => literal -a fires
            #   if a < 0: qubit abs(a) is 1 => literal abs(a) fires
            # b fires when:
            #   if b > 0: qubit b is 0 => literal -b fires
            #   if b < 0: qubit abs(b) is 1 => literal abs(b) fires

            # So constraint is:
            # (source_literal => NOT target_literal)
            # which is equivalent to:
            # (NOT source_literal OR NOT target_literal)
            # This gives us two implications:
            # source_literal => NOT target_literal
            # target_literal => NOT source_literal

            if a > 0:
                lit_a = -a  # qubit a=0 means literal -a (node -a) is true
            else:
                lit_a = -a  # qubit abs(a)=1 means literal abs(a) (node abs(a)) is true

            if b > 0:
                lit_b = -b  # qubit b=0 means literal -b (node -b) is true
            else:
                lit_b = -b  # qubit abs(b)=1 means literal abs(b) (node abs(b)) is true

            # Constraint: if lit_a is true, then lit_b must be false
            # This is: lit_a => NOT lit_b
            # Equivalent to: NOT( lit_a AND lit_b )
            # In implication graph: add edge from lit_a to NOT(lit_b)
            # and from lit_b to NOT(lit_a)

            not_lit_b = -lit_b
            not_lit_a = -lit_a

            adj[lit_a].append(not_lit_b)
            adj[lit_b].append(not_lit_a)
            rev_adj[not_lit_b].append(lit_a)
            rev_adj[not_lit_a].append(lit_b)

        # Now run Kosaraju's algorithm to check if 2-SAT is satisfiable
        visited = [False] * (2 * n + 1)
        order = []
        component = [0] * (2 * n + 1)

        def dfs1(u):
            visited[u] = True
            for v in adj[u]:
                if not visited[v]:
                    dfs1(v)
            order.append(u)

        def dfs2(u, comp_id):
            component[u] = comp_id
            for v in rev_adj[u]:
                if component[v] == 0:
                    dfs2(v, comp_id)

        # First DFS on original graph
        for i in range(1, n+1):
            if not visited[i]:
                dfs1(i)
            if not visited[-i]:
                dfs1(-i)

        # Second DFS on transpose graph in reverse finish order
        comp_id = 1
        while order:
            u = order.pop()
            if component[u] == 0:
                dfs2(u, comp_id)
                comp_id += 1

        # Check if any variable and its negation are in same SCC
        for i in range(1, n+1):
            if component[i] == component[-i]:
                print("NO")
                return

        # Extract solution: for each variable, choose the one with higher component number
        result = [0] * (n + 1)
        for i in range(1, n+1):
            if component[i] > component[-i]:
                result[i] = 1  # qubit i is 1
            else:
                result[i] = 0  # qubit i is 0

        print("YES")
        print(*result[1:])

    threading.Thread(target=main).start()

solve()
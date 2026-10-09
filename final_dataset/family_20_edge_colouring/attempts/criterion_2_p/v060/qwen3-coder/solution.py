import sys
from collections import defaultdict, deque

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    idx = 0
    n_T = int(data[idx])
    idx += 1
    n_P = int(data[idx])
    idx += 1
    m = int(data[idx])
    idx += 1
    
    documents = []
    translator_docs = defaultdict(list)
    proofreader_docs = defaultdict(list)
    
    for i in range(m):
        u = int(data[idx]) - 1
        idx += 1
        v = int(data[idx]) - 1
        idx += 1
        documents.append((u, v))
        translator_docs[u].append(i)
        proofreader_docs[v].append(i)
    
    # Determine K (maximum degree)
    K = 0
    for u in translator_docs:
        K = max(K, len(translator_docs[u]))
    for v in proofreader_docs:
        K = max(K, len(proofreader_docs[v]))
    
    # Edge coloring using BFS-like approach
    # We model this as edge coloring of a bipartite graph
    # Each document is an edge between translator and proofreader
    
    # For each node, keep track of which colors are used on its edges
    translator_colors = [set() for _ in range(n_T)]
    proofreader_colors = [set() for _ in range(n_P)]
    
    # Result array
    result = [0] * m
    
    # For each document, assign a color
    for i in range(m):
        u, v = documents[i]
        # Find a color not used by u or v
        color = 1
        while color in translator_colors[u] or color in proofreader_colors[v]:
            color += 1
        result[i] = color
        translator_colors[u].add(color)
        proofreader_colors[v].add(color)
    
    print("YES")
    print(' '.join(map(str, result)))

if __name__ == "__main__":
    main()
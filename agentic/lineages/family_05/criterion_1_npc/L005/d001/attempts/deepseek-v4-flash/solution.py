import sys

def solve():
    input = sys.stdin.readline
    k, t = map(int, input().split())
    triples = []
    for _ in range(t):
        x, y, z = map(int, input().split())
        triples.append((x-1, y-1, z-1))
    
    # For each compute node, store list of (image, shard) pairs
    by_node = [[] for _ in range(k)]
    for x, y, z in triples:
        by_node[x].append((y, z))
    
    # DP over compute nodes: mask of used images and shards
    # We'll store for each mask of images, the possible mask of shards
    # But k up to 22, so 2^22 * 2^22 is too big.
    # Instead, we do DP over compute nodes, tracking used images and shards.
    # We can use memoization with bitmasks for images and shards.
    
    # Since k <= 22, we can do DP over images mask, and for each compute node,
    # try all possible (image, shard) pairs.
    
    # We'll do recursion with memoization: state = (node_index, image_mask, shard_mask)
    # But that's too many states. Instead, we can do DP over images only,
    # and for each image mask, we know which shards are used.
    
    # Better: Since k <= 22, we can do DP over images mask, and for each compute node,
    # we assign an image and a shard. We'll use bitmask for images and shards.
    
    # We'll do DP: dp[mask_images] = set of possible shard masks
    # But set of masks can be large. However, k=22 => 2^22 = 4M, too big for set of masks.
    
    # Alternative: Use bipartite matching between images and shards for each subset of compute nodes?
    # Actually, we can model as: choose a permutation of images and shards for compute nodes.
    
    # Since k <= 22, we can do DP over compute nodes with bitmask of images and shards,
    # but we can prune: we only need to know if there's a perfect matching.
    
    # Let's do DP over compute nodes, with bitmask of used images and shards.
    # We'll use memoization with (node_idx, image_mask, shard_mask).
    # But that's 22 * 2^22 * 2^22 impossible.
    
    # Instead, we can do DP over images mask only, and for each image mask,
    # we store the set of possible shard masks. But that's still huge.
    
    # However, k <= 22, so we can do DP over images mask, and for each image mask,
    # we store a bitset of shard masks? That's 2^22 * 2^22 bits = 2^44 bits = 2^41 bytes, too big.
    
    # Let's think differently: This is a 3D matching problem, NP-hard in general,
    # but k <= 22 allows exponential in k, but not 2^(2k).
    
    # We can do DP over compute nodes, but we only need to track which images and shards are used.
    # Since k <= 22, we can use bitmask for images and shards, and do DFS with memoization.
    # The number of states is at most k * 2^k * 2^k = 22 * 4M * 4M = too big.
    
    # But we can reduce: For each compute node, we only have limited options.
    # We can do backtracking with pruning, but worst-case still exponential.
    
    # However, k=22 is small enough for meet-in-the-middle? Or we can use DP over images mask,
    # and for each image mask, we store the set of shard masks reachable.
    # The number of distinct shard masks per image mask is at most 2^k, but in practice small.
    
    # Let's implement DP over images mask, storing a set of shard masks.
    # We'll iterate compute nodes, and for each compute node, we try all its (image, shard) pairs.
    
    # dp[mask_images] = set of shard masks
    dp = {0: {0}}
    
    for node in range(k):
        new_dp = {}
        for img_mask, shard_masks in dp.items():
            for img, shard in by_node[node]:
                if not (img_mask >> img) & 1 and not any((shard_masks >> shard) & 1 for _ in [0]): # check shard not used
                    # Actually we need to check shard not used in the specific shard_mask
                    pass
        # This is getting messy.
    
    # Let's do a cleaner approach: Use recursion with memoization on (node_idx, image_mask, shard_mask).
    # But we can prune: if we have used more images than nodes processed, etc.
    # Since k=22, the number of states might be manageable if we use bitmasks and memoization.
    # Let's try that.
    
    from functools import lru_cache
    
    # Precompute for each node, list of (img, shard)
    # We'll do DFS: assign node idx, with used images mask and shards mask.
    # If we reach k, success.
    
    # But state space: 22 * 2^22 * 2^22 = 22 * 4M * 4M = 3.7e14, too big.
    
    # We need a better approach.
    
    # Since k <= 22, we can do DP over images mask, and for each image mask,
    # we store the set of shard masks that can be achieved using some subset of compute nodes.
    # But we need to assign each compute node exactly one triple.
    
    # Actually, we can think of it as: we need to pick a permutation of images and shards
    # such that for each compute node i, (i, perm_img[i], perm_shard[i]) is in the list.
    
    # This is equivalent to finding a perfect matching in a 3-partite hypergraph.
    # We can use DP over subsets of compute nodes? That's 2^22 = 4M, and for each subset,
    # we need to know if there's a matching. But we also need to track images and shards.
    
    # Another idea: Since k <= 22, we can use DP over images mask, and for each image mask,
    # we store the set of shard masks that can be matched with some subset of compute nodes.
    # But we need to ensure each compute node used exactly once.
    
    # Let's do DP over compute nodes, but we only track used images and shards.
    # We'll use memoization with (node_idx, image_mask, shard_mask).
    # But we can reduce state by noting that the number of used images equals node_idx,
    # and number of used shards equals node_idx. So we can encode state as (node_idx, image_mask, shard_mask)
    # but we can derive node_idx from popcount(image_mask) = popcount(shard_mask) = node_idx.
    # So state is just (image_mask, shard_mask) with equal popcounts.
    # Number of such states: sum_{i=0}^k C(k,i)^2 = C(2k,k) ~ C(44,22) ~ 2e12, too big.
    
    # But k=22, C(44,22) ~ 2e12, too big.
    
    # We need a different approach.
    
    # Since k <= 22, we can use meet-in-the-middle: split compute nodes into two halves.
    # For each half, enumerate all possible assignments of images and shards.
    # Then combine.
    
    # For each half, we can generate all possible (image_mask, shard_mask) pairs that are achievable.
    # Number of assignments per half: at most (k!)^2? Actually each compute node has at most k^2 options,
    # but we can prune. In worst case, each node has k^2 options, so for half of 11 nodes,
    # that's (k^2)^11 = 22^22 ~ huge. But we can use DP over subsets.
    
    # Let's do DP over subsets of compute nodes in each half.
    # For each subset, we can compute possible (image_mask, shard_mask) pairs.
    # But that's 2^11 = 2048 subsets per half, and for each subset we store set of pairs.
    # That's feasible.
    
    # Let's implement:
    # Split nodes into two halves: first half size n1 = k//2, second half size n2 = k - n1.
    # For each half, we do DP over subsets of nodes in that half.
    # dp_half[mask] = set of (image_mask, shard_mask) achievable using exactly the nodes in mask.
    # We'll build by adding one node at a time.
    
    # But we need to combine two halves: we need image_mask1 | image_mask2 = full, shard_mask1 | shard_mask2 = full,
    # and they are disjoint.
    
    # Let's implement.
    
    n1 = k // 2
    n2 = k - n1
    nodes1 = list(range(n1))
    nodes2 = list(range(n1, k))
    
    # For each half, build dp over subsets
    def build_dp(nodes):
        m = len(nodes)
        dp = [set() for _ in range(1 << m)]
        dp[0].add((0,0))
        for mask in range(1 << m):
            if not dp[mask]:
                continue
            # Try adding a node not in mask
            for i in range(m):
                if not (mask >> i) & 1:
                    node = nodes[i]
                    for img, shard in by_node[node]:
                        # Check if img/shard already used in any state in dp[mask]
                        # We'll need to update each state individually
                        for img_mask, shard_mask in dp[mask]:
                            if not (img_mask >> img) & 1 and not (shard_mask >> shard) & 1:
                                new_mask = mask | (1 << i)
                                dp[new_mask].add((img_mask | (1 << img), shard_mask | (1 << shard)))
        return dp
    
    dp1 = build_dp(nodes1)
    dp2 = build_dp(nodes2)
    
    full_img = (1 << k) - 1
    full_shard = (1 << k) - 1
    
    # Combine: for each mask1 in dp1, mask2 in dp2, if mask1 | mask2 == full_mask_nodes,
    # and image masks disjoint, shard masks disjoint, and union = full.
    full_nodes_mask = (1 << k) - 1
    # But dp1 and dp2 are indexed by local masks (size n1, n2). We need to map to global.
    
    # Actually, we can just iterate over all states in dp1 and dp2.
    # For each state in dp1: (img1, shard1) with popcount = size of mask1.
    # For each state in dp2: (img2, shard2) with popcount = size of mask2.
    # We need img1 & img2 == 0, shard1 & shard2 == 0, and img1|img2 == full, shard1|shard2 == full.
    # Also mask1 and mask2 must cover all nodes: mask1 covers nodes1 subset, mask2 covers nodes2 subset.
    # Since we split nodes, we need mask1 = all nodes1, mask2 = all nodes2.
    
    # So we only need dp1[full_mask1] and dp2[full_mask2].
    
    full1 = (1 << n1) - 1
    full2 = (1 << n2) - 1
    
    states1 = dp1[full1]
    states2 = dp2[full2]
    
    # Find a pair
    for img1, shard1 in states1:
        for img2, shard2 in states2:
            if (img1 & img2) == 0 and (shard1 & shard2) == 0:
                if (img1 | img2) == full_img and (shard1 | shard2) == full_shard:
                    # Found! Now reconstruct assignment.
                    # We need to output triples.
                    # We'll reconstruct from dp1 and dp2 by storing parent info.
                    # But we didn't store parents. We'll do a separate reconstruction.
                    # Let's just do a backtracking search with the found masks.
                    # We'll assign nodes in order.
                    assignment = [None] * k
                    # For first half
                    used_img1 = img1
                    used_shard1 = shard1
                    # We'll backtrack through dp1 to find which node got which img/shard.
                    # We can do a recursive reconstruction.
                    def reconstruct(nodes, dp, full_mask, img_mask, shard_mask):
                        # nodes list, dp for that half, full_mask, target img_mask, shard_mask
                        m = len(nodes)
                        res = [None] * m
                        # We'll go from full_mask down to 0
                        mask = full_mask
                        while mask:
                            # find a node i in mask such that removing it gives a state in dp[mask ^ (1<<i)]
                            # that can lead to current img_mask, shard_mask
                            for i in range(m):
                                if (mask >> i) & 1:
                                    prev_mask = mask ^ (1 << i)
                                    node = nodes[i]
                                    for img, shard in by_node[node]:
                                        if (img_mask >> img) & 1 and (shard_mask >> shard) & 1:
                                            # Check if prev state has img_mask without this img, shard_mask without this shard
                                            if (img_mask ^ (1 << img)) in [im for im, _ in dp[prev_mask]]:
                                                # Need to check exact pair
                                                for im2, sh2 in dp[prev_mask]:
                                                    if im2 == (img_mask ^ (1 << img)) and sh2 == (shard_mask ^ (1 << shard)):
                                                        res[i] = (node, img, shard)
                                                        img_mask = im2
                                                        shard_mask = sh2
                                                        mask = prev_mask
                                                        break
                                                if res[i] is not None:
                                                    break
                                    if res[i] is not None:
                                        break
                        return res
                    
                    assign1 = reconstruct(nodes1, dp1, full1, img1, shard1)
                    assign2 = reconstruct(nodes2, dp2, full2, img2, shard2)
                    
                    # Combine
                    for i, (node, img, shard) in enumerate(assign1):
                        assignment[node] = (img+1, shard+1)
                    for i, (node, img, shard) in enumerate(assign2):
                        assignment[node] = (img+1, shard+1)
                    
                    print("YES")
                    for node in range(k):
                        img, shard = assignment[node]
                        print(node+1, img, shard)
                    return
    
    print("NO")

if __name__ == "__main__":
    solve()
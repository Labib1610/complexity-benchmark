# Quorum Bootstrapping

Time limit: 2 s
Memory limit: 256 MB

A distributed computing cluster consists of $n$ nodes. Certain pairs of nodes have successfully established a bidirectional cryptographic tunnel. A "consensus quorum" is defined as a subset of nodes $Q$ where every distinct pair of nodes within $Q$ maintains an active tunnel. 

To initialize the decentralized ledger, the system must elect a bootstrapping quorum. Because the power set of nodes has size $2^n$, evaluating all subsets to find a strictly optimal configuration is generally computationally prohibitive. Instead, the protocol dictates that we find any valid quorum of a targeted size $k$. Since multiple such subsets may exist, the protocol enforces determinism: the chosen quorum must be the lexicographically first sequence when the node IDs in the subset are sorted in ascending order (i.e., minimizing the first node ID, then the second, and so on).

For the current network deployment phase, the targeted quorum size $k$ is strictly set to 3. You are provided with the list of active tunnels. It is guaranteed that the network topology contains at least one valid quorum of this required size. 

## Input
The first line contains two integers $n$ and $m$ (3 ≤ $n$ ≤ 2000, 3 ≤ $m$ ≤ min($n(n−1)/2$, $2 \cdot 10^5$)), representing the number of nodes and the number of active tunnels.
Each of the next $m$ lines contains two integers $u$ and $v$ (1 ≤ $u, v$ ≤ $n$, $u \neq v$), indicating a tunnel between node $u$ and node $v$. Each pair of nodes is connected by at most one tunnel. 
It is guaranteed that at least one valid quorum of size 3 exists.

## Output
Print three integers $a$, $b$, and $c$ on a single line, separated by spaces, with $a < b < c$, representing the node IDs of the selected consensus quorum.

## Example 1
Input:
```
4 5
1 2
1 3
2 3
2 4
3 4
```
Output:
```
1 2 3
```

## Example 2
Input:
```
5 6
1 2
1 4
2 4
3 4
3 5
4 5
```
Output:
```
1 2 4
```

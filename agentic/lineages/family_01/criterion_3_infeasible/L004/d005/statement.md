# Critical Interference

Time limit: 2 s
Memory limit: 256 MB

A proposed communications standard attempts to allocate $n$ transceivers (labeled 1 through $n$) into a network. However, testing has revealed $m$ specific bidirectional interference links between pairs of transceivers. 

To diagnose the core issue in the network's topology, engineers analyze the interference signatures of transceiver triplets. For any chosen subset of exactly three transceivers, let's denote them (in any order) as $v_1, v_2,$ and $v_3$. We construct a $3 \times 3$ signature matrix $S$, where the entry $S_{i,j}$ is $1$ if there is a bidirectional interference link between $v_i$ and $v_j$, and $0$ otherwise. By definition, a transceiver does not interfere with itself, so the diagonal entries are always zero ($S_{i,i} = 0$ for all $i \in \{1, 2, 3\}$).

Your objective is to isolate a subset of exactly three transceivers whose signature matrix $S$ has a determinant exactly equal to $2$. The existence of such a subset proves a critical flaw in the network. It is guaranteed that at least one such subset is present.

## Input
The first line contains the transceiver count $n$ and the interference link count $m$ ($3 \le n \le 2000$, $3 \le m \le \min(n \cdot (n-1)/2, 2 \cdot 10^5)$).
The following $m$ lines each detail a pair of transceivers $u$ and $v$ that share a mutual interference link.
At least one subset of three transceivers satisfying the determinant condition is guaranteed to exist.

## Output
Provide the labels of the three transceivers forming the subset, printed on a single line in ascending numerical order.
In the event that several such subsets exist, you must resolve the ambiguity by selecting the subset that includes the transceiver with the absolute lowest label. Should multiple subsets share this lowest-labeled transceiver, further narrow your selection to those whose second-lowest label is as small as possible. If ambiguity still persists, choose the subset whose highest label is minimal.

## Example 1
### Input
```
4 5
1 2
1 3
2 3
2 4
3 4
```
### Output
```
1 2 3
```

## Example 2
### Input
```
5 6
1 2
1 4
2 4
3 4
3 5
4 5
```
### Output
```
1 2 4
```
# Critical Interference

Time limit: 2 s
Memory limit: 256 MB

A proposed communications standard attempts to allocate $n$ transceivers (labeled 1 through $n$) into a network. However, testing has revealed $m$ specific bidirectional interference links between pairs of transceivers. Each link connects two distinct transceivers, and no two links connect the same pair.

To diagnose the core issue in the network's topology, engineers analyze the *cross-talk isolation matrix* of transceiver triplets. For any chosen subset of exactly three transceivers, we order them by their labels as $u_1 < u_2 < u_3$. 
We then construct a $3 \times 3$ matrix $W$, where the entry $W_{i,j}$ (for $1 \le i, j \le 3$) is defined as follows:
- $W_{i,j} = 1$ if $i \neq j$ and testing has revealed an interference link between $u_i$ and $u_j$.
- $W_{i,j} = 0$ if $i \neq j$ and there is no interference link between them.
- $W_{i,i} = -1$ for all $i \in \{1, 2, 3\}$, as the self-interference baseline is inverted.

The *stability characteristic* of the triplet is defined as the determinant of this matrix $W$. 

Your objective is to isolate a subset of exactly three transceivers whose stability characteristic is exactly $4$. The existence of such a subset proves a critical flaw in the network. It is guaranteed that at least one such subset is present.

## Input
The first line contains the transceiver count $n$ and the interference link count $m$ ($3 \le n \le 2000$, $3 \le m \le \min(n \cdot (n-1)/2, 2 \cdot 10^5)$).
The following $m$ lines each detail a pair of transceivers $u$ and $v$ that share a mutual interference link.
At least one subset of three transceivers satisfying the stability condition is guaranteed to exist.

## Output
Provide the labels of the three transceivers forming the subset, printed on a single line as three integers $a$, $b$, and $c$ with $a < b < c$.
Among all valid triples $(a, b, c)$ with $a < b < c$, choose the one with the smallest $a$; if there is a tie, choose the one with the smallest $b$; if there is still a tie, choose the one with the smallest $c$.

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
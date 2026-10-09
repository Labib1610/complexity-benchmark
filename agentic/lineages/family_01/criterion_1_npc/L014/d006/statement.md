# Problem A — Grid Harmonic Resonance

Time limit: 2 s
Memory limit: 256 MB

You are deploying a computational grid consisting of $n$ processing nodes, labeled 1 through $n$. Your task is to configure the clock speed for each node. The available clock speed options for any node are 1, 2, and 3 GHz.

Certain pairs of nodes share a direct synchronization link. Due to hardware limitations, if the clock speeds $x$ and $y$ of two linked nodes are such that the value $(x^3 + y^3 + x \cdot y)$ does NOT end in the digit 1, they will experience harmonic resonance and the link will fail. To ensure the grid is fully operational, every synchronization link must connect two nodes that do not experience harmonic resonance.

You are provided with the number of nodes and the exact pairs that share a synchronization link. You must output a fully functional clock speed assignment for the grid, or indicate if it is impossible.

## Input
The first line contains two integers $n$ and $m$ — the number of processing nodes and the number of synchronization links ($1 \le n \le 40$, $0 \le m \le n \cdot (n-1)/2$).
Each of the following $m$ lines contains two distinct integers $u$ and $w$ ($1 \le u, w \le n$, $u \neq w$), representing a pair of nodes connected by a synchronization link. It is guaranteed that each unordered pair of nodes appears at most once in the input.

## Output
If no valid clock speed assignment can be found, print a single line containing `NO`.
Otherwise, print `YES` on the first line. On the second line, print $n$ integers $a_1, a_2, \dots, a_n$ (where each $a_i \in \{1, 2, 3\}$), representing the clock speed assigned to node $i$. Any valid assignment will be accepted.

## Example 1
Input:
```
4 5
1 2
1 3
2 3
1 4
2 4
```
Output:
```
YES
1 2 3 3
```

## Example 2
Input:
```
4 6
1 2
1 3
1 4
2 3
2 4
3 4
```
Output:
```
NO
```
# Production Line Diagnostics

Time limit: 2 s   Memory limit: 256 MB

A manufacturing facility operates continuously. Certain pairs of manufacturing steps require a shared specialized calibration tool. 

Your diagnostic software must isolate a root cause of an allocation failure by identifying a group of exactly three steps that form an unresolvable bottleneck. 

Consider any group of exactly three distinct steps, which we can arbitrarily label as $s_1, s_2$, and $s_3$. We evaluate their mutual dependencies by constructing three vectors, $\mathbf{v}_1, \mathbf{v}_2$, and $\mathbf{v}_3$, in $\mathbb{R}^3$.

For each $i \in \{1, 2, 3\}$, the vector $\mathbf{v}_i = (x_{i,1}, x_{i,2}, x_{i,3})$ is defined such that:
- $x_{i,j} = 1$ if step $s_i$ and step $s_j$ require a shared calibration tool.
- $x_{i,j} = 0$ if they do not require a shared tool, or if $i = j$.

A group of three distinct steps is classified as an unresolvable bottleneck if and only if their corresponding vectors $\mathbf{v}_1, \mathbf{v}_2$, and $\mathbf{v}_3$ are linearly independent over the real numbers.

## Input
The first line contains two integers $n$ and $m$ ($3 \le n \le 2000$, $3 \le m \le \min(n \cdot (n-1)/2, 2 \cdot 10^5)$), representing the total number of manufacturing steps and the number of shared tool requirements. Steps are numbered from $1$ to $n$.

Each of the following $m$ lines contains two integers $u$ and $v$ ($1 \le u, v \le n$, $u \neq v$), indicating that step $u$ and step $v$ require a shared calibration tool.

It is guaranteed that at least one unresolvable bottleneck exists in the provided data.

## Output
Print three integers $a$, $b$, and $c$ on a single line, separated by spaces, with $a < b < c$, representing the identifiers of the three steps that form an unresolvable bottleneck. If multiple such groups exist, output the combination that is sequentially lowest: the one with the smallest possible value for $a$; in case of a tie, the smallest possible value for $b$; and finally the smallest possible value for $c$.

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
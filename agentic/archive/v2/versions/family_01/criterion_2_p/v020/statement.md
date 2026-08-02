# Grid Bus Assignment

Time limit: 1 s   Memory limit: 256 MB

A power grid manages $n$ regional distribution hubs, numbered from $1$ to $n$. To balance load and prevent resonance, the grid operates on two distinct bus lines, labeled $1$ and $2$. Every hub must be assigned to exactly one of these two bus lines.

There are $m$ transmission lines installed between pairs of hubs. Each line links two distinct hubs $u$ and $v$. A physical stability constraint requires that any two hubs linked by a transmission line must be assigned to different bus lines.

Your task is to determine whether it is possible to assign a bus line ($1$ or $2$) to every hub such that all transmission line constraints are satisfied. If a valid configuration exists, output `YES` along with the assignment sequence $s_1, s_2, \dots, s_n$ that is lexicographically smallest. If no such configuration can satisfy all constraints, output `NO`.

An assignment sequence $A = (a_1, a_2, \dots, a_n)$ is lexicographically smaller than $B = (b_1, b_2, \dots, b_n)$ if at the smallest index $i$ where $a_i \neq b_i$, $a_i < b_i$.

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 2\cdot 10^5$, $0 \le m \le 2\cdot 10^5$), representing the number of hubs and transmission lines, respectively.

Each of the following $m$ lines contains two integers $u$ and $v$ ($1 \le u, v \le n$, $u \neq v$), representing a transmission line between hub $u$ and hub $v$.

## Output
If no valid assignment exists, print a single line containing `NO`.

Otherwise, print `YES` on the first line. On the second line, print $n$ space-separated integers $s_1, s_2, \dots, s_n$ (where each $s_i \in \{1, 2\}$), representing the lexicographically smallest valid assignment.

## Example 1
Input:
```
4 4
1 2
2 3
3 4
1 4
```
Output:
```
YES
1 2 1 2
```

## Example 2
Input:
```
3 3
1 2
1 3
2 3
```
Output:
```
NO
```

# Problem B — System Equilibrium

Time limit: 1 s   Memory limit: 256 MB

You are tasked with finding a state vector $S = \begin{pmatrix} s_1 \\ s_2 \\ \vdots \\ s_n \end{pmatrix}$ such that $s_i \in \{1, 2\}$ for all $1 \le i \le n$, which puts a simulated system into equilibrium.

The system consists of $n$ particles and a log of $m$ interactions. Each interaction involves two particles $u$ and $v$. Let $d_i$ be the total number of times particle $i$ appears across all $m$ interactions (if an interaction involves the same particle twice, i.e., $u = v$, it contributes 2 to the count $d_u$).

The system is in equilibrium if and only if its total interaction energy is exactly equal to its theoretical base energy. 
The interaction energy is defined as $2 \sum_{j=1}^m s_{u_j} s_{v_j}$, where the sum is over all $m$ logged interactions. 
The base energy is defined as $3 \sum_{i=1}^n d_i s_i - 5m$.

If there are multiple valid vectors $S$ that satisfy the equilibrium condition, you must output the sequence $s_1 \dots s_n$ that is lexicographically smallest.

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 2\cdot 10^5$, $0 \le m \le 2\cdot 10^5$).
Each of the following $m$ lines contains two integers $u$ and $v$ ($1 \le u, v \le n$) — the indices of the two particles involved in the $j$-th interaction. The interactions are given in order for $j = 1, 2, \dots, m$.

## Output
If no such vector $S$ exists, print a single line containing `NO`.
Otherwise, print `YES` on the first line. On the second line, print $n$ integers $s_1 \dots s_n$ (where each $s_i \in \{1,2\}$) representing the elements of the lexicographically smallest valid vector $S$.

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
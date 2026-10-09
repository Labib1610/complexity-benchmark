# Problem B — System Equilibrium

Time limit: 1 s   Memory limit: 256 MB

You are tasked with finding a state vector $S = \begin{pmatrix} s_1 \\ s_2 \\ \vdots \\ s_n \end{pmatrix}$ such that $s_i \in \{1, 2\}$ for all $1 \le i \le n$, which puts a simulated system into equilibrium.

The system consists of $n$ particles and a log of $m$ interactions. Each interaction involves two particles $u$ and $v$.
The equilibrium of the system is governed by a strict set of conditional dependency rules triggered by the logged interactions.

For every logged interaction between particle $u$ and particle $v$, the following dependency rules must all be satisfied to maintain equilibrium:
- If $s_u = 1$, then it is required that $s_v = 2$.
- If $s_u = 2$, then it is required that $s_v = 1$.
- If $s_v = 1$, then it is required that $s_u = 2$.
- If $s_v = 2$, then it is required that $s_u = 1$.

If any of these implications are violated for any interaction in the log, the system fails to reach equilibrium. Note that if an interaction logs the same particle twice (i.e., $u = v$), the rules apply to it as well, which may immediately destabilize the system.

If there are multiple valid state vectors $S$ that satisfy all dependency rules, you must output the sequence $s_1 \dots s_n$ that is lexicographically smallest.

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
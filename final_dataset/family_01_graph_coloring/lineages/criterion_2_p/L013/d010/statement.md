# Problem B — Transmission Configuration

Time limit: 1 s   Memory limit: 256 MB

You are configuring a transmission system with $n$ gears. You must assign each gear $i$ a gear ratio $p_i \in \{1, 2\}$.

You are given a list of $m$ meshing pairs. The $k$-th pair indicates that gear $u_k$ and gear $v_k$ are directly meshed together.
To ensure the correct torque conversion, every meshed pair must have a combined gear ratio of exactly 2. The combined gear ratio of two directly meshed gears is defined as the product of their individual gear ratios ($p_{u_k} \times p_{v_k}$).

Your objective is to determine if there exists a valid gear ratio assignment for all $n$ gears. If there are multiple valid assignments, you must output the one whose sequence $p_1, p_2, \dots, p_n$ is lexicographically smallest. (A sequence $a$ is lexicographically smaller than a sequence $b$ if, at the first index $i$ where they differ, $a_i < b_i$.)

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 2\cdot 10^5$, $0 \le m \le 2\cdot 10^5$), representing the number of gears and the number of meshing pairs.
The following $m$ lines each contain two integers $u$ and $v$ ($1 \le u, v \le n$), specifying the 1-based indices of the two gears in a meshing pair.

## Output
If no valid gear ratio assignment is possible, print a single line containing `NO`.
Otherwise, print `YES` on the first line. On the second line, output $n$ integers $p_1, p_2, \dots, p_n$ (where each $p_i \in \{1, 2\}$) denoting the assigned gear ratios. Among all valid assignments, you must output the lexicographically smallest sequence.

## Example 1
**Input:**
```text
4 4
1 2
2 3
3 4
1 4
```
**Output:**
```text
YES
1 2 1 2
```

## Example 2
**Input:**
```text
3 3
1 2
1 3
2 3
```
**Output:**
```text
NO
```
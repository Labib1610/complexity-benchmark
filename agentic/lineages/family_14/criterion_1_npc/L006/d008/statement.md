# Power-Series Transform Configuration

Time limit: 5 s   Memory limit: 256 MB

## Description

A data engineering team is configuring a system of $n$ continuous feature variables, indexed 1 through $n$. The team is focused on a specific subset of $t$ critical variables.

The team can activate a selection from $m$ available bidirectional updates. Each available update acts on a specific pair of variables $u$ and $v$, and has a one-time activation cost $w$.

If the team selects a subset of these updates, they construct an $n \times n$ symmetric matrix $M$ as follows:
- $M_{u,v} = M_{v,u} = 1$ if the available update between $u$ and $v$ is selected.
- All other entries of $M$ are $0$.

Using this matrix $M$, a power-series transform matrix $S$ is mathematically defined by the infinite series:
$S = \sum_{k=0}^{\infty} \frac{M^k}{k!}$

The team's objective is to select a subset of updates such that in the resulting matrix $S$, the entry $S_{i,j} > 0$ for every pair of critical variables $i$ and $j$ (including when $i = j$).

The team is permitted to activate updates involving non-critical variables, provided their inclusion helps establish the required positivity condition among the critical variables. Each available update is either selected for activation or not selected. If selected, its activation cost is paid exactly once. The total cost is the sum of the activation costs of the distinct updates the team chooses to activate.

Determine the minimum total activation cost required to select a set of updates such that the condition $S_{i,j} > 0$ is satisfied for all pairs of critical variables $i$ and $j$.

## Input

The first line provides three integers $n$, $m$, and $t$ (1 ≤ $t$ ≤ 10, 1 ≤ $n$ ≤ 100, 0 ≤ $m$ ≤ $n$·($n$−1)/2).
The second line lists $t$ distinct integers representing the indices of the critical variables.
Each of the subsequent $m$ lines specifies an available update using three integers $u$, $v$, and $w$ (1 ≤ $u$, $v$ ≤ $n$, $u$ ≠ $v$, 1 ≤ $w$ ≤ 1000000). This indicates an update between variables $u$ and $v$ with a one-time activation cost of $w$.
It is guaranteed that the set of all $m$ available updates is sufficient to satisfy the requirement for all critical variables.

## Output

Print a single integer: the minimum total activation cost required to ensure $S_{i,j} > 0$ for all pairs of critical variables $i$ and $j$ under the selected updates.

## Examples

### Example 1

**Input**
```
4 6 3
1 2 3
1 4 1
2 4 1
3 4 1
1 2 2
2 3 2
1 3 2
```

**Output**
```
3
```

### Example 2

**Input**
```
4 4 3
1 2 3
1 2 1
2 3 1
1 4 10
3 4 10
```

**Output**
```
2
```

### Example 3

**Input**
```
3 2 1
1
1 2 5
2 3 5
```

**Output**
```
0
```

## Note

In Example 1, activating the updates that involve the non-critical variable 4 (which require costs of 1, 1, and 1; total cost = 3) is more efficient than activating the updates directly involving only the three critical variables (which would result in a total cost of 4). The updates between (1, 4) and (2, 4) make $S_{1,2} > 0$, and including (3, 4) ensures the positivity condition holds for all pairs among the critical variables 1, 2, and 3. Thus, variable 4 acts as an effective intermediary. 
In Example 3, there is only a single critical variable. The requirement $S_{1,1} > 0$ is inherently satisfied because the $k=0$ term of the series is the identity matrix, meaning $S_{i,i} \ge 1 > 0$ regardless of which updates are selected. Therefore, no updates need to be activated, resulting in a total cost of 0.
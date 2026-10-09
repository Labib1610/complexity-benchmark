# Problem A — Tier Differential Resolution

Time limit: 2 s
Memory limit: 256 MB

You are configuring a distributed system consisting of $n$ components, numbered 1 through $n$. Each component $i$ must be assigned an integer operating tier $t_i$ such that $t_i \in \{1, 2, 3\}$.

The system contains $m$ critical data links between specific pairs of components. To prevent data collision, any two components $u$ and $v$ connected by a critical link must maintain a strict differential in their operating tiers. Specifically, their assigned tiers must satisfy the condition:
$|t_u - t_v| \ge 1$

Systems of differential constraints can frequently be resolved efficiently by propagating bounds through a dependency network. In many practical deployments, such bounds propagate cleanly without contradiction. Your task is to evaluate the given network of critical links and find a valid tier assignment for all $n$ components, or correctly identify if the system of constraints is unsatisfiable.

## Input
The first line contains two integers $n$ and $m$ — the number of components and the number of critical links ($1 \le n \le 40$, $0 \le m \le n(n-1)/2$).
Each of the next $m$ lines contains two integers $u$ and $v$ — indicating a critical link between component $u$ and component $v$.

## Output
If there is no valid tier assignment that satisfies all constraints, print a single line containing `NO`.
Otherwise, print `YES` on the first line. On the second line, print $n$ integers $t_1, t_2, \dots, t_n$ (each in $\{1, 2, 3\}$), where $t_i$ is the tier assigned to component $i$. Any valid assignment is accepted.

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

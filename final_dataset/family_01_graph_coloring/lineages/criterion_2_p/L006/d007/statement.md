# Problem B — Chemical Equilibrium

Time limit: 1 s   Memory limit: 256 MB

You are simulating a chemical system with $n$ distinct reactants to find a stable configuration. For the system to reach equilibrium, each reactant $i$ must be assigned a steady-state concentration $c_i \in \{1, 2\}$ (in mol/L).

The system log contains $m$ elementary bimolecular reactions. Each reaction involves two reactants $u$ and $v$.
According to the law of mass action, the rate of a reaction between $u$ and $v$ is equal to the product of their concentrations, $c_u \times c_v$.

To achieve equilibrium, every logged reaction must proceed at a rate of exactly 2.
(Note: If a logged reaction involves the same reactant twice, meaning $u = v$, its rate would be $c_u^2$, which can only be 1 or 4. This immediately violates the equilibrium requirement and destabilizes the system).

If there are multiple valid concentration assignments that satisfy all logged reactions, you must output the sequence $c_1 \dots c_n$ that is lexicographically smallest.

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 2\cdot 10^5$, $0 \le m \le 2\cdot 10^5$).
Each of the following $m$ lines contains two integers $u$ and $v$ ($1 \le u, v \le n$) — the indices of the two reactants involved in the $j$-th logged reaction. The reactions are given in order for $j = 1, 2, \dots, m$.

## Output
If no such assignment exists, print a single line containing `NO`.
Otherwise, print `YES` on the first line. On the second line, print $n$ integers $c_1 \dots c_n$ (where each $c_i \in \{1,2\}$) representing the elements of the lexicographically smallest valid assignment.

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
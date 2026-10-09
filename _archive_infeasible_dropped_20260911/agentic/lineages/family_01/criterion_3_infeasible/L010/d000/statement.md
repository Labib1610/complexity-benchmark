# Problem C — Declaration of Indivisibility

Time limit: 2 s   Memory limit: 256 MB

A legal mediator is tasked with dividing an estate of $n$ assets between two heirs. However, there is a complication: certain pairs of assets are bound by joint liability clauses, which strictly prohibit them from being awarded to the same heir.

The mediator has realized that it is fundamentally impossible to divide the estate between just two heirs under these conditions. To formally close the case, the mediator must submit a declaration of indivisibility. By law, this declaration must cite a specific trio of assets where every pair within the trio is bound by a joint liability clause. Since no two of these three assets can be given to the same heir, this configuration clearly demonstrates that a two-way split cannot be achieved.

You are given the list of joint liability clauses. It is guaranteed that at least one such trio exists. Your task is to find one to complete the declaration.

## Input
The first line contains two integers $n$ and $m$ ($3 \le n \le 2000$, $3 \le m \le \min(n \cdot (n-1)/2, 2 \cdot 10^5)$), representing the number of assets and the number of joint liability clauses. The assets are numbered $1$ to $n$.
Each of the following $m$ lines contains two integers $u$ and $v$ — indicating that asset $u$ and asset $v$ are bound by a joint liability clause.
It is guaranteed that there is at least one trio of assets that mutually share liability clauses.

## Output
Output three integers $a$, $b$, and $c$ on a single line, separated by spaces, representing the three assets for the declaration. The assets must be printed in ascending order ($a < b < c$). If there are multiple valid trios, output the one that is lexicographically smallest (i.e., minimize $a$; in case of a tie, minimize $b$; and if still tied, minimize $c$).

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

# Problem C — Chemical Hazard Triplet Audit

Time limit: 2 s   Memory limit: 256 MB

A chemical synthesis facility stores $n$ hazardous reagents, indexed $1$ through $n$. Due to chemical incompatibility, certain pairs of reagents react violently if brought into contact with one another.

A safety compliance audit requires identifying a group of three distinct reagents such that every pair within the trio is mutually incompatible. The facility guarantee asserts that at least one such mutually incompatible trio exists among the stored reagents.

Your task is to identify one such group of three reagents. If multiple such trios exist, you must select the one that produces the lexicographically smallest tuple $(a, b, c)$ of reagent indices, where $a < b < c$.

## Input
The first line contains two space-separated integers $n$ and $m$ ($3 \le n \le 2000$, $3 \le m \le \min(n(n-1)/2, 2 \cdot 10^5)$), indicating the number of chemical reagents and the number of incompatible reagent pairs, respectively.
Each of the following $m$ lines contains two space-separated integers $u$ and $v$ ($1 \le u, v \le n$, $u \neq v$), denoting that reagent $u$ and reagent $v$ are mutually incompatible.
It is guaranteed that at least one group of three mutually incompatible reagents exists.

## Output
Print three space-separated integers $a$, $b$, and $c$ on a single line satisfying $a < b < c$, such that reagents $a$ and $b$ are incompatible, reagents $a$ and $c$ are incompatible, and reagents $b$ and $c$ are incompatible.
If there are multiple valid triples, output the one that is lexicographically smallest (i.e., minimizing $a$; then minimizing $b$; then minimizing $c$).

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

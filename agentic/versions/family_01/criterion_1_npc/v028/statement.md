# Gastronomic Harmony

Time limit: 2 s
Memory limit: 256 MB

You are designing a daily nutritional plan consisting of $n$ distinct ingredients. Each ingredient must be incorporated into exactly one of the available daily meal slots, which are identified by the integers 1, 2, and 3.

Due to specific enzymatic reactions, certain pairs of ingredients will cause severe indigestion if they are consumed during the same meal slot. You have a list of these incompatible pairs.

Determine whether it is possible to assign every ingredient to a meal slot such that no two incompatible ingredients are assigned to the same slot. If a valid plan exists, provide one.

## Input
The first line contains two integers $n$ and $m$ — the number of ingredients and the number of incompatible pairs ($1 \le n \le 40$, $0 \le m \le n(n-1)/2$).
Each of the next $m$ lines contains two integers $u$ and $v$ — an incompatible pair of ingredients. Ingredients are numbered from 1 to $n$.

## Output
If no valid meal plan can be formed, print a single line `NO`.
Otherwise, print `YES` on the first line. On the second line, print $n$ integers $s_1, s_2, \dots, s_n$ (each in $\{1, 2, 3\}$), where $s_i$ is the meal slot assigned to ingredient $i$. Any valid plan is accepted.

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

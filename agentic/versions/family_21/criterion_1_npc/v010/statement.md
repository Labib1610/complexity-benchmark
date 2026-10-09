# Problem A — Securing a Volatile Storage Complex

Time limit: 5 s
Memory limit: 256 MB

## Description
An underground storage complex consists of $n$ chambers linked by $m$ transit tubes. Each tube requires a specific expenditure of labor and materials to barricade permanently. Once a tube is barricaded, nothing can travel through it in either direction.

Certain chambers are designated as reactive sites. Each reactive site holds a unique, volatile substance. If substances from any two different reactive sites are brought together, a catastrophic reaction will occur. To guarantee safety, you must ensure that it is physically impossible for a substance to be transported from one reactive site to any other reactive site. Since substances can move freely through any unbarricaded tube and through any intermediate non-reactive chambers, you must barricade a selection of tubes such that no unbroken sequence of unbarricaded tubes exists between any two reactive sites. 

You are given a fixed budget $B$ for barricading. Determine if there is a valid selection of tubes whose combined barricading expenditure does not exceed the budget and which successfully prevents any two reactive sites from reaching each other. If such a selection exists, list the tubes to barricade. Otherwise, report that it cannot be done within the budget.

## Input
Line 1: four integers $n$, $m$, $k$, $B$, representing the number of chambers, tubes, reactive sites, and the budget.
Line 2: $k$ integers, the IDs of the chambers that are reactive sites.
Next $m$ lines: three integers $u$, $v$, $w$ per line, indicating a tube between chamber $u$ and chamber $v$ with barricading expenditure $w$.

## Output
If it is possible to barricade a set of tubes within the budget $B$ to satisfy the safety condition, print `YES` on the first line. On the second line, print an integer $c$, the number of tubes you chose to barricade. On each of the next $c$ lines, print two integers $u$ and $v$ representing a barricaded tube. (If there are multiple valid sets of tubes within the budget, any of them will be accepted).

If it is impossible to secure the complex within the budget, print `NO`.

## Example 1

**Input**
```text
4 4 3 20
1 2 3
1 4 3
2 4 4
3 4 5
1 2 10
```

**Output**
```text
YES
3
1 4
2 4
1 2
```

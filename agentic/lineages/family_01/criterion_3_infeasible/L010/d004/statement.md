# Signature Meal Selection

Time limit: 2 s   Memory limit: 256 MB

An elite culinary institute is establishing a new tasting menu drawing from a collection of $n$ distinct recipes. Following rigorous taste tests, the institute has published $m$ pairing certificates. Each certificate lists exactly two recipes that have been verified to taste good together.

To graduate, a student must curate a "signature meal" containing exactly three distinct recipes, which we will refer to as $x$, $y$, and $z$. To ensure perfect balance, the selection must be fully supported by the published certificates: there must be a certificate listing recipes $x$ and $y$, a certificate listing recipes $y$ and $z$, and a certificate listing recipes $x$ and $z$.

Your objective is to computationally identify the recipes for a perfectly balanced signature meal. The provided certificates originate from prior successful graduations, guaranteeing that at least one valid signature meal can be assembled.

## Input
The initial line provides two integers $n$ and $m$ ($3 \le n \le 2000$, $3 \le m \le \min(n \cdot (n-1)/2, 2 \cdot 10^5)$).
The subsequent $m$ lines each contain two integers $u$ and $v$, identifying the two recipes on a published certificate.
All test cases guarantee the existence of at least one valid signature meal.

## Output
Output three integers $a$, $b$, and $c$ on a single line, satisfying $a < b < c$, which identify the recipes comprising the signature meal. Should multiple valid meals exist, provide the lexicographically smallest combination (minimize $a$, then minimize $b$, then minimize $c$).

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
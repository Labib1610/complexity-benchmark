# Signature Meal Selection

Time limit: 2 s   Memory limit: 256 MB

An elite culinary institute is establishing a new tasting menu drawing from a collection of $n$ distinct recipes. Following rigorous taste tests, the institute has documented $m$ distinct harmonious pairings. Each documented pairing establishes that a specific pair of recipes mutually complement one another.

To graduate, a student must curate a "signature meal" containing exactly three distinct recipes. A signature meal achieves perfect balance when every possible two-recipe combination drawn from it is explicitly documented as a harmonious pairing.

Your objective is to computationally identify a perfectly balanced signature meal. The provided pairing documents originate from prior successful graduations, guaranteeing that at least one valid signature meal can be assembled.

## Input
The initial line provides two integers $n$ and $m$ ($3 \le n \le 2000$, $3 \le m \le \min(n \cdot (n-1)/2, 2 \cdot 10^5)$).
The subsequent $m$ lines each contain two integers $u$ and $v$, identifying a pair of recipes that are mutually complementary.
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
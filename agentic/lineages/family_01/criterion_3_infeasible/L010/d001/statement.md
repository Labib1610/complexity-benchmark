# Signature Meal Selection

Time limit: 2 s   Memory limit: 256 MB

A prestigious culinary academy is designing a new tasting menu from a repertoire of $n$ distinct recipes. Through extensive taste-testing, the academy has compiled a catalog of $m$ harmonious pairings. A pairing in the catalog indicates that two specific recipes complement each other perfectly (this relationship is mutual).

The academy's graduation requirement dictates that a student must present a "signature meal" consisting of exactly three distinct recipes. However, the meal is only considered perfectly balanced if every recipe included in the meal complements every other recipe included in the meal. In other words, for any two recipes chosen to be part of the same signature meal, their pairing must appear in the harmony catalog.

Given the sheer number of possible combinations, your task is to automate the search for a perfectly balanced signature meal. It is guaranteed that the catalog contains at least one such valid trio of recipes.

## Input
The first line contains two integers $n$ and $m$ (3 ≤ n ≤ 2000, 3 ≤ m ≤ min(n·(n−1)/2, 2·10⁵)).
Each of the next $m$ lines contains two integers $u$ and $v$ — the identifiers of two recipes that form a harmonious pairing.
It is guaranteed that at least one perfectly balanced signature meal can be formed.

## Output
Print three integers $a$, $b$, and $c$ on one line with $a < b < c$ representing the identifiers of the three recipes in the signature meal. If multiple such meals can be formed, output the one that is lexicographically smallest (smallest $a$; ties broken by smallest $b$; then smallest $c$).

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
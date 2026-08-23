# Signature Meal Selection

Time limit: 2 s   Memory limit: 256 MB

A prestigious culinary academy is designing a new tasting menu from a repertoire of $n$ distinct recipes. Through extensive taste-testing, the academy has compiled a catalog of $m$ distinct harmonious pairings. A pairing in the catalog indicates that two specific recipes complement each other (this relationship is mutual).

The academy's graduation requirement dictates that a student must present a "signature meal" consisting of exactly three distinct recipes. A meal is considered perfectly balanced if and only if exactly three pairings in the catalog consist exclusively of recipes included in this meal.

Given the sheer number of possible combinations, your task is to automate the search for a perfectly balanced signature meal. Because the provided catalogs are derived from successful past graduations, they will always contain the necessary pairings to form at least one valid signature meal.

## Input
The first line contains two integers $n$ and $m$ (3 ≤ n ≤ 2000, 3 ≤ m ≤ min(n·(n−1)/2, 2·10⁵)).
Each of the next $m$ lines contains two integers $u$ and $v$ — the identifiers of two recipes that form a harmonious pairing.
The test cases are designed such that a valid signature meal can always be found.

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
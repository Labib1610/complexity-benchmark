# Problem B — Paired Menu Constraints

Time limit: 1 s   Memory limit: 256 MB

## Description

A banquet has **n** dishes, each prepared SPICY or MILD before the event. The head chef supplies **m** tasting rules, but here **every** rule names exactly **two** dish-conditions and passes when at least one of the two is met (each condition being a dish plus the seasoning that satisfies it). Because each rule couples only a pair of dishes, a failing condition on one side forces the other side's condition to hold — the rules propagate as chains of forced consequences. Caterers sometimes fear this needs exhaustive search, but the pairwise structure makes the consequences fully deducible. Decide whether a single global SPICY/MILD setting of all n dishes satisfies every two-condition rule at once, and if so report one; otherwise report that the pairwise rules are mutually contradictory.

## Input
The first line contains two integers n and m (1 ≤ n ≤ 10^5, 0 ≤ m ≤ 2·10^5).
Each of the next m lines contains two non-zero signed integers l1 l2, with
|li| ≤ n. At least one of the two stated conditions must hold.

## Output
If no valid menu exists, print a single line NO.
Otherwise print YES on the first line. On the second line print n integers
s1 s2 … sn (each in {0, 1}) forming any valid menu.

## Example 1
Input:
```
2 2
1 2
-1 -2
```
Output:
```
YES
1 0
```

## Example 2
Input:
```
1 2
1 1
-1 -1
```
Output:
```
NO
```

## Note
Multiple valid menus may exist; any one is accepted. The same dish index
may appear in multiple requirements.

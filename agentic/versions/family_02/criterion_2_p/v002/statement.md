# Problem B — Paired Hub Constraints

Time limit: 1 s   Memory limit: 256 MB

## Description

A logistics network has **n** transit hubs, each set ACTIVE or DORMANT before the shift. Management supplies **m** routing protocols, but here **every** protocol names exactly **two** hub-conditions and passes when at least one of the two is met (each condition being a hub plus the polarity that satisfies it). Because each protocol couples only a pair of hubs, a failing condition on one side forces the other side's condition to hold — the protocols propagate as chains of forced consequences. Planners sometimes fear this needs exhaustive search, but the pairwise structure makes the consequences fully deducible. Decide whether a single global ACTIVE/DORMANT setting of all n hubs satisfies every two-condition protocol at once, and if so report one; otherwise report that the pairwise protocols are mutually contradictory.

## Input
The first line contains two integers n and m (1 ≤ n ≤ 10^5, 0 ≤ m ≤ 2·10^5).
Each of the next m lines contains two non-zero signed integers l1 l2, with
|li| ≤ n. At least one of the two stated conditions must hold.

## Output
If no valid assignment exists, print a single line NO.
Otherwise print YES on the first line. On the second line print n integers
s1 s2 … sn (each in {0, 1}) forming any valid assignment.

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
Multiple valid assignments may exist; any one is accepted. The same hub index
may appear in multiple requirements.

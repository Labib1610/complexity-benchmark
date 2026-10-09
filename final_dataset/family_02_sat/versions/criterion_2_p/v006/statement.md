# Problem B — Paired Window Constraints

Time limit: 1 s   Memory limit: 256 MB

## Description

An industrial control panel contains **n** toggle switches, which must each be locked to either the UP or DOWN position before a manufacturing run begins. Safety regulations provide **m** operational requirements. Each requirement specifies exactly two acceptable switch states (a specific switch being UP, or a specific switch being DOWN). To pass a safety inspection, at least one of the two states in every requirement must be met. Because each requirement involves only a pair of switch states, an unmet state on one side forces the other side's state to be met — the requirements propagate as chains of forced consequences. Engineers sometimes fear this needs exhaustive search, but the pairwise structure makes the consequences fully deducible. Determine if there is a single global UP/DOWN configuration of all n switches that satisfies every safety requirement simultaneously, and if so report one; otherwise report that the safety requirements are mutually contradictory.

## Input
The first line contains two integers n and m (1 ≤ n ≤ 10^5, 0 ≤ m ≤ 2·10^5).
Each of the next m lines contains two non-zero signed integers l1 l2, with
|li| ≤ n. A positive integer indicates the corresponding switch must be UP, and a negative integer indicates it must be DOWN. At least one of the two stated states must be met.

## Output
If no valid configuration exists, print a single line NO.
Otherwise print YES on the first line. On the second line print n integers
s1 s2 … sn (each in {0, 1}) forming any valid configuration, where 1 represents UP and 0 represents DOWN.

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
Multiple valid configurations may exist; any one is accepted. The same switch index
may appear in multiple requirements.

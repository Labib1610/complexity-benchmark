# Problem A — Control System Configuration

Time limit: 2 s   Memory limit: 256 MB

## Description

A control system exposes **n** two-position dials, each of which the operator must set firmly to position 1 or position 0 before the run — no dial may be left floating, and there is no third state. Commissioning has produced **m** inspection checks gathered from separate subsystem audits; every check names three dial-settings and passes precisely when **at least one** of the three named settings is met (a setting names a dial together with the mode — 1 or 0 — that satisfies it). A check with a met setting imposes nothing further; a check with none of its three settings met is violated. The same dial typically appears across many checks, sometimes demanded at 1 by one and at 0 by another, and the checks may overlap heavily or barely at all — none of that matters except through the exact settings each check lists. Decide whether there is a single global 1/0 configuration of all n dials that passes **every** check simultaneously, and if so report one such configuration; otherwise the check set is over-constrained. Passing the checks one at a time is trivial — the difficulty is one configuration consistent with all of them at once.

## Input
The first line contains two integers n and m (1 ≤ n ≤ 90, 0 ≤ m ≤ 400).
Each of the next m lines contains three non-zero signed integers l1 l2 l3,
with |li| ≤ n. The sign indicates the required mode (positive for 1, negative for 0). At least one of the three stated settings must hold.

## Output
If no valid configuration exists, print a single line NO.
Otherwise print YES on the first line. On the second line print n integers
s1 s2 … sn (each in {0, 1}), where si is the state of dial i. Any valid
configuration is accepted.

## Example 1
Input:
```
3 2
1 2 3
-1 2 -3
```
Output:
```
YES
0 0 1
```

## Example 2
Input:
```
1 2
1 1 1
-1 -1 -1
```
Output:
```
NO
```

## Note
Each requirement group has exactly three entries. The same dial index may appear
more than once in a group.

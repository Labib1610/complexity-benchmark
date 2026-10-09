# Problem A — Valve Configuration

Time limit: 2 s   Memory limit: 256 MB

## Description

A control system exposes **n** valves, each of which the operator must set firmly to OPEN or CLOSED before the run — no valve may be left floating, and there is no third state. Commissioning has produced **m** acceptance rules gathered from separate subsystem audits; every rule names three valve requirements and passes precisely when **at least one** of the three named conditions is met (a condition names a valve together with the state — OPEN or CLOSED — that fulfills it). A rule with a fulfilled condition imposes nothing further; a rule with none of its three conditions fulfilled is violated. The same valve typically appears across many rules, sometimes demanded OPEN by one and CLOSED by another, and the rules may overlap heavily or barely at all — none of that matters except through the exact conditions each rule lists. Decide whether there is a single global OPEN/CLOSED configuration of all n valves that fulfills **every** rule simultaneously, and if so report one such configuration; otherwise the rule set is over-constrained. Fulfilling the rules one at a time is trivial — the difficulty is one configuration consistent with all of them at once.

## Input
The first line contains two integers n and m (1 ≤ n ≤ 90, 0 ≤ m ≤ 400).
Each of the next m lines contains three non-zero signed integers l1 l2 l3,
with |li| ≤ n. A positive integer requests the corresponding valve be OPEN (1), and a negative integer requests it be CLOSED (0). At least one of the three stated conditions must hold for each rule.

## Output
If no valid configuration exists, print a single line NO.
Otherwise print YES on the first line. On the second line print n integers
s1 s2 … sn (each in {0, 1}), where si is the state of valve i. Any valid
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
Each requirement group has exactly three entries. The same valve index may appear
more than once in a group.

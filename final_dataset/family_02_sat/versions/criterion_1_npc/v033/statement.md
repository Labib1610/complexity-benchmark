# Problem A — Calibration Sequence

Time limit: 2 s   Memory limit: 256 MB

## Description

A calibration system exposes **n** two-position levers, each of which the operator must set firmly to UP or DOWN before the run — no lever may be left floating, and there is no third state. Commissioning has produced **m** safety checks gathered from separate subsystem audits; every check targets three lever-positions and succeeds precisely when **at least one** of the three targeted positions matches the actual setup (a targeted position names a lever together with the orientation — UP or DOWN — that satisfies it). A check with a matched position imposes nothing further; a check with none of its three targeted positions matched fails. The same lever typically appears across many checks, sometimes demanded UP by one and DOWN by another, and the checks may overlap heavily or barely at all — none of that matters except through the exact positions each check targets. Decide whether there is a single global UP/DOWN setting of all n levers that passes **every** check simultaneously, and if so report one such setting; otherwise the check set is over-constrained. Passing the checks one at a time is trivial — the difficulty is one configuration consistent with all of them at once.

## Input
The first line contains two integers n and m (1 ≤ n ≤ 90, 0 ≤ m ≤ 400).
Each of the next m lines contains three non-zero signed integers l1 l2 l3,
with |li| ≤ n. A positive integer indicates the lever must be UP, and a negative integer indicates it must be DOWN. At least one of the three targeted positions must match the actual configuration for the check to pass.

## Output
If no valid configuration exists, print a single line NO.
Otherwise print YES on the first line. On the second line print n integers
s1 s2 … sn (each in {0, 1}), where si is the state of lever i (1 for UP, 0 for DOWN). Any valid configuration is accepted.

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
Each check has exactly three entries. The same lever index may appear
more than once in a check.

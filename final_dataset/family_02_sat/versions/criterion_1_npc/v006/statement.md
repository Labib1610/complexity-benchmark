# Problem A — Build Configuration Check

Time limit: 2 s   Memory limit: 256 MB

## Description

A software compiler exposes **n** binary feature flags, each of which the build system must set firmly to ENABLED or DISABLED before compilation — no flag may be left floating, and there is no third state. Integration has produced **m** test suites gathered from separate module owners; every suite names three flag-dependencies and passes precisely when **at least one** of the three named conditions is met (a condition names a flag together with the polarity — ENABLED or DISABLED — that satisfies it). A suite with a met condition imposes nothing further; a suite with none of its three conditions met fails the build. The same flag typically appears across many suites, sometimes demanded ENABLED by one and DISABLED by another, and the suites may overlap heavily or barely at all — none of that matters except through the exact conditions each suite lists. Decide whether there is a single global ENABLED/DISABLED setting of all n flags that satisfies **every** test suite simultaneously, and if so report one such setting; otherwise the configuration is over-constrained. Satisfying the suites one at a time is trivial — the difficulty is one assignment consistent with all of them at once.

## Input
The first line contains two integers n and m (1 ≤ n ≤ 90, 0 ≤ m ≤ 400).
Each of the next m lines contains three non-zero signed integers l1 l2 l3,
with |li| ≤ n. A positive integer indicates the flag must be ENABLED, and a negative integer indicates it must be DISABLED. At least one of the three stated conditions must hold.

## Output
If no valid assignment exists, print a single line NO.
Otherwise print YES on the first line. On the second line print n integers
s1 s2 … sn (each in {0, 1}), where si is the state of flag i (1 for ENABLED, 0 for DISABLED). Any valid assignment is accepted.

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
Each suite has exactly three entries. The same flag index may appear
more than once in a suite.

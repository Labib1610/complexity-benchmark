# Problem A — Feature Flag Deployment

Time limit: 2 s   Memory limit: 256 MB

## Description

A release manager must configure **n** feature flags, each of which must be toggled firmly to ENABLED or DISABLED before deployment — no flag may be left undeclared, and there is no intermediate state. Integration testing has produced **m** deployment policies gathered from separate team requirements; every policy names three flag-dependencies and passes precisely when **at least one** of the three named conditions is met (a condition names a flag together with the state — ENABLED or DISABLED — that satisfies it). A policy with a met condition imposes nothing further; a policy with none of its three conditions met blocks the release. The same flag typically appears across many policies, sometimes demanded ENABLED by one and DISABLED by another, and the policies may overlap heavily or barely at all — none of that matters except through the exact conditions each policy lists. Decide whether there is a single global ENABLED/DISABLED configuration of all n flags that satisfies **every** policy simultaneously, and if so report one such configuration; otherwise the release is blocked. Satisfying the policies one at a time is trivial — the difficulty is one configuration consistent with all of them at once.

## Input
The first line contains two integers n and m (1 ≤ n ≤ 90, 0 ≤ m ≤ 400).
Each of the next m lines contains three non-zero signed integers l1 l2 l3,
with |li| ≤ n. A positive value represents a condition that the corresponding flag is ENABLED, while a negative value represents a condition that it is DISABLED. At least one of the three stated conditions must hold.

## Output
If no valid configuration exists, print a single line NO.
Otherwise print YES on the first line. On the second line print n integers
s1 s2 … sn (each in {0, 1}), where si is the state of flag i (1 for ENABLED, 0 for DISABLED). Any valid configuration is accepted.

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
Each policy has exactly three entries. The same flag index may appear
more than once in a policy.

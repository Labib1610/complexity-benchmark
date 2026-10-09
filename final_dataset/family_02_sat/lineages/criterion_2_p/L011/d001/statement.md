# Problem B — Paired Window Constraints

Time limit: 1 s   Memory limit: 256 MB

## Description

Before a manufacturing run can commence, an industrial control panel with **n** toggle switches must be configured. Every switch must be locked into either an UP or DOWN position. The facility's safety protocol consists of **m** paired operational rules. Every rule lists two target switch states (for instance, a specific switch being UP, or a specific switch being DOWN). For the system to pass inspection, every single rule must have at least one of its two target states satisfied by the final configuration. This dual-condition setup guarantees that if one component's state is suboptimal, a backup state compensates for it.

Your task is to determine whether it is possible to find one overarching UP/DOWN configuration for all **n** switches that satisfies all **m** rules at the same time. If such a configuration exists, you must provide one. If the rules contradict each other such that no valid configuration is possible, you must report this failure.

## Input
The first line provides two integers, n and m (1 ≤ n ≤ 10^5, 0 ≤ m ≤ 2·10^5).
The subsequent m lines each contain two non-zero signed integers, l1 and l2, where |li| ≤ n. A positive value means the specified switch is targeted to be UP, while a negative value means it is targeted to be DOWN. For each line, the final configuration must match at least one of the two targets.

## Output
If there is no valid configuration, output a single line containing NO.
If a valid configuration is possible, output YES on the first line. On the second line, output n space-separated integers s1 s2 … sn (each being 0 or 1) that represent a valid configuration. Here, 1 indicates UP and 0 indicates DOWN.

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
Multiple valid configurations may exist; any valid one will be accepted. The same switch index can be referenced in multiple rules.
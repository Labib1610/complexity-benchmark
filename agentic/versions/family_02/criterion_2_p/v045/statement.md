# Problem B — Fail-Safe Lever Configurations

Time limit: 1 s
Memory limit: 256 MB

## Description

An industrial control panel is equipped with $n$ two-position levers. Before activating the main assembly line, every lever must be locked into either the ACTIVE or STANDBY position. The safety protocol outlines $m$ fail-safe conditions. Every condition specifies two acceptable lever positions (for example, 'lever 4 ACTIVE' or 'lever 7 STANDBY'). To satisfy the safety protocol, every condition must have at least one of its two specified lever positions fulfilled. Because each condition links exactly two positions, choosing not to fulfill one position strictly forces the other to be fulfilled to maintain safety. 

Determine if there is a single global configuration of all $n$ levers that satisfies every fail-safe condition simultaneously. If a valid configuration exists, report it; otherwise, report that the safety protocol is inherently contradictory.

## Input

The first line contains two integers $n$ and $m$. The number of levers $n$ is at least one, and is bounded by the facility's hardware capacity of exactly ten thousand control blocks, with each block holding exactly ten levers. The number of fail-safe conditions $m$ can be as low as zero, and goes up to exactly twice the maximum hardware capacity of levers.

Each of the next $m$ lines contains two non-zero signed integers $l_1$ and $l_2$. The absolute values of these integers denote lever indices and will not exceed $n$. A positive integer means the specified lever is required to be ACTIVE. A negative integer means the specified lever is required to be STANDBY. At least one of the two stated positions must be fulfilled.

## Output

If no valid configuration exists, print a single line `NO`.
Otherwise, print `YES` on the first line. On the second line, print $n$ integers $s_1, s_2, \dots, s_n$ (each in `{0, 1}`) forming any valid configuration, where `1` represents ACTIVE and `0` represents STANDBY.

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
Multiple valid configurations may exist; any one is accepted. The same lever index may appear in multiple fail-safe conditions.

# Problem B — Paired Window Constraints

Time limit: 1 s   Memory limit: 256 MB

## Description

A control panel has **n** relays, each set to either Mode 1 or Mode 0 before the run. Commissioning supplies **m** acceptance rules, where **every** rule names exactly **two** relay-targets and passes when at least one of the two targets is met (each target being a relay plus the mode that satisfies it). Decide whether a single global configuration of all n relays satisfies every rule at once, and if so report one; otherwise report that no such configuration is possible.

## Input
The first line contains two integers n and m (1 ≤ n ≤ 10^5, 0 ≤ m ≤ 2·10^5).
Each of the next m lines contains two non-zero signed integers l1 l2, with
|li| ≤ n. A positive value x represents a target of Mode 1 for relay |x|, while a negative value x represents a target of Mode 0 for relay |x|. At least one of the two stated targets on each line must hold.

## Output
If no valid configuration exists, print a single line NO.
Otherwise print YES on the first line. On the second line print n integers
s1 s2 … sn (each in {0, 1}) forming any valid configuration.

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
Multiple valid configurations may exist; any one is accepted. The same relay-target may appear in multiple rules.

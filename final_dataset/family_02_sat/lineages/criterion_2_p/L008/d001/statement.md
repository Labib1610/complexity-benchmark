# Problem B — Paired Window Constraints

Time limit: 1 s   Memory limit: 256 MB

## Description

A control panel has **n** relays, each set to either Mode 1 or Mode 0 before the run. Commissioning supplies **m** safety interlocks. Each interlock monitors a specific pair of relay modes. An interlock will trigger a system halt if the global configuration simultaneously violates both of the modes it monitors. Decide whether a single global configuration of all n relays can operate without triggering any halts, and if so report one; otherwise report that no such configuration is possible.

## Input
The first line contains two integers n and m (1 ≤ n ≤ 10^5, 0 ≤ m ≤ 2·10^5).
Each of the next m lines contains two non-zero signed integers l1 l2, with |li| ≤ n. A positive value x designates a monitored state of Mode 1 for relay |x|, while a negative value x designates a monitored state of Mode 0 for relay |x|. For the system to survive the interlock on this line, it is strictly forbidden for the configuration to contradict the state designated by l1 while simultaneously contradicting the state designated by l2.

## Output
If no valid configuration exists, print a single line NO.
Otherwise print YES on the first line. On the second line print n integers s1 s2 … sn (each in {0, 1}) forming any valid configuration.

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
Multiple valid configurations may exist; any one is accepted. The same relay mode may be monitored by multiple interlocks.
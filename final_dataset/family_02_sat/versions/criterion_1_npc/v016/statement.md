# Problem A — Fluid Network Interlocks

Time limit: 2 s   Memory limit: 256 MB

## Description

A chemical plant's fluid network contains **n** discrete valves. Before initiating the reaction sequence, the operator must set each valve to either OPEN or CLOSED. There are no intermediate or floating states.

During safety certification, **m** hardware interlocks were installed. Each interlock is wired to monitor exactly three specific valve conditions. A condition specifies a valve's ID and its required state (OPEN or CLOSED). An interlock remains "secure" if and only if **at least one** of its three monitored conditions matches the actual physical state of the valves. If an interlock finds that none of its three monitored conditions are met, it will trigger an emergency halt.

You are guaranteed that the network design adheres to two strict capacity limits:
1. No single valve is monitored in more than 1,200 conditions across the entire interlock network.
2. The total sum of the absolute valve IDs across all conditions in the network never exceeds 108,000.

Your task is to determine whether there is a single, global OPEN/CLOSED configuration for all **n** valves that makes every single interlock secure at the same time. If such a configuration exists, you must provide one. Otherwise, report that the network is over-constrained.

## Input
The first line contains two integers n and m (1 ≤ n ≤ 90, 0 ≤ m ≤ 400), representing the number of valves and the number of interlocks, respectively.
Each of the following m lines describes an interlock using three non-zero signed integers c1, c2, and c3.
Each integer ci represents a monitored condition: its absolute value |ci| (where 1 ≤ |ci| ≤ n) is the valve ID. A positive value means the interlock monitors for the valve to be OPEN, while a negative value means it monitors for the valve to be CLOSED.

## Output
If there is no configuration that secures all interlocks simultaneously, print a single line containing NO.
Otherwise, print YES on the first line. On the second line, print n space-separated integers v1, v2, ..., vn, where vi is 1 if valve i should be OPEN, and 0 if valve i should be CLOSED. Any valid configuration is accepted.

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
Each interlock always monitors exactly three conditions. The same valve ID might be monitored more than once by the same interlock.

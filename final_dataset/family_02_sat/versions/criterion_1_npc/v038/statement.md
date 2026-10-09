# Problem A — System Commissioning Alarms

Time limit: 2 s   Memory limit: 256 MB

## Description

A facility operates a primary control panel with $n$ mechanical toggles. The operator must firmly lock each toggle into either position 1 (engaged) or position 0 (disengaged). There is no neutral position.

During commissioning, engineers compiled $m$ safety checks from various subsystem tests. Each check monitors exactly three toggle-position criteria. A criterion is defined by a toggle's index and a required position. A safety check will trigger a system-wide alarm if and only if all three of its criteria fail to match the current global state of the panel. As long as a check observes that its criteria are met by the panel's state in one or more instances, it remains silent.

A criterion is denoted by a non-zero integer: its absolute value identifies the toggle, while its sign dictates the required position (positive for position 1, negative for position 0). The same toggle may be monitored by multiple checks, potentially demanding position 1 in some checks and position 0 in others. 

You must determine whether there exists a complete panel configuration that keeps all $m$ safety checks silent simultaneously. If a safe configuration is possible, you must provide one.

As a guaranteed property of the facility's design, the sum of the absolute values of the toggle identifiers in any single check will never exceed $3n$. Additionally, the aggregate count of criteria evaluated across the entire set of checks is exactly $3m$.

## Input
The first line provides two integers $n$ and $m$ (1 ≤ n ≤ 90, 0 ≤ m ≤ 400).
The subsequent $m$ lines each contain three non-zero integers $l_1, l_2, l_3$, representing the criteria for a single safety check. Each integer's absolute value is between 1 and $n$ inclusive.

## Output
If there is no way to configure the panel without triggering an alarm, output a single line with `NO`.
If a safe configuration exists, output `YES` on the first line. On the second line, output $n$ integers $s_1, s_2, \dots, s_n$ separated by spaces, where $s_i \in \{0, 1\}$ represents the position of the $i$-th toggle. If multiple safe configurations exist, any valid one will be accepted.

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
Each safety check lists exactly three criteria. A single toggle index may appear multiple times within the same check.

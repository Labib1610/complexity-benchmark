# Problem A — Plant Calibration

Time limit: 2 s   Memory limit: 256 MB

## Description

An industrial processing plant contains $n$ main control valves. Before the system can be pressurized, every single valve must be locked into one of two states: OPEN or CLOSED. Intermediate states are impossible.

The plant is equipped with $m$ independent safety monitors to prevent catastrophic pressure buildup. Each monitor is wired to check exactly three specific valve conditions. A monitor considers the system safe if **at least one** of its three checked conditions is met. If a monitor evaluates all three of its conditions as unmet, it will trigger a plant-wide emergency shutdown.

The same valve may be checked by multiple monitors, sometimes required to be OPEN by one monitor's condition and CLOSED by another's. Your task is to determine whether it is possible to lock all $n$ valves into a single global configuration (each valve being either OPEN or CLOSED) such that every single safety monitor is satisfied simultaneously. If such a configuration exists, you must provide it.

## Input
The first line contains two integers $n$ and $m$ (1 ≤ $n$ ≤ 90, 0 ≤ $m$ ≤ 400).
Each of the next $m$ lines describes a safety monitor using three non-zero integers $l_1, l_2, l_3$, with $|l_i| \le n$.
Each integer $l_i$ represents a condition on a valve. If $l_i > 0$, the condition is that valve $l_i$ is OPEN. If $l_i < 0$, the condition is that valve $|l_i|$ is CLOSED. At least one of the three stated conditions must hold for the monitor to be satisfied.

## Output
If no safe configuration exists for the plant, print a single line `NO`.
Otherwise print `YES` on the first line. On the second line print $n$ integers $s_1, s_2, \dots, s_n$ (each in {0, 1}), where $s_i$ is the state of valve $i$ (1 for OPEN, 0 for CLOSED). Any safe configuration is accepted.

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
Each safety monitor always checks exactly three conditions. A monitor may check the same valve more than once.

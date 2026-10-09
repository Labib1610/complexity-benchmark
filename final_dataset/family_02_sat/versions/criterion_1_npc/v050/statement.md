# Valve Calibration

Time limit: 2 s   Memory limit: 256 MB

## Description

An industrial laboratory has $n$ control valves, numbered 1 through $n$. Each valve must be calibrated to exactly one of two settings: 1 or 0.

The system is monitored by $m$ safety relays. Each relay is wired to make exactly three specific observations about the valve settings.

For a relay to remain stable, it requires at least one of its three observations to match the actual calibration of the valves. If a single wire detects the specific setting it is looking for, the relay is stable, regardless of what the other two wires detect. A relay only becomes unstable if all three of its observations contradict the actual valve calibrations.

You must determine if there is a global calibration for all $n$ valves that keeps every single relay stable at the same time.

## Input
The first line contains two integers $n$ and $m$ (1 ≤ n ≤ 90, 0 ≤ m ≤ 400).
Each of the following $m$ lines describes a safety relay and contains three non-zero signed integers $w_1, w_2, w_3$, with $|w_i| \le n$. 
The absolute value $|w_i|$ represents the valve index (from 1 to $n$). If $w_i$ is positive, the observation matches when valve $|w_i|$ is calibrated to 1. If $w_i$ is negative, the observation matches when valve $|w_i|$ is calibrated to 0.

## Output
If there is no way to calibrate the valves to keep all relays stable, print a single line containing NO.
Otherwise, print YES on the first line. On the second line, print $n$ integers $s_1 s_2 \dots s_n$ (where each $s_i \in \{0, 1\}$), representing the calibration of each valve from 1 to $n$. Any valid calibration is accepted.

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
Each safety relay specifies exactly three observations. It is possible for the same valve index to be specified more than once within the same relay's observations.

# Phase 2: Calibration Resolution

Time limit: 2 s   Memory limit: 256 MB

## Description

The calibration pipeline for a deep-sea telemetry array operates in three sequential phases. In Phase 1, raw acoustic reflections are parsed by the firmware to generate a list of mechanical limits. You are responsible for Phase 2, which involves resolving these limits into a definitive operational state. Once Phase 2 completes successfully, Phase 3 compiles your state matrix into a telemetry payload and broadcasts it to the ocean floor. 

For Phase 2, you are given a set of $n$ acoustic relays. Each relay must be locked into exactly one of two functional modes: primary or secondary. The Phase 1 output provides $m$ mechanical limits. Each limit specifies exactly three potential relay-mode combinations. A limit is considered resolved if the final system state adopts at least one of the three combinations it lists. A combination specifies a specific relay and the mode it must be in.

The relays are heavily interdependent. A single relay may be required to be in primary mode by some combinations and secondary mode by others, and the limits may overlap significantly. You must determine if there exists a single, comprehensive configuration for all $n$ relays that resolves all $m$ limits concurrently. If such a configuration exists, you must output it so Phase 3 can proceed. Otherwise, the limits are contradictory.

## Input
The first line contains two integers $n$ and $m$ (1 ≤ n ≤ 90, 0 ≤ m ≤ 400).
The following $m$ lines each represent a mechanical limit provided by Phase 1. Each line contains three non-zero integers $l_1, l_2, l_3$, where the absolute value $|l_i|$ indicates the relay index (from 1 to $n$). A positive value means the combination requires the relay to be in primary mode, while a negative value means it requires the relay to be in secondary mode.

## Output
If there is no way to resolve all limits, print a single line NO, which will trigger a Phase 1 recalibration.
If a valid configuration exists, print YES on the first line. On the second line, print $n$ integers $s_1, s_2, \dots, s_n$ separated by spaces, where $s_i = 1$ if relay $i$ is put into primary mode, and $s_i = 0$ if relay $i$ is put into secondary mode. Any valid configuration that resolves all limits is acceptable.

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
Each mechanical limit lists exactly three entries. The same relay index may appear more than once in a single limit.

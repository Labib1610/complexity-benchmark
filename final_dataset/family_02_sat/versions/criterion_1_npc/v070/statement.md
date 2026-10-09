# Phase 2: Calibration Resolution

Time limit: 2 s   Memory limit: 256 MB

## Description

Before a deep-sea telemetry array can commence data transmission, its operational matrix must be fully stabilized. The array is built from $n$ acoustic relays. To configure the array, you must assign every relay to exactly one of two transmission channels: the Alpha channel or the Beta channel.

During the pre-transmission sequence, the system's diagnostic firmware identifies $m$ distinct acoustic interference patterns. Every interference pattern must be resolved to achieve stabilization.

The firmware characterizes each interference pattern by proposing exactly three channel adjustments. A channel adjustment specifies a required channel for a specific relay (for instance, "set relay 5 to the Alpha channel" or "set relay 9 to the Beta channel"). The physical mechanics of the array dictate that an interference pattern is successfully resolved if the final array configuration incorporates at least one of the three channel adjustments proposed for that pattern.

Because the relays are interconnected, a channel adjustment that resolves one interference pattern may contradict the adjustments proposed for another. Your objective is to compute a comprehensive channel configuration for all $n$ relays that simultaneously resolves all $m$ interference patterns. If no such configuration exists, the array cannot be stabilized.

## Input
The first line contains two integers $n$ and $m$ (1 ≤ n ≤ 90, 0 ≤ m ≤ 400), representing the number of relays and the number of interference patterns, respectively.
The following $m$ lines each describe an interference pattern. Each line contains three non-zero integers $p_1, p_2, p_3$. The absolute value of each integer denotes a relay's index (from 1 to $n$). A positive integer indicates an adjustment requiring the relay to use the Alpha channel. A negative integer indicates an adjustment requiring the relay to use the Beta channel.

## Output
If the array cannot be stabilized, output a single line containing `NO`.
If a stabilizing configuration exists, output `YES` on the first line. On the second line, output $n$ space-separated integers $c_1, c_2, \dots, c_n$, where $c_i = 1$ if relay $i$ is assigned to the Alpha channel, and $c_i = 0$ if relay $i$ is assigned to the Beta channel. If there are multiple valid configurations, any of them will be accepted.

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
Every interference pattern proposes exactly three channel adjustments. A single relay index may appear more than once within the same interference pattern.

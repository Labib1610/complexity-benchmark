# Problem A — Tri-Band Telemetry

Time limit: 2 s   Memory limit: 256 MB

A deep-sea exploration crew is deploying an array of sensor buoys. Each buoy must be configured to transmit telemetry data on exactly one of three distinct acoustic bands, labeled 1, 2, and 3.

Due to acoustic reflections in the underwater trenches, certain pairs of buoys are prone to cross-talk. If two buoys in such a pair transmit on the same acoustic band, their signals will become garbled. You must configure the array by assigning an acoustic band to every buoy so that no two buoys prone to cross-talk share the same band. If the environment is too dense and no such configuration exists, you must report the failure.

## Input
The first line of input provides two integers $n$ and $m$ — the total number of buoys and the number of cross-talk conditions. The number of buoys $n$ is at least one. Its maximum possible value is determined by the submarine's total carrying capacity: exactly four storage racks that each hold exactly ten buoys. The number of cross-talk conditions $m$ is at least zero, and will never exceed the absolute maximum where every single buoy experiences cross-talk with every other buoy in the array.

Each of the subsequent $m$ lines contains two integers $u$ and $v$, indicating that buoy $u$ and buoy $v$ are prone to cross-talk.

## Output
If it is impossible to configure the buoys without cross-talk, output a single line containing `NO`.
Otherwise, output `YES` on the first line. On the second line, output $n$ integers $b_1, b_2, \dots, b_n$ (where each $b_i \in \{1, 2, 3\}$), representing the acoustic band assigned to the $i$-th buoy. Any valid configuration is accepted.

## Example 1
Input:
```
4 5
1 2
1 3
2 3
1 4
2 4
```
Output:
```
YES
1 2 3 3
```

## Example 2
Input:
```
4 6
1 2
1 3
1 4
2 3
2 4
3 4
```
Output:
```
NO
```

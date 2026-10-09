# Problem A — Quantum Phase Synchronization in Modular Grids

Time limit: 2 s   Memory limit: 256 MB

## Description

A modular sensor grid contains **n** distinct sensors. Each sensor must be calibrated to one of two discrete phase states: `1` (positive) or `0` (inverted).

The grid's integrity is ensured by **m** validation nodes. Each validation node monitors exactly three sensor feeds. A feed is represented by a non-zero integer: the absolute value indicates the sensor being monitored. If the integer is positive, the feed is active when that sensor is in state `1`. If the integer is negative, the feed is active when that sensor is in state `0`.

A validation node operates correctly as long as at least one of its three feeds is active. If all three feeds are inactive simultaneously, the node experiences a critical fault. 

To ensure the grid can be safely deployed, you must determine if there exists a global phase calibration for all **n** sensors such that no validation node experiences a fault. If such a calibration exists, you must provide it.

The grid's design guarantees certain structural limits:
- The total sum of the absolute values of the sensor identifiers within any single validation node's footprint never exceeds 270.
- The total number of feeds evaluated across the entire grid is at most 1200.

## Input
The first line contains two integers **n** and **m** (1 ≤ n ≤ 90, 0 ≤ m ≤ 400) — the number of sensors and validation nodes, respectively.
Each of the next **m** lines contains three non-zero integers **f1 f2 f3** (|fi| ≤ n), representing the three feeds monitored by that validation node.

## Output
If there is no way to calibrate the sensors without causing a fault, print `NO` on a single line.
Otherwise, print `YES` on the first line. On the second line, print **n** space-separated integers **s1 s2 … sn** (each either `0` or `1`), representing the phase state for each sensor from 1 to **n**. Any calibration that prevents all faults is acceptable.

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
Each validation node always lists exactly three feeds. The same sensor may provide multiple feeds to the same validation node.

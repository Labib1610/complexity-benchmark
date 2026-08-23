# Resonance Field Alignment

Time limit: 1 s
Memory limit: 256 MB

A containment grid consists of $n$ resonance nodes. Each node must be calibrated to one of two polarity states, designated as state 1 and state 2.

The grid contains $m$ interference monitors, each operating between a specific pair of nodes. A monitor functions correctly only when it observes a polarity differential between its assigned pair. If both nodes connected by a monitor are calibrated to the exact same polarity state, the monitor will fail and initiate a grid shutdown.

Due to hardware limitations, the grid adheres to the following structural guarantees:
- The total number of monitor endpoints across all nodes is exactly $2m$, which will never exceed $400,000$.
- For any monitor linking node $u$ and node $v$, the absolute difference between their identifiers is strictly less than $n$ ($|u - v| < n$), and the sum of their identifiers is at most $2n$ ($u + v \le 2n$).

You must determine if there exists a valid polarity calibration for all $n$ nodes such that every monitor observes a differential. If multiple safe calibrations exist, the automated safety protocol mandates selecting the sequence of polarities $s_1, s_2, \dots, s_n$ that is as small as possible when compared element by element starting from the first node.

## Input
The first line provides two integers $n$ and $m$ ($1 \le n \le 2 \cdot 10^5$, $0 \le m \le 2 \cdot 10^5$).
The following $m$ lines each contain two integers $u$ and $v$ ($1 \le u, v \le n$), representing an interference monitor operating between node $u$ and node $v$.

## Output
If no safe calibration is possible, output a single line containing `NO`.
Otherwise, output `YES` on the first line. On the second line, output $n$ integers (each being 1 or 2) representing the lexicographically smallest safe polarity sequence.

## Example 1
Input:
```
4 4
1 2
2 3
3 4
1 4
```
Output:
```
YES
1 2 1 2
```

## Example 2
Input:
```
3 3
1 2
1 3
2 3
```
Output:
```
NO
```

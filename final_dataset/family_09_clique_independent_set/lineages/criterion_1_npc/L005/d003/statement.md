# Problem A — Zero-Interference Cluster

Time limit: 5 s   Memory limit: 256 MB

## Description

A scientific observatory is equipped with **n** telemetry sensors (numbered 1 to **n**). 
During initial calibration, engineers catalogued **m** potential interference patterns. Each interference pattern is generated if and only if two specific sensors are active simultaneously.

The observatory needs to activate a focused cluster of exactly **k** sensors for a delicate measurement. 
A cluster configuration is considered **clean** if the total number of generated interference patterns is exactly zero. 

Given the total number of sensors **n**, the number of known interference patterns **m**, and the target cluster size **k**, determine whether a clean cluster of exactly **k** sensors can be configured, and if so, report one.

## Input

The first line contains three integers **n**, **m**, and **k** (1 ≤ n ≤ 46, 0 ≤ m ≤ n·(n−1)/2, 1 ≤ k ≤ n).
Each of the next **m** lines contains two integers **u** and **v** (1 ≤ u, v ≤ n, u ≠ v), representing the two sensors that together generate a specific interference pattern. The input will never list the same pair of sensors more than once.

## Output

If a clean cluster of **k** sensors exists, print `YES` on the first line, then on the second line print the **k** distinct sensor numbers to be activated, separated by spaces. If multiple clean clusters exist, any valid configuration is accepted. Print only the **k** activated sensors.

If no such cluster exists, print `NO`.

## Examples

### Example 1

**Input**
```
4 4 3
1 2
1 3
2 3
3 4
```

**Output**
```
NO
```

### Example 2

**Input**
```
5 2 3
1 2
3 4
```

**Output**
```
YES
1 3 5
```

### Example 3

**Input**
```
3 3 1
1 2
2 3
1 3
```

**Output**
```
YES
1
```

## Note

In Example 2, activating sensors 1, 3, and 5 is clean. The first interference pattern requires both 1 and 2 to be active (sensor 2 is inactive), and the second pattern requires both 3 and 4 to be active (sensor 4 is inactive). Thus, zero interference patterns are generated.
In Example 1, any choice of 3 sensors will cause both sensors associated with at least one interference pattern to be active, meaning the total number of generated patterns will be greater than zero.
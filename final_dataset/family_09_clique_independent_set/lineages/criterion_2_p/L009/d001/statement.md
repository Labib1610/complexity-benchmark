# Problem B — Interference-Free Group

Time limit: 2 s   Memory limit: 256 MB

## Description

A sensor network consists of **n** devices (numbered 1 to **n**) and **m** interference links. Each link joins a pair of devices that interfere with each other.

The physical arrangement of the network guarantees a specific structural property: any closed loop of interfering devices (a sequence of distinct devices where each device interferes with the next, and the last device interferes with the first) will always consist of an even number of devices.

A collection of devices is considered **interference-free** if no two devices within the collection share an interference link.

Given a target size **k**, determine whether an interference-free collection of exactly **k** devices exists, and if so, report one such collection.

## Input

The first line contains three integers **n**, **m**, and **k** (1 ≤ n ≤ 100000, 0 ≤ m ≤ 400000, 1 ≤ k ≤ n).
Each of the next **m** lines contains two integers **u** and **v** (1 ≤ u, v ≤ n, u ≠ v): an interference link. No link is listed twice, and the network is guaranteed to satisfy the even-loop property described above.

## Output

If an interference-free collection of exactly **k** devices exists, print `YES` on the first line. On the second line, print **k** distinct device numbers that form such a collection, separated by spaces. Any valid collection will be accepted.

If no such collection can be formed, print `NO`.

## Examples

### Example 1

**Input**
```
4 4 2
1 3
1 4
2 3
2 4
```

**Output**
```
YES
1 2
```

### Example 2

**Input**
```
5 0 5
```

**Output**
```
YES
1 2 3 4 5
```

### Example 3

**Input**
```
4 4 3
1 3
1 4
2 3
2 4
```

**Output**
```
NO
```

## Note

In Example 1, devices 1 and 2 do not share an interference link. In Example 3, the largest possible interference-free collection consists of only 2 devices, making a target size of 3 impossible.
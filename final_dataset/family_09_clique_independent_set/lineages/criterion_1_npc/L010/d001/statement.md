# Problem A — Isolated Monitoring Array

Time limit: 5 s   Memory limit: 256 MB

## Description

A facility operates **n** monitoring devices (labeled 1 to **n**). There are **m** mutual conflicts between certain pairs of devices. A conflict between device **u** and device **v** means they are incompatible as an unordered pair, and they cannot both be chosen in the same array.

An isolated monitoring array is exactly a set of devices where no listed conflict exists between any two chosen devices.

You are given a target array size **k**. Determine if there is an isolated monitoring array containing exactly **k** devices. If such an array can be formed, you must identify one.

## Input

The first line contains three integers **n**, **m**, and **k** (1 ≤ n ≤ 46, 0 ≤ m ≤ n·(n−1)/2, 1 ≤ k ≤ n).
Each of the next **m** lines contains two integers **u** and **v** (1 ≤ u, v ≤ n, u ≠ v), representing a mutual conflict between device **u** and device **v**. No conflict pair is listed more than once.

## Output

If an isolated monitoring array of exactly **k** devices can be formed, output `YES` on the first line. On the second line, output the **k** distinct device labels that make up this array, separated by spaces. If multiple valid arrays exist, print any one of them (in any order).

If no such array can be formed, output `NO`.

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

In Example 2, devices 1, 3, and 5 have no mutual conflicts among them. In Example 1, no three of the four devices are mutually free of conflicts.
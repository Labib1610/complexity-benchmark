# Problem B — Safe Antenna Activation

Time limit: 2 s   Memory limit: 256 MB

## Description

A communication array consists of **n** transmission antennas, labeled 1 through **n**. Certain pairs of these antennas will cause destructive interference if they are both powered on. You are provided with a list of **m** such interfering pairs.

The array's hardware topology guarantees a specific structural property: the interference network contains no closed loops of odd length. That is, it is impossible to find any sequence of an odd number of distinct antennas where each interferes with the next, and the last interferes with the first.

Your task is to determine if it is possible to power on exactly **k** antennas such that no destructive interference occurs among the chosen set. If such a configuration is possible, you must also provide one valid selection.

## Input

The first line contains three integers **n**, **m**, and **k** (1 ≤ n ≤ 100000, 0 ≤ m ≤ 400000, 1 ≤ k ≤ n).
Each of the following **m** lines contains two integers **u** and **v** (1 ≤ u, v ≤ n, u ≠ v), representing a pair of antennas that cause destructive interference. No pair is listed more than once. The input is guaranteed to satisfy the structural property described above.

## Output

If there is a valid selection of exactly **k** antennas, output `YES` on the first line. On the second line, output **k** distinct integers separated by spaces, representing the labels of the chosen antennas. If there are multiple valid selections, any of them will be accepted.

If no such selection of exactly **k** antennas exists, output `NO`.

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
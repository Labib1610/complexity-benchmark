# Problem A — Interference-Free Broadcast

Time limit: 5 s   Memory limit: 256 MB

## Description

A telecommunications company is configuring a new broadcast array. There are **n** candidate transmission channels available (numbered 1 through **n**). However, due to harmonic resonance, certain pairs of channels are completely incompatible; deploying them simultaneously will cause catastrophic signal degradation. There are **m** such documented interference conflicts.

An interference-free broadcast array is a selection of channels where absolutely no two selected channels share an interference conflict.

Given a target array size **k**, determine if it is possible to select exactly **k** channels that form an interference-free broadcast array, and if so, report one such selection.

## Input

The first line contains three integers **n**, **m**, and **k** (1 ≤ n ≤ 46, 0 ≤ m ≤ n·(n−1)/2, 1 ≤ k ≤ n).
Each of the next **m** lines contains two integers **u** and **v** (1 ≤ u, v ≤ n, u ≠ v): an interference conflict between channel **u** and channel **v**. No conflict is listed twice.

## Output

If an interference-free broadcast array of exactly **k** channels exists, print `YES` on the first line, then on the second line print **k** distinct channel numbers forming such an array, separated by spaces. Any array in which no two channels conflict is accepted.

If no such array exists, print `NO`.

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

In Example 2, channels 1, 3 and 5 have no interference conflicts among them. In Example 1 no three of the four channels are mutually compatible.
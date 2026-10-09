# Problem B — Interference-Free Group (Two Categories)

Time limit: 2 s   Memory limit: 256 MB

## Description

A communication system has **n** devices (numbered 1..n) and **m** interference links. Each link joins two devices that interfere with each other.

In this system the devices split into **two categories**, and **every interference link connects a device in one category to a device in the other** — there is no interference between two devices of the same category. (The categories are not given to you; you may recover them from the links.)

A group of devices is **interference-free** if no two devices in the group interfere.

Given a target size **k**, decide whether an interference-free group of exactly **k** devices exists, and if so report one.

## Input

The first line contains three integers **n**, **m**, and **k** (1 ≤ n ≤ 100000, 0 ≤ m ≤ 400000, 1 ≤ k ≤ n).
Each of the next **m** lines contains two integers **u** and **v** (1 ≤ u, v ≤ n, u ≠ v): an interference link. No link is listed twice, and the links are guaranteed to follow the two-category structure above (every link runs between the two categories).

## Output

If an interference-free group of **k** devices exists, print `YES` on the first line, then on the second line print **k** distinct device numbers forming such a group, separated by spaces. Any group in which no two devices are linked is accepted.

If no such group exists, print `NO`.

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

This is the same interference-free problem as Problem A, but the system has the two-category structure (interference links run only between the two categories), which makes an efficient exact solution possible. In Example 1 devices 1 and 2 (same category) do not interfere. In Example 3 the largest interference-free group has only 2 devices, so 3 is impossible.

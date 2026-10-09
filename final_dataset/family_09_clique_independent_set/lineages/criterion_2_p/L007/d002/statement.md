# Problem B — Conflict-Free Subset

Time limit: 2 s   Memory limit: 256 MB

## Description

A network contains **n** transmitters (numbered 1 to **n**) and **m** conflict pairs. Each conflict pair indicates two transmitters that interfere with each other and cannot operate simultaneously.

The interference in this network follows a strict structural rule: if you can form a closed loop of three or more distinct transmitters $t_1, t_2, \dots, t_c$ such that each transmitter in the sequence interferes with the next (and the last interferes with the first), the total number of transmitters in that loop ($c$) is always even.

A subset of transmitters is **conflict-free** if no two transmitters in the subset interfere.

Given a target size **k**, decide whether a conflict-free subset of exactly **k** transmitters exists, and if so, report one.

## Input

The first line contains three integers **n**, **m**, and **k** (1 ≤ n ≤ 100000, 0 ≤ m ≤ 400000, 1 ≤ k ≤ n).
Each of the next **m** lines contains two integers **u** and **v** (1 ≤ u, v ≤ n, u ≠ v): a conflict pair. No conflict pair is listed twice, and the pairs are guaranteed to follow the structural rule above (every closed loop of conflicts has an even number of transmitters).

## Output

If a conflict-free subset of **k** transmitters exists, print `YES` on the first line, then on the second line print **k** distinct transmitter numbers forming such a subset, separated by spaces. Any subset in which no two transmitters conflict is accepted.

If no such subset exists, print `NO`.

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

This is the same conflict-free problem as Problem A, but the network has the even-loop structure, which makes an efficient exact solution possible. In Example 1, transmitters 1 and 2 do not conflict. In Example 3, the largest conflict-free subset has only 2 transmitters, so 3 is impossible.
# Problem A — Audit Panel

Time limit: 5 s   Memory limit: 256 MB

## Description

A regulatory agency is forming an audit panel from a pool of **n** nominated experts (numbered 1 to **n**). During the vetting process, **m** specific pairs of experts were found to have a professional conflict of interest.

To ensure impartiality, the final panel must not contain any two experts who have a conflict of interest with each other. The agency requires that the panel consist of exactly **k** experts.

Determine whether it is possible to form a valid panel, and if so, identify the experts to be appointed.

## Input

The first line contains three integers **n**, **m**, and **k** (1 ≤ n ≤ 46, 0 ≤ m ≤ n·(n−1)/2, 1 ≤ k ≤ n).
Each of the next **m** lines contains two integers **u** and **v** (1 ≤ u, v ≤ n, u ≠ v): a pair of experts with a conflict of interest. No conflicting pair is listed twice.

## Output

If a valid panel of exactly **k** experts can be formed, print `YES` on the first line, then on the second line print **k** distinct expert numbers forming such a panel, separated by spaces. Any panel in which no two experts have a conflict is accepted.

If no such panel can be formed, print `NO`.

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

In Example 2, experts 1, 3, and 5 have no conflicts of interest among themselves. In Example 1, it is impossible to find three experts out of the four who are completely free of mutual conflicts.

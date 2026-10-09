# Problem A — Stable Mixture

Time limit: 5 s   Memory limit: 256 MB

## Description

A chemical laboratory has **n** compounds (numbered 1..n) and **m** known dangerous reactions. Each reaction occurs if a specific pair of compounds is mixed together.

A mixture of compounds is **stable** if no two compounds in the mixture react dangerously (there is no dangerous reaction between any pair of them).

Given a target size **k**, decide whether a stable mixture of exactly **k** compounds exists, and if so report one.

## Input

The first line contains three integers **n**, **m**, and **k** (1 ≤ n ≤ 46, 0 ≤ m ≤ n·(n−1)/2, 1 ≤ k ≤ n).
Each of the next **m** lines contains two integers **u** and **v** (1 ≤ u, v ≤ n, u ≠ v): a pair of compounds that react dangerously. No pair is listed twice.

## Output

If a stable mixture of **k** compounds exists, print `YES` on the first line, then on the second line print **k** distinct compound numbers forming such a mixture, separated by spaces. Any mixture in which no two compounds react is accepted.

If no such mixture exists, print `NO`.

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

A stable mixture requires that no two chosen compounds may react. In Example 2, compounds 1, 3 and 5 have no dangerous reactions among them. In Example 1, no three of the four compounds are mutually non-reactive.

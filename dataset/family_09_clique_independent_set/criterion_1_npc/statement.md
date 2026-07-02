# Problem A — Tight-Knit Group

Time limit: 5 s   Memory limit: 256 MB

## Description

A social network has **n** users (numbered 1..n) and **m** friendship connections. Each connection joins two users who are friends.

A group of users is **tight-knit** if every two users in the group are directly connected by a friendship.

Given a target size **k**, decide whether a tight-knit group of exactly **k** users exists, and if so report one.

## Input

The first line contains three integers **n**, **m**, and **k** (1 ≤ n ≤ 40, 0 ≤ m ≤ n·(n−1)/2, 1 ≤ k ≤ n).
Each of the next **m** lines contains two integers **u** and **v** (1 ≤ u, v ≤ n, u ≠ v): a friendship connection. No connection is listed twice.

## Output

If a tight-knit group of **k** users exists, print `YES` on the first line, then on the second line print **k** distinct user numbers forming such a group, separated by spaces. Any group in which all pairs are directly connected is accepted.

If no such group exists, print `NO`.

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
YES
1 2 3
```

### Example 2

**Input**
```
4 3 3
1 2
2 3
3 4
```

**Output**
```
NO
```

### Example 3

**Input**
```
3 0 1
```

**Output**
```
YES
1
```

## Note

In Example 1, users 1, 2, and 3 are all pairwise friends. In Example 2 there is no set of three users who are all mutually connected.

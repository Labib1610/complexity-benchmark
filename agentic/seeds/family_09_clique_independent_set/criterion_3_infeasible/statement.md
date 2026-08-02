# Problem C — Oversized Request

Time limit: 1 s   Memory limit: 256 MB

## Description

A social network has **n** users (numbered 1..n) and **m** friendship connections. A group of users is **tight-knit** if every two users in the group are directly connected by a friendship.

You are asked whether a tight-knit group of exactly **r** users exists. In the input you are given, **r is larger than the total number of users n**, so no group can possibly contain that many users.

Determine whether such a group exists.

## Input

The first line contains three integers **n**, **m**, and **r** (1 ≤ n ≤ 100000, 0 ≤ m ≤ 200000, r > n).
Each of the next **m** lines contains two integers **u** and **v** (1 ≤ u, v ≤ n, u ≠ v): a friendship connection.

## Output

Print a single line containing `NO`, since no tight-knit group of r users can exist.

## Examples

### Example 1

**Input**
```
3 2 5
1 2
2 3
```

**Output**
```
NO
```

### Example 2

**Input**
```
2 1 10
1 2
```

**Output**
```
NO
```

## Note

A group cannot contain more users than exist in the network, so a request for r > n users is impossible.

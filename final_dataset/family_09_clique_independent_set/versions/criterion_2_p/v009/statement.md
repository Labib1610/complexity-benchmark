# Problem B — Social Network Camps

Time limit: 2 s   Memory limit: 256 MB

## Description

A social network has **n** users (numbered 1..n) and **m** friendship connections. Each connection joins two users who are friends.

In this network the users split into **two camps**, and **every friendship connects a user in one camp to a user in the other** — there are no friendships between two users of the same camp. (The camps are not given to you; you may recover them from the connections.)

Given a target size **k**, your objective is to decide whether there exists a group of exactly **k** users that is **all-strangers** (meaning no two users in the group are friends), and if so, report one such group.

## Input

The first line contains three integers **n**, **m**, and **k** (1 ≤ n ≤ 100000, 0 ≤ m ≤ 400000, 1 ≤ k ≤ n).
Each of the next **m** lines contains two integers **u** and **v** (1 ≤ u, v ≤ n, u ≠ v): a friendship connection. No connection is listed twice, and the connections are guaranteed to follow the two-camp structure above (every friendship runs between the two camps).

## Output

If an all-strangers group of **k** users exists, print `YES` on the first line, then on the second line print **k** distinct user numbers forming such a group, separated by spaces. Any group in which no two users are connected is accepted.

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

This is the same all-strangers problem as Problem A, but the network has the two-camp structure (friendships run only between the two camps), which makes an efficient exact solution possible. In Example 1 users 1 and 2 (same camp) are not friends. In Example 3 the largest all-strangers group has only 2 users, so 3 is impossible.

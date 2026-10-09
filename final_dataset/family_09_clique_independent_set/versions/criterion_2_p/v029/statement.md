# Problem B — Completely Disconnected Group

Time limit: 2 s   Memory limit: 256 MB

## Description

A social network has **n** users (numbered 1..n) and **m** friendship connections. Each connection joins two users who are friends.

In this network, it is guaranteed that every user can be assigned a binary status (either 0 or 1) such that every friendship connects a user with status 0 to a user with status 1 — there are no friendships between users who share the same status. (The statuses are not given to you; you must deduce them from the connections.)

A group of users is **completely disconnected** if no two users in the group are friends.

Given a target size **k**, decide whether a completely disconnected group of exactly **k** users exists, and if so report one.

## Input

The first line contains three integers **n**, **m**, and **k** (1 ≤ n ≤ 100000, 0 ≤ m ≤ 400000, 1 ≤ k ≤ n).
Each of the next **m** lines contains two integers **u** and **v** (1 ≤ u, v ≤ n, u ≠ v): a friendship connection. No connection is listed twice, and the connections are guaranteed to follow the binary status structure described above (every friendship runs between users of different statuses).

## Output

If a completely disconnected group of **k** users exists, print `YES` on the first line, then on the second line print **k** distinct user numbers forming such a group, separated by spaces. Any group in which no two users are connected is accepted.

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

In Example 1, users 1 and 2 (who can share the same status) are not friends. In Example 3, the largest completely disconnected group has only 2 users, so finding a group of 3 is impossible.

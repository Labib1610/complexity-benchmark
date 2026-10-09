# Problem B — All-Strangers Group (Restricted Connections)

Time limit: 2 s   Memory limit: 256 MB

## Description

A social network has **n** users (numbered 1..n) and **m** friendship connections. Each connection joins two users who are friends.

In this network, every user inherently possesses one of two mutually exclusive profile types. The system strictly enforces that every friendship connection links a user of one profile type to a user of the other type — there are absolutely no friendships between two users who share the same profile type. (The profile types are not given to you; you may deduce them from the connections.)

A group of users is **all-strangers** if no two users in the group are friends.

Given a target size **k**, decide whether an all-strangers group of exactly **k** users exists, and if so report one.

## Input

The first line contains three integers **n**, **m**, and **k** (1 ≤ n ≤ 100000, 0 ≤ m ≤ 400000, 1 ≤ k ≤ n).
Each of the next **m** lines contains two integers **u** and **v** (1 ≤ u, v ≤ n, u ≠ v): a friendship connection. No connection is listed twice, and the connections are guaranteed to follow the restricted structure above (every friendship runs between two users of different profile types).

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

This is the all-strangers problem, but the network has the restricted structure (friendships run only between different profile types), which makes an efficient exact solution possible. In Example 1 users 1 and 2 (same profile type) are not friends. In Example 3 the largest all-strangers group has only 2 users, so 3 is impossible.

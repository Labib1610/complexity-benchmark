# Problem A — All-Strangers Group

Time limit: 5 s   Memory limit: 256 MB

## Description

A social network has **n** users (numbered 1..n) and **m** friendship connections. Each connection joins two users who are friends.

A group of users is **all-strangers** if no two users in the group are friends (there is no connection between any pair of them).

Given a target size **k**, decide whether an all-strangers group of exactly **k** users exists, and if so report one.

## Input

The first line contains three integers **n**, **m**, and **k**. The number of users **n** is at least 1 and at most the network's strict capacity limit of 46 accounts. The number of connections **m** ranges from 0 up to the maximum possible number of unique pairs of users. The target size **k** is at least 1 and at most the total number of users **n**.

Each of the next **m** lines contains two integers **u** and **v** (representing valid, distinct user IDs from 1 to **n**): a friendship connection. No connection is listed twice.

## Output

If an all-strangers group of **k** users exists, print `YES` on the first line, then on the second line print **k** distinct user numbers forming such a group, separated by spaces. Any group in which no two users are connected is accepted.

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

In Example 2, users 1, 3 and 5 have no friendships among them. In Example 1 no three of the four users are mutually unconnected.

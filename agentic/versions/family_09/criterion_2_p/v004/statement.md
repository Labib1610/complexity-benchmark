# Problem B — All-Strangers Group

Time limit: 2 s   Memory limit: 256 MB

## Description

A social network has **n** users (numbered 1..n) and **m** friendship connections. Each connection joins two users who are friends.

A group of users is **all-strangers** if no two users in the group are friends. There are $\binom{n}{k}$ possible groups of size **k** to consider. You must evaluate this space of combinations to decide whether an all-strangers group of exactly **k** users exists, and if so report one.

In this network, the users happen to split into two categories, and every friendship connects a user in one category to a user in the other — there are no friendships between two users of the same category. (The categories are not given to you; you may recover them from the connections.)

## Input

The first line contains three integers **n**, **m**, and **k** (1 ≤ n ≤ 100000, 0 ≤ m ≤ 400000, 1 ≤ k ≤ n).
Each of the next **m** lines contains two integers **u** and **v** (1 ≤ u, v ≤ n, u ≠ v): a friendship connection. No connection is listed twice, and the connections are guaranteed to follow the two-category structure above (every friendship runs between the two categories).

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

In Example 1 users 1 and 2 (same category) are not friends. In Example 3, exploring the combinations reveals the largest all-strangers group has only 2 users, so 3 is impossible.

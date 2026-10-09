# Problem B — Stranger Selection Stage

Time limit: 2 s   Memory limit: 256 MB

## Description

You are building a decentralized consensus protocol. The workflow consists of three stages:

1. **Network Discovery**: We identify a social network of **n** users (numbered 1..n) and **m** friendship connections. Each connection joins two users who are friends.
2. **Stranger Selection (Your Task)**: We must form a committee of exactly **k** users. To prevent collusion, the committee must be an **all-strangers** group—no two users in the group can be friends.
3. **Consensus Execution**: The selected committee runs the protocol (handled by another system).

In this network, the discovery stage guarantees that users split into **two camps**, and **every friendship connects a user in one camp to a user in the other** — there are no friendships between two users of the same camp. (The camps are not given to you; you may recover them from the connections.)

Given the target size **k**, decide whether an all-strangers group of exactly **k** users exists for the Stranger Selection stage, and if so report one.

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

In Example 1 users 1 and 2 (same camp) are not friends. In Example 3 the largest all-strangers group has only 2 users, so 3 is impossible.

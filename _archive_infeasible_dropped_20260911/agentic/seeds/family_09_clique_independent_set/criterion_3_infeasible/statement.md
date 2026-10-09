# Problem C — All-Strangers Group: Certify Impossibility

Time limit: 2 s   Memory limit: 256 MB

## Description

A social network has **n** users (numbered 1..n) and **m** friendship connections. A group of users is **all-strangers** if no two users in the group are friends.

You are asked whether an all-strangers group of exactly **k** users exists. For every input in this problem it is **guaranteed that no such group exists**. Your job is not to search; it is to **prove** the impossibility with a short certificate that can be checked directly against the input.

Exactly one of the following two reasons always applies. Print the one that holds:

- **The request is too large.** If **k is greater than n**, there are not even k users to choose, so no group of that size can exist.
  Print a single line: `SIZE`

- **Everyone is connected.** If the network is **complete** — every pair of users is friends — then any two users are connected, so the largest all-strangers group has just one user; for k ≥ 2 no such group exists.
  Print a single line: `COMPLETE`

## Input

The first line contains three integers **n**, **m**, and **k** (1 ≤ n ≤ 100000, 0 ≤ m ≤ n·(n−1)/2, 1 ≤ k).
Each of the next **m** lines contains two integers **u** and **v** (1 ≤ u, v ≤ n, u ≠ v): a friendship connection. No connection is listed twice.

## Output

Print a single line: `SIZE` (if k > n) or `COMPLETE` (if the graph is complete and k ≥ 2).

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
SIZE
```

### Example 2

**Input**
```
3 3 2
1 2
1 3
2 3
```

**Output**
```
COMPLETE
```

## Note

In Example 1 the request asks for 5 users out of only 3, so `SIZE` is the certificate. In Example 2 all three users are mutually connected (a complete network), so the largest all-strangers group has one user and `COMPLETE` proves that 2 is impossible.

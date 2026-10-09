# Problem B — Disconnected Assembly (Hidden Codes)

Time limit: 2 s   Memory limit: 256 MB

## Description

A system consists of **n** components (numbered 1..n) and **m** bidirectional interference links. Each link joins two components that interfere with each other.

The system possesses a hidden structural property: it is possible to assign every component a secret integer code such that for every interference link, the sum of the secret codes of the two linked components is an odd number. (The codes are not given to you; you only know that such an assignment exists.)

A subset of components is **safe** if no two components in the subset interfere with each other.

Given a target size **k**, decide whether a safe subset of exactly **k** components exists, and if so report one.

## Input

The first line contains three integers **n**, **m**, and **k** (1 ≤ n ≤ 100000, 0 ≤ m ≤ 400000, 1 ≤ k ≤ n).
Each of the next **m** lines contains two integers **u** and **v** (1 ≤ u, v ≤ n, u ≠ v): an interference link. No link is listed twice, and the links are guaranteed to follow the hidden code structure above.

## Output

If a safe subset of **k** components exists, print `YES` on the first line, then on the second line print **k** distinct component numbers forming such a subset, separated by spaces. Any subset in which no two components interfere is accepted.

If no such subset exists, print `NO`.

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

In Example 1, components 1 and 2 do not interfere, so they can form a safe subset of size 2. In Example 3, the largest possible safe subset has only 2 components, making a subset of size 3 impossible.
# Problem B — Mutually Disconnected Collection

Time limit: 2 s   Memory limit: 256 MB

## Description

A system has **n** elements (numbered 1..n) and **m** bidirectional links. Each link joins two elements.

In this system, the elements can be assigned one of two unstated roles, such that **every link connects an element with one role to an element with the other role** — there are no links between two elements sharing the same role. (The roles are not given to you; you may deduce them from the links.)

A collection of elements is **mutually disconnected** if no two elements in the collection share a link.

Given a target size **k**, decide whether a mutually disconnected collection of exactly **k** elements exists, and if so report one.

## Input

The first line contains three integers **n**, **m**, and **k** (1 ≤ n ≤ 100000, 0 ≤ m ≤ 400000, 1 ≤ k ≤ n).
Each of the next **m** lines contains two integers **u** and **v** (1 ≤ u, v ≤ n, u ≠ v): a link. No link is listed twice, and the links are guaranteed to follow the alternating-role structure above (every link runs between elements of different roles).

## Output

If a mutually disconnected collection of **k** elements exists, print `YES` on the first line, then on the second line print **k** distinct element numbers forming such a collection, separated by spaces. Any collection in which no two elements are linked is accepted.

If no such collection exists, print `NO`.

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

In Example 1, elements 1 and 2 (which must have the same role) are not linked. In Example 3, the largest mutually disconnected collection has only 2 elements, so a target of 3 is impossible.

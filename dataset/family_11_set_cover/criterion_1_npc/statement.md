# Problem A — Consultant Hiring

Time limit: 5 s   Memory limit: 256 MB

## Description

A project requires **u** distinct skills (numbered 1..u). You can hire from **s** available consultants; each consultant brings a specific set of skills. A skill is **covered** if at least one hired consultant has it.

With a budget of **k** hires, decide whether you can cover **every** required skill, and if so report which consultants to hire.

## Input

The first line contains three integers **u**, **s**, and **k** (1 ≤ u ≤ 20, 1 ≤ s ≤ 200, 0 ≤ k ≤ s).
Each of the next **s** lines describes one consultant: an integer **c** (the number of skills that consultant has) followed by **c** distinct skill ids (each between 1 and u).

## Output

If **k** hires can cover every skill, print `YES` on the first line, then on the second line print the indices (from 1 to s, in the order the consultants are listed) of the hired consultants, separated by spaces (at most k of them). Any selection of at most k consultants that covers every skill is accepted.

If it cannot be done with k hires, print `NO`.

## Examples

### Example 1

**Input**
```
4 3 2
2 1 2
2 3 4
2 2 3
```

**Output**
```
YES
1 2
```

### Example 2

**Input**
```
4 4 2
1 1
1 2
1 3
1 4
```

**Output**
```
NO
```

### Example 3

**Input**
```
1 1 1
1 1
```

**Output**
```
YES
1
```

## Note

In Example 1, consultants 1 and 2 together bring skills {1,2} ∪ {3,4} = all four. In Example 2, each consultant brings a single distinct skill, so four hires are needed and two are not enough.

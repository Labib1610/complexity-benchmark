# Problem B — Consultant Hiring (Paired Skills)

Time limit: 2 s   Memory limit: 256 MB

## Description

A project requires **u** distinct skills (numbered 1..u). You can hire from **s** available consultants; each consultant brings a specific set of skills. A skill is **covered** if at least one hired consultant has it.

In this project **every consultant brings exactly two skills**, and the skills divide into two kinds so that each consultant pairs one skill of the first kind with one of the second (you may recover the two kinds from the consultants). Every skill is brought by at least one consultant.

With a budget of **k** hires, decide whether you can cover **every** required skill, and if so report which consultants to hire.

## Input

The first line contains three integers **u**, **s**, and **k** (1 ≤ u ≤ 200000, 1 ≤ s ≤ 400000, 0 ≤ k ≤ s).
Each of the next **s** lines describes one consultant: the integer **2** followed by that consultant's two distinct skill ids (each between 1 and u). Every skill appears in at least one consultant, and the skills follow the two-kind pairing described above.

## Output

If **k** hires can cover every skill, print `YES` on the first line, then on the second line print the indices (from 1 to s) of the hired consultants (at most k of them), separated by spaces. Any selection of at most k consultants covering every skill is accepted.

If it cannot be done with k hires, print `NO`.

## Examples

### Example 1

**Input**
```
4 4 2
2 1 3
2 1 4
2 2 3
2 2 4
```

**Output**
```
YES
1 4
```

### Example 2

**Input**
```
4 4 1
2 1 3
2 1 4
2 2 3
2 2 4
```

**Output**
```
NO
```

### Example 3

**Input**
```
2 1 1
2 1 2
```

**Output**
```
YES
1
```

## Note

This is the same consultant-hiring (set cover) problem as Problem A. The only difference is that every consultant brings exactly two paired skills, which makes an efficient exact solution possible. In Example 1, consultant 1 brings {1,3} and consultant 4 brings {2,4}, together covering all four skills. In Example 2 no two of the consultants cover all four skills, so one hire short of two cannot work.

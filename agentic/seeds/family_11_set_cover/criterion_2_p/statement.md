# Problem B — Paired-Skill Hiring

Time limit: 2 s   Memory limit: 256 MB

## Description

A project requires two kinds of skills: **uA** frontend skills (numbered 1..uA) and **uB** backend skills (numbered 1..uB). Every available consultant brings **exactly one** frontend skill and **exactly one** backend skill.

A skill is **covered** if at least one hired consultant has it. Every skill (frontend and backend) is brought by at least one consultant.

Hire the **fewest** consultants so that every frontend skill and every backend skill is covered.

## Input

The first line contains three integers **uA**, **uB**, and **s** (1 ≤ uA, uB ≤ 100000, 1 ≤ s ≤ 800000).
Each of the next **s** lines contains two integers **a** and **b** (1 ≤ a ≤ uA, 1 ≤ b ≤ uB): a consultant bringing frontend skill **a** and backend skill **b**. It is guaranteed every frontend skill and every backend skill appears in at least one consultant.

## Output

Print a single integer: the minimum number of consultants to hire so that every skill is covered.

## Examples

### Example 1

**Input**
```
2 2 2
1 1
2 2
```

**Output**
```
2
```

### Example 2

**Input**
```
1 3 3
1 1
1 2
1 3
```

**Output**
```
3
```

### Example 3

**Input**
```
2 2 3
1 1
2 1
2 2
```

**Output**
```
2
```

## Note

In Example 2, one frontend skill pairs with three different backend skills; covering all three backend skills needs three hires.

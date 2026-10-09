# Problem C — Missing Skill

Time limit: 1 s   Memory limit: 256 MB

## Description

A project requires **u** distinct skills (numbered 1..u). You can hire from **s** available consultants; each consultant brings a specific set of skills. A skill is **covered** if at least one hired consultant has it.

In the input you are given, **at least one required skill is brought by no consultant at all**. That skill can never be covered by any selection of hires, so the project can never be fully staffed.

Report the smallest id of a skill that no consultant has.

## Input

The first line contains two integers **u** and **s** (1 ≤ u ≤ 200000, 1 ≤ s ≤ 200000).
Each of the next **s** lines describes one consultant: an integer **c** (the number of skills that consultant has) followed by **c** distinct skill ids (each between 1 and u). The total number of listed skills across all consultants is at most 200000. It is guaranteed that at least one skill appears in no consultant's set.

## Output

Print a single integer: the smallest id of a skill that no consultant has.

## Examples

### Example 1

**Input**
```
4 2
2 1 2
1 3
```

**Output**
```
4
```

### Example 2

**Input**
```
3 1
1 1
```

**Output**
```
2
```

## Note

In Example 1, skills 1, 2, and 3 are brought by some consultant, but no consultant has skill 4.

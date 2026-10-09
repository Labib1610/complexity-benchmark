# Problem B — Sequencing the Batch on One Station

Time limit: 2 s   Memory limit: 256 MB

## Description
A single station must process a batch of $n$ distinct operations. The schedule for this station is defined as a linear arrangement of these operations. Since all operations must be executed exactly once, there are exactly $n!$ potential processing orders. Your task is to evaluate this space of permutations and find a sequence that perfectly satisfies a given set of $m$ structural rules, or prove that no such sequence exists.

Each rule is defined by a pair of operations, $a$ and $b$. The rule mandates that operation $a$ must be executed at some point before operation $b$ in the schedule. A sequence is only considered valid if it satisfies all $m$ rules simultaneously. 

You must search the possible schedules to determine if a valid processing order exists within the $n!$ arrangements. If the rules are mutually exclusive such that absolutely zero of the permutations are valid, you must definitively report that the rule set is contradictory.

## Input
The first line contains two integers $n$ and $m$. Operations are numbered from $1$ to $n$.
Each of the following $m$ lines contains two integers $a$ and $b$, indicating that operation $a$ must be processed before operation $b$.

## Output
If a valid processing order exists, print `YES` followed by a permutation of the integers $1$ to $n$ representing the valid sequence. (If there are multiple valid sequences, any one is acceptable).
If no valid sequence exists, print `NO`.

## Example 1

### Input
```
4 5
1 2
1 3
2 4
3 4
3 2
```

### Output
```
YES
1 3 2 4
```

## Example 2

### Input
```
3 3
1 2
2 3
3 1
```

### Output
```
NO
```

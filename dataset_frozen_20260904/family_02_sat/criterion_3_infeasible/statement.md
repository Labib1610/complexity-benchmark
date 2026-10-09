# Problem C — Forced Conflict Certificate

Time limit: 1 s   Memory limit: 256 MB

The same two-condition requirement structure is guaranteed to have no valid
assignment. Your goal is not to schedule — it is to certify the impossibility.

Each requirement of the form (l1 l2) carries an implicit rule: if condition l1
is violated (the opposite state is chosen), then condition l2 must hold, and
vice versa. These rules can be chained. It is guaranteed that at least one task
is trapped: following the chain of rules forces both "task j is active" and
"task j is inactive" simultaneously.

Find the smallest index j of such a trapped task and print it.

## Input
The first line contains two integers n and m (1 ≤ n ≤ 10^5, 1 ≤ m ≤ 2·10^5).
Each of the next m lines contains two non-zero signed integers l1 l2, with
|li| ≤ n.
It is guaranteed that no valid assignment exists and that at least one task
is forced into a contradiction by the rule chains.

## Output
Print a single integer j — the smallest task index that the rule chains force
into contradiction (both active and inactive simultaneously).

## Example 1
Input:
```
1 2
1 1
-1 -1
```
Output:
```
1
```

## Example 2
Input:
```
3 2
2 2
-2 -2
```
Output:
```
2
```

## Note
Requirement (1 1) implies "if task 1 is inactive, then it must be active";
requirement (−1 −1) implies "if task 1 is active, then it must be inactive."
Following both chains forces task 1 to be simultaneously active and inactive,
so the answer is 1.

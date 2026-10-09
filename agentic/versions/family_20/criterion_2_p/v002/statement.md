# Problem B — Manuscript Reviews in a Two-Sided Publishing House

Time limit: 2 s   Memory limit: 256 MB

## Description
A publishing house connects a pool of authors to a pool of editors. Each manuscript review joins exactly one author to exactly one editor, and no review ever occurs between two people on the same side — the process is strictly two-sided. Different people handle different numbers of reviews, and the busiest person in the whole house sets the scale of the schedule.

Work is organised into numbered review cycles 1, 2, 3, …, and completing a manuscript review consumes one whole cycle. The single binding safety rule is that two reviews involving a common person may never be scheduled in the same cycle, because a person cannot focus on two of their reviews at once. Manuscript lengths, person seniority, genre classes, and which side a review's participant sits on are all irrelevant beyond this meeting-rule; only which reviews share a person matters.

Because the busiest person has some number of reviews and none of them can share a cycle, at least that many cycles are unavoidable. The operations goal is to schedule using **no more** cycles than that unavoidable minimum — exactly the busiest-person count. Assign every review a cycle drawn from that many cycles so that no person ever has two of their reviews scheduled in the same cycle. (The two-sided process guarantees the unavoidable minimum is always achievable; despite appearances, no cycle beyond the busiest-person count is ever needed.)

## Input
First line: three integers nL, nR, m (1 ≤ nL, nR ≤ 100000, 0 ≤ m ≤ 400000).
Next m lines: two integers u v (1 ≤ u ≤ nL, 1 ≤ v ≤ nR): a review between author u and editor v.

## Output
Print `YES`, then a line with m integers in 1..Δ — the cycle of review i in input order (reviews involving any common person must differ).

## Example
### Input
```
3 3 4
1 1
2 1
2 2
3 3
```

### Output
```
YES
1 2 1 1
```

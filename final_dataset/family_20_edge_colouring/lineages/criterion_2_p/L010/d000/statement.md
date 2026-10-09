# Problem B — Briefing Sessions at a Two-Sided Conference

Time limit: 2 s   Memory limit: 256 MB

## Description
A conference event connects a group of morning presenters to a group of afternoon reviewers. Each briefing session joins exactly one morning presenter to exactly one afternoon reviewer, and no briefing ever runs between two participants in the same group — the meetings are strictly two-sided. Different participants have different numbers of briefings, and the busiest participant in the whole event sets the scale of the schedule.

The agenda is organised into numbered time slots 1, 2, 3, …, and holding a briefing consumes one whole time slot. The single binding rule is that two briefings involving a common participant may never be scheduled in the same time slot, because a participant cannot attend two briefings at once. Briefing durations, room sizes, topics, and which group a participant belongs to are all irrelevant beyond this meeting-rule; only which briefings share a participant matters.

Because the busiest participant has some number of briefings and none of them can share a time slot, at least that many time slots are unavoidable. The operations goal is to schedule using **no more** time slots than that unavoidable minimum — exactly the busiest-participant count. Assign every briefing a time slot drawn from that many time slots so that no participant ever has two of their briefings scheduled in the same time slot. (The two-sided structure guarantees the unavoidable minimum is always achievable; despite appearances, no time slot beyond the busiest-participant count is ever needed.)

## Input
First line: three integers nL, nR, m (1 ≤ nL, nR ≤ 100000, 0 ≤ m ≤ 400000).
Next m lines: two integers u v (1 ≤ u ≤ nL, 1 ≤ v ≤ nR): a briefing between morning presenter u and afternoon reviewer v.

## Output
Print `YES`, then a line with m integers in 1..Δ — the time slot of briefing i in input order (briefings involving any common participant must differ).

## Example

### Input
```text
3 3 4
1 1
1 2
2 1
3 3
```

### Output
```text
YES
1 2 2 1
```

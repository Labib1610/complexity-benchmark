# Problem B — Full-Coverage Mentor/Apprentice Pairing

Time limit: 2 s   Memory limit: 256 MB

## Description
The guild's training segment must be fully committed for the term, and the planners have flagged this sub-problem as the one most likely to blow up combinatorially — so treat it with appropriate care. The members split into two equal groups: a set of mentors, badged consecutively from the first badge, and an equal-sized set of apprentices, badged in the block immediately following the mentors. Every mentor and every apprentice is a distinct member, and the council insists that **all** of them be committed simultaneously in this single plan.

A mentor may be teamed with an apprentice only when that exact mentor–apprentice combination appears on the compatibility list; unapproved combinations are forbidden no matter how convenient. A mentor is typically compatible with several apprentices, and an apprentice with several mentors, so the compatibility list can be large and densely overlapping, with many more approved combinations than the plan will ultimately use. None of that redundancy matters except through which exact combinations are approved — the counts, the overlaps, and the order of the list are all incidental.

A valid schedule activates approved combinations so that **every** mentor and **every** apprentice is committed in **exactly one** activated combination: each member used exactly once, none omitted, none shared between two combinations. Because both groups are the same size, a valid schedule commits every member and leaves nothing over. Decide whether the compatibility list admits such a complete one-to-one commitment of all members, and if so output one; otherwise report that the approved combinations cannot simultaneously commit every member. (Although the instances can look daunting, the two-sided structure is far more forgiving than a three-way tiling — do not assume the worst-case machinery is required.)

## Input
First line: two integers q and t (1 ≤ q ≤ 100000, 0 ≤ t ≤ 400000).
Next t lines: two integers a b (1 ≤ a ≤ q < b ≤ 2q): an allowed pair.

## Output
If possible, print `YES` then q lines each with the two items of one chosen pair; otherwise `NO`.

## Example

**Input:**
```
3 4
1 4
1 5
2 5
3 6
```

**Output:**
```
YES
1 4
2 5
3 6
```

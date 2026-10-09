# Problem B — Certification Drives for the Delivery Fleet

Time limit: 2 s   Memory limit: 256 MB

## Description
A certification program pairs a roster of delivery drivers with a roster of safety inspectors. Each required drive joins exactly one driver to exactly one inspector, and no drive ever pairs two people from the same roster — the pairing is strictly two-sided. Different personnel have different numbers of required drives, and the busiest person in the whole program sets the scale of the schedule.

The schedule is organised into numbered days 1, 2, 3, …, and completing a drive consumes one whole day. The single binding safety rule is that two drives involving a common person may never be scheduled on the same day, because an individual cannot participate in two drives at once. Vehicle types, route lengths, driver experience, and which roster a person belongs to are all irrelevant beyond this meeting-rule; only which drives share a person matters.

Because the busiest person has some number of drives and none of them can share a day, at least that many days are unavoidable. The operations goal is to schedule using **no more** days than that unavoidable minimum — exactly the busiest person's drive count. Assign every drive a day drawn from that many days so that no person ever has two of their drives scheduled on the same day. (The two-sided pairing guarantees the unavoidable minimum is always achievable; despite appearances, no day beyond the busiest person's count is ever needed.)

## Input
First line: three integers nL, nR, m (1 ≤ nL, nR ≤ 100000, 0 ≤ m ≤ 400000).
Next m lines: two integers u v (1 ≤ u ≤ nL, 1 ≤ v ≤ nR): a drive between driver u and inspector v.

## Output
Print `YES`, then a line with m integers in 1..Δ — the day assigned to drive i in input order (drives sharing any person must differ).

## Example

### Input
```text
3 3 4
1 1
1 2
2 2
3 3
```

### Output
```text
YES
1 2 1 1
```

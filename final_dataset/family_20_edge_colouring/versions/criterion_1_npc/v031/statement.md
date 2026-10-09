# Problem A — Broadcast Slots for the Debate Series

Time limit: 5 s   Memory limit: 256 MB

## Description
A broadcaster organises a debate series whose participants are public figures. The series has been engineered so that **every** participant takes part in **exactly three** bilateral debates — the schedule is uniformly three-way for every person. Broadcasting is organised into three prime-time slots, and airing a debate always consumes one whole slot.

Logistical rules forbid double-booking a participant: for any public figure, no two of their three debates may be aired in the same slot, because a person cannot be in two studios at once. Equivalently, the three debates involving any participant must be spread across three different slots. The physical studio locations, the topics, and which moderators are assigned are all irrelevant to the scheduling question — the only thing that binds is that debates sharing a participant never share a slot.

There are exactly three slots available and no more. Assign each debate in the series one of the three slots so that for every participant their three debates occupy three distinct slots, or determine that three slots are provably insufficient for this series. (Having only three slots for a uniformly three-way series leaves no slack whatsoever — a single unavoidable clash makes the whole schedule impossible.)

## Input
The first line has two integers **n** and **m** (n even, m = 3n/2, 2 ≤ n ≤ 2000).
Each of the next **m** lines has two integers u v (1 ≤ u < v ≤ n): a debate between participants u and v.

## Output
If an assignment exists, print `YES`, then a line with **m** integers in {1,2,3} — the slot of debate i in input order (debates sharing a participant must differ). Otherwise print `NO`.

## Example
Input:
```
4 6
1 2
1 3
1 4
2 3
2 4
3 4
```
Output:
```
YES
1 2 3 3 2 1
```

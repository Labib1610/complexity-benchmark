# Problem A — Arranging the Exhibition Across Sequential Rooms

Time limit: 5 s   Memory limit: 256 MB

## Description
A museum must arrange a batch of historical artifacts before a hard space limit. All artifacts take the same
amount of space — one display spot each — and are placed in a sequence of consecutive rooms. In any
single room, there are a limited number of identical spots, so the number of artifacts that can be exhibited
in any one room is capped by the number of spots; there is no benefit to leaving a spot empty,
but there is also no penalty beyond the room limit.

The artifacts are not independent. Some artifacts provide historical context required by others, giving rise to
sequence requirements: whenever one artifact must be seen before another can be understood, the dependent artifact has to
be placed in a strictly later room than the artifact it depends on — being in the same room is not enough,
since an artifact viewed in a room is only fully digested from the next room onward. Pedestals, artifact
priorities, and which specific spot holds an artifact are irrelevant; an artifact may go in any spot, and only
the room it occupies matters.

The exhibition length is expressed as a maximum number of rooms. Assign every artifact a room within the limit so
that all sequence requirements hold and no room is assigned more artifacts than there are spots, or
report that the batch cannot be exhibited within the limit. (With few spots the per-room cap and the
sequence chains pull against each other, so a layout that respects the sequence may still overflow the
room capacity and vice versa.)

## Input
First line: four integers n, M, T, m. Each of the next m lines: two integers a b — artifact a must be placed in a strictly earlier room than artifact b.

## Output
Print `YES` then n integers room[1..n] (the room of each artifact, in 1..T); otherwise `NO`.

## Example

**Input**
```text
4 2 3 3
1 2
1 3
2 4
```

**Output**
```text
YES
1 2 2 3
```

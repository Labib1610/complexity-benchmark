# Problem B — Full-Coverage Controller/Platform Pairing

Time limit: 2 s   Memory limit: 256 MB

## Description
The directorate's remote segment must be fully committed for the drill, and the planners require a careful allocation. The assets split into two equal groups: a set of controllers, badged consecutively from the first badge, and an equal-sized set of platforms, badged in the block immediately following the controllers. Every controller and every platform is a distinct asset, and command insists that **all** of them be committed simultaneously in this single plan.

A controller may be teamed with a platform only when that exact controller–platform combination appears on the certification list; uncertified combinations are forbidden no matter how convenient. A controller is typically certified with several platforms, and a platform with several controllers, so the certification list can be large and densely overlapping, with many more certified combinations than the plan will ultimately use. None of that redundancy matters except through which exact combinations are certified — the counts, the overlaps, and the order of the list are all incidental.

An acceptable roster activates certified combinations so that **every** controller and **every** platform is committed in **exactly one** activated combination: each asset used exactly once, none omitted, none shared between two combinations. Because both groups are the same size, an acceptable roster commits every asset and leaves nothing over. Decide whether the certification list admits such a complete one-to-one commitment of all assets, and if so output one; otherwise report that the certified combinations cannot simultaneously commit every asset.

## Input
First line: two integers q and t (1 ≤ q ≤ 100000, 0 ≤ t ≤ 400000).
Next t lines: two integers a and b (1 ≤ a ≤ q < b ≤ 2q): an allowed combination.

## Output
If possible, print `YES` then q lines each with the two items of one chosen combination; otherwise `NO`.

## Example
### Input
```
3 5
1 4
1 5
2 4
2 6
3 5
```

### Output
```
YES
1 4
2 6
3 5
```

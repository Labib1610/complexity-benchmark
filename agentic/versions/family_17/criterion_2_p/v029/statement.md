# Problem B — Full-Coverage Controller/Platform Pairing

Time limit: 2 s   Memory limit: 256 MB

## Description
The directorate's remote segment must be fully committed for the drill. The assets split into two equal collections: controllers, labeled consecutively starting from 1, and an equal-sized collection of platforms, labeled in the block immediately following the controllers. Every controller and every platform is a distinct asset, and command insists that **all** of them be committed simultaneously in this single plan.

A controller may be teamed with a platform only when that exact controller–platform combination appears on the authorization list; unauthorized combinations are forbidden. A controller is typically authorized with several platforms, and a platform with several controllers, so the authorization list can be large, with many more authorized combinations than the plan will ultimately use. None of that redundancy matters except through which exact combinations are authorized — the counts, the overlaps, and the order of the list are all incidental.

An acceptable roster activates authorized combinations so that **every** controller and **every** platform is committed in **exactly one** activated combination: each asset used exactly once, none omitted, none shared between two combinations. Because both collections are the same size, an acceptable roster commits every asset and leaves nothing over. Decide whether the authorization list admits such a complete and exclusive commitment of all assets, and if so output one; otherwise report that the authorized combinations cannot simultaneously commit every asset.

## Input
First line: two integers q and t (1 ≤ q ≤ 100000, 0 ≤ t ≤ 400000).
Next t lines: two integers a b (1 ≤ a ≤ q < b ≤ 2q): an allowed pair.

## Output
If possible, print `YES` then q lines each with the two items of one chosen pair; otherwise `NO`.

## Example

### Input
```
3 4
1 4
1 5
2 5
3 6
```

### Output
```
YES
1 4
2 5
3 6
```

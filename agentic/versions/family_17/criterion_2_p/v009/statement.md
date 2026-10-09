# Problem B — Full-Coverage Controller/Platform Pairing

Time limit: 2 s   Memory limit: 256 MB

## Description
The assets split into two equal groups: a set of controllers, numbered consecutively starting from 1, and an equal-sized set of platforms, numbered in the block immediately following the controllers. Every controller and every platform is a distinct asset.

A controller may be teamed with a platform only when that exact controller–platform combination appears on the certification list; uncertified combinations are forbidden no matter how convenient. A controller is typically certified with several platforms, and a platform with several controllers, so the certification list can be large and densely overlapping, with many more certified combinations than the plan will ultimately use. None of that redundancy matters except through which exact combinations are certified — the counts, the overlaps, and the order of the list are all incidental.

The directorate's remote segment requires a roster for the upcoming drill. An acceptable roster activates certified combinations so that **every** controller and **every** platform is committed in **exactly one** activated combination: each asset used exactly once, none omitted, none shared between two combinations. Because both groups are the same size, an acceptable roster commits every asset and leaves nothing over. Decide whether the certification list admits such a complete one-to-one commitment of all assets, and if so output one; otherwise report that the certified combinations cannot simultaneously commit every asset. 

## Input
First line: two integers q and t (1 ≤ q ≤ 100000, 0 ≤ t ≤ 400000).
Next t lines: two integers a b (1 ≤ a ≤ q < b ≤ 2q): an allowed pair.

## Output
If possible, print `YES` then q lines each with the two items of one chosen pair; otherwise `NO`.

## Example

### Input
```
2 3
1 3
1 4
2 3
```

### Output
```
YES
1 4
2 3
```

# Problem B — Full-Coverage Controller/Platform Pairing

Time limit: 2 s   Memory limit: 256 MB

## Description
The directorate's remote segment must be fully committed for an upcoming drill. The assets split into two equal groups: a set of controllers, badged consecutively from 1 to q, and an equal-sized set of platforms, badged in the block immediately following the controllers from q+1 to 2q. Every controller and every platform is a distinct asset, and command insists that all of them be committed simultaneously in this single plan.

A controller may be teamed with a platform only when that exact controller–platform combination appears on the certification list; uncertified combinations are forbidden. The certification list provides all the available options for these pairings.

An acceptable roster activates certified combinations so that every controller and every platform is committed in exactly one activated combination: each asset used exactly once, none omitted, none shared between two combinations. Decide whether the certification list admits such a complete one-to-one commitment of all assets, and if so output one; otherwise report that the certified combinations cannot simultaneously commit every asset.

## Input
First line: two integers q and t (1 ≤ q ≤ 100000, 0 ≤ t ≤ 400000).
Next t lines: two integers a b (1 ≤ a ≤ q < b ≤ 2q): an allowed pair.

## Output
If possible, print `YES` then q lines each with the two items of one chosen pair; otherwise `NO`.

## Example
**Input**
```
3 4
1 4
2 5
3 6
2 6
```

**Output**
```
YES
1 4
2 5
3 6
```

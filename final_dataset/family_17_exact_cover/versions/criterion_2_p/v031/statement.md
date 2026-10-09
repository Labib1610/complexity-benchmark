# Problem B — Full-Coverage Plug/Socket Pairing

Time limit: 2 s   Memory limit: 256 MB

## Description
The facility's power grid must be fully connected for the test. The components split into two equal groups: a set of plugs, numbered consecutively starting from 1, and an equal-sized set of sockets, numbered in the block immediately following the plugs. Every plug and every socket is a distinct component, and engineering insists that all of them be connected simultaneously in this single configuration.

A plug may be paired with a socket only when that exact plug–socket combination appears on the compatibility list; incompatible combinations are forbidden no matter how convenient. A plug is typically compatible with several sockets, and a socket with several plugs, so the compatibility list can be large and densely overlapping, with many more compatible combinations than the configuration will ultimately use. None of that redundancy matters except through which exact combinations are compatible — the counts, the overlaps, and the order of the list are all incidental.

An acceptable configuration activates compatible combinations so that every plug and every socket is connected in exactly one activated combination: each component used exactly once, none omitted, none shared between two combinations. Because both groups are the same size, an acceptable configuration connects every component and leaves nothing over. Decide whether the compatibility list admits such a complete one-to-one connection of all components, and if so output one; otherwise report that the compatible combinations cannot simultaneously connect every component.

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
2 5
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

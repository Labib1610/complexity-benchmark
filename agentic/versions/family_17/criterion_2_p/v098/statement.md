# Problem B — Full-Coverage Controller/Platform Pairing

Time limit: 2 s   Memory limit: 256 MB

## Description
The directorate's remote segment relies on two types of assets, which are assigned numerical identifiers based on their operational role. Controllers receive consecutive integers from $1$ to $q$, and platforms receive consecutive integers from $q+1$ to $2q$. 

A certification list dictates the operational capabilities of these assets. It contains specific combinations, each consisting of exactly one controller and exactly one platform, that have been approved to operate together. Uncertified combinations are forbidden, no matter how convenient they might be. A controller is typically certified with several platforms, and a platform with several controllers, leading to a list with many more certified combinations than will ultimately be used. The counts, overlaps, and order of this list are incidental.

An acceptable roster is formed by activating a subset of these certified combinations. When a combination is activated, the involved controller and platform are committed to each other. No asset may be shared between two activated combinations.

Command insists that the upcoming drill must fully commit the remote segment. Therefore, the roster must activate combinations such that **every** controller and **every** platform is committed exactly once. None can be omitted, and none can be used multiple times. Decide whether the certification list admits such a complete one-to-one commitment of all $2q$ assets, and if so output one; otherwise report that the certified combinations cannot simultaneously commit every asset.

## Input
First line: two integers $q$ and $t$ ($1 \le q \le 100000$, $0 \le t \le 400000$).
Next $t$ lines: two integers $a$ and $b$ ($1 \le a \le q < b \le 2q$), representing an allowed pair.

## Output
If possible, print `YES` followed by $q$ lines, each containing the two items of one chosen pair. Otherwise, print `NO`.

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

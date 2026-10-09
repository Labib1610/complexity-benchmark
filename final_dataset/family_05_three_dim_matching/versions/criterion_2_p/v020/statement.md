# Problem B — Port Manifest

Time limit: 2 s
Memory limit: 256 MB

## Description

A port authority must finalize **k** shipping manifests. There are three categories of assets, each containing exactly **k** items:

- **k** shipping containers, numbered 1..k,
- **k** RFID tags, numbered 1..k,
- **k** cargo vessels, numbered 1..k.

A valid manifest entry consists of exactly one container, one RFID tag, and one cargo vessel. You are given a list of cleared entries `(u, v, w)`.

In this port's system, **each shipping container is permanently affixed with exactly one RFID tag, and no two containers share the same tag** — so the container-to-tag pairing is already fixed. The only thing left to decide is the cargo vessels.

Choose exactly **k** cleared entries so that every container, every RFID tag, and every cargo vessel is used in **exactly one** chosen manifest entry. Determine whether this is possible, and if so report one valid set of entries.

## Input

The first line contains two integers **k** and **t** (1 ≤ k ≤ 1200, 0 ≤ t ≤ k·k): the number of items per category and the number of cleared entries.
Each of the next **t** lines contains three integers **u**, **v**, **w** (1 ≤ u, v, w ≤ k), representing a cleared entry. No entry is listed more than once. For each container, every listed entry uses the same RFID tag, and different containers use different RFID tags.

## Output

If a valid selection of **k** manifest entries exists, print `YES` on the first line, then print **k** lines, each containing the three items `u v w` of one chosen entry (in any order). Any valid selection is accepted.

If no valid selection exists, print `NO`.

## Examples

### Example 1

**Input**
```
2 3
1 1 1
1 1 2
2 2 2
```

**Output**
```
YES
1 1 1
2 2 2
```

### Example 2

**Input**
```
2 2
1 1 1
2 2 1
```

**Output**
```
NO
```

### Example 3

**Input**
```
1 1
1 1 1
```

**Output**
```
YES
1 1 1
```

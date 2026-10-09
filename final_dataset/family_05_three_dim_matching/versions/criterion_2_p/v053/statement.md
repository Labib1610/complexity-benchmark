# Problem B — Port Manifest

Time limit: 2 s
Memory limit: 256 MB

## Description

A modern automated port handles a vast space of potential shipping logistics. The port authority must finalize a set of exactly **k** shipping manifests. The operation involves three distinct pools of assets, each containing exactly **k** items:
- **k** shipping containers, numbered 1 to **k**,
- **k** RFID tags, numbered 1 to **k**,
- **k** cargo vessels, numbered 1 to **k**.

A single valid manifest entry is defined as a triplet consisting of one container, one RFID tag, and one cargo vessel. The port's automated clearance system has generated a list of **t** cleared entries, represented as `(u, v, w)`. 

Your objective is to search through the **t** available entries and select exactly **k** of them. This selection must satisfy a strict simultaneous coverage constraint: across the **k** chosen entries, every container, every RFID tag, and every cargo vessel must be used exactly once. With **t** potentially as large as **k**², the number of possible **k**-sized subsets is astronomical. You must determine if a valid subset exists, navigating this massive search space to find a complete three-way configuration.

The port's hardware dictates that each shipping container is permanently affixed with exactly one RFID tag, and no two containers share the same tag. 

If a valid configuration exists, report the chosen entries.

## Input

The first line contains two integers **k** and **t** (1 ≤ **k** ≤ 1200, 0 ≤ **t** ≤ **k**·**k**): the number of items per asset category and the total number of cleared entries.

Each of the next **t** lines contains three integers **u**, **v**, and **w** (1 ≤ **u**, **v**, **w** ≤ **k**), describing a cleared entry comprising container **u**, RFID tag **v**, and cargo vessel **w**. No entry is listed more than once. For each container, every listed entry uses the same RFID tag, and different containers use different RFID tags.

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

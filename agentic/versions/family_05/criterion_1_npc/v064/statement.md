# Problem A — Precision Lens Production

Time limit: 5 s   Memory limit: 256 MB

## Description

A manufacturing facility must fulfill a daily quota of exactly **k** precision lenses. The facility is equipped with exactly **k** technicians, **k** calibration rigs, and **k** inspection windows, with each resource numbered from 1 to **k**. Producing one lens requires the assignment of one technician, one rig, and one window.

Only certain specific combinations of a technician, a rig, and a window are certified to work together. You will receive the list of all certified combinations.

To meet the quota without resource conflicts, you must select exactly **k** of these certified combinations so that every technician, every calibration rig, and every inspection window is utilized in exactly one selected combination. Determine if such a production schedule is possible, and if it is, output the chosen combinations.

## Input

The first line contains two integers **k** and **t** (1 ≤ k ≤ 22, 0 ≤ t ≤ k·k·k), representing the quota (which equals the number of each resource) and the total number of certified combinations.
Each of the following **t** lines contains three integers **x**, **y**, and **z** (1 ≤ x, y, z ≤ k), indicating a certified combination of technician **x**, calibration rig **y**, and inspection window **z**. No combination is repeated in the input.

## Output

If a valid schedule exists, print `YES` on the first line. Then, print **k** lines, each containing three integers `x y z` representing the technician, rig, and window for one selected combination. Any valid schedule meeting the requirements is acceptable; you may print the combinations in any order.

If no such schedule can be formed, print `NO`.

## Examples

### Example 1

**Input**
```
2 3
1 1 1
1 2 2
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
2 1 2
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

## Note

In Example 2, both certified combinations require calibration rig 1. It is impossible to utilize calibration rig 2, meaning exactly 2 lenses cannot be produced.

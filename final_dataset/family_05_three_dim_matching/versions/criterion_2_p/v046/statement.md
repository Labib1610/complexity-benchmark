# Cargo Flight Dispatch

Time limit: 2 s   Memory limit: 256 MB

## Description

A freight company needs to execute exactly **k** deliveries today. The company has **k** pilots (numbered 1 through k), **k** aircraft (numbered 1 through k), and **k** departure windows (numbered 1 through k).

Each pilot is certified to operate exactly one specific aircraft, and each aircraft is assigned to exactly one pilot. The aviation authority provides a list of approved flight clearances. Each clearance specifies a pilot, their assigned aircraft, and a departure window they are allowed to use. 

To complete the daily schedule, the company must select exactly **k** clearances from the approved list. A valid daily schedule must ensure that every pilot flies exactly once, every aircraft is used exactly once, and every departure window is utilized exactly once. Determine if a valid schedule can be formed, and if so, provide one.

## Input

The first line contains two integers **k** and **t** (1 ≤ k ≤ 1200, 0 ≤ t ≤ k·k), representing the number of deliveries needed and the total number of approved clearances.

Each of the following **t** lines contains three integers **p**, **a**, and **w** (1 ≤ p, a, w ≤ k), representing an approved clearance for pilot **p**, aircraft **a**, and departure window **w**. No clearance is listed more than once. For each pilot, every listed clearance uses the same aircraft, and different pilots use different aircraft.

## Output

If a valid schedule exists, output `YES` on the first line, then print **k** lines, each containing the three integers `p a w` of one selected clearance (in any order). Any valid schedule is accepted.

If no valid schedule is possible, output `NO`.

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

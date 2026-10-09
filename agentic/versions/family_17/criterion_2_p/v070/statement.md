# Phase-Locked Loop Calibration

Time limit: 2 s   Memory limit: 256 MB

## Description
An array of $2q$ oscillators must be fully synchronized for a calibration test. The array is strictly divided into two operational tiers: oscillators $1$ through $q$ operate as frequency references, while oscillators $q+1$ through $2q$ operate as phase trackers.

Synchronization is achieved by locking a reference oscillator to a phase tracker. This lock can only be established if the specific pair is hardware-compatible; a list of all compatible pairs is provided.

For the calibration test to proceed, the system must be configured such that every single oscillator—across both tiers—is involved in exactly one locked pair. No oscillator may remain unlocked, and no oscillator may be locked to more than one partner. Determine whether such a complete configuration exists. If it does, output the pairs to be locked; if it cannot be achieved, indicate that the calibration must be aborted.

## Input
The first line contains two integers $q$ and $t$ ($1 \le q \le 100000$, $0 \le t \le 400000$), where $q$ dictates the number of oscillators in each tier, and $t$ is the number of compatible pairs.
Each of the following $t$ lines contains two integers $a$ and $b$ ($1 \le a \le q < b \le 2q$), denoting that reference oscillator $a$ and phase tracker $b$ are hardware-compatible.

## Output
If a complete configuration is possible, print `YES` on the first line, followed by $q$ lines, each containing the two oscillator identifiers for a locked pair. If multiple configurations are valid, any one may be printed. If no such configuration exists, print `NO`.

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

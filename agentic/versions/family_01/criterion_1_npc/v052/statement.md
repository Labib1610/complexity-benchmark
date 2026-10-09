# Problem A — Quantum Sensor Calibration

Time limit: 2 s
Memory limit: 256 MB

An array of $n$ distributed sensors must be calibrated by assigning each one to exactly one of three available quantum frequencies, designated as 1, 2, and 3. 

Because of spatial entanglement, specific pairs of sensors are known to exhibit phase resonance. The operational rule for the array is strict: if any two phase-resonant sensors are configured to operate on the same frequency, their signals destructively cancel, causing a system fault. 

You are given the total number of sensors and the exhaustive list of all phase-resonant pairs. Determine a complete calibration profile that assigns a frequency to every sensor such that no system fault occurs, or report that no such configuration is possible.

## Input
The first line provides two integers $n$ and $m$ — the number of sensors and the number of phase-resonant pairs ($1 \le n \le 40$, $0 \le m \le n \cdot (n-1)/2$).
Each of the subsequent $m$ lines contains two integers $u$ and $v$ ($1 \le u, v \le n$), indicating that sensor $u$ and sensor $v$ are phase-resonant.

## Output
If no valid calibration profile can be established, output a single line containing `NO`.
Otherwise, output `YES` on the first line. On the second line, output $n$ integers $f_1, f_2, \dots, f_n$ (where each $f_i \in \{1, 2, 3\}$), representing the frequency assigned to sensor $i$. If multiple valid profiles exist, any of them will be accepted.

## Example 1
Input:
```
4 5
1 2
1 3
2 3
1 4
2 4
```
Output:
```
YES
1 2 3 3
```

## Example 2
Input:
```
4 6
1 2
1 3
1 4
2 3
2 4
3 4
```
Output:
```
NO
```

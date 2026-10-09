# Satellite Sensor Configuration

Time limit: 1 s
Memory limit: 256 MB

## Description
A satellite array contains $n$ configurable sensors.
Each sensor must be assigned exactly one operating mode: high-gain (represented by 1) or low-gain (represented by 0).
The thermal control system lists $m$ safety requirements.
A safety requirement specifies two target sensor modes.
Every requirement mandates that at least one of its two target modes is active.
Determine whether a single system-wide configuration exists that fulfills all safety requirements simultaneously.

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 10^5$, $0 \le m \le 2 \cdot 10^5$), representing the number of sensors and the number of safety requirements.
Each of the next $m$ lines contains two non-zero integers $l_1$ and $l_2$ ($1 \le |l_i| \le n$).
An integer $l_i > 0$ specifies that sensor $l_i$ is in the high-gain state.
An integer $l_i < 0$ specifies that sensor $|l_i|$ is in the low-gain state.
Each line represents one safety requirement where at least one of the two specified states must be active.

## Output
If no valid configuration exists, print a single line `NO`.
Otherwise, print `YES` on the first line. On the second line, print $n$ integers $s_1, s_2, \dots, s_n$ (each in $\{0, 1\}$) forming any valid configuration, where $s_i$ is the mode of sensor $i$.

## Example 1
Input:
```
2 2
1 2
-1 -2
```
Output:
```
YES
1 0
```

## Example 2
Input:
```
1 2
1 1
-1 -1
```
Output:
```
NO
```

## Note
Multiple valid configurations may exist; any one is accepted. The same sensor may appear in multiple requirements, and a single requirement may specify the same sensor twice.

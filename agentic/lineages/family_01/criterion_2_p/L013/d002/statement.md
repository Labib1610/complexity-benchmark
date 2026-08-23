# Magnetic Resonance Equilibrium

Time limit: 1 s
Memory limit: 256 MB

A high-energy particle accelerator consists of $n$ magnetic containment fields. The operational state of each field is controlled by a calibration dial, which must be locked to a setting of either 1 or 2.

To prevent cascading failures, the accelerator employs $m$ interference monitors. Each monitor bridges exactly two specific fields. A monitor continuously evaluates the cross-interference between its two assigned fields by computing the bitwise AND of their calibration settings. The containment grid remains stable if and only if every monitor registers a computed result of exactly 0. If any monitor evaluates to a non-zero value (1 or 2), the safety mechanism triggers an immediate system halt.

Your task is to determine whether a valid configuration of calibration settings exists for all $n$ fields that keeps the entire grid stable. Because the control systems are deterministic, if multiple safe configurations are possible, you must provide the lexicographically smallest sequence of settings (meaning the sequence $s_1, s_2, \dots, s_n$ is minimized element by element, from the first field to the last).

## Input
The first line provides two integers $n$ and $m$ ($1 \le n \le 2 \cdot 10^5$, $0 \le m \le 2 \cdot 10^5$).
Each of the subsequent $m$ lines contains two integers $u$ and $v$, indicating that an interference monitor bridges field $u$ and field $v$.

## Output
If it is impossible to configure the dials without causing a system halt, output a single line containing `NO`.
Otherwise, output `YES` on the first line. On the second line, output $n$ integers $s_1, \dots, s_n$ (each being 1 or 2) representing the lexicographically smallest stable configuration.

## Example 1
Input:
```
4 4
1 2
2 3
3 4
1 4
```
Output:
```
YES
1 2 1 2
```

## Example 2
Input:
```
3 3
1 2
1 3
2 3
```
Output:
```
NO
```
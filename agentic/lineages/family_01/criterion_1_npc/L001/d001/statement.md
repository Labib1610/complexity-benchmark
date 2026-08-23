# Problem A — Acoustic Levitation Calibration

Time limit: 2 s   Memory limit: 256 MB

An acoustic levitation array consists of $n$ ultrasonic transducers, numbered $1$ to $n$. To manipulate delicate samples in mid-air, each transducer must be configured to operate in one of three phase modes, represented by the integers 1, 2, and 3.

The geometry of the levitation chamber creates $m$ distinct interference zones. Each zone is exposed to the direct emissions of exactly two specific transducers. If the two transducers overlapping in an interference zone are set to the identical phase mode, the resulting acoustic resonance will destabilize and destroy the sample. Consequently, any two transducers that share an interference zone must be configured with distinct phase modes.

Your task is to determine a safe phase mode configuration for all $n$ transducers. Because the array's controller firmware loads the configuration sequentially, it requires a deterministic setup: if there are multiple safe configurations, you must provide the one that is lexicographically smallest (comparing the mode of transducer 1 first, then transducer 2, and so on). If there is no way to configure the transducers without causing destructive resonance in at least one interference zone, the calibration sequence must be aborted.

## Input
The first line contains two integers $n$ and $m$ — the number of transducers and the number of interference zones ($1 \le n \le 40$, $0 \le m \le n(n-1)/2$).
Each of the next $m$ lines contains two integers $u$ and $v$ — representing the two transducers that emit into a shared interference zone ($1 \le u, v \le n$, $u \neq v$).

## Output
If the calibration must be aborted because no safe configuration is possible, print a single line containing `NO`.
Otherwise, print `YES` on the first line. On the second line, print $n$ integers $c_1, c_2, \dots, c_n$ (where each $c_i \in \{1, 2, 3\}$), representing the phase mode of transducer $i$. Among all valid configurations, output the lexicographically smallest sequence.

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
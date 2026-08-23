# Problem B — Harmonic Resonance

Time limit: 1 s
Memory limit: 256 MB

An acoustic testing facility contains $n$ sound emitters. Each emitter must be assigned a frequency multiplier chosen from the set $\{1, 2\}$.

The facility also includes $m$ interference detectors. Each detector monitors a specific pair of emitters. For a detector to register a stable harmonic, the product of the frequency multipliers of the two emitters it monitors must be exactly 2. If this condition is not met, the detector registers a dissonance.

Your task is to determine whether it is possible to assign a frequency multiplier to every emitter such that all $m$ detectors register a stable harmonic simultaneously.

## Input
The first line provides two integers $n$ and $m$ ($1 \le n \le 2 \cdot 10^5$, $0 \le m \le 2 \cdot 10^5$).
Each of the following $m$ lines contains two integers $u$ and $v$, indicating that an interference detector monitors emitter $u$ and emitter $v$.

## Output
If it is impossible to achieve a state where all detectors register a stable harmonic, output a single line containing NO.
Otherwise, output YES on the first line. On the second line, output $n$ integers $f_1 \dots f_n$ (where each $f_i \in \{1, 2\}$), representing the lexicographically smallest valid sequence of frequency multipliers.

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
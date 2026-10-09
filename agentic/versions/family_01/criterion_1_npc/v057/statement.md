# Acoustic Levitation Arrays

Time limit: 2 s   Memory limit: 256 MB

A complete acoustic levitation sequence consists of three stages: spatial calibration, phase assignment, and amplitude modulation. You are responsible for implementing the second stage.

During the first stage, the system scans the $n$ acoustic emitters and maps their geometry. This spatial calibration generates a list of $m$ specific pairs of emitters that have overlapping focal points.

Your software module must now perform the phase assignment stage. Each emitter must be programmed with exactly one of three available phase offset codes: 1, 2, or 3. If two emitters share a focal point and are assigned the exact same phase offset, their acoustic waves will perfectly synchronize. This causes a resonance spike that will shatter the levitated sample. Therefore, your module must guarantee that any two emitters with an overlapping focal point receive distinct phase offsets.

If your module successfully assigns a safe phase sequence, the sequence is passed to the third stage, where amplitude modulation calculates the precise power levels for each emitter. If your module determines that no safe phase assignment is possible for the given geometry, the entire sequence must abort.

Given the focal point overlap data from the first stage, determine if a safe phase assignment exists, and if so, output one valid configuration to feed into the third stage.

## Input
The first line contains two integers $n$ and $m$ — the number of emitters and the number of overlapping focal points identified during spatial calibration ($1 \le n \le 40$, $0 \le m \le n(n-1)/2$).
Each of the next $m$ lines contains two integers $u$ and $v$, indicating that emitter $u$ and emitter $v$ share a focal point.

## Output
If the geometry forces an unsafe configuration, print a single line NO.
Otherwise, print YES on the first line. On the second line print $n$ integers $p_1, p_2, \dots, p_n$ (each in $\{1, 2, 3\}$), where $p_i$ is the phase offset assigned to emitter $i$. If multiple valid phase assignments exist, any valid sequence may be passed to the next stage.

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

# Problem A — Harmonic Grid Calibration

Time limit: 2 s
Memory limit: 256 MB

A quantum communication grid is composed of $n$ active signal emitters, identified by integers from 1 up to $n$. The installation is physically constrained to a maximum of 40 emitter bays. 

During the initialization phase, every emitter must be calibrated with a specific tuning frequency. The available frequency parameters are exactly 1, 2, and 3.

The grid utilizes $m$ direct transmission conduits, which can range in quantity from 0 up to $n(n-1)/2$ (the theoretical maximum where all distinct pairs are connected). Each conduit links exactly two emitters. To maintain stability, there is a critical safety threshold: whenever two emitters $u$ and $v$ are linked by a conduit, their interference factor $I(u, v)$ must not be a multiple of 3. The interference factor is defined as:
$$ I(u, v) = p_u^2 + p_u \cdot p_v + p_v^2 $$
where $p_u$ and $p_v$ are the selected tuning frequencies of emitters $u$ and $v$ respectively. If $I(u, v)$ evaluates to a multiple of 3 on any conduit, a resonance cascade will occur. Your task is to find a frequency calibration for all $n$ emitters that avoids a cascade.

Should the grid be impossible to safely initialize, your program must report this failure. Given that multiple stable calibrations might exist, the system demands the specific calibration that minimizes the final grid potential $V_n$. The potential of a calibration sequence is evaluated sequentially as follows:
- $V_1 = p_1$
- $V_k = 4 \cdot V_{k-1} + p_k$ for $k = 2, 3, \dots, n$

## Input
The first line provides two integers $n$ and $m$ (1 ≤ $n$ ≤ 40, 0 ≤ $m$ ≤ $n(n−1)/2$) — the number of active emitters and the number of active conduits.
The following $m$ lines each provide two integers $u$ and $v$ (1 ≤ $u, v$ ≤ $n$, $u \neq v$), indicating the identifiers of two emitters connected by a conduit.

## Output
If it is impossible to initialize the grid without causing a resonance cascade, output a single line containing `NO`.
If a valid calibration sequence exists, output `YES` on the first line. On the second line, output $n$ integers $p_1, p_2, \dots, p_n$ (where each $p_i \in \{1, 2, 3\}$), representing the assigned frequency for each emitter from 1 to $n$. This sequence must be the one that minimizes the final grid potential $V_n$.

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
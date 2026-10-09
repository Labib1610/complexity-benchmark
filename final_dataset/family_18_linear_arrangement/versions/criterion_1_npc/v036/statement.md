# Problem A — Calibration Rail Setup

Time limit: 5 s
Memory limit: 256 MB

## Description
A testing facility needs to calibrate $n$ newly manufactured instruments. These instruments must be mounted onto a single straight calibration rail containing exactly $n$ evenly spaced brackets. Every instrument occupies exactly one bracket, leaving no bracket empty.

During calibration, certain pairs of instruments must share a continuous data feed. A physical cable must be routed along the rail to connect each such pair. The brackets are sequentially numbered from $1$ to $n$ and spaced one meter apart, meaning a cable connecting an instrument at bracket $i$ and one at bracket $j$ requires exactly $|i - j|$ meters of cabling.

The facility has a total stock of $B$ meters of cabling available for this setup. All required pairs must be connected simultaneously without exceeding this stock. Determine if a valid bracket assignment exists, and if so, provide the assignment for each instrument.

## Input
The first line contains three integers $n$, $m$, and $B$.
Each of the following $m$ lines contains two integers $x$ and $y$, indicating that instrument $x$ and instrument $y$ require a data feed. Instruments are numbered from $1$ to $n$.

## Output
If the setup is possible, print `YES` on the first line. On the second line, print $n$ integers separated by spaces, where the $k$-th integer represents the bracket number (from $1$ to $n$) assigned to instrument $k$.
If it is impossible, print `NO`.

## Example

### Input
```
4 3 4
1 2
1 3
1 4
```

### Output
```
YES
2 1 3 4
```

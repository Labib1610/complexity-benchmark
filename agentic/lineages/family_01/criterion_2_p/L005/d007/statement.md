# Problem B — Power Calibration

Time limit: 1 s
Memory limit: 256 MB

An industrial facility operates a network of $n$ automated machines. Each machine must be calibrated to a power mode of either 1 or 2.

The facility's safety system has identified $m$ critical pairs of machines. These pairs share a power bus, and their modes must be carefully balanced to prevent surges. 

For any critical pair with assigned modes $x$ and $y$, the pair's resonance factor is defined as $x^3 + y^3$. The total system resonance is the product of the resonance factors of all $m$ critical pairs. 

To comply with the safety protocol and prevent dangerous harmonic cascades, the total system resonance must be exactly $9^m$. 

Your task is to find a calibration for all $n$ machines that satisfies this requirement, or determine that no such calibration exists.

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 2\cdot 10^5$, $0 \le m \le 2\cdot 10^5$), representing the number of machines and the number of critical pairs, respectively.
Each of the next $m$ lines contains two integers $u$ and $v$ ($1 \le u, v \le n$), indicating a critical pair of machines. Machines are numbered from $1$ to $n$.

## Output
If it is impossible to safely calibrate the machines, print NO on a single line.
Otherwise, print YES on the first line. On the second line, print $n$ integers $c_1, c_2, \dots, c_n$ (where each $c_i \in \{1, 2\}$) representing the lexicographically smallest valid calibration.

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
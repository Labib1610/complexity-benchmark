# Problem B — Spectral Alignment Constraints

Time limit: 1 s   Memory limit: 256 MB

## Description

A research facility operates $n$ quantum emitters. Each emitter $i$ must be calibrated with a binary state $s_i \in \{0, 1\}$.

The facility's containment grid is maintained by $m$ interference monitors. Each monitor receives signals from exactly two channels, defined in the system by two non-zero integers $c_1$ and $c_2$. 

A channel specified by a value $c$ extracts a state parameter $v$ based on emitter $|c|$:
- If $c > 0$, the parameter is $v = s_{|c|}$.
- If $c < 0$, the parameter is $v = 1 - s_{|c|}$.

Inside the monitor, the two received parameters $v_1$ and $v_2$ are used to generate two linear wave functions over the spatial domain $x \in [0, 1]$:
$$f_1(x) = x + 2v_1 - 1$$
$$f_2(x) = x + 2v_2 - 1$$

The monitor computes the resonance integral $I$ by integrating their product over the unit interval:
$$I = \int_{0}^{1} f_1(x) f_2(x) \, dx$$

A critical instability occurs if the resonance integral evaluates to exactly $1/3$. If this happens in any of the $m$ monitors, the containment grid collapses.

You must determine if there is a calibration sequence $s_1, \dots, s_n$ for the $n$ emitters such that every monitor remains stable (i.e., $I \neq 1/3$ for all monitors). If such a sequence exists, output the required states.

## Input
The first line of the input provides two integers $n$ and $m$ ($1 \le n \le 10^5$, $0 \le m \le 2 \cdot 10^5$), representing the number of emitters and the number of monitors, respectively.

The next $m$ lines each contain two non-zero integers $c_1$ and $c_2$ ($|c_i| \le n$), representing the two channels for that monitor. 

## Output
If it is impossible to configure all $n$ emitters without collapsing the grid, output a single line with the word `NO`.

If a stable configuration is possible, print `YES` on the first line. On the second line, print $n$ space-separated integers $s_1, s_2, \dots, s_n$ (where each $s_i \in \{0, 1\}$) to specify the chosen state for each emitter from 1 to $n$.

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
There might be several stable configurations; outputting any valid one is correct. A single emitter can connect channels to multiple monitors.
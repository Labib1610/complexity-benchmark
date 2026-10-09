# Problem B — Frequency Filter Tuning

Time limit: 1 s   Memory limit: 256 MB

## Description

A radio facility contains **n** transmitters. Each transmitter must be tuned to a frequency of either 0 MHz or 1 MHz. 
The facility is equipped with **m** filters to prevent interference. Each filter monitors a pair of transmitters, specified by two non-zero integers $l_1$ and $l_2$. 

The absolute value $|l_i|$ identifies which transmitter is being monitored. The sign of $l_i$ defines the polarity $s_i$ of that connection: $s_i = 1$ if $l_i > 0$, and $s_i = -1$ if $l_i < 0$.

For a given tuning of the transmitters, each filter calculates a structural integrity score. Let $v_1$ and $v_2$ be the actual tuned frequencies (0 or 1) of the transmitters monitored by the first and second connections, respectively. The filter calculates a bias $B$ and a raw signal $R$ as follows:
- The bias is $B = \frac{s_1 + s_2}{2}$.
- The raw signal is $R = v_1 s_1 + v_2 s_2$.

A filter operates stably if and only if its raw signal is greater than or equal to its bias ($R \ge B$). If $R < B$, a system fault occurs.

You must determine whether there exists a single global tuning of all **n** transmitters (each set to 0 or 1) such that all **m** filters operate stably simultaneously. If such a tuning exists, report one; otherwise, report that the filter requirements are mutually contradictory.

## Input
The first line contains two integers **n** and **m** (1 ≤ n ≤ 10^5, 0 ≤ m ≤ 2·10^5).
Each of the next **m** lines contains two non-zero signed integers $l_1$ and $l_2$. For each integer, $1 \le |l_i| \le n$. 
The two integers in a filter may have the same absolute value (meaning the filter monitors the same transmitter twice, potentially with the same or opposite signs).

## Output
If no valid tuning exists, print a single line `NO`.
Otherwise, print `YES` on the first line. On the second line, print **n** integers $f_1 \ f_2 \dots f_n$ (each in {0, 1}) forming any valid tuning, where the $i$-th integer represents the frequency of transmitter $i$.

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
Multiple valid tunings may exist; any one is accepted. The same transmitter may appear in multiple filters, and even twice within the same filter.
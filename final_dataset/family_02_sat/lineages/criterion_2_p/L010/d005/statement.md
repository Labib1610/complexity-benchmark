# Problem B — Frequency Filter Tuning

Time limit: 1 s   Memory limit: 256 MB

## Description

A radio facility contains **n** transmitters. Each transmitter must be tuned to a base frequency of either 0 MHz or 1 MHz. 
The facility is equipped with **m** filters to prevent interference. Each filter monitors a pair of transmitters, specified by two non-zero integers $l_1$ and $l_2$. 

The absolute value $|l_i|$ identifies which transmitter is being monitored. The sign of $l_i$ establishes a target frequency for that connection: a positive sign sets a target of 1 MHz, while a negative sign sets a target of 0 MHz.

For a given tuning of the transmitters, each filter calculates a combined deviation. The deviation for a single connection is the absolute difference between the transmitter's actual tuned frequency (in MHz) and its target frequency (in MHz). The filter's combined deviation is the sum of the deviations of its two connections.

A filter operates stably if and only if its combined deviation is strictly less than 2 MHz. If the combined deviation reaches 2 MHz, a system fault occurs.

You must determine whether there exists a single global tuning of all **n** transmitters (each set to 0 or 1) such that all **m** filters operate stably simultaneously. If such a tuning exists, report one; otherwise, report that the filter requirements are mutually contradictory.

## Input
The first line contains two integers **n** and **m** (1 ≤ n ≤ 10^5, 0 ≤ m ≤ 2·10^5).
Each of the next **m** lines contains two non-zero signed integers $l_1$ and $l_2$. For each integer, $1 \le |l_i| \le n$. 
The two integers in a filter may have the same absolute value (meaning the filter monitors the same transmitter twice, potentially with the same or opposite signs).

## Output
If no valid tuning exists, print a single line `NO`.
Otherwise, print `YES` on the first line. On the second line, print **n** integers $s_1 \ s_2 \dots s_n$ (each in {0, 1}) forming any valid tuning, where the $i$-th integer represents the frequency of transmitter $i$.

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
# Problem A — Orbital Network Frequency Coordination

Time limit: 2 s   Memory limit: 256 MB

An aerospace consortium is preparing the initialization profile for $n$ orbital uplink stations, numbered $1$ through $n$. Each station must be assigned a frequency value from the set $\{1, 2, 3\}$.

Spatial analysis has identified $m$ pairs of stations whose broadcast footprints intersect. For each listed pair, the two stations must receive different frequencies to avoid interference.

A complete profile is a sequence of $n$ frequencies, where the $i$-th value is the frequency allocated to station $i$. The consortium evaluates all interference-free profiles. If the set of valid profiles is empty, the deployment cannot proceed. 

Otherwise, the system must select the single valid profile that minimizes the sequence. When comparing two valid profiles, the system checks the frequencies starting from index 1 onward, and chooses the profile with the smaller frequency at the first station index where they differ.

## Input
The first line contains two integers $n$ and $m$ — the number of uplink stations and the number of intersecting footprint pairs ($1 \le n \le 40$, $0 \le m \le n(n-1)/2$).
Each of the next $m$ lines contains two integers $u$ and $v$ — representing a pair of stations that have intersecting footprints and must use different frequencies.

## Output
If no interference-free profile exists, print a single line containing `NO`.
Otherwise, print `YES` on the first line. On the second line, print $n$ integers $f_1, f_2, \dots, f_n$ (where each $f_i \in \{1, 2, 3\}$), representing the frequency allocated to station $i$. Output the profile that is minimized according to the tie-break rule described above.

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
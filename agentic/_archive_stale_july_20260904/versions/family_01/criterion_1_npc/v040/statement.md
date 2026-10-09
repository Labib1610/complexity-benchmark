# Problem A — Orbital Frequency Configuration

Time limit: 2 s   Memory limit: 256 MB

The preliminary phase of a satellite deployment mission has concluded. Orbital mechanics analysts have finalized the launch trajectories for $n$ satellites. During this analysis, they identified specific pairs of trajectories that will bring the respective satellites into close proximity. If two such satellites transmit on the same frequency band, their signals will interfere.

Your module handles the next phase: frequency configuration. The communications hardware supports operation on any of the bands designated 1, 2, and 3. Your task is to assign each of the $n$ satellites to exactly one of these bands such that no two satellites with close-proximity trajectories share a band.

If an assignment cannot be found, the launch must be delayed. If it can, your output will be passed directly to the automated upload system, which programs the satellites sequentially. To maintain standardized firmware states, the upload system mandates a specific prioritization: among all valid band assignments, you must provide the one where the band number for the first satellite is as small as possible; if there are still multiple valid assignments, minimize the band number for the second satellite, and so on through the $n$-th satellite.

## Input
The first line contains two integers $n$ and $m$ — the number of satellites and the number of close-proximity pairs ($1 \le n \le 40$, $0 \le m \le n \cdot (n-1)/2$).
Each of the following $m$ lines provides two integers $u$ and $v$, indicating that the trajectories of satellite $u$ and satellite $v$ will cause them to approach too closely.

## Output
If there is no way to assign the bands without interference, print `NO` on a single line.
Otherwise, print `YES` on the first line. On the second line, print $n$ integers $s_1, s_2, \dots, s_n$ (each being 1, 2, or 3), where $s_i$ is the band assigned to satellite $i$. This sequence must satisfy the upload system's prioritization rule mentioned above.

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

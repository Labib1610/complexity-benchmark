# Problem A — Orbital Telemetry Pipeline

Time limit: 2 s   Memory limit: 256 MB

The orbital mapping pipeline operates in three distinct stages to ensure stable telemetry from a constellation of $n$ satellites. 

**Stage A: Calibration.** The system registers the satellites and conducts signal diagnostics. This stage has already been completed. Its output is a log of $m$ satellite pairs whose transmission beams overlap and cause cross-talk.

**Stage B: Frequency Allocation (Your Module).** You must process the diagnostic log from Stage A to configure the communications array. The array hardware supports exactly three distinct frequency bands, designated 1, 2, and 3. Your module must assign every satellite to exactly one frequency band. To guarantee data integrity, no two satellites flagged for cross-talk in Stage A may be assigned the same frequency band. 

**Stage C: Initialization.** The satellites boot up and begin transmission using your configuration. The boot sequence is fully deterministic: if multiple valid allocations exist, your module must provide the one that is lexicographically first. That is, it must minimize the frequency band assigned to satellite 1; if there are ties, it must minimize the band for satellite 2, and so on. If no valid allocation can be found, your module must halt the pipeline.

Write the software for Stage B.

## Input
The first line of the input contains two integers $n$ and $m$ — the number of satellites and the number of cross-talk pairs (1 ≤ $n$ ≤ 40, 0 ≤ $m$ ≤ $n \cdot (n-1)/2$). 
Each of the following $m$ lines contains two integers $u$ and $v$ — a pair of satellites that experience cross-talk.

## Output
If the pipeline must be halted because no valid frequency allocation exists, print a single line containing `NO`. 
Otherwise, print `YES` on the first line. On the second line, print $n$ integers $f_1, f_2, \dots, f_n$ (each in $\{1, 2, 3\}$), where $f_i$ is the frequency band assigned to satellite $i$. Remember to output the lexicographically smallest valid sequence.

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

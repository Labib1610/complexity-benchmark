# Problem A — Harmonizing the Celestial Chorus

Time limit: 5 s
Memory limit: 256 MB

## Description
A grand celestial chorus must be performed to avert a cosmic anomaly. The chorus consists of $n$ distinct melodic verses. The performance spans a sequence of celestial phases. 

The ensemble consists of $M$ master vocalists. Each verse requires the undivided breath and focus of exactly one vocalist for an entire phase. The headcount of your ensemble thus imposes a strict physical limit on the number of verses that can be sung concurrently during any single phase.

Furthermore, the verses are harmonically entangled. Certain verses establish a foundational resonance that others require. If verse $b$ relies on the resonance of verse $a$, the foundational verse $a$ must be performed in an earlier phase than $b$. The celestial ether requires the boundary between phases to carry and settle the resonance; consequently, a foundational verse and its dependent cannot merely be sung by different vocalists in the same phase. 

The cosmic anomaly will strike precisely when the $T$-th phase concludes. Any verse sung after this point will be sung to a shattered world, meaning the entirety of the chorus must be safely concluded by the end of phase $T$. 

Determine a phase for each of the $n$ verses such that the ensemble's capacity is never exceeded, all resonance requirements are satisfied, and the performance concludes before the anomaly strikes. If it is impossible to orchestrate such a performance, you must declare it so.

## Input
The first line contains four integers: $n$, $M$, $T$, and $m$.
Each of the next $m$ lines contains two integers $a$ and $b$, indicating that verse $a$ provides a foundational resonance required by verse $b$. Verses are numbered from $1$ to $n$.

## Output
If a valid performance schedule exists, print `YES` on the first line, followed by a second line containing $n$ space-separated integers. The $i$-th integer must represent the phase (from $1$ to $T$) during which the $i$-th verse is sung. If no such schedule is possible, print `NO`.

## Example

**Input**
```
5 2 3 4
1 2
1 3
2 4
3 5
```

**Output**
```
YES
1 2 2 3 3
```

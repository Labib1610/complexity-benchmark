# Problem A — Mixtape Sequencing

Time limit: 5 s   Memory limit: 256 MB

## Description
A sound engineer is arranging a mixtape consisting of $n$ distinct audio tracks. The tracks must be assigned to $n$ sequential playback slots, numbered $1$ through $n$. Each track occupies exactly one slot, and every slot must contain exactly one track. This means the arrangement is a one-to-one mapping of tracks to playback slots.

Certain pairs of tracks (exactly $m$ such pairs) share a distinct harmonic motif. The listener's experience of a shared motif depends on how far apart the two tracks are placed in the mixtape. Specifically, if one track is placed in slot $x$ and the other is placed in slot $y$, the *resonance gap* for that motif is $|x - y|$.

The engineer has a strict limit on the overall dissonance. The sum of the resonance gaps across all $m$ shared motifs must not exceed a given threshold $B$.

You must determine if there is a valid assignment of tracks to slots that satisfies this condition. If there is, you must provide one; otherwise, report that it is impossible.

## Input
The first line contains three integers $n$, $m$, and $B$ — the number of tracks, the number of shared motifs, and the maximum allowed total resonance gap, respectively.
Each of the following $m$ lines contains two integers $u$ and $v$ ($1 \le u, v \le n$, $u \neq v$), indicating that track $u$ and track $v$ share a harmonic motif.

## Output
If a valid assignment exists, print `YES` on the first line. On the second line, print $n$ space-separated integers. The $i$-th integer must be the playback slot (from $1$ to $n$) assigned to track $i$.
If no such assignment fits the threshold, print `NO`.

## Examples

**Input 1:**
```
4 3 4
1 2
1 3
1 4
```

**Output 1:**
```
YES
2 1 3 4
```

**Input 2:**
```
4 6 9
1 2
1 3
1 4
2 3
2 4
3 4
```

**Output 2:**
```
NO
```

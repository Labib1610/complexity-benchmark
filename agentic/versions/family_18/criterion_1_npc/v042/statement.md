# Problem A — Synthesis Sequence Optimization

Time limit: 5 s
Memory limit: 256 MB

## Description
A pharmaceutical company is designing a new batch protocol involving $n$ distinct chemical reactions (numbered 1 to $n$). The protocol is strictly sequential: it consists of $n$ consecutive operational steps, numbered 1 to $n$. You must assign exactly one reaction to each operational step.

During the process, certain pairs of reactions must share a specialized containment vessel. There are $m$ such pairs. For each pair, a vessel is allocated starting at the step of the reaction that occurs earlier, and it remains occupied until the step of the reaction that occurs later. The duration for which the vessel is occupied is measured by the number of step intervals between the two reactions. Specifically, if the two reactions are scheduled at step $x$ and step $y$, the vessel is occupied for $|x - y|$ units of time.

To minimize contamination risks and degradation, the facility imposes a strict limit on the total time vessels are occupied. The grand total of the occupied durations for all $m$ required vessels must not exceed a safety threshold of $B$ units.

Your task is to determine if there is a valid assignment of reactions to operational steps such that the total vessel occupation time is at most $B$.

## Input
The first line contains three integers $n$, $m$, and $B$ — the number of reactions, the number of vessel-sharing pairs, and the maximum allowed total occupation time.
Each of the following $m$ lines contains two integers $u$ and $v$ ($1 \le u, v \le n$), indicating that reaction $u$ and reaction $v$ must share a containment vessel.

## Output
If a valid sequence can be formed within the time threshold, print `YES` on the first line. On the second line, output $n$ space-separated integers representing your sequence: the $i$-th integer must be the operational step (from 1 to $n$) at which reaction $i$ is executed. If multiple valid sequences exist, you may output any one that respects the threshold.
If no such sequence is possible, print `NO`.

## Example

**Input**
```
4 3 4
1 2
1 3
1 4
```

**Output**
```
YES
2 1 3 4
```

**Note on the Example**
Reaction 1 is scheduled at step 2, reaction 2 at step 1, reaction 3 at step 3, and reaction 4 at step 4.
The vessel occupation times are:
- Between reaction 1 (step 2) and reaction 2 (step 1): duration $|2 - 1| = 1$
- Between reaction 1 (step 2) and reaction 3 (step 3): duration $|2 - 3| = 1$
- Between reaction 1 (step 2) and reaction 4 (step 4): duration $|2 - 4| = 2$
The total duration is $1 + 1 + 2 = 4$, which exactly meets the threshold $B$.

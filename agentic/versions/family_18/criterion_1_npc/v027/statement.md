# Problem A — Synthesis Stabilization

Time limit: 5 s   Memory limit: 256 MB

## Description
An experimental synthesis process requires exactly $n$ distinct chemical catalysts. The process runs for $n$ consecutive minutes, and exactly one catalyst must be introduced into the reactor at the start of each minute. Therefore, the schedule is a one-to-one mapping of catalysts to the minutes $1$ through $n$.

Certain pairs of catalysts are interdependent. When the earlier catalyst of an interdependent pair is introduced, an unstable intermediate compound forms. This intermediate compound degrades by one unit each minute until the later catalyst of the pair is introduced, which stabilizes it. The total degradation caused by a single interdependent pair is simply the number of minutes elapsed between the introduction of its two constituent catalysts. 

The synthesis facility has strict safety margins regarding the accumulation of degraded material. A maximum allowable degradation threshold $B$ is established for the entire process. The total degradation is calculated by summing the degradation amounts from all interdependent pairs. There is no limit on the degradation from any individual pair, nor on how many intermediate compounds can be degrading simultaneously; the safety margin applies only to the grand total.

Determine whether it is possible to schedule the $n$ catalysts—assigning each to a unique minute—such that the total degradation across all interdependent pairs does not exceed the threshold $B$. If a safe schedule exists, provide the minute assigned to each catalyst; otherwise, report that no such schedule is possible.

## Input
The first line contains three integers $n$, $m$, and $B$.  
Each of the next $m$ lines contains two integers $u$ and $v$, indicating that catalyst $u$ and catalyst $v$ form an interdependent pair.

## Output
If a safe schedule exists, print `YES` on the first line. On the second line, print $n$ integers, where the $i$-th integer is the minute ($1 \dots n$) assigned to catalyst $i$. If multiple valid schedules exist, any is acceptable.  
If no such schedule is possible, print `NO`.

## Example

**Input:**
```
4 3 4
1 2
2 3
3 4
```

**Output:**
```
YES
1 2 3 4
```

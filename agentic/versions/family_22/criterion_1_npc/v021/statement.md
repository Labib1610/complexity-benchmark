# Phase-Shift Terraforming

Time limit: 5 s
Memory limit: 256 MB

## Description
You are orchestrating a terraforming operation across $n$ distinct target zones. The operation is carried out in discrete time increments called phases. You have a fleet of $M$ identical atmospheric processors. During any single phase, each processor can treat at most one zone, meaning you can treat a maximum of $M$ zones per phase. 

The planetary council has mandated that the entire operation must be completed within a hard deadline of $T$ phases.

The environment is highly reactive. Certain zones release specific chemical catalysts when treated, which are strictly required to stabilize other zones before they can be processed. If zone $b$ requires the catalyst from zone $a$, then zone $a$ must be treated in a phase strictly prior to the phase in which zone $b$ is treated. Treating them in the same phase will fail, because the catalyst from zone $a$ needs time to disperse and only becomes available at the start of the next phase. 

You do not need to track which specific processor treats which zone, as they are fully interchangeable. Furthermore, processors are reused across phases, so the limit of $M$ zones applies independently to each individual phase. The interplay between the maximum processor capacity per phase and the chains of catalyst requirements will determine if a valid deployment exists.

Your task is to assign each of the $n$ zones to exactly one phase (from 1 to $T$) such that no phase contains more than $M$ zones, and all catalyst requirements are satisfied. If it is impossible to schedule all zones within $T$ phases under these conditions, you must report that it cannot be done.

## Input
The first line contains four integers $n$, $M$, $T$, and $m$.
Each of the next $m$ lines contains two integers $a$ and $b$, indicating that zone $a$ must be treated in a strictly earlier phase than zone $b$.

## Output
If a valid schedule exists, print `YES` followed by $n$ integers. The $i$-th integer must represent the phase (between 1 and $T$) during which zone $i$ is treated. If no such schedule is possible, print `NO`.

## Example 1

### Input
```
5 2 3 4
1 2
1 3
2 4
3 5
```

### Output
```
YES
1 2 2 3 3
```

## Example 2

### Input
```
5 2 3 5
1 2
1 3
2 4
3 5
4 5
```

### Output
```
NO
```

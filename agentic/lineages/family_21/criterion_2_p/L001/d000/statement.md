# Matchday Crowd Control

Time limit: 2 s   Memory limit: 256 MB

## Description
A metropolitan transit authority operates a system of stations joined by direct tram segments. For an upcoming high-risk sports fixture, two specific stations will host rival supporter factions. To guarantee public safety, the authority must ensure there is no sequence of active tram segments connecting these two stations. 

Suspending a tram segment requires deploying a specific number of security personnel to secure the track and redirect regular passengers. The authority has a hard limit on the total number of personnel available for these closures. The status of all other stations is irrelevant to the safety mandate, provided the two designated faction stations cannot reach one another through any combination of active segments.

Determine a set of tram segments to suspend such that the total personnel required does not exceed the available limit, and no travel is possible between the two faction stations. If the personnel limit makes this impossible, report that the stations cannot be separated.

## Input
The first line contains five integers: $n$ (total stations), $m$ (total tram segments), $s$ (the first faction station), $t$ (the second faction station), and $B$ (the personnel limit).
The following $m$ lines each contain three integers $u$, $v$, and $w$, indicating a bidirectional tram segment between station $u$ and station $v$ that requires $w$ personnel to suspend.

## Output
If a valid suspension plan exists, output `YES` on the first line. On the second line, output the number of suspended segments $c$. On each of the next $c$ lines, output two integers $u$ and $v$ representing a suspended segment. If multiple valid plans exist, any plan requiring at most $B$ personnel is acceptable.
If no such plan is possible within the personnel limit, output `NO`.

## Example

### Input
```text
5 6 1 5 10
1 2 4
1 3 5
2 4 6
3 4 3
2 5 3
4 5 4
```

### Output
```text
YES
2
2 5
4 5
```

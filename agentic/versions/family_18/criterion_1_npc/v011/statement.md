# Problem A — Gallery Curation

Time limit: 5 s
Memory limit: 256 MB

## Description
A museum curator is arranging a new exhibition containing $n$ distinct historical artifacts (identified by integers from 1 to $n$). The gallery features a single, long corridor with exactly $n$ display cases aligned in a straight row. The display cases are numbered sequentially from 1 to $n$. Each artifact must be placed into exactly one display case, and every display case must hold exactly one artifact.

To prepare for the exhibition, researchers have submitted $m$ study requests. Each request specifies a pair of artifacts that must be compared. To compare a pair, a researcher must walk between their respective display cases. The walking distance for a single request is exactly the absolute difference between the display case numbers. For example, if one artifact is in case 2 and the other is in case 5, the walking distance for that request is 3. Only the numerical difference between case locations matters for the distance calculation.

The museum administration has set a strict total walking budget for the researchers, denoted by $B$. The grand total of the walking distances across all $m$ requests must not exceed $B$. There is no limit on the distance of any individual request; only the aggregate sum across all $m$ requests matters.

Determine whether the artifacts can be assigned to the display cases so that the total walking distance stays within the budget $B$. If so, output a valid assignment; otherwise, report that no such assignment exists. (An arrangement that minimizes distance for certain requests might drastically increase it for others, so the overall sum is what dictates success.)

## Input
The first line contains three integers $n$, $m$, and $B$ — the number of artifacts (and display cases), the number of study requests, and the maximum allowed total walking distance.
Each of the following $m$ lines contains two integers $u$ and $v$ ($1 \le u, v \le n$), indicating a study request that requires comparing artifact $u$ and artifact $v$.

## Output
If an arrangement exists that satisfies the budget, print `YES` on the first line. On the second line, print $n$ integers representing the display case numbers assigned to artifact 1, artifact 2, ..., artifact $n$. These $n$ integers must form a valid permutation of the numbers 1 to $n$.
If no such arrangement is possible, print `NO`.

## Example 1
### Input
```
4 3 4
1 2
1 3
1 4
```
### Output
```
YES
2 1 3 4
```

## Example 2
### Input
```
4 6 9
1 2
1 3
1 4
2 3
2 4
3 4
```
### Output
```
NO
```

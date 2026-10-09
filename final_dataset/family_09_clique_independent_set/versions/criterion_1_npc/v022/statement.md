# Problem A — Plugin Harmony

Time limit: 5 s
Memory limit: 256 MB

## Description

A software platform supports $n$ optional plugins, numbered 1 through $n$. There are $m$ known compatibility issues, each involving a specific pair of plugins that will crash the system if installed together.

You need to configure a deployment containing exactly $k$ distinct plugins. Each compatibility issue present in your selection adds 1 to the deployment's instability score. Your goal is to find a deployment with an instability score of exactly 0. 

Because the instability score is a simple sum of independent pairwise interactions, and because you only need to find a single valid deployment rather than enumerating all possibilities, the search space can often be navigated efficiently by prioritizing plugins with fewer issues or by iteratively swapping plugins to reduce the score. The interactions are strictly binary and unweighted. Given these structural regularities and the strict system bounds ($n \le 46$), your task is to definitively determine whether a zero-instability deployment of size $k$ exists, and to report one if it does.

## Input

The first line contains three integers $n$, $m$, and $k$ (1 ≤ n ≤ 46, 0 ≤ m ≤ n·(n−1)/2, 1 ≤ k ≤ n).
Each of the following $m$ lines contains two integers $u$ and $v$ (1 ≤ u, v ≤ n, u ≠ v), representing a compatibility issue between plugin $u$ and plugin $v$. No issue is listed more than once.

## Output

If a zero-instability deployment of $k$ plugins exists, print `YES` on the first line. On the second line, print $k$ distinct plugin numbers forming such a deployment, separated by spaces. If multiple such zero-instability deployments exist, any one of them is acceptable.

If no such deployment exists, print `NO`.

## Examples

### Example 1

**Input**
```
4 4 3
1 2
1 3
2 3
3 4
```

**Output**
```
NO
```

### Example 2

**Input**
```
5 2 3
1 2
3 4
```

**Output**
```
YES
1 3 5
```

### Example 3

**Input**
```
3 3 1
1 2
2 3
1 3
```

**Output**
```
YES
1
```

## Note

A zero-instability deployment means no two chosen plugins share a compatibility issue. In Example 2, plugins 1, 3, and 5 have no compatibility issues among them. In Example 1, it is impossible to choose three plugins without including at least one incompatible pair.

# Corporate Consolidation

Time limit: 2 s   Memory limit: 256 MB

## Description

In a regulated market, there are $n$ independent corporations (numbered 1 through $n$) and a set of $m$ proposed bilateral merger agreements. Each agreement involves two specific corporations and requires a defined legal fee to finalize. Whenever an agreement is finalized, the two corporations—along with any affiliates they have previously merged with—consolidate into a single unified conglomerate.

Within this market, a particular group of $t$ corporations are identified as key patent holders. Your goal is to choose a subset of the proposed agreements to finalize such that all $t$ key patent holders are ultimately absorbed into the same conglomerate, and the total legal fee incurred is minimized.

To maintain market equilibrium, the antitrust regulatory board has issued a certificate that enforces strict structural limits on the proposed agreements. The certificate guarantees that for any chosen group of companies, the count of proposed agreements existing exclusively between members of that group is always strictly smaller than the number of companies in the group. Furthermore, the board mandates that the overall count of proposed agreements, $m$, must be exactly $n - 1$.

## Input

The first line contains three integers $n$, $m$, and $t$ ($1 \le t \le n$, $1 \le n \le 200000$).
The second line contains $t$ distinct integers: the identifiers of the key patent holders.
Each of the next $m$ lines contains three integers $u$, $v$, and $w$ ($1 \le u, v \le n$, $u \neq v$, $1 \le w \le 1000000$), representing a proposed agreement between corporation $u$ and corporation $v$ with a legal fee of $w$.

## Output

Print a single integer: the minimum total legal fee required to reach a market state where all key patent holders belong to the same conglomerate.

## Examples

### Example 1

**Input**
```
4 3 2
1 4
1 2 5
2 3 1
3 4 2
```

**Output**
```
8
```

### Example 2

**Input**
```
5 4 1
3
1 2 4
2 3 6
3 4 2
4 5 9
```

**Output**
```
0
```

### Example 3

**Input**
```
3 2 3
1 2 3
1 2 4
2 3 5
```

**Output**
```
9
```

## Note

In Example 1, the key patent holders 1 and 4 are brought into the same conglomerate by finalizing the agreements that merge 1 with 2, 2 with 3, and 3 with 4. The total legal fee is 5 + 1 + 2 = 8. 
In Example 2, there is only one key patent holder, so the required market state is already satisfied and no agreements need to be finalized.
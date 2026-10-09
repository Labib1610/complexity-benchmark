# Problem A — Portfolio Risk Mitigation

Time limit: 2 s   Memory limit: 256 MB

A wealth management firm is structuring a new fund composed of $n$ distinct financial assets. To maintain regulatory compliance, the firm must distribute these assets across three separate investment portfolios, identified as portfolio 1, portfolio 2, and portfolio 3. 

Market analysis has revealed that certain pairs of these assets are critically interlinked. If two interlinked assets are placed into the same portfolio, it creates an unacceptable concentration of risk. Therefore, the firm's strict policy dictates that no two interlinked assets may be assigned to the same portfolio. 

You must assign every single asset to exactly one of the three portfolios such that no two interlinked assets share a portfolio, or determine that this distribution is impossible.

## Input
The first line contains two integers $n$ and $m$ — the total number of financial assets and the number of interlinked asset pairs ($1 \le n \le 40$, $0 \le m \le n(n-1)/2$). The assets are numbered from $1$ to $n$.
Each of the next $m$ lines contains two integers $u$ and $v$ — a pair of assets that are critically interlinked.

## Output
If no valid distribution exists, print a single line NO.
Otherwise print YES on the first line. On the second line print $n$ integers $p_1\ p_2\ \dots\ p_n$ (each in $\{1,2,3\}$), where $p_i$ is the portfolio of asset $i$. Any valid distribution is accepted.

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

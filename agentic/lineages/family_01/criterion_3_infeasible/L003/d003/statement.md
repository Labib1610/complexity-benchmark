# Arbitrage Hedge

Time limit: 2 s   Memory limit: 256 MB

A financial firm is analyzing $n$ market commodities, labeled with integer IDs from 1 to $n$. Through historical data, they have verified $m$ specific exchange parities, each indicating that two particular commodities can be traded directly for one another without slippage.

The quantitative team wants to form a "Hedge Ring". A Hedge Ring is a portfolio consisting of exactly three distinct commodities. To be perfectly hedged, the portfolio must satisfy a strict structural condition: no matter which of the three commodities is selected as the "base asset", the remaining two commodities in the portfolio must be a pair that has a verified exchange parity.

Market conditions guarantee that at least one valid Hedge Ring exists. Your task is to process the parities and identify one such portfolio.

## Input
The first line contains two integers $n$ and $m$ ($3 \le n \le 2000$, $3 \le m \le \min(n(n-1)/2, 2 \cdot 10^5)$).
Each of the next $m$ lines contains two integers $u$ and $v$ — a pair of commodities that have a verified exchange parity.
It is guaranteed that at least one Hedge Ring exists.

## Output
Print three integers $a$, $b$, and $c$ on one line with $a < b < c$ representing the commodities in the Hedge Ring. Output the lexicographically smallest such set (smallest $a$; ties broken by smallest $b$; then smallest $c$).

## Example 1
Input:
```
4 5
1 2
1 3
2 3
2 4
3 4
```
Output:
```
1 2 3
```

## Example 2
Input:
```
5 6
1 2
1 4
2 4
3 4
3 5
4 5
```
Output:
```
1 2 4
```
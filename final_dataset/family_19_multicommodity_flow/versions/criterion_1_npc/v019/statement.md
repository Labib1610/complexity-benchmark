# Interbank Settlement Rebalancing

Time limit: 5 s
Memory limit: 256 MB

## Description
A clearing house manages $n$ financial institutions. There are $m$ established one-way settlement agreements. An agreement from institution $u$ to $v$ allows $u$ to send individual settlement batches to $v$. Due to processing constraints, each agreement has a strict daily ceiling on the total number of batches it can handle, regardless of what currency is being transferred.

Today, there are $k$ different fiat currencies that need rebalancing. For each currency $i$, a central bank initiates exactly $d_i$ batches at a specific institution $s_i$, which must ultimately be absorbed by a specific institution $t_i$.

The institutions themselves do not hold these batches overnight; they merely pass them along. Thus, for any given currency $i$, the number of batches an institution sends out minus the number of batches it receives must equal:
- $d_i$, if the institution is $s_i$ (the origin for currency $i$).
- $-d_i$, if the institution is $t_i$ (the destination for currency $i$).
- $0$, for all other institutions.

The number of batches transferred cannot be negative, and all batches are indivisible whole units. The daily ceiling on any settlement agreement applies to the sum of batches of all $k$ currencies transferred through it.

Determine if there is a valid daily assignment of batches for all currencies such that the required rebalancing is achieved without exceeding the daily ceiling of any settlement agreement.

## Input
The first line contains three integers $n$, $m$, and $k$.
The next $k$ lines each contain three integers $s_i$, $t_i$, and $d_i$, representing the origin institution, destination institution, and required number of batches for currency $i$.
The next $m$ lines each contain three integers $u$, $v$, and $cap$, representing a directed settlement agreement from institution $u$ to institution $v$ with a daily ceiling of $cap$ batches.

## Output
If a valid assignment exists, print `YES` on the first line. Then, output $k$ lines, each containing $m$ integers. The $j$-th integer on the $i$-th line should be the number of batches of currency $i$ transferred through the $j$-th settlement agreement (in the order the agreements are given in the input).
If no such assignment is possible, print `NO`.

## Example

### Input
```
4 5 2
1 4 1
1 3 1
1 2 1
2 4 1
1 3 1
3 4 1
2 3 1
```

### Output
```
YES
1 1 0 0 0
0 0 1 0 0
```

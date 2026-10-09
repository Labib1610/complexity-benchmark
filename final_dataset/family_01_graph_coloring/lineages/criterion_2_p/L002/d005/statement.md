# Tiered Settlement Obligations

Time limit: 1 s   Memory limit: 256 MB

A financial clearinghouse is migrating $n$ institutional accounts to a new regulatory framework. Under this framework, each account must be assigned a compliance tier, strictly designated as either `1` or `2`.

The clearinghouse has identified $m$ reciprocal obligations between specific pairs of accounts. To satisfy risk-margin requirements, any two accounts $u$ and $v$ involved in a reciprocal obligation must be assigned tiers $t_u$ and $t_v$ such that they can form a valid joint supervisory committee. 

The rule for the committee is as follows: it must consist of exactly $t_u$ members chosen from a pool of $t_u + t_v$ distinct delegates. To ensure definitive tie-breaking during audits, the total number of distinct possible ways to choose the members for this committee must be strictly an odd number. (Note that choosing $t_v$ members from the same pool yields the identical number of distinct combinations, so the order of $u$ and $v$ does not matter).

If there is no way to assign tiers to all $n$ accounts such that every reciprocal obligation satisfies this committee rule, the migration must be halted. When multiple valid tier assignments are possible, the compliance protocol mandates selecting the sequence of tier designations (ordered from account 1 to $n$) that is lexicographically smallest.

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 2\cdot 10^5$, $0 \le m \le 2\cdot 10^5$), representing the number of accounts and the number of reciprocal obligations.
Each of the next $m$ lines contains two integers $u$ and $v$ ($1 \le u, v \le n$) — a pair of accounts that share a reciprocal obligation.

## Output
If no valid tier assignment can be found, print `NO` on a single line.
Otherwise, print `YES` on the first line. On the second line, print $n$ integers $s_1 \dots s_n$ (each either `1` or `2`), denoting the compliance tier for accounts 1 through $n$. This sequence must be the lexicographically smallest valid assignment.

## Example 1
Input:
```
4 4
1 2
2 3
3 4
1 4
```
Output:
```
YES
1 2 1 2
```

## Example 2
Input:
```
3 3
1 2
1 3
2 3
```
Output:
```
NO
```
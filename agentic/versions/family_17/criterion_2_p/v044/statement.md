# Full-Coverage Controller/Platform Pairing

Time limit: 2 s   Memory limit: 256 MB

## Description
The directorate's upcoming drill requires selecting a precise operational configuration from an astronomically large space of possibilities. You are given a certification list containing up to 400,000 certified combinations. Your task is to search this space and select a subset of these combinations to form the active roster. Since any combination can either be included or excluded, the theoretical search space of possible configurations is up to $2^{400,000}$.

A configuration is only valid if it achieves full exact coverage without any conflicts. Specifically, the subset of chosen combinations must commit every single asset exactly once. Any configuration that omits an asset or assigns an asset to multiple active combinations is invalid.

The assets are divided into $q$ controllers (numbered $1$ through $q$) and $q$ platforms (numbered $q+1$ through $2q$). Each certified combination in the list consists of two items: one controller and one platform. You must determine if there exists at least one valid subset of combinations that perfectly commits all $2q$ assets, and if so, output the chosen combinations. Otherwise, report that no such configuration exists.

## Input
The first line contains two integers $q$ and $t$ ($1 \le q \le 100000$, $0 \le t \le 400000$).
The next $t$ lines each contain two integers $a$ and $b$ ($1 \le a \le q < b \le 2q$), representing a certified combination of controller $a$ and platform $b$.

## Output
If a valid configuration is possible, print `YES` followed by $q$ lines, each containing the two items of one chosen combination from the active roster. Otherwise, print `NO`.

## Example

**Input**
```text
3 4
1 4
2 5
3 6
1 5
```

**Output**
```text
YES
1 4
2 5
3 6
```

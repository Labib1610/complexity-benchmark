# Problem B — Protocol Implementation

Time limit: 2 s   Memory limit: 256 MB

## Description
An industrial complex operates $n$ processing units and $m$ bidirectional transfer pipes. Each pipe has a specific shutdown expense. A system configuration is defined by selecting a subset of pipes to shut down, leaving the rest active. Because there are $2^m$ possible subsets of pipes, you must carefully select which pipes to include in your configuration.

A proposed shutdown configuration is valid if it meets two criteria:
1. The total shutdown expense of the chosen subset of pipes is at most $B$.
2. The isolation protocol is satisfied: there must be no sequence of active pipes connecting unit $s$ and unit $t$.

The operational status of all other units is irrelevant to the protocol—they may continue to exchange material in any arrangement. Your task is to determine if a valid shutdown configuration exists, and if so, to provide one.

## Input
The first line contains five integers $n$, $m$, $s$, $t$, and $B$.
The next $m$ lines each contain three integers $u$, $v$, and $w$, representing a bidirectional pipe between unit $u$ and unit $v$ with a shutdown expense of $w$.

## Output
If a valid configuration exists, print `YES` on the first line. On the second line, print the number $c$ of pipes to shut down. On each of the next $c$ lines, print two integers $u$ and $v$ representing a shut-down pipe. If no valid configuration exists, print `NO`.

## Example

**Input**
```text
4 4 1 4 10
1 2 5
2 4 6
1 3 4
3 4 7
```

**Output**
```text
YES
2
1 2
1 3
```

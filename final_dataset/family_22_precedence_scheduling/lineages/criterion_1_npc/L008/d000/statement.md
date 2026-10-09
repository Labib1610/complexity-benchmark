# Problem A — Compound Synthesis Stages

Time limit: 5 s
Memory limit: 256 MB

## Description
A laboratory is preparing $n$ distinct chemical compounds. Each compound requires exactly one heating stage to process. The lab's furnace can accommodate at most $M$ compounds per heating stage, limiting the number of compounds that can be processed simultaneously.

Certain compounds serve as base ingredients for others. If compound $a$ is an ingredient for compound $b$, compound $a$ must be processed in a strictly earlier heating stage than compound $b$. They cannot share a heating stage because the finalized form of $a$ must be available before $b$ begins processing.

The furnace elements will require maintenance after $T$ heating stages, meaning all $n$ compounds must be successfully processed using at most $T$ stages. 

Assign each of the $n$ compounds to a specific heating stage (numbered 1 through $T$) such that no stage exceeds the $M$-compound capacity and all ingredient requirements are satisfied. If no such assignment exists, report that the preparation cannot be completed before maintenance.

## Input
First line: four integers $n$, $M$, $T$, and $m$. 
Each of the next $m$ lines: two integers $a$ and $b$ — compound $a$ is an ingredient for compound $b$. Compounds are numbered from 1 to $n$.

## Output
Print `YES` then $n$ integers (the heating stage of each compound, in 1..T); otherwise print `NO`.

## Example

**Input**
```text
5 2 3 4
1 3
2 3
3 4
3 5
```

**Output**
```text
YES
1 1 2 3 3
```

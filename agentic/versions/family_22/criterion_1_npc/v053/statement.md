# Problem A — Standardized Compound Batching

Time limit: 5 s
Memory limit: 256 MB

## Description
A laboratory is preparing $n$ distinct chemical compounds. The synthesis process is highly standardized: every compound requires exactly one uniform heating stage.

To maximize efficiency, the lab uses a batch furnace capable of processing up to $M$ compounds simultaneously in a single stage. As long as the furnace capacity is not exceeded, any combination of compounds can share a stage.

The only restriction comes from the synthesis recipe. Certain compounds act as base ingredients for others. If compound $a$ is an ingredient for compound $b$, compound $a$ must be completely processed in a strictly earlier heating stage than compound $b$. The finalized form of $a$ must be ready before $b$ enters the furnace. 

Because the compounds are uniform and the stages are identical, one might assume the compounds can simply be processed as early as their ingredients allow. Furthermore, since the longest chain of ingredients cannot exceed $T$ in any valid schedule and the total number of compounds $n$ is bounded by $M \times T$, the constraints appear highly regular. However, the furnace elements are scheduled for routine maintenance after exactly $T$ heating stages. 

Your task is to determine whether there is a valid assignment of all $n$ compounds to the $T$ available stages (numbered 1 through $T$) such that the $M$-compound capacity is never exceeded and all ingredient prerequisites are respected. 

## Input
The first line contains four integers $n$, $M$, $T$, and $m$. 
Each of the next $m$ lines contains two integers $a$ and $b$, indicating that compound $a$ is an ingredient for compound $b$. Compounds are identified by integers from 1 to $n$.

## Output
If a valid assignment exists, print `YES` on the first line. On the second line, print $n$ space-separated integers, where the $i$-th integer represents the heating stage (from 1 to $T$) assigned to compound $i$. If no such assignment is possible, print `NO`.

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

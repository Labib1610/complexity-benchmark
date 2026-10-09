# Problem B — Sequencing the Batch on One Station

Time limit: 2 s
Memory limit: 256 MB

## Description
A single manufacturing station must process a batch of $n$ distinct unit-time tasks. Your objective is to determine a complete processing sequence for these tasks. 

With $n$ tasks to schedule, there are $n!$ possible sequences in which the station could process the batch. You must evaluate this space of permutations to find a sequence that satisfies a given set of $m$ chronological rules. Each rule is provided as a pair of tasks $(a, b)$, which dictates that task $a$ must be processed at some position strictly prior to task $b$ in the sequence. 

You must find a single sequence that honors all $m$ rules simultaneously. If the given rules contradict one another, such that out of all $n!$ possible combinations not a single arrangement satisfies every rule, you must detect this and report failure.

## Input
The first line contains two integers $n$ and $m$. 
Each of the next $m$ lines contains two integers $a$ and $b$ ($1 \le a, b \le n$), representing a rule that task $a$ must be processed before task $b$.

## Output
If a valid sequence exists, print `YES` on the first line, followed by a permutation of the integers from $1$ to $n$ (a valid processing sequence) on the second line. If there are multiple valid sequences, any one of them will be accepted. If no sequence satisfies all rules, print `NO`.

## Example 1
**Input**
```
3 2
1 2
2 3
```
**Output**
```
YES
1 2 3
```

## Example 2
**Input**
```
3 3
1 2
2 3
3 1
```
**Output**
```
NO
```

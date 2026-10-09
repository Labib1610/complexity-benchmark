# Problem B — Organizing the Execution

Time limit: 2 s   Memory limit: 256 MB

## Description
A single automated mechanism must perform a batch of $n$ distinct operations. It can only handle one operation at a time, so it must work through them consecutively until all are finished.

Certain operations rely on conditions established by others. You are provided with a list of $m$ strict rules. Each rule specifies that a particular operation must be completely finished before another specific operation is allowed to commence.

Your objective is to determine a complete sequence of all $n$ operations that accommodates every given rule. Because the mechanism processes exactly one operation at a time, the sequence will simply be a single list of all operations from first to last.

Determine if such a sequence can be formed. If the rules create an impossible situation where operations mutually block each other from ever starting, you must indicate that it cannot be done. Any valid sequence that includes all $n$ operations exactly once and violates no rules is accepted.

## Input
The first line contains two integers $n$ and $m$, representing the number of operations and the number of rules, respectively. Operations are numbered from $1$ to $n$.
Each of the next $m$ lines contains two integers $a$ and $b$, meaning operation $a$ must be completed before operation $b$ can commence.

## Output
If a valid sequence exists, print `YES` followed by a permutation of the integers $1 \dots n$ representing the sequence of operations. If there are multiple valid sequences, any one will be accepted.
If no such sequence is possible, print `NO`.

## Example 1
### Input
```
4 4
1 2
1 3
2 4
3 4
```
### Output
```
YES
1 2 3 4
```

## Example 2
### Input
```
3 3
1 2
2 3
3 1
```
### Output
```
NO
```

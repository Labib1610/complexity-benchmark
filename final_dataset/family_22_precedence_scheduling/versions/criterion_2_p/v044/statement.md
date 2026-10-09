# Problem B — Valid Configuration Search

Time limit: 2 s
Memory limit: 256 MB

## Description
You are responsible for configuring a deployment pipeline for $n$ database migration scripts. The deployment engine executes scripts in a strict linear sequence. Because there are $n$ distinct scripts, the configuration space consists of exactly $n!$ possible execution permutations. Your task is to evaluate this space and find a single valid sequence.

A sequence is considered valid if and only if it satisfies a specific set of $m$ compliance rules. Each rule is defined by a pair of scripts $(a, b)$. For the sequence to be accepted by the deployment engine, script $a$ must appear at some position in the sequence prior to script $b$. If a sequence violates even one of these $m$ rules, the entire configuration is invalid.

You must determine whether there exists at least one permutation among the $n!$ possibilities that satisfies all $m$ rules, and if so, construct it. If the rule set is self-contradictory such that the entire configuration space contains zero valid sequences, you must report that it is impossible.

## Input
The first line contains two integers $n$ and $m$. 
Each of the next $m$ lines contains two integers $a$ and $b$, representing a compliance rule where script $a$ must be positioned before script $b$ in the permutation.

## Output
If a valid permutation exists in the configuration space, print `YES` on the first line, followed by a second line containing a space-separated sequence of the integers $1$ to $n$ representing the valid permutation. If no sequence among the $n!$ possibilities satisfies all rules, print `NO`.

## Example

### Input
```
4 5
1 2
1 3
2 4
3 4
1 4
```

### Output
```
YES
1 2 3 4
```

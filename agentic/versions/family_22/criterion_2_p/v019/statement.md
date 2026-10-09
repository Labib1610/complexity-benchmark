# Alchemical Synthesis

Time limit: 2 s   Memory limit: 256 MB

## Description
An alchemist is preparing a complex elixir requiring $n$ distinct liquid extracts, numbered 1 through $n$. These extracts must be poured into a cauldron one at a time until all $n$ have been added. The procedure strictly requires one extract to be poured at a time, creating a single, complete sequence of additions.

The extracts are highly reactive, and the alchemist has recorded $m$ safety protocols to prevent the cauldron from boiling over. Each protocol specifies two extracts, $a$ and $b$, and requires that extract $a$ must already be present in the cauldron at the exact moment extract $b$ is poured in. There is no requirement that $b$ is added immediately after $a$; it is only required that $a$ appears somewhere earlier in the sequence of additions than $b$.

Your task is to determine a complete sequence for adding all $n$ extracts that satisfies every safety protocol simultaneously. If the protocols create an unresolvable paradox—where no such sequence can possibly exist—you must report that the elixir cannot be synthesized.

## Input
The first line contains two integers $n$ and $m$.
Each of the next $m$ lines contains two integers $a$ and $b$, representing a safety protocol where extract $a$ must be in the cauldron before extract $b$ is added.

## Output
If a valid sequence exists, print `YES` followed by a permutation of the integers 1 to $n$ (separated by spaces or newlines) representing a safe order of additions. If there are multiple valid sequences, any one is acceptable.
If it is impossible to safely add all extracts, print `NO`.

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

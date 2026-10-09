# Compiling the Charter

Time limit: 2 s
Memory limit: 256 MB

## Description
A legal clerk is tasked with assembling a final charter consisting of $n$ distinct clauses (numbered $1$ to $n$). The clauses will be arranged in a single continuous document, read from first to last.

Certain clauses rely on definitions or premises established by others. You are provided with a list of $m$ rules. Each rule specifies that a particular clause must be placed somewhere before another specific clause in the finalized text. The exact distance between them in the document does not matter, as long as the relative order is maintained.

You must determine if there is a way to arrange all $n$ clauses in a single sequence that satisfies every given rule. If contradictory rules make this impossible (for example, if the rules dictate a scenario where a clause is ultimately forced to appear before itself), you must declare the compilation invalid. Otherwise, provide a valid arrangement.

## Input
First line: two integers $n$ and $m$.
Each of the next $m$ lines: two integers $a$ and $b$, meaning clause $a$ must appear before clause $b$ in the document.

## Output
Print `YES` then a space-separated permutation of the integers $1$ to $n$ representing a valid sequence of clauses from first to last. If there are multiple valid sequences, any of them will be accepted. 
If no such arrangement exists, print `NO`.

## Example 1

### Input
```text
4 4
1 2
2 3
1 4
4 3
```

### Output
```text
YES
1 4 2 3
```

## Example 2

### Input
```text
3 3
1 2
2 3
3 1
```

### Output
```text
NO
```

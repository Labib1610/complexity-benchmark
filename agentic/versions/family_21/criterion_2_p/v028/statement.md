# Problem B — Intercepting the Cascade

Time limit: 2 s   Memory limit: 256 MB

## Description
A cellular process is driven by a collection of proteins and the reversible interactions between them. Each interaction can be permanently suppressed by introducing a specific amount of a targeted inhibitor. 

Two particular proteins, $s$ and $t$, are of critical concern. You must ensure that no chain of active interactions can transmit a state change from protein $s$ to protein $t$, nor from $t$ to $s$. Once an interaction is suppressed, it cannot transmit changes in either direction.

The state of the other proteins in the system is irrelevant, provided the primary condition is met. You are allocated a maximum total dosage $B$ of inhibitor across the entire procedure. The sum of the inhibitor amounts for the suppressed interactions must not exceed this allowance. Determine a set of interactions to suppress that satisfies these conditions, or report that the allowance is insufficient.

## Input
Line 1: five integers $n, m, s, t, B$.
Next $m$ lines: three integers $u$ $v$ $w$ — an interaction between protein $u$ and protein $v$ requiring $w$ units of inhibitor to suppress.

## Output
`YES`, then a line with the number $c$ of suppressed interactions, then $c$ lines "`u v`"; or `NO`.

## Example

**Input**
```text
4 4 1 4 10
1 2 4
1 3 5
2 4 6
3 4 3
```

**Output**
```text
YES
2
1 2
3 4
```

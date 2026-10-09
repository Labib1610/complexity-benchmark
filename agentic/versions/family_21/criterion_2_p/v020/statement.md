# Problem B — Language Barrier

Time limit: 2 s   Memory limit: 256 MB

## Description
A global enterprise relies on a pool of bilingual interpreters to facilitate communication across different regional offices. Each interpreter is certified to translate back and forth between exactly two specific languages, and terminating an interpreter's contract requires paying a fixed buyout fee. 

A highly sensitive internal memo has been drafted in a specific language (the origin language). The enterprise wants to ensure that this memo can never be translated, even through multiple intermediate languages, into a specific target language used by a competing department. Once an interpreter's contract is bought out, they can no longer provide any translations.

The other languages in the enterprise may end up with access to the memo or remain ignorant of it — their status is unconstrained and plays no part in whether the plan is accepted. What is measured is solely the total buyout fee, which is the sum of the fees for the terminated interpreters. There is a strict budget for these buyouts that this total must not exceed.

Choose a set of interpreters to terminate whose total buyout fee is within the budget and whose removal guarantees that no chain of remaining interpreters can bridge the origin language and the target language, or report that no in-budget terminations can separate them. (Ensuring a barrier between just two specific languages is far more straightforward than isolating many languages simultaneously — multi-language partitioning machinery is unnecessary here, and a solver that reaches for it will waste effort on a fundamentally simpler separation.)

## Input
Line 1: five integers $n, m, s, t, B$. 
Next $m$ lines: three integers $u\ v\ w$ — an interpreter between language $u$ and language $v$ with a buyout fee of $w$.

## Output
`YES`, then a line with the number $c$ of removed interpreters, then $c$ lines `u v`; or `NO`.

## Example 1

**Input**
```text
4 5 1 4 10
1 2 4
1 3 6
2 3 2
2 4 5
3 4 3
```

**Output**
```text
YES
2
2 4
3 4
```

## Example 2

**Input**
```text
4 5 1 4 7
1 2 4
1 3 6
2 3 2
2 4 5
3 4 3
```

**Output**
```text
NO
```
